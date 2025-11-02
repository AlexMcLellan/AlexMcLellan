import pandas as pd
import numpy as np
from pvlib import location
from pvlib import irradiance

class Radiometer:
    """A 4-component radiometer model that takes into account sensor location and time of day."""

    def __init__(self, latitude, longitude, timestamp, air_temperature, relative_humidity):
        """Initializes the Radiometer with sensor location, a timestamp, air temperature, and relative humidity."""
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp
        self.air_temperature = air_temperature
        self.relative_humidity = relative_humidity
        self._calculate_radiation_components()

    def _calculate_radiation_components(self):
        """Calculates the four radiation components using pvlib and empirical models."""
        # Create a location object
        site = location.Location(self.latitude, self.longitude)

        # Create a DatetimeIndex for the single timestamp
        times = pd.DatetimeIndex([self.timestamp])

        # Calculate solar position
        solar_position = site.get_solarposition(times)

        # Calculate clear-sky irradiance
        clearsky = site.get_clearsky(times, model='ineichen')

        # Shortwave down is the global horizontal irradiance (GHI)
        self.shortwave_down = clearsky['ghi'].iloc[0]

        # Assume a constant albedo of 0.2 for the ground surface
        self.shortwave_up = 0.2 * self.shortwave_down

        # Longwave radiation calculations
        stefan_boltzmann_constant = 5.67e-8

        # Longwave down calculated using the Brutsaert (1975) model for clear-sky emissivity
        # See: https://esd.copernicus.org/articles/14/1363/2023/
        vapor_pressure = (self.relative_humidity / 100) * 6.112 * np.exp((17.67 * self.air_temperature) / (self.air_temperature + 243.5))
        emissivity_clear_sky = 1.24 * (vapor_pressure / (self.air_temperature + 273.15))**(1/7)
        self.longwave_down = emissivity_clear_sky * stefan_boltzmann_constant * (self.air_temperature + 273.15)**4

        # Longwave up is calculated from longwave_down assuming surface temperature equals air temperature
        surface_emissivity = 0.98
        self.longwave_up = (surface_emissivity / emissivity_clear_sky) * self.longwave_down


    def calculate_net_radiation(self):
        """Calculates the net radiation."""
        return (self.shortwave_down - self.shortwave_up) + (self.longwave_down - self.longwave_up)

    def get_components(self):
        """Returns the four radiation components."""
        return {
            "shortwave_up": self.shortwave_up,
            "shortwave_down": self.shortwave_down,
            "longwave_up": self.longwave_up,
            "longwave_down": self.longwave_down,
        }
