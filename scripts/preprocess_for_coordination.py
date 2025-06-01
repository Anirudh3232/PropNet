import pandas as pd
import re


df = pd.read_csv("data/Truth_Seeker_Model_Dataset.csv")


df = df[["author", "tweet", "manual_keywords", "target"]].dropna()


def extract_hashtags(text):
    return re.findall(r"#\w+", str(text).lower())

df["hashtags"] = df["tweet"].apply(extract_hashtags)


df["manual_keywords"] = df["manual_keywords"].astype(str).str.lower().str.strip()
df["target"] = df["target"].astype(str).str.lower().str.strip()



df.to_csv("data/preprocessed_coordination.csv", index=False)
print("Saved: data/preprocessed_coordination.csv")
