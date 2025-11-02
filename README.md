# 4-Component Radiometer Simulation

This project is a Python simulation of a 4-component radiometer. It provides a model for calculating net radiation from the four primary components of solar and terrestrial radiation, taking into account the sensor's location and the time of day.

## Installation

This project uses the `pvlib-python` library to model solar radiation. To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To run the simulation, execute the `main.py` script:

```bash
python3 main.py
```

The script will print the individual radiation components and the calculated net radiation to the console for a predefined location (Boulder, CO) and time. You can modify these values in the `main.py` script to simulate different scenarios.
