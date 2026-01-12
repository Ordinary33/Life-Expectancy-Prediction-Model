# Life Expectancy Predictor Model

![Python](https://img.shields.io/badge/python-3.13-blue)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.3.0-orange)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange)

Predict life expectancy of countries based on health, demographic, and economic indicators using machine learning.

## Table of Contents

- [Overview](#overview)  
- [Dataset](#dataset)  
- [Project Structure](#project-structure)   
- [Modeling](#modeling)  
- [Future Improvements](#future-improvements)  
---

## Overview

This project predicts life expectancy of countries using machine learning. It demonstrates a complete ML pipeline:

1. Data Cleaning  
2. Exploratory Data Analysis (EDA)  
3. Preprocessing  
4. Train/Validation/Test Split  
5. Model Training & Evaluation  

---

## Dataset

- Contains country-level statistics including:  
  - `Adult Mortality`, `Alcohol`, `BMI`, `GDP`, `Schooling`, `HIV/AIDS`, etc.  
- Source: [https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who/code]  
- Preprocessing steps:
  - Interpolation of missing numerical values per country  
  - Mean imputation for remaining missing values  
  - Encoding categorical features like `Country`  

---

## Project Structure
```text
life-expectancy-predictor/
│
├─ data/ # Raw and processed datasets
├─ notebooks/ # Jupyter notebooks for cleaning, EDA, modeling
├─ src/ # Python scripts for preprocessing, modeling
├─ models/ # Saved trained models
├─ README.md
├─ requirements.txt
└─ .gitignore
```

## Future Improvements
- Experiment with additional regression algorithms  
- Feature selection / dimensionality reduction  

