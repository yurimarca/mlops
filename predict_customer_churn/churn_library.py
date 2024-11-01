"""Library which implements all functions related to predicting customer churn"""

# import libraries
import os
os.environ['QT_QPA_PLATFORM']='offscreen'

#import shap
#import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

from pathlib import Path

# from sklearn.preprocessing import normalize
# from sklearn.model_selection import train_test_split

# from sklearn.linear_model import LogisticRegression
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import GridSearchCV

# from sklearn.metrics import plot_roc_curve, classification_report



def import_data(pth):
    '''
    returns dataframe for the csv found at pth

    input:
            pth: a path to the csv
    output:
            df: pandas dataframe
    '''
    try:
        df = pd.read_csv(pth)
        return df
    except e:
        print(f"Error loading csv file: {pth}")

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



def encoder_helper(df, category_lst, response):
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

    #for cat in category_lst:
        

    # gender encoded column
    gender_lst = []
    gender_groups = df.groupby('Gender').mean()['Churn']

    for val in df['Gender']:
        gender_lst.append(gender_groups.loc[val])

    df['Gender_Churn'] = gender_lst    
    #education encoded column
    edu_lst = []
    edu_groups = df.groupby('Education_Level').mean()['Churn']

    for val in df['Education_Level']:
        edu_lst.append(edu_groups.loc[val])

    df['Education_Level_Churn'] = edu_lst

    #marital encoded column
    marital_lst = []
    marital_groups = df.groupby('Marital_Status').mean()['Churn']

    for val in df['Marital_Status']:
        marital_lst.append(marital_groups.loc[val])

    df['Marital_Status_Churn'] = marital_lst

    #income encoded column
    income_lst = []
    income_groups = df.groupby('Income_Category').mean()['Churn']

    for val in df['Income_Category']:
        income_lst.append(income_groups.loc[val])

    df['Income_Category_Churn'] = income_lst

    #card encoded column
    card_lst = []
    card_groups = df.groupby('Card_Category').mean()['Churn']
     
    for val in df['Card_Category']:
        card_lst.append(card_groups.loc[val])

    df['Card_Category_Churn'] = card_lst


def perform_feature_engineering(df, response):
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
    pass


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
    pass

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
    pass
    
if __name__ == "__main__":
    # Read data stored in the given file
    file_pth = r"./data/bank_data.csv"
    df = import_data(file_pth)

    perform_eda(df)
    
    
