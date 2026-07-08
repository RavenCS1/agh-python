import math

class Planet:
    def __init__(self, name, radius_km, mass_kg, distance_from_star_mkm):
        self._name = name
        self._radius_km = radius_km
        self._mass_kg = mass_kg
        self._distance_from_star_mkm = distance_from_star_mkm

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
    def distance_from_star_mkm(self):
        return self._distance_from_star_mkm

    def __str__(self):
        return f"Planet {self._name} with radius {self._radius_km} km and mass {self._mass_kg} kg. The planet is {self._distance_from_star_mkm} million km from its star."

    def __lt__(self, other):
        return self._mass_kg < other._mass_kg

    def __eq__(self, other):
        if not isinstance(other, Planet):
            return False
        return all([self._name.casefold() == other._name.casefold(),
                   math.isclose(self._radius_km, other._radius_km),
                   math.isclose(self._mass_kg, other._mass_kg),
                   math.isclose(self._distance_from_star_mkm, other._distance_from_star_mkm)])

    def orbital_period(self):
        return math.pow(self.distance_from_star_mkm / 149.6 , 1.5)

    @staticmethod
    def gravitational_force(mass1_kg, mass2_kg, distance_km):
        return (6.674e-11 * mass1_kg * mass2_kg) / (distance_km * distance_km * 1000 * 1000)

    @classmethod
    def from_dict(cls, other):
        return cls(
            other["name"],
            other["radius_km"],
            other["mass_kg"],
            other["distance_from_star_mkm"],
        )

if __name__ == "__main__":

    earth = Planet("Earth", 6378, 5.972e24, 149.6)

    earth_2 = Planet.from_dict({"name" : "Earth", "radius_km" : 6378, "mass_kg" : 5.972e24, "distance_from_star_mkm" : 149.6})

    venus = Planet("Venus", 6051.8, 4.867e24, 108.2)
    mars = Planet("Mars", 3389.5, 6.39e23, 227.9)

    print(earth)
    print(earth.name)
    print(earth.radius_km)
    print(earth.mass_kg)
    print(earth.distance_from_star_mkm)

    print(f"Are both earths identical? {earth == earth_2}")
    print(f"Are earth and venus identical? {earth == venus}")
    print(f"mars < venus < earth by mass? {mars < venus < earth}")

    print(f"Mars: orbital period = {mars.orbital_period()} Earth years.")
    print(f"Gravitational force between Earth and the Sun = {Planet.gravitational_force(earth.mass_kg, 1.989e30, earth.distance_from_star_mkm * 1e6)} N.")
