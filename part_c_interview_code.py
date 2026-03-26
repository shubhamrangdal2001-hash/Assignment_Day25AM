# Part C - Q2 Coding: Filter rows where column value > average
# Week 05 Day 25 AM | PG Diploma AI-ML & Agentic AI Engineering IIT Gandhinagar

import pandas as pd

df = pd.read_csv("titanic_sample.csv")
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Fare"] = df["Fare"].fillna(df["Fare"].median())

# Filter passengers with Fare greater than average Fare
avg_fare = df["Fare"].mean()
print(f"Average Fare: {avg_fare:.2f}")

above_avg = df[df["Fare"] > avg_fare]
print(f"Passengers with Fare > average: {len(above_avg)}")
print(above_avg[["PassengerId", "Pclass", "Sex", "Fare", "Survived"]].head(10))

# Same for Age column
avg_age = df["Age"].mean()
print(f"\nAverage Age: {avg_age:.2f}")
above_avg_age = df[df["Age"] > avg_age]
print(f"Passengers older than average: {len(above_avg_age)}")
print(above_avg_age[["PassengerId", "Age", "Sex", "Survived"]].head(10))
