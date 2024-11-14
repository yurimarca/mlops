"""
Test functions and logging for churn library
churn.

Author: Yuri Marca
Date: November 14th, 2024
"""


import os
import logging
from churn_library import ChurnLibrarySolution

logging.basicConfig(
    filename='./logs/churn_library.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')


def test_import(import_data):
    '''
    Test data import function.
    '''
    try:
        df = import_data("./data/bank_data.csv")
        logging.info("Testing import_data: SUCCESS")
    except FileNotFoundError as err:
        logging.error("Testing import_data: The file wasn't found")
        raise err

    try:
        assert df.shape[0] > 0
        assert df.shape[1] > 0
        logging.info("Testing import_data: DataFrame has valid shape")
    except AssertionError as err:
        logging.error("Testing import_data: The file doesn't" +
                      " have rows and columns")
        raise err


def test_eda(perform_eda, df):
    '''
    Test perform_eda function.
    '''
    try:
        perform_eda(df)
        assert os.path.isfile('./images/eda/churn_dist.png')
        assert os.path.isfile('./images/eda/customer_age_dist.png')
        assert os.path.isfile('./images/eda/marital_status_dist.png')
        assert os.path.isfile('./images/eda/total_trans_count_dist.png')
        logging.info("Testing perform_eda: SUCCESS")
    except AssertionError as err:
        logging.error("Testing perform_eda: EDA files were not" +
                      " created as expected")
        raise err
    except Exception as err:
        logging.error("Testing perform_eda: An error occurred - %s",
                                                                err)
        raise err


def test_encoder_helper(encoder_helper, df):
    '''
    Test encoder helper function.
    '''
    try:
        category_lst = ['Gender', 'Education_Level', 'Marital_Status',
                        'Income_Category', 'Card_Category']
        df = encoder_helper(df, category_lst)

        for category in category_lst:
            assert f"{category}_Churn" in df.columns
        logging.info("Testing encoder_helper: SUCCESS")
    except AssertionError as err:
        logging.error("Testing encoder_helper: Not all encoded " + \
                        "columns are present in the DataFrame")
        raise err
    except Exception as err:
        logging.error("Testing encoder_helper: An error occurred - %s",
                                                                    err)
        raise err


def test_perform_feature_engineering(perform_feature_engineering, df):
    '''
    Test perform_feature_engineering function.
    '''
    try:
        features_train, features_test, target_train, \
                        target_test = perform_feature_engineering(df)

        assert len(features_train) > 0
        assert len(features_test) > 0
        assert len(target_train) > 0
        assert len(target_test) > 0
        logging.info("Testing perform_feature_engineering: SUCCESS")
    except AssertionError as err:
        logging.error(
            "Testing perform_feature_engineering: Data splitting " + \
                "failed, no data in train/test splits")
        raise err
    except Exception as err:
        logging.error(
            "Testing perform_feature_engineering: Error - %s", err)
        raise err


def test_train_models(
        train_models,
        features_train,
        features_test,
        target_train,
        target_test):
    '''
    Test train_models function.
    '''
    try:
        train_models(features_train, features_test,
                        target_train, target_test)

        assert os.path.isfile('./models/rfc_model.pkl')
        assert os.path.isfile('./models/logistic_model.pkl')
        assert os.path.isfile('./images/results/roc_curve_result.png')
        logging.info("Testing train_models: SUCCESS")
    except AssertionError as err:
        logging.error(
            "Testing train_models: Model files or evaluation images "+ \
            "not found after training")
        raise err
    except Exception as err:
        logging.error("Testing train_models: An error occurred - %s",
                                                                    err)
        raise err


if __name__ == "__main__":
    cls = ChurnLibrarySolution()

    # Test data import
    test_import(cls.import_data)
    DF = cls.import_data("./data/bank_data.csv")

    # Test perform_eda
    test_eda(cls.perform_eda, DF)

    # Test encoder_helper
    test_encoder_helper(cls.encoder_helper, DF)

    # Test perform_feature_engineering
    training_split = cls.perform_feature_engineering(DF)

    test_perform_feature_engineering(cls.perform_feature_engineering,
                                        DF)

    # Test train_models
    test_train_models(cls.train_models,*training_split)
