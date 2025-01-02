# Employee Attrition Prediction System

A machine learning project to predict employee attrition and help businesses identify and address factors contributing to employee turnover. The project uses a stacking ensemble model and includes a Flask-based web application for easy predictions.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Methodology](#methodology)
   - Data Preprocessing
   - Stacking Model
   - Hyperparameter Tuning
4. [Web Application](#web-application)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Results](#results)
8. [Future Enhancements](#future-enhancements)
9. [Technologies Used](#technologies-used)
10. [Acknowledgements](#acknowledgements)

---

## Introduction
Employee attrition is a major concern for many organizations, impacting productivity and costs. This project aims to classify employee attrition using a stacking ensemble model with Logistic Regression as the meta-learner. The solution is deployed as a web application to provide HR professionals with actionable insights.

---

## Dataset
The dataset used for this project is sourced from [Kaggle](https://www.kaggle.com/datasets/jash312/hr-employee-attrition-datasets?select=HR+Employee+data.csv). It contains information about employees, including their demographic details, job roles, and performance metrics.

**Features Include:**
- Age
- Job Satisfaction
- Work Environment Satisfaction
- Monthly Income
- Years at Company
- And more...

**Target Variable:** Attrition (Yes/No)

---

## Methodology

### Data Preprocessing
A Scikit-Learn pipeline was used to preprocess the dataset:
- Remove the outliers using percentile method 
- Numerical features were scaled using StandardScaler.
- Categorical features were encoded using One-Hot Encoding.
- Missing values were handled effectively to ensure model quality.

### Stacking Model
A stacking ensemble model was implemented with:
- **Base Learners:** Support Vector Machine (SVM), K-Nearest Neighbors (KNN), Random Forest (RF)
- **Meta Learner:** Logistic Regression

### Hyperparameter Tuning
Grid search was used to optimize the hyperparameters of the individual models for better performance.

---

## Web Application
The trained model was deployed using a Flask web application. The app allows users to:
1. Input employee data through a user-friendly form.
2. Get predictions on whether the employee is likely to leave.

---

## Technologies Used
- Python
- Scikit-Learn
- Flask
- Pickle
- HTML/CSS
- Jupyter Notebook

---
