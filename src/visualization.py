import pandas as pd
import matplotlib.pyplot as plt
import os

def create_tableau_visualization(forecast_path):
    """
    Simulate Tableau visualization by generating a Matplotlib plot.
    Saves the plot in the same directory as the input CSV.
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

    # ✅ Save to the same folder as the forecast CSV
     # Save plot
    plot_path = os.path.join(os.path.dirname(forecast_path), 'forecast_plot.png')
    os.makedirs(os.path.dirname(plot_path), exist_ok=True)
    plt.savefig(plot_path)



    print(f"✅ Visualization saved to {plot_path}")
