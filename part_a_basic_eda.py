# Part A - Basic EDA using Pandas
# Dataset: titanic_sample.csv (600 rows)
# Week 05 Day 25 AM | PG Diploma AI-ML & Agentic AI Engineering IIT Gandhinagar

import pandas as pd

# Load dataset
df = pd.read_csv("titanic_sample.csv")

# ---- 1. Basic Exploration ----
print("=== First 5 Rows ===")
print(df.head())

print("\n=== Last 5 Rows ===")
print(df.tail())

print("\n=== Shape ===")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\n=== Column Names ===")
print(df.columns.tolist())

# ---- 2. Data Cleaning ----
print("\n=== Missing Values ===")
print(df.isnull().sum())

# Fill missing Age with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Fare with median
df["Fare"] = df["Fare"].fillna(df["Fare"].median())

# Fill missing Embarked with mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

print("\n=== After Cleaning ===")
print(df.isnull().sum())

# ---- 3. Descriptive Statistics ----
print("\n=== describe() output ===")
print(df.describe())

print("\n=== Key Interpretations ===")
print(f"  Avg Age    : {df['Age'].mean():.2f}  |  Min: {df['Age'].min()}  |  Max: {df['Age'].max()}  |  Std: {df['Age'].std():.2f}")
print(f"  Avg Fare   : {df['Fare'].mean():.2f}  |  Max: {df['Fare'].max():.2f}  |  Std: {df['Fare'].std():.2f}")
print(f"  Survival % : {df['Survived'].mean()*100:.1f}%")

# ---- 4. Categorical Analysis ----
print("\n=== Unique Values in 'Sex' ===")
print(df["Sex"].unique())

print("\n=== Unique Values in 'Pclass' ===")
print(sorted(df["Pclass"].unique()))

print("\n=== Frequency - Sex ===")
print(df["Sex"].value_counts())

print("\n=== Frequency - Pclass ===")
print(df["Pclass"].value_counts().sort_index())

print("\n=== Frequency - Embarked ===")
print(df["Embarked"].value_counts())
