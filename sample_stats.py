from datasets import load_test_df, load_train_df

def label_distribution():
    train_df, test_df = load_train_df(), load_test_df()
    train_label_distribution= {label: 0 for label in range(0,10)}
    print(train_label_distribution)