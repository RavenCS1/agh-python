from dataclasses import dataclass, field
import uuid

@dataclass
class Driver:
    name : str
    license_type : str
    vehicle : str

@dataclass
class Package:
    destination : str
    weight : float
    priority : str
    id : str = field(default_factory = lambda: str(uuid.uuid4()))

@dataclass
class VehicleStatus:
    fueled : bool = True
    roadworthy : bool = True

@dataclass
class Vehicle:
    registration_number : str
    capacity : float
    vehicle_type : str
    parameters : dict = field(default_factory = lambda: {"GPS": "yes"})
    status : VehicleStatus = field(default_factory = VehicleStatus)

def handle_package(package):
    match package.priority:
        case "high":
            print("Package has high priority")
        case "medium":
            print("Package has medium priority")
        case "low":
            print("Package has low priority")
        case _ as p:
            print(f"Invalid package priority - {p}")

def can_drive(driver, vehicle):
    info = (driver.license_type, vehicle.vehicle_type)
    match info:
        case ("C", "truck")|("C", "van")|("B", "van"):
            return True
        case _:
            return False

def categorize_package(package):
    info = [package.priority, package.weight]
    match info:
        case ["high", weight] if weight > 10:
            print("large,priority")
        case ["high", weight] if weight < 2:
            print("small,priority")
        case ["high", weight] if weight >= 2 and weight <= 10:
            print("regular, priority")
        case [priority, _] if priority != "high":
            print("standard")

def ready_for_road(vehicle, check_gps = False):
    info = [vehicle.status.fueled, vehicle.status.roadworthy, vehicle.parameters["GPS"], check_gps]
    match info:
        case [fueled, roadworthy, GPS, checker] if all([fueled, roadworthy]) and not checker:
            return True
        case [fueled, roadworthy, GPS, checker] if all([fueled, roadworthy]) and checker and GPS == "yes":
            return True
        case [fueled, roadworthy, GPS, checker] if not all([fueled, roadworthy]) or checker and GPS == "no":
            return False

class WarehousePackage:
    __match_args__ = ("code", "status", "weight")

    def __init__(self, code, status, weight):
        self.code = code
        self.status = status
        self.weight = weight

def assign_to_warehouse(package):
    match package:
        case WarehousePackage(_, "awaiting shipment", w) if w > 20:
            print(f"{package.code}: -> warehouse 1")
        case WarehousePackage(_, "awaiting shipment", w) if w <= 20:
            print(f"{package.code}: -> warehouse 2")
        case WarehousePackage(_, "received", _):
            print(f"{package.code}: -> warehouse 3")
        case _:
            print(f"{package.code}: -> warehouse unknown")

if __name__ == "__main__":

    print("\ncreating data")
    vehicle1 = Vehicle("KR12345", 15.0, "truck")
    driver1 = Driver("Jan", "C", vehicle1.registration_number)
    package1 = Package(destination="Warszawa", weight=12.5, priority="high")
    package2 = Package(destination="Kraków", weight=1.5, priority="high")
    package3 = Package(destination="Gdańsk", weight=5.0, priority="medium")
    print(vehicle1)
    print(driver1)
    print(package1)


    print("\n priority")
    handle_package(package1)
    handle_package(package2)
    handle_package(Package(destination="Warszawa", weight=12.5, priority="invalid"))

    print("\n permissions:")
    print("Expected: True ->", can_drive(driver1, vehicle1))

    vehicle2 = Vehicle("WW11223", 10.0, "van")
    driver2 = Driver("Anna", "B", vehicle2.registration_number)
    print("Expected: True ->", can_drive(driver2, vehicle2))

    driver3 = Driver("Tomek", "B", "AB11111")
    vehicle3 = Vehicle("AB11111", 20.0, "truck")
    print("Expected: False ->", can_drive(driver3, vehicle3))

    print("\n categorization:")
    categorize_package(package1)
    categorize_package(package2)
    categorize_package(package3)

    print("\n readiness:")
    print("Expected: True ->", ready_for_road(vehicle1))
    vehicle1.status.fueled = False
    print("Expected: False ->", ready_for_road(vehicle1))
    vehicle2.parameters["GPS"] = "no"
    print("Expected: True ->", ready_for_road(vehicle2, check_gps=False))
    print("Expected: False ->", ready_for_road(vehicle2, check_gps=True))

    print("\n__match_args__:")
    mp1 = WarehousePackage("PX01", "awaiting shipment", 25)
    mp2 = WarehousePackage("PX02", "awaiting shipment", 15)
    mp3 = WarehousePackage("PX03", "received", 5)
    mp4 = WarehousePackage("PX04", "other", 8)

    assign_to_warehouse(mp1)
    assign_to_warehouse(mp2)
    assign_to_warehouse(mp3)
    assign_to_warehouse(mp4)
