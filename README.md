# Week 05 Day 25 AM - EDA Assignment
### PG Diploma · AI-ML & Agentic AI Engineering · IIT Gandhinagar
Gitlink: https://github.com/shubhamrangdal2001-hash/Assignment_Day25AM.git
## Overview
This assignment covers Exploratory Data Analysis (EDA) using Pandas on a Titanic-style dataset (600 rows).

## Dataset
- **File:** `titanic_sample.csv`
- **Rows:** 600
- **Columns:** PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Fare, Embarked

## Files
| File | Description |
|------|-------------|
| `generate_dataset.py` | Generates the CSV dataset |
| `part_a_basic_eda.py` | Basic exploration, cleaning, stats, categorical analysis |
| `part_b_data_manipulation.py` | Filtering, new columns, sorting, groupby |
| `part_c_interview_code.py` | Interview Q2: filter rows above average |

## How to Run

### Step 1 — Generate Dataset
```bash
python generate_dataset.py
```

### Step 2 — Run Each Part
```bash
python part_a_basic_eda.py
python part_b_data_manipulation.py
python part_c_interview_code.py
```

## Requirements
```bash
pip install pandas numpy
```

## Key Findings
- Dataset has 600 rows with missing values in Age (90), Fare (10), and Embarked (5)
- Average passenger age: ~30 years | Average fare: ~30.43
- 37.8% of passengers survived
- Male passengers (392) outnumbered female (208)
- Most passengers embarked from Southampton (S)
