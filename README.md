💊 Pharmaceutical Demand Forecasting
Live Demo: Pharma Forecasting App

A machine learning project to forecast pharmaceutical demand using synthetic data and Meta's Prophet library. The pipeline simulates real-world data workflows including data generation, preprocessing, time series modeling, cloud deployment, and interactive visualization using Streamlit and D3.js.

🚀 Project Overview
This project replicates a professional ML pipeline tailored for the pharmaceutical supply chain. It simulates how organizations can use data science to anticipate drug demand and optimize inventory.

🔍 Key Highlights
📊 Synthetic Dataset: Emulates SAP S/4HANA sales data for monthly pharmaceutical sales.

🧹 Data Preprocessing: Cleaned using pandas, simulating AWS Glue transformations.

📈 Forecasting Model: Built with Meta's Prophet, a robust time series forecasting tool.

✅ Evaluation Metrics: MAE, MSE, RMSE for regression and F1-score for binary demand classification.

☁️ Cloud Simulation: Mimics AWS SageMaker for deployment readiness.

📉 Visualization: D3.js-powered visuals embedded in a user-friendly Streamlit app.

🧪 Try It Yourself
🔗 Launch the App:
https://pharma-forecasting-app.streamlit.app/

Interact with the model, select forecast ranges, and view dynamic charts powered by D3.js and Streamlit.

⚙️ Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/DiponkarSinha/pharma-demand-forecasting.git
cd pharma-demand-forecasting
2. Install Dependencies
Ensure Python 3.8+ is installed. Then install all required libraries:

bash
Copy
Edit
pip install -r requirements.txt
Dependencies: pandas, prophet, streamlit, numpy, scikit-learn

3. Prepare the Data
Place your dataset in the /data folder. The expected format is:

csv
Copy
Edit
| ds        | y       |
|-----------|---------|
| 2022-01-01| 1534.23 |
| 2022-02-01| 1589.40 |
Use sample_demand_data.csv for testing.

4. Run the App Locally
bash
Copy
Edit
streamlit run app.py
5. Run the Full Workflow in Jupyter
Open the notebook to explore the full data science process:

bash
Copy
Edit
jupyter notebook notebooks/demand_forecasting.ipynb
📊 Visualizations
The app includes interactive charts:

Line chart of historical vs. forecasted demand

Powered by D3.js, rendered from visualizations/d3_visualization.html

🗂️ Project Structure
bash
Copy
Edit
pharma-demand-forecasting/
├── data/
│   ├── sample_demand_data.csv        # Input dataset
│   ├── cleaned_demand_data.csv       # After preprocessing
│   ├── forecast_output.csv           # Prophet output
│   └── d3_data.csv                   # Formatted for D3.js
├── src/
│   ├── data_preprocessing.py         # Data cleaning functions
│   ├── model_training.py             # Prophet training logic
│   └── aws_integration.py            # SageMaker simulation script
├── visualizations/
│   └── d3_visualization.html         # Embedded D3.js chart
├── notebooks/
│   └── demand_forecasting.ipynb      # Full ML pipeline
├── app.py                            # Streamlit app
├── requirements.txt                  # Dependencies
└── README.md                         # You're here!
📜 License
This project is licensed under the MIT License.

🙋‍♂️ Contact
Diponkar Sinha
LinkedIn • GitHub
