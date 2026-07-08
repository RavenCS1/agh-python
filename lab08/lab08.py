
def pprint(struct):

    print()

    if isinstance(struct, (list, tuple)):

        if not struct:
            print("list/tuple is empty")

        else:

            for l in struct:
                print(l)

    elif isinstance(struct, dict):

        if not struct:
            print("dict is empty")

        else:

            id_width = max(max(len(str(k)) for k in struct.keys()), len("id"))

            if any(not isinstance(val, dict) for val in struct.values()):

                for k,v in struct.items():
                    print(f"{str(k):<{id_width}} :\t{v}")

            else:

                columns = []
                for inner_dict in struct.values():
                    for col in inner_dict:
                        if col not in columns:
                            columns.append(col)

                column_widths = {k : len(str(k)) for k in columns}

                for val in struct.values():
                    for k,v in val.items():
                        column_widths[k] = max(column_widths[k], len(str(v)))

                header = f"{'id':<{id_width}}  " + "  ".join(f"{col:<{column_widths[col]}}" for col in columns)
                print(header)
                print("-" * len(header))

                for k,v in struct.items():

                    row = f"{str(k):<{id_width}}"
                    for col in columns:
                        val = v.get(col, '')
                        row += f"  {str(val):^{column_widths[col]}}" if isinstance(val, (int, float)) else f"  {str(val):<{column_widths[col]}}"

                    print(row)

    else:
        print(struct)

    print()
    print()

################################################################################

import glob

#+++++++++++++++++++++++ Exercise 1 ++++++++++++++++++++++++++
def read_file(filename):
    readings = []
    with open(filename) as f:
        next(f)
        for line in f:
            values = line.split(",")
            readings.append({"time" : float(values[0]),
                           "temperature" : float(values[1]),
                           "pressure" : float(values[2]),
                           "phase" : values[3].rstrip("\n")})
    return readings

print()
print("Exercise 1:\n")

pprint(read_file("tank_A.dat"))
pprint(read_file("tank_D.dat"))

print('\n\n')

#+++++++++++++++++++++++ Exercise 2 ++++++++++++++++++++++++++
def load_all_tanks():
    files = glob.glob('*.dat')
    files.sort()
    result = {}
    for file in files:
        tank_name = file.split(".")[0]
        readings = []
        with open(file) as f:
            next(f)
            for line in f:
                readings.append(float(line.split(",")[1]))
        result[tank_name] = {"readings" : readings}
    return result

print("Exercise 2:\n")

tank_data = load_all_tanks() # Note: <-- our internal structure

for k, v in tank_data.items():
    print(k)
    pprint(v["readings"])

print('\n\n')

#+++++++++++++++++++++++ Exercise 3 ++++++++++++++++++++++++++
def add_accuracy(data = tank_data):
    for key in data.keys():
        data[key].update({"accuracy" : {}})
    with open("sensors.csv") as f:
        next(f)
        for line in f:
            values = line.split(",")
            if(values[3] == "temperatura"):
                data[values[2]]["accuracy"].update({"temperature" : float(values[7])})
            else:
                data[values[2]]["accuracy"].update({"pressure" : float(values[7])})

print("Exercise 3:\n")

add_accuracy()

for k, v in tank_data.items():
    print(k)
    pprint(v["accuracy"])

print('\n\n')

#+++++++++++++++++++++++ Exercise 4 ++++++++++++++++++++++++++
def select_readings():
    files = glob.glob('*.dat')
    files.sort()
    for file in files:
        new_file = file.split(".")[0] + "_selection.csv"
        with open(file) as infile, open(new_file, "w") as outfile:
            outfile.write(infile.readline())
            next(infile)
            for line in infile:
                values = line.split(",")
                if(273.14 <= float(values[1]) <= 273.18 and 610.657 <= float(values[2]) <= 612.657):
                    outfile.write(line)

print(f"Exercise 4:\n")

select_readings()

print('\n\n')

#+++++++++++++++++++++++ Exercise 5 ++++++++++++++++++++++++++
def write_phase_report(data = tank_data):
    with open("phase_report.txt", "w") as outfile:
        outfile.write("tank name,mixed phase occurrences\n")
        for key in data.keys():
            line = ""
            line += key + ","
            counter = 0
            with open(key + "_selection.csv") as infile:
                next(infile)
                for data_line in infile:
                    if(data_line.split(",")[3].strip() == "mieszana"):
                        counter += 1
            line += str(counter)
            outfile.write(line + "\n")

print("Exercise 5:\n")

write_phase_report()

print('\n\n')

#+++++++++++++++++++++++ Exercise 6 ++++++++++++++++++++++++++
def append_previous_report():
    with open("previous_phase_report.txt") as infile, open("phase_report.txt", "a") as outfile:
        next(infile)
        for line in infile:
            outfile.write(line)

print("Exercise 6:\n")
append_previous_report()

#+++++++++++++++++++++++ Exercise 7 ++++++++++++++++++++++++++
def generate_configs():
    with open("sensors.csv") as infile:
        next(infile)
        for line in infile:
            values = line.split(",")
            with open("sensor_" + values[0] + "_config.yaml", "w") as outfile:
                outfile.write("identifier:\n\n")
                outfile.write("\t" + "name: " + values[1] + "\n")
                outfile.write("\t" + "sensor_id: " + values[0] + "\n")
                outfile.write("\t" + "tank: " + values[2].split("_")[0].capitalize() + "_" + values[2].split("_")[1].capitalize() + "\n\n")
                outfile.write("configuration:\n\n")
                outfile.write("\t" + "sensor_type: " + values[3] + "\n")
                outfile.write("\t" + "unit: " + values[4] + "\n\n")
                outfile.write("operating_point:\n\n")
                outfile.write("\t" + "measurement_frequency: " + values[5] + "\n")
                outfile.write("\t" + "cycle_length: " + values[6] + "\n")
                outfile.write("\t" + "scaling_factor: " + values[8] + "\n")

print("Exercise 7:\n")
generate_configs()
