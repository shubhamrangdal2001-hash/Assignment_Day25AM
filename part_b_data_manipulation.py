# Part B - Stretch Problem: Filtering, New Columns, Sorting, Grouping
# Dataset: titanic_sample.csv (600 rows)
# Week 05 Day 25 AM | PG Diploma AI-ML & Agentic AI Engineering IIT Gandhinagar

import pandas as pd

# Load and clean dataset
df = pd.read_csv("titanic_sample.csv")
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Fare"] = df["Fare"].fillna(df["Fare"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# ---- 1. Filter with Multiple Conditions ----
# Female passengers who survived AND paid more than 50 in fare
filtered_df = df[(df["Sex"] == "female") & (df["Survived"] == 1) & (df["Fare"] > 50)]
print("=== Female Survivors with Fare > 50 ===")
print(filtered_df[["PassengerId", "Sex", "Pclass", "Age", "Fare", "Survived"]].head(10))
print(f"Total records: {len(filtered_df)}")

# ---- 2. Create New Column Based on Existing Data ----
def age_group(age):
    if age < 18:
        return "Child"
    elif age < 40:
        return "Adult"
    else:
        return "Senior"

df["AgeGroup"] = df["Age"].apply(age_group)
print("\n=== AgeGroup Column Created ===")
print(df[["Age", "AgeGroup"]].head(8))
print("\nDistribution:")
print(df["AgeGroup"].value_counts())

# ---- 3. Sort by Numerical Column ----
sorted_df = df.sort_values(by="Fare", ascending=False).reset_index(drop=True)
print("\n=== Top 5 Highest Fares ===")
print(sorted_df[["PassengerId", "Pclass", "Sex", "Fare", "Survived"]].head())

# ---- 4. Group and Compute Mean ----
grouped = df.groupby("Pclass")[["Age", "Fare", "Survived"]].mean().round(2)
print("\n=== Mean Age, Fare, Survival Rate by Pclass ===")
print(grouped)

sex_survival = df.groupby("Sex")["Survived"].mean().mul(100).round(1)
print("\n=== Survival Rate (%) by Sex ===")
print(sex_survival)
