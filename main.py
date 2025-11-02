from radiometer.model import Radiometer

def main():
    """Main function to run the radiometer simulation."""
    # Example values for the four radiation components
    shortwave_up = 100
    shortwave_down = 500
    longwave_up = 300
    longwave_down = 200

    # Create a Radiometer instance
    radiometer = Radiometer(shortwave_up, shortwave_down, longwave_up, longwave_down)

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
