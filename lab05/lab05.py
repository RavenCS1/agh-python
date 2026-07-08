import random

# indexed by id
sensor_group = {
    1: {"type": "temperature", "active": True, "data_buffer": [22.5, 23.1, 22.8]},
    2: {"type": "humidity", "active": False, "data_buffer": [45, 47, 46]},
    3: {"type": "motion", "active": True, "data_buffer": [False, False, True]},
    4: {"type": "smoke", "active": True, "data_buffer": [False, False, False]},
    5: {"type": "temperature", "active": True, "data_buffer": [19.2, 18.9, 19.5]},
    6: {"type": "humidity", "active": True, "data_buffer": []},
    7: {"type": "motion", "active": False, "data_buffer": [False, False, False]},
    8: {"type": "smoke", "active": True, "data_buffer": [False, True, False]},
    9: {"type": "temperature", "active": True, "data_buffer": [25.3, 24.9, 25.7]},
    10: {"type": "humidity", "active": False, "data_buffer": [60, 61, 58]}
}

data_queue = [
    {"id": 1, "value": 23.4},
    {"id": 15, "value": 25},
    {"id": 3, "value": True},
    {"id": 6, "value": 51},
    {"id": 4, "value": True},
    {"id": 14, "value": False},
    {"id": 2, "value": 44},
    {"id": 9, "value": 24.5},
    {"id": 10, "value": 59},
    {"id": 7, "value": True},
    {"id": 5, "value": 18.7},
    {"id": 1, "value": 22},
    {"id": 1, "value": 13.5},
]

command_queue = [

    {"command": "emulate_readings"},
    {"command": "distribute_data"},

    {"command": "emulate_readings"},
    {"command": "distribute_data"},

    {"command": "toggle_status", "extra_info" : [3, 2, 1]},

    {"command": "emulate_readings"},
    {"command": "distribute_data"},

    {"command": "print_last_reading", "extra_info" : 7},

    {"command": "check_last_reading_condition", "extra_info" : {"sensor" : 5, "condition" : "< 50"}},

    {"command": "print_known_sensors"},

    {"command": "print_known_sensors", "extra_info" : {"active" : True, "type" : "smoke"}},

    {"command": "stop"},
]

# The structures above should not be treated as global variables.
# Function calls should not be modified.

################## Exercise 1 ######################
def last_reading(id, sensors = sensor_group):
    if id not in sensors:
        return (False, None)
    buffer = sensors[id]["data_buffer"]
    if not buffer:
        return (True, None)
    return (True, buffer[-1])

print()
print("Exercise 1:")
print(f"{last_reading(10)}, {last_reading(6)}, {last_reading(15)}")

################## Exercise 2 ######################
def add_value(id, val, sensors = sensor_group):
    if id not in sensors:
        return False
    if not isinstance(val, (int, float, bool)):
        return False
    sensors[id]["data_buffer"].append(val)
    return True

print()
print("Exercise 2:")
print(f"{add_value(15, 10)}, {add_value(6, 1)}, {add_value(6, 2)}, {add_value(6, 3)}, {add_value(6, "wrong type")}, {sensor_group[6]["data_buffer"]}")


################## Exercise 3 ######################
def check_condition(val, expr):
    return eval(f"{val}{expr}")

print()
print("Exercise 3:")
print(f"{check_condition(50, "> 20")}, {check_condition(20, "+ 30 <= 40")}")

################## Exercise 4 ######################
def distribute_data(queue = data_queue, sensors = sensor_group):
    while queue:
        data = queue.pop(0)
        result = add_value(data["id"], data["value"], sensors)
        if not result:
            known = list(sensors.keys())
            print(f"Error: attempted to add {data["value"]} to sensor {data["id"]}, but only these sensors exist: {known}.")

print()
print("Exercise 4:")

distribute_data()

for k, v in sensor_group.items():
    print(f"{k}: {v}")

################## Exercise 5 ######################
def toggle_status(*val, sensors = sensor_group):
    for id in val:
        if id in sensors:
            sensors[id]["active"] = not sensors[id]["active"]

print()
print("Exercise 5:")

print(f"{sensor_group[5]["active"]}, {sensor_group[6]["active"]}")
toggle_status(5, 6)
print(f"{sensor_group[5]["active"]}, {sensor_group[6]["active"]}")


################## Exercise 6 ######################
def filter_sensors(sensors = sensor_group, **filters):
    return {k: v for k, v in sensors.items() if all(v[key] == val for key, val in filters.items())}

print()
print("Exercise 6:")

for k, v in sensor_group.items():
    print(f"{k}: {v}")

print()
print("after filtering: active = True, type = 'motion':")
print()

for k, v in (filter_sensors(active = True, type = "motion")).items():
    print(f"{k}: {v}")

print()
print("after filtering: active = True, type = 'smoke':")
print()

for k, v in (filter_sensors(active = True, type = "smoke")).items():
    print(f"{k}: {v}")

################## Exercise 7 ######################
def emulate_readings(sensors = sensor_group, queue = data_queue):
    ids = list(sensors.keys())
    random.shuffle(ids)
    for id in ids:
        sensor = sensors[id]
        if not sensor["active"]:
            continue
        sensor_type = sensor["type"]
        if sensor_type == "temperature":
            val = random.randint(10, 20)
        elif sensor_type == "humidity":
            val = random.randint(60, 80)
        elif sensor_type == "motion":
            val = random.choice([True, False])
        elif sensor_type == "smoke":
            val = random.choice([True, False])
        else:
            val = None
        queue.append({"id": id, "value": val})

for _ in range(3):
    emulate_readings()

print()
print("Exercise 7:")

print(f"{data_queue}")

################## Exercise 8 ######################
def event_loop(sensors = sensor_group, queue = data_queue, commands = command_queue):
    while True:
        if not commands:
            break
        entry = commands.pop(0)
        command = entry["command"]
        info = entry.get("extra_info", None)

        print(f"Executing command: {command}")

        if command == "stop":
            break
        elif command == "emulate_readings":
            emulate_readings(sensors, queue)
        elif command == "distribute_data":
            distribute_data(queue, sensors)
        elif command == "toggle_status":
            toggle_status(*info, sensors = sensors)
        elif command == "print_last_reading":
            result = last_reading(info, sensors)
            print(f"  Last reading of sensor {info}: {result}")
        elif command == "check_last_reading_condition":
            id = info["sensor"]
            condition_str = info["condition"]
            found, operation = last_reading(id, sensors)
            if found and operation is not None:
                result = check_condition(operation, condition_str)
                print(f"  Sensor: {id} - last reading: {operation} - satisfies condition '{condition_str}': {result}")
            else:
                print(f"  Sensor: {id} was not found or data is missing.")
        elif command == "print_known_sensors":
            if info is None:
                for k, v in sensors.items():
                    print(f"  {k}: {v}")
            else:
                for k, v in filter_sensors(sensors, **info).items():
                    print(f"  {k}: {v}")

print()
print(f"Exercise 8:")

event_loop()
