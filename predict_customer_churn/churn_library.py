"""
Library which implements all functions related to predicting customer churn

Author: Yuri Marca
Date: November 3rd, 2024
"""

# import libraries
import os
os.environ['QT_QPA_PLATFORM']='offscreen'

import shap
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

from pathlib import Path

from sklearn.preprocessing import normalize
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

from sklearn.metrics import plot_roc_curve, classification_report



def import_data(pth):
    '''
    returns dataframe for the csv found at pth

    input:
            pth: a path to the csv
    output:
            df: pandas dataframe
    '''
    try:
        df = pd.read_csv(pth, index_col=0)
        return df
    except FileNotFoundError:
        print(f"File not found: {pth}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None

def perform_eda(df, img_folder='./images/eda'):
    '''
    perform eda on df and save figures to images folder
    input:
            df: pandas dataframe

    output:
            None
    '''

    img_folder_path = Path(img_folder)

    # Check if the folder exists
    if not img_folder_path.exists():
        img_folder_path.mkdir(parents=True)

    # Create Churn variable
    df['Churn'] = df['Attrition_Flag'].apply(lambda val: 0 if val == "Existing Customer" else 1)

    # Plot and save churn distribution
    fig = plt.figure(figsize=(20,10)) 
    df['Churn'].hist()
    fig.savefig(img_folder_path / 'churn_dist.png')
    plt.close(fig)

    # Plot and save customer age distribution
    fig = plt.figure(figsize=(20,10)) 
    df['Customer_Age'].hist()
    fig.savefig(img_folder_path / 'customer_age_dist.png')
    plt.close(fig)

    # Plot and save maritial status distribution
    fig = plt.figure(figsize=(20,10)) 
    df.Marital_Status.value_counts('normalize').plot(kind='bar')
    fig.savefig(img_folder_path / 'marital_status_dist.png')
    plt.close(fig)    

    # Plot and save total transaction count distribution
    fig = plt.figure(figsize=(20,10)) 
    sns.histplot(df['Total_Trans_Ct'], stat='density', kde=True)
    fig.savefig(img_folder_path / 'total_trans_count_dist.png')
    plt.close(fig)

    # Plot and save features correlation
    fig = plt.figure(figsize=(20,10)) 
    sns.heatmap(df.drop(columns=['Attrition_Flag', 'Gender', 'Education_Level', 'Marital_Status', 'Income_Category', 'Card_Category']).corr(), annot=False, cmap='Dark2_r', linewidths = 2)
    fig.savefig(img_folder_path / 'features_correlation.png')
    plt.close(fig)



def encoder_helper(df, category_lst, response='Churn'):
    '''
    helper function to turn each categorical column into a new column with
    propotion of churn for each category - associated with cell 15 from the notebook

    input:
            df: pandas dataframe
            category_lst: list of columns that contain categorical features
            response: string of response name [optional argument that could be used for naming variables or index y column]

    output:
            df: pandas dataframe with new columns for
    '''

    for category in category_lst:
        if category in df.columns:
            cat_groups = df.groupby(category)[response].mean()
            new_column = category + "_" + response
            df[new_column] = df[category].map(lambda x: cat_groups[x])
        else:
            print(f"Warning: {category} column not found in dataframe.")

    return df


def perform_feature_engineering(df, response='Churn'):
    '''
    input:
              df: pandas dataframe
              response: string of response name [optional argument that could be used for naming variables or index y column]

    output:
              X_train: X training data
              X_test: X testing data
              y_train: y training data
              y_test: y testing data
    '''
    keep_cols = ['Customer_Age', 'Dependent_count', 'Months_on_book',
                 'Total_Relationship_Count', 'Months_Inactive_12_mon',
                 'Contacts_Count_12_mon', 'Credit_Limit', 'Total_Revolving_Bal',
                 'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt',
                 'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio',
                 'Gender_Churn', 'Education_Level_Churn', 'Marital_Status_Churn', 
                 'Income_Category_Churn', 'Card_Category_Churn', 'Churn']

    df = df[keep_cols]
    y = df[response]
    X = df.drop(response, axis=1)

    # train test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42)

    return X_train, X_test, y_train, y_test


def classification_report_image(y_train,
                                y_test,
                                y_train_preds_lr,
                                y_train_preds_rf,
                                y_test_preds_lr,
                                y_test_preds_rf):
    '''
    produces classification report for training and testing results and stores report as image
    in images folder
    input:
            y_train: training response values
            y_test:  test response values
            y_train_preds_lr: training predictions from logistic regression
            y_train_preds_rf: training predictions from random forest
            y_test_preds_lr: test predictions from logistic regression
            y_test_preds_rf: test predictions from random forest

    output:
             None
    '''
    # RandomForestClassifier 
    plt.figure(figsize=(6, 6))
    plt.rc('figure', figsize=(6, 6))

    # Add texts for classification report
    plt.text(0.01, 1.25,
             'Random Forest Train',
             {'fontsize': 10}, fontproperties='monospace')
    plt.text(0.01, 0.05,
             classification_report(y_test, y_test_preds_rf),
             {'fontsize': 10}, fontproperties='monospace')
    plt.text(0.01, 0.6,
             'Random Forest Test',
             {'fontsize': 10}, fontproperties='monospace')
    plt.text(0.01, 0.7,
             classification_report(y_train, y_train_preds_rf),
             {'fontsize': 10}, fontproperties='monospace')

    # Remove axes
    plt.axis('off')

    # Save the figure to a file
    plt.savefig(fname='./images/results/rf_results.png')

    # Close the figure
    plt.close()
    
    # LogisticRegression 
    plt.figure(figsize=(6, 6))
    plt.rc('figure', figsize=(6, 6))

    # Add texts for classification report
    plt.text(0.01, 1.25,
             'Logistic Regression Train',
             {'fontsize': 10}, fontproperties='monospace')
    plt.text(0.01, 0.05,
             classification_report(y_train, y_train_preds_lr),
             {'fontsize': 10}, fontproperties='monospace')
    plt.text(0.01, 0.6,
             'Logistic Regression Test',
             {'fontsize': 10}, fontproperties='monospace')
    plt.text(0.01, 0.7,
             classification_report(y_test, y_test_preds_lr),
             {'fontsize': 10}, fontproperties='monospace')

    # Remove axes
    plt.axis('off')

    # Save the figure to a file
    plt.savefig(fname='./images/results/logistic_results.png')

    # Close the figure
    plt.close()


def feature_importance_plot(model, X_data, output_pth):
    '''
    creates and stores the feature importances in pth
    input:
            model: model object containing feature_importances_
            X_data: pandas dataframe of X values
            output_pth: path to store the figure

    output:
             None
    '''
    # Feature importances
    importances = model.best_estimator_.feature_importances_

    # Sort Feature importances in descending order
    indices = np.argsort(importances)[::-1]

    # Sorted feature importances
    names = [features.columns[i] for i in indices]

    # Initialize a new figure
    plt.figure(figsize=(25, 15))

    # Create plot title and labels
    plt.title("Feature Importance")
    plt.ylabel('Importance')

    # Add bars
    plt.bar(range(features.shape[1]), importances[indices])

    # Set x-axis labels
    plt.xticks(range(features.shape[1]), names, rotation=90)

    # Save the image to a file
    plt.savefig(fname=output_pth + 'feature_importances.png')

    # Close the figure
    plt.close()

def train_models(X_train, X_test, y_train, y_test):
    '''
    train, store model results: images + scores, and store models
    input:
              X_train: X training data
              X_test: X testing data
              y_train: y training data
              y_test: y testing data
    output:
              None
    '''
    # RandomForestClassifier and LogisticRegression
    rfc = RandomForestClassifier(random_state=42, n_jobs=-1)
    lrc = LogisticRegression(n_jobs=-1, max_iter=1000)

    # Parameters for Grid Search
    param_grid = {'n_estimators': [200, 500],
                  'max_features': ['auto', 'sqrt'],
                  'max_depth' : [4, 5, 100],
                  'criterion' :['gini', 'entropy']}

    # Grid Search and fit for RandomForestClassifier
    cv_rfc = GridSearchCV(estimator=rfc, param_grid=param_grid, cv=5)
    cv_rfc.fit(X_train, y_train)

    # LogisticRegression
    lrc.fit(X_train, y_train)

    # Save best models
    joblib.dump(cv_rfc.best_estimator_, './models/rfc_model.pkl')
    joblib.dump(lrc, './models/logistic_model.pkl')

    # Compute train and test predictions for RandomForestClassifier
    y_train_preds_rf = cv_rfc.best_estimator_.predict(X_train)
    y_test_preds_rf  = cv_rfc.best_estimator_.predict(X_test)

    # Compute train and test predictions for LogisticRegression
    y_train_preds_lr = lrc.predict(X_train)
    y_test_preds_lr  = lrc.predict(X_test)

    # Compute ROC curve
    plt.figure(figsize=(15, 8))
    axis = plt.gca()
    lrc_plot = plot_roc_curve(lrc, X_test, y_test, ax=axis, alpha=0.8)                          
    rfc_disp = plot_roc_curve(cv_rfc.best_estimator_, X_test, y_test, ax=axis, alpha=0.8)       
    plt.savefig(fname='./images/results/roc_curve_result.png')
    #plt.show()

    # Compute and results
    classification_report_image(y_train, y_test,
                                y_train_preds_lr, y_train_preds_rf,
                                y_test_preds_lr,  y_test_preds_rf)

    # Compute and feature importance
    feature_importance_plot(cv_rfc,
                            X_test,
                            './images/results/')
    
if __name__ == "__main__":
    # Read data stored in the given file
    FILE_PATH = r"./data/bank_data.csv"
    DF = import_data(FILE_PATH)

    perform_eda(DF)
    
    # feature engineering
    category_list = [ 'Gender', 'Education_Level', 
                      'Marital_Status','Income_Category', 
                      'Card_Category']
    DF = encoder_helper(DF, category_list)

    print(DF.head())

    # Feature engineering
    X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = perform_feature_engineering(
                                            DF, 'Churn')

    # Model training,prediction and evaluation
    train_models(X_train=X_TRAIN,
                 X_test=X_TEST,
                 y_train=Y_TRAIN,
                 y_test=Y_TEST)
