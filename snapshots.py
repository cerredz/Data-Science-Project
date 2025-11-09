import pandas as pd

if __name__ == "__main__":
    categories=["t-shirt/top", "trouser", "pullover", "dress", "coat", "sandal", "shirt", "sneaker", "bag", "ankle boot"]
    TRAIN_PATH, TEST_PATH = "data/train.csv", "data/test.csv"

    train_df=pd.read_csv(TRAIN_PATH)
    test_df=pd.read_csv(TEST_PATH)

    print(f"Training Dataset Snapshot\n{train_df.head()}")
    print(f"Testing Dataset Snapshot\n{test_df.head()}")