import pandas as pd
from radiometer.model import Radiometer

def main():
    """Main function to run the radiometer simulation."""
    # Define sensor location (e.g., Boulder, CO)
    latitude = 40.0150
    longitude = -105.2705

    # Define a timestamp
    timestamp = pd.Timestamp('2023-10-27 12:00:00', tz='America/Denver')

    # Define atmospheric conditions
    air_temperature = 15  # degrees Celsius
    relative_humidity = 50  # percent

    # Create a Radiometer instance
    radiometer = Radiometer(latitude, longitude, timestamp, air_temperature, relative_humidity)

    # Get the radiation components
    components = radiometer.get_components()
    print("Radiation Components:")
    for component, value in components.items():
        print(f"  {component}: {value}")

    # Calculate and print the net radiation
    net_radiation = radiometer.calculate_net_radiation()
    print(f"Net Radiation: {net_radiation}")

if __name__ == "__main__":
    main()
