import unittest
from radiometer.model import Radiometer

class TestRadiometer(unittest.TestCase):
    """Unit tests for the Radiometer class."""

    def setUp(self):
        """Set up a Radiometer instance for testing."""
        self.radiometer = Radiometer(
            shortwave_up=100,
            shortwave_down=500,
            longwave_up=300,
            longwave_down=200
        )

    def test_get_components(self):
        """Test that the get_components method returns the correct values."""
        components = self.radiometer.get_components()
        self.assertEqual(components["shortwave_up"], 100)
        self.assertEqual(components["shortwave_down"], 500)
        self.assertEqual(components["longwave_up"], 300)
        self.assertEqual(components["longwave_down"], 200)

    def test_calculate_net_radiation(self):
        """Test that the calculate_net_radiation method returns the correct value."""
        net_radiation = self.radiometer.calculate_net_radiation()
        self.assertEqual(net_radiation, 300)

if __name__ == "__main__":
    unittest.main()
