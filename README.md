# Pharmaceutical Demand Forecasting

A machine learning project to forecast pharmaceutical demand using the Prophet library, with a pipeline simulating data extraction, cleaning, modeling, evaluation, and visualization. The project demonstrates skills in time series forecasting, data preprocessing, cloud integration, and interactive visualizations.

## Project Description

This project builds an end-to-end workflow for forecasting pharmaceutical demand, replicating a professional data science pipeline:

- **Data Source**: Synthetic dataset mimicking SAP S/4HANA sales data, representing monthly pharmaceutical sales.
- **Preprocessing**: Data cleaning and transformation using Pandas, simulating AWS Glue jobs.
- **Modeling**: Time series forecasting using Meta's Prophet library.
- **Evaluation**: Model performance assessed using Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and F1 score (for binary classification of demand).
- **Deployment**: Simulated AWS SageMaker deployment for model hosting.
- **Visualization**: Interactive visualizations using D3.js, integrated into a Streamlit app.
- **Application**: A Streamlit app for user-friendly forecasting and visualization of pharmaceutical demand.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/DiponkarSinha/pharma-demand-forecasting.git
   cd pharma-demand-forecasting