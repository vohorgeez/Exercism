class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    orbital_periods = {
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'earth': 1.0,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132
    }
    
    def on_mercury(self):
        return round(self.seconds / 31557600 / self.orbital_periods['mercury'], 2)
    
    def on_venus(self):
        return round(self.seconds / 31557600 / self.orbital_periods['venus'], 2)
    
    def on_earth(self):
        return round(self.seconds / 31557600 / self.orbital_periods['earth'], 2)
    
    def on_mars(self):
        return round(self.seconds / 31557600 / self.orbital_periods['mars'], 2)
    
    def on_jupiter(self):
        return round(self.seconds / 31557600 / self.orbital_periods['jupiter'], 2)
    
    def on_saturn(self):
        return round(self.seconds / 31557600 / self.orbital_periods['saturn'], 2)
    
    def on_uranus(self):
        return round(self.seconds / 31557600 / self.orbital_periods['uranus'], 2)
    
    def on_neptune(self):
        return round(self.seconds / 31557600 / self.orbital_periods['neptune'], 2)