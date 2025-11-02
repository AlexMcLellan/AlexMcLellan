import unittest
import pandas as pd
from radiometer.model import Radiometer

class TestRadiometer(unittest.TestCase):
    """Unit tests for the Radiometer class."""

    def setUp(self):
        """Set up a Radiometer instance for testing."""
        latitude = 40.0150
        longitude = -105.2705
        timestamp = pd.Timestamp('2023-10-27 12:00:00', tz='America/Denver')
        air_temperature = 15  # degrees Celsius
        relative_humidity = 50  # percent
        self.radiometer = Radiometer(latitude, longitude, timestamp, air_temperature, relative_humidity)

    def test_get_components(self):
        """Test that the get_components method returns a dictionary of floats."""
        components = self.radiometer.get_components()
        self.assertIsInstance(components, dict)
        for component, value in components.items():
            self.assertIsInstance(value, float)
            self.assertGreaterEqual(value, 0)

    def test_calculate_net_radiation(self):
        """Test that the calculate_net_radiation method returns a float."""
        net_radiation = self.radiometer.calculate_net_radiation()
        self.assertIsInstance(net_radiation, float)

if __name__ == "__main__":
    unittest.main()
