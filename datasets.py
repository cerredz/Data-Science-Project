import pandas as pd    
from pathlib import Path

def load_train_df():
    TRAIN_PATH="data/train.csv"
    train_df=pd.read_csv(TRAIN_PATH)
    return train_df

def load_test_df():
    TEST_PATH="data/test.csv"
    test_df=pd.read_csv(TEST_PATH)
    return test_df