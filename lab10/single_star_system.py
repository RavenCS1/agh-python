from planet import Planet
from star import Star

class SingleStarSystem:
    _single_star_system_count = 0

    def __init__(self, star, planets = None):
        self._star = star
        if planets is None:
            planets = []
        self._planets = sorted(planets, key = lambda x: x.distance_from_star_mkm)
        SingleStarSystem._single_star_system_count += 1

    @property
    def star(self):
        return self._star

    @property
    def planets(self):
        return self._planets

    @star.setter
    def star(self, new_star):
        self._star = new_star

    @planets.setter
    def planets(self, new_planets):
        self._planets = new_planets

    def __del__(self):
        SingleStarSystem._single_star_system_count -= 1

    @classmethod
    def single_star_system_count(cls):
        return cls._single_star_system_count

    def __len__(self):
        return len(self._planets)

    def __contains__(self, planet):
        return planet in self._planets

    def __getitem__(self, index):
        return self._planets[index]

    def __delitem__(self, index):
        del self._planets[index]

    def add_planet(self, planet):
        self._planets.append(planet)
        self._planets.sort(key = lambda x: x.distance_from_star_mkm)

    @classmethod
    def from_dict(cls, other):
        star = Star.from_dict(other["star"])
        planets = [Planet.from_dict(x) for x in other.get("planets", [])]
        return cls(star, planets)

if __name__ == "__main__":

    sun = Star("Sun", 696340, 1.989e30, 3.83e26)

    mercury = Planet("Mercury", 2439.7, 3.3011e23, 57.91)
    venus   = Planet("Venus", 6051.8, 4.8675e24, 108.2)
    earth   = Planet("Earth", 6371.0, 5.97237e24, 149.6)
    mars    = Planet("Mars", 3389.5, 6.4171e23, 227.9)
    jupiter = Planet("Jupiter", 69911, 1.8982e27, 778.5)
    saturn  = Planet("Saturn", 58232, 5.6834e26, 1434)
    uranus  = Planet("Uranus", 25362, 8.6810e25, 2871)
    neptune = Planet("Neptune", 24622, 1.02413e26, 4495)
    pluto   = Planet("Pluto", 1188.3, 1.303e22, 5906.4)

    solar_system = SingleStarSystem(
        sun,
        [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]
    )

    print(f"Number of systems: {SingleStarSystem.single_star_system_count()}")
    solar_system_2 = SingleStarSystem(
        sun,
        [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]
    )
    print(f"Number of systems: {SingleStarSystem.single_star_system_count()}")
    del solar_system_2
    print(f"Number of systems: {SingleStarSystem.single_star_system_count()}")

    print(solar_system.star)
    for p in solar_system.planets:
        print(p)

    print(f"Number of planets: {len(solar_system)}")

    print(f"Contains pluto: {pluto in solar_system}")
    del solar_system[-1]
    print(f"Contains pluto: {pluto in solar_system}")

    solar_system.add_planet(pluto)
    print(f"Contains pluto: {pluto in solar_system}")

    test = SingleStarSystem.from_dict({
        "star" : {"name" : "Sun", "radius_km" : 696340, "mass_kg" : 1.989e30, "luminosity_w" : 3.83e26},
        "planets" : [
            {"name" : "Earth", "radius_km" : 6378, "mass_kg" : 5.972e24, "distance_from_star_mkm" : 149.6}
        ]
        })

    print(test.star)
    for p in test.planets:
        print(p)
