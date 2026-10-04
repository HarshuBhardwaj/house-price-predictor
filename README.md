# 🏠 House Price Prediction

A Machine Learning project that predicts house prices based on different property features. The project uses **Linear Regression** for prediction and **Streamlit** to provide an interactive web application.

## 📌 Project Overview

The goal of this project is to build a machine learning model that can estimate the price of a house based on features such as:

- Area
- Number of bedrooms
- Number of bathrooms
- Number of stories
- Main road access
- Guest room
- Basement
- Air conditioning
- Parking spaces
- Preferred area
- Furnishing status

The trained model is integrated with a Streamlit web application where users can enter house details and get an estimated price.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Jupyter Notebook

## 🤖 Machine Learning

The project follows these steps:

1. Data loading
2. Data cleaning
3. Exploratory Data Analysis (EDA)
4. Feature encoding
5. Outlier analysis
6. Feature scaling
7. Train-test split
8. Linear Regression model training
9. Model evaluation
10. Streamlit deployment

## 📊 Model Evaluation

The model is evaluated using regression metrics:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

## 🌐 Streamlit Application

The Streamlit application allows users to enter property details and receive a predicted house price.

### Input Features

- Area
- Bedrooms
- Bathrooms
- Stories
- Main road
- Guest room
- Basement
- Air conditioning
- Parking
- Preferred area
- Furnishing status

## 📁 Project Structure

```text
house-price-prediction/
│
├── app.py
├── house_price_model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
