import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("data/Truth_Seeker_Model_Dataset.csv")


print("\n Dataset Overview:")
print("-" * 50)
print(f"Total rows: {len(df)}")
print(f"Total columns: {len(df.columns)}")
print("\nColumns:", ", ".join(df.columns))


print("\n Data Preview:")
print("-" * 50)
print(df.head())


print("\n Numerical Statistics:")
print("-" * 50)
print(df.describe())


print("\n Missing Values:")
print("-" * 50)
missing = df.isnull().sum()
print(missing[missing > 0])


if 'label' in df.columns:
    print("\n️ Label Distribution:")
    print("-" * 50)
    label_dist = df['label'].value_counts()
    print(label_dist)


    plt.figure(figsize=(10, 6))
    sns.barplot(x=label_dist.index, y=label_dist.values)
    plt.title('Distribution of Labels')
    plt.xlabel('Label')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('data/label_distribution.png')
    print("\nLabel distribution plot saved as 'data/label_distribution.png'")
