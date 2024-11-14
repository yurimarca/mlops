"""
Library which implements all functions related to predicting customer 
churn.

Author: Yuri Marca
Date: November 3rd, 2024
"""

# import libraries
import os

from pathlib import Path
import numpy as np
import pandas as pd

import joblib

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import plot_roc_curve, classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

import shap

os.environ['QT_QPA_PLATFORM'] = 'offscreen'
sns.set()


class ChurnLibrarySolution:
    """
    A class that encapsulates the entire churn prediction process,
    including data loading, EDA, feature engineering, model training,
    evaluation, and saving results.
    """

    def __init__(self,
                 img_folder='./images',
                 model_folder='./models'):
        """
        Initializes the paths for data, image, and model folders.

        Parameters:
        - img_folder: Path to the folder where EDA images will be saved.
        - model_folder: Path to the folder where to save trained models.
        """

        # Create the image folder if it doesn't exist
        self.img_eda_folder = Path(img_folder) / 'eda'
        if not self.img_eda_folder.exists():
            self.img_eda_folder.mkdir(parents=True)

        self.img_res_folder = Path(img_folder) / 'results'
        if not self.img_res_folder.exists():
            self.img_res_folder.mkdir(parents=True)

        # Create the model folder if it doesn't exist
        self.model_folder = Path(model_folder)
        if not self.model_folder.exists():
            self.model_folder.mkdir(parents=True)

    def import_data(self, path):
        """
        Returns dataframe for the csv found at pth

        Input:
            - path: Path to the CSV file containing the data.
        Output:
            - df: Pandas dataframe
        """
        try:
            # Reads the CSV file into a pandas DataFrame
            df = pd.read_csv(path, index_col=0)
        except FileNotFoundError:
            print(f"File not found: {path}")
        return df

    def perform_eda(self, df):
        """
        Perform EDA on df and save figures to images folder
        Input:
            - df: Pandas dataframe
        """

        # Create a binary target column 'Churn' from 'Attrition_Flag'
        df['Churn'] = df['Attrition_Flag'].apply(
            lambda val: 0 if val == "Existing Customer" else 1)

        # Dictionary to store EDA plots with filenames and plot details
        eda_plots = {
            'churn_dist.png': ('Churn', 'hist'),
            'customer_age_dist.png': ('Customer_Age', 'hist'),
            'marital_status_dist.png': ('Marital_Status',
                                        'bar',
                                        'normalize'),
            'total_trans_count_dist.png': ('Total_Trans_Ct',
                                           'sns_histplot')
        }

        # Generate and save each plot
        for file, (column, plot_type, *args) in eda_plots.items():
            fig = plt.figure(figsize=(20, 10))
            if plot_type == 'hist':
                df[column].hist()
            elif plot_type == 'bar':
                df[column].value_counts(args[0]).plot(kind='bar')
            elif plot_type == 'sns_histplot':
                sns.histplot(df[column], stat='density', kde=True)
            fig.savefig(self.img_eda_folder / file)
            plt.close(fig)

        # Generate and save a heatmap for feature correlations
        fig = plt.figure(figsize=(20, 10))
        cols_to_drop = ['Attrition_Flag', 'Gender', 'Education_Level',
                        'Marital_Status', 'Income_Category',
                        'Card_Category']
        df_aux = df.drop(columns=cols_to_drop)
        sns.heatmap(df_aux.corr(), annot=False,
                    cmap='Dark2_r', linewidths=2)
        fig.savefig(self.img_eda_folder / 'features_correlation.png')
        plt.close(fig)

    def encoder_helper(self, df, category_lst, response='Churn'):
        """
        Helper function to turn each categorical column into a new
        column with propotion of churn for each category

        Input:
            - df: Pandas dataframe
            - category_lst: List of columns that contain categorical
            features
            - response: String of response name [optional argument that
            could be used for naming variables or index y column]
        Output:
            df: Pandas dataframe with new columns for
        """
        for category in category_lst:
            # Check if category column exists in DataFrame
            if category in df.columns:
                # Calculate churn proportion for each category level
                cat_groups = df.groupby(category)[response].mean()
                new_column = category + "_" + response
                # Map churn proportion back to each row in the DataFrame
                df[new_column] = df[category].map(cat_groups)
            else:
                print(f"Warning: {category} column not found in df.")

        return df

    def perform_feature_engineering(self, df, response='Churn'):
        """
        Performs feature engineering by encoding categorical variables
        and splitting data into training and testing sets.

        Input:
              - df: Pandas dataframe
              - response: String of response name [optional argument
              that could be used for naming variables or index y column]
        output:
              - features_train: Features training data
              - features_test: Features testing data
              - target_train: Target training data
              - target_test: Target testing data
        """
        # List of categorical columns to be encoded
        category_list = ['Gender', 'Education_Level', 'Marital_Status',
                         'Income_Category', 'Card_Category']

        df = self.encoder_helper(df, category_list)

        # Define the columns to keep for model training
        keep_cols = [
            'Customer_Age', 'Dependent_count', 'Months_on_book',
            'Total_Relationship_Count', 'Months_Inactive_12_mon',
            'Contacts_Count_12_mon', 'Credit_Limit',
            'Total_Revolving_Bal', 'Avg_Open_To_Buy',
            'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt', 'Total_Trans_Ct',
            'Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio',
            'Gender_Churn', 'Education_Level_Churn',
            'Marital_Status_Churn', 'Income_Category_Churn',
            'Card_Category_Churn', 'Churn'
        ]

        # Keep only necessary columns for modeling
        df = df[keep_cols]
        y = df[response]
        x = df.drop(response, axis=1)

        # Split data into training and testing sets
        features_train, features_test, target_train, target_test = \
            train_test_split(x, y, test_size=0.3, random_state=42)

        return features_train, features_test, target_train, target_test

    def classification_report_image(self, targets, predictions):
        """
        Produces classification report for training and testing results
        and stores report as image in images folder.
        
        Input:
            - targets: Dictionary containing true training and test 
            values
              Format:
                {'train': target_train, 'test': target_test}
              
            - predictions: Dictionary containing model predictions for
              training and testing sets.
              Format:
                {
                    'Model': {'train': target_train_preds_model, 
                                'test': target_test_preds_model}
                }
        """
        for model_name, preds in predictions.items():
            plt.rc('figure', figsize=(5, 5))

            # Add texts for classification report for training/test sets
            plt.text(0.01, 1.25, f'{model_name} Train',
                        {'fontsize': 10}, fontproperties='monospace')
            plt.text(0.01, 0.7, classification_report(targets['train'],
                                                        preds['train']),
                        {'fontsize': 10}, fontproperties='monospace')
            plt.text(0.01, 0.6, f'{model_name} Test',
                        {'fontsize': 10}, fontproperties='monospace')
            plt.text(0.01, 0.05, classification_report(targets['test'],
                                                        preds['test']),
                    {'fontsize': 10}, fontproperties='monospace')

            # Remove axes
            plt.axis('off')
            plt.tight_layout()

            # Save the figure to a file
            file_name = f'{model_name.lower().replace(" ", "_")}'
            file_name += '_results.png'
            plt.savefig(self.img_res_folder / file_name)
            plt.close()

    def feature_importance_plot(self, model, features_test):
        """
        Creates and stores the feature importances in pth
        input:
            - model: Model object containing feature_importances_
            - features_test: Pandas dataframe of features values
        """
        # Feature importances
        importances = model.best_estimator_.feature_importances_

        # Sort Feature importances in descending order
        indices = np.argsort(importances)[::-1]

        # Rearrange feature so they match the sorted feature importances
        names = [features_test.columns[i] for i in indices]

        fig = plt.figure(figsize=(20, 5))
        plt.title("Feature Importance")
        plt.ylabel('Importance')
        plt.bar(range(features_test.shape[1]), importances[indices])
        plt.xticks(range(features_test.shape[1]), names, rotation=90)
        plt.tight_layout()

        # Save the image to a file
        fig.savefig(self.img_res_folder / 'feature_importances.png')
        plt.close(fig)

        # SHAP Figure
        fig = plt.figure(figsize=(20, 5))

        explainer = shap.TreeExplainer(model.best_estimator_)
        shap_values = explainer.shap_values(features_test)

        # Create the SHAP summary plot
        shap.summary_plot(shap_values, features_test,
                          plot_type="bar", show=False)

        # Save the plot as an image file
        fig.savefig(self.img_res_folder / "shap_summary_plot.png",
                    format="png",
                    dpi=300,
                    bbox_inches="tight")

        plt.close(fig)

    def train_models(self,
                     features_train,
                     features_test,
                     target_train,
                     target_test):
        """
        Trains Random Forest and Logistic Regression models, evaluates
        them, and saves the models and evaluation results.
        Input:
              - features_train: Features training data
              - features_test: Features testing data
              - target_train: Target training data
              - target_test: Target testing data
        """
        # Initialize Random Forest and Logistic Regression models
        rfc = RandomForestClassifier(random_state=42, n_jobs=-1)
        lrc = LogisticRegression(n_jobs=-1, max_iter=1000)

        # Define hyperparameters for Grid Search
        param_grid = {'n_estimators': [200, 500],
                      'max_features': ['auto', 'sqrt'],
                      'max_depth': [4, 5, 100],
                      'criterion': ['gini', 'entropy']}

        # Grid Search for Random Forest model
        cv_rfc = GridSearchCV(estimator=rfc,
                              param_grid=param_grid,
                              cv=5)
        cv_rfc.fit(features_train, target_train)

        best_estimator_rf = cv_rfc.best_estimator_

        # Train Logistic Regression model
        lrc.fit(features_train, target_train)

        # Save best models to disk
        joblib.dump(cv_rfc.best_estimator_,
                    self.model_folder / 'rfc_model.pkl')
        joblib.dump(lrc, self.model_folder / 'logistic_model.pkl')

        # Plot and save ROC curves
        plt.figure(figsize=(15, 8))
        axis = plt.gca()
        plot_roc_curve(lrc, features_test,
                        target_test, ax=axis, alpha=0.8)
        plot_roc_curve(best_estimator_rf, features_test,
                        target_test, ax=axis, alpha=0.8)
        plt.savefig(self.img_res_folder / 'roc_curve_result.png')
        plt.close()

        targets = {
            'train': target_train,
            'test': target_test
        }

        # Generate predictions for both train and test data
        predictions = {
            'RF': {'train': best_estimator_rf.predict(features_train), 
                    'test': best_estimator_rf.predict(features_test)},
            'Logistic': {'train': lrc.predict(features_train), 
                        'test': lrc.predict(features_test)}
        }

        # Save classification reports and feature importance
        self.classification_report_image(targets, predictions)
        self.feature_importance_plot(cv_rfc, features_test)


if __name__ == "__main__":
    # Instantiate and run the churn prediction solution
    cls = ChurnLibrarySolution()

    # Read data stored in the given file
    FILE_PATH = r"./data/bank_data.csv"
    DF = cls.import_data(FILE_PATH)

    cls.perform_eda(DF)

    # Feature engineering
    training_split = cls.perform_feature_engineering(DF)

    # Model training,prediction and evaluation
    cls.train_models(*training_split)
