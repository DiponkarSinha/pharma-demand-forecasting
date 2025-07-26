Pharmaceutical Demand Forecasting

A machine learning project to forecast pharmaceutical demand using the Prophet library, with a pipeline simulating data extraction, cleaning, modeling, evaluation, and visualization. The project demonstrates skills in time series forecasting, data preprocessing, cloud integration, and interactive visualizations.

Project Description

This project builds an end-to-end workflow for forecasting pharmaceutical demand, replicating a professional data science pipeline:





Data Source: Synthetic dataset mimicking SAP S/4HANA sales data, representing monthly pharmaceutical sales.



Preprocessing: Data cleaning and transformation using Pandas, simulating AWS Glue jobs.



Modeling: Time series forecasting using Meta's Prophet library.



Evaluation: Model performance assessed using Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and F1 score (for binary classification of demand).



Deployment: Simulated AWS SageMaker deployment for model hosting.



Visualization: Interactive visualizations using D3.js, integrated into a Streamlit app.



Application: A Streamlit app for user-friendly forecasting and visualization of pharmaceutical demand.

Demo

Try the deployed Streamlit app to interact with the forecasting model and view visualizations:

🔗 Pharma Forecasting App

Setup Instructions





Clone the Repository:

git clone https://github.com/DiponkarSinha/pharma-demand-forecasting.git
cd pharma-demand-forecasting



Install Dependencies: Ensure Python 3.8+ is installed. Then, install required packages:

pip install -r requirements.txt

Dependencies: pandas, prophet, streamlit, numpy, scikit-learn.



Run the Streamlit App Locally: Launch the app to interact with the forecasting model and view D3.js visualizations:

streamlit run app.py





Data Preparation: Place the synthetic dataset (sample_demand_data.csv) in the data/ directory. The dataset should have columns ds (date) and y (demand).



Run the Notebook: The Jupyter notebook (notebooks/demand_forecasting.ipynb) contains the full workflow:





Preprocessing, training, evaluation, AWS simulation, and visualization. Run it using:

jupyter notebook notebooks/demand_forecasting.ipynb

Visualization

Interactive visualizations are implemented using D3.js, showing:





Historical vs. forecasted demand as line charts.




The D3.js visualization is generated in visualizations/d3_visualization.html and embedded in the Streamlit app.

Project Structure

pharma-demand-forecasting/
├── data/
│   ├── sample_demand_data.csv
│   ├── cleaned_demand_data.csv
│   ├── forecast_output.csv
│   └── d3_data.csv
├── src/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   └── aws_integration.py
├── visualizations/
│   └── d3_visualization.html
├── notebooks/
│   └── demand_forecasting.ipynb
├── app.py
├── requirements.txt
└── README.md

License

This project is licensed under the MIT License. See the LICENSE file for details.