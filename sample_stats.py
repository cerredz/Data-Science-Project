from datasets import load_test_df, load_train_df
import numpy as np
import pandas as pd

def label_distribution():
    train_df, test_df = load_train_df(), load_test_df()
    train_label_distribution = {label: 0 for label in range(0, 10)}
    test_label_distribution = {label: 0 for label in range(0, 10)}

    for index, row in train_df.iterrows():
        label = row['label'] 
        train_label_distribution[label] += 1

    for index, row in test_df.iterrows():
        label = row['label']  
        test_label_distribution[label] += 1
    
    return train_label_distribution, test_label_distribution

def pixel_intensity():
    train_df, test_df = load_train_df(), load_test_df()
    categories = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", 
                  "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
    
    full_df = pd.concat([train_df, test_df], ignore_index=True)
    pixel_columns = [col for col in full_df.columns if col != 'label']
    stats = {}
    for label in range(10):
        label_data = full_df[full_df['label'] == label][pixel_columns].values.flatten()
        stats[categories[label]] = {
            'mean': np.mean(label_data),
            'std': np.std(label_data),
        }
    
    return stats

if __name__ == "__main__":
    train_dist, test_dist = label_distribution()
    print(f"Training Label Distribution: \n{train_dist}")
    print(f"\nTest Label Distribution: \n{test_dist}")

    category_stats = pixel_intensity()
    for category, stats in category_stats.items():
        print(f"{category}: | Mean Intensity: {stats['mean']:.2f} | Std Dev: {stats['std']:.2f}")
