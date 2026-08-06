# 
 Analytics Pipeline

Overview

This module builds an analytics pipeline using the Titanic dataset. The pipeline performs data preprocessing, feature engineering, model training, evaluation, and prediction using machine learning models.

Features

- Load Titanic dataset
- Handle missing values
- Encode categorical features
- Feature scaling (if applicable)
- Train machine learning models
- Evaluate model performance
- Save the trained pipeline as "titanic_pipeline.pkl"

Project Structure

analytics_pipeline/
│── analytics_pipeline.ipynb
│── titanic.csv
│── titanic_pipeline.pkl
│── README.md
│── requirements.txt

How to Run

1. Install the required packages:

pip install -r requirements.txt

2. Open the notebook:

jupyter notebook analytics_pipeline.ipynb

3. Run all cells from top to bottom.

Output

- Cleaned dataset
- Trained machine learning model
- Evaluation metrics
- Saved pipeline ("titanic_pipeline.pkl")
