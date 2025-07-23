from prophet import Prophet
import pandas as pd
import os

def train_and_forecast(input_path, output_path, forecast_periods=365):
    """
    Train Prophet model and generate forecasts.
    Input: Cleaned CSV with 'ds' and 'y' columns.
    Output: Forecast CSV with 'ds', 'yhat', 'yhat_lower', 'yhat_upper'.
    """
    # Load cleaned data
    data = pd.read_csv(input_path)

    # Initialize and train Prophet model
    model = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=True)
    model.fit(data)

    # Create future dataframe and forecast
    future = model.make_future_dataframe(periods=forecast_periods)
    forecast = model.predict(future)

    # Save forecast
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(output_path, index=False)
    print(f"Forecast saved to {output_path}")

    return model, forecast

if __name__ == "__main__":
    train_and_forecast('data/cleaned_demand_data.csv', 'data/forecast_output.csv')