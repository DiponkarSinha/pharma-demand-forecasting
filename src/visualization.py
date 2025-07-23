import pandas as pd
import matplotlib.pyplot as plt

def create_tableau_visualization(forecast_path):
    """
    Simulate Tableau visualization by generating a Matplotlib plot.
    In production, this would connect to Tableau Server for dashboard creation.
    """
    # Load forecast data
    forecast = pd.read_csv(forecast_path)
    forecast['ds'] = pd.to_datetime(forecast['ds'])

    # Plot forecast
    plt.figure(figsize=(10, 6))
    plt.plot(forecast['ds'], forecast['yhat'], label='Forecast', color='blue')
    plt.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'],
                     color='blue', alpha=0.1, label='Confidence Interval')
    plt.title('Pharmaceutical Demand Forecast')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.legend()
    plt.savefig('data/forecast_plot.png')
    plt.close()
    print("Visualization saved to data/forecast_plot.png")

    # Placeholder for Tableau integration
    print("Tableau integration: In production, upload 'forecast_output.csv' to Tableau Server.")
    print("Create a dashboard with time series plots and metrics.")

if __name__ == "__main__":
    create_tableau_visualization('data/forecast_output.csv')