


import pandas as pd
import os

def preprocess_data(input_path, output_path):
    """
    Preprocess sales data, simulating AWS Glue cleaning.
    Input: CSV with date, product, sales columns.
    Output: Cleaned CSV with 'ds' (date) and 'y' (sales) columns.
    """
    # Load data
    data = pd.read_csv(input_path)

    # Simulate SAP S/4HANA data extraction and cleaning
    data['date'] = pd.to_datetime(data['date'])
    data = data.dropna(subset=['sales'])  # Remove missing sales
    data = data[data['sales'] >= 0]      # Remove negative sales
    data = data.groupby('date').agg({'sales': 'sum'}).reset_index()  # Aggregate by date

    # Prepare for Prophet
    data = data.rename(columns={'date': 'ds', 'sales': 'y'})

    # Save cleaned data
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    data.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

if __name__ == "__main__":
    preprocess_data('data/sample_demand_data.csv', 'data/cleaned_demand_data.csv')