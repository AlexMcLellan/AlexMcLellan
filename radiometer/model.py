class Radiometer:
    """A 4-component radiometer model."""

    def __init__(self, shortwave_up, shortwave_down, longwave_up, longwave_down):
        """Initializes the Radiometer with the four radiation components."""
        self.shortwave_up = shortwave_up
        self.shortwave_down = shortwave_down
        self.longwave_up = longwave_up
        self.longwave_down = longwave_down

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
