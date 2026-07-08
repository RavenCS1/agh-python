import math

class Star:
    def __init__(self, name, radius_km, mass_kg, luminosity_w):
        self._name = name
        self._radius_km = radius_km
        self._mass_kg = mass_kg
        self._luminosity_w = luminosity_w

    @property
    def name(self):
        return self._name

    @property
    def radius_km(self):
        return self._radius_km

    @property
    def mass_kg(self):
        return self._mass_kg

    @property
    def luminosity_w(self):
        return self._luminosity_w

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @radius_km.setter
    def radius_km(self, new_radius):
        self._radius_km = new_radius

    @mass_kg.setter
    def mass_kg(self, new_mass):
        self._mass_kg = new_mass

    @luminosity_w.setter
    def luminosity_w(self, new_luminosity):
        self._luminosity_w = new_luminosity

    def __str__(self):
        return f"Star {self._name} with radius {self._radius_km} km and mass {self._mass_kg} kg. The star has a luminosity of {self._luminosity_w}."

    def __lt__(self, other):
        return self._mass_kg < other._mass_kg

    def __eq__(self, other):
        if not isinstance(other, Star):
            return False
        return all([self._name.casefold() == other._name.casefold(),
                   math.isclose(self._radius_km, other._radius_km),
                   math.isclose(self._mass_kg, other._mass_kg),
                   math.isclose(self._luminosity_w, other._luminosity_w)])

    @classmethod
    def from_dict(cls, other):
        return cls(
            other["name"],
            other["radius_km"],
            other["mass_kg"],
            other["luminosity_w"],
        )

if __name__ == "__main__":

    sun = Star("Sun", 696340, 1.989e30, 3.83e26)

    sun_2 = Star.from_dict({"name" : "Sun", "radius_km" : 696340, "mass_kg" : 1.989e30, "luminosity_w" : 3.83e26})

    proxima_centauri = Star("Proxima Centauri", 107280, 2.428e29, 6.506e23)
    barnards_star = Star("Barnard's Star", 136360, 2.864e29, 1.531e23)

    print(sun)
    print(sun.name)
    print(sun.radius_km)
    print(sun.mass_kg)
    print(sun.luminosity_w)

    print(f"Are both suns identical? {sun == sun_2}")
    print(f"proxima_centauri < barnards_star < sun by mass? {proxima_centauri < barnards_star < sun}")

    print(proxima_centauri.luminosity_w)
    proxima_centauri.luminosity_w = 1
    print(proxima_centauri.luminosity_w)
