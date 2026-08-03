MERCURY_VALUE = 0.2408467
VENUS_VALUE = 0.61519726
EARTH_VALUE = 1.0
MARS_VALUE = 1.8808158
JUPITER_VALUE = 11.862615
SATURN_VALUE = 29.447498
URANUS_VALUE = 84.016846
NEPTUNE_VALUE = 164.79132

class SpaceAge:
    def __init__(self, seconds):
        self.years = seconds / 31_557_600
    
    def on_mercury(self):
        return round((self.years/MERCURY_VALUE), 2)
    
    def on_venus(self):
        return round((self.years/VENUS_VALUE), 2)

    def on_earth(self):
        return round((self.years/EARTH_VALUE), 2)

    def on_mars(self):
        return round((self.years/MARS_VALUE), 2)

    def on_jupiter(self):
        return round((self.years/JUPITER_VALUE), 2)

    def on_saturn(self):
        return round((self.years/SATURN_VALUE), 2)

    def on_uranus(self):
        return round((self.years/URANUS_VALUE), 2)

    def on_neptune(self):
        return round((self.years/NEPTUNE_VALUE), 2)