
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

import random

loaded_logs = [
    {"ip": "192.168.1.1", "timestamp": "2023-04-01T12:00:00", "method": "GET", "page": "www.google.com", "status": 200},
    {"ip": "192.168.1.1", "timestamp": "2023-04-01T12:05:00", "method": "POST", "page": "www.google.com", "status": 404},
    {"ip": "192.168.1.1", "timestamp": "2023-04-01T12:10:00", "method": "GET", "page": "www.github.com", "status": 200},
    {"ip": "192.168.1.2", "timestamp": "2023-04-01T12:15:00", "method": "POST", "page": "www.facebook.com", "status": 503},
    {"ip": "192.168.1.2", "timestamp": "2023-04-01T12:20:00", "method": "GET", "page": "www.twitter.com", "status": 200},
    {"ip": "192.168.1.3", "timestamp": "2023-04-01T12:25:00", "method": "POST", "page": "www.instagram.com", "status": 403},
    {"ip": "192.168.1.3", "timestamp": "2023-04-01T12:30:00", "method": "GET", "page": "www.github.com", "status": 200},
    {"ip": "192.168.1.4", "timestamp": "2023-04-01T12:35:00", "method": "GET", "page": "www.stackoverflow.com", "status": 200},
    {"ip": "192.168.1.4", "timestamp": "2023-04-01T12:40:00", "method": "POST", "page": "www.google.com", "status": 500},
    {"ip": "192.168.1.5", "timestamp": "2023-04-01T12:45:00", "method": "GET", "page": "www.reddit.com", "status": 200},
    {"ip": "192.168.1.5", "timestamp": "2023-04-01T12:50:00", "method": "GET", "page": "www.youtube.com", "status": 400},
    {"ip": "192.168.1.1", "timestamp": "2023-04-01T12:55:00", "method": "POST", "page": "www.google.com", "status": 200},
    {"ip": "192.168.1.1", "timestamp": "2023-04-01T13:00:00", "method": "GET", "page": "www.reddit.com", "status": 404},
    {"ip": "192.168.1.2", "timestamp": "2023-04-01T13:05:00", "method": "GET", "page": "www.instagram.com", "status": 200},
    {"ip": "192.168.1.2", "timestamp": "2023-04-01T13:10:00", "method": "POST", "page": "www.twitter.com", "status": 500},
]


#+++++++++++++++++++++++ Exercise 1 ++++++++++++++++++++++++++
def line(lines = loaded_logs):
    for line in lines:
        yield line

print()
print("Exercise 1:\n")

for l in line():
   print(l)

print('\n\n')

#+++++++++++++++++++++++ Exercise 2 ++++++++++++++++++++++++++
def format_line(fun = line):
    for entry in fun():
        yield tuple(entry.values())


print("Exercise 2:\n")

for l in format_line():
   print(l)

print('\n\n')

#+++++++++++++++++++++++ Exercise 3 ++++++++++++++++++++++++++
def successful_entries(lines = loaded_logs):
    yield from filter(lambda x: 200<= x["status"] < 300, lines)



print("Exercise 3:\n")

for l in successful_entries():
   print(l)

print('\n\n')


#+++++++++++++++++++++++ Exercise 4 ++++++++++++++++++++++++++
def group_by_ip(lines = loaded_logs):
    groups = {}
    for line in lines:
        groups.setdefault(line["ip"], []).append(line)
    yield from groups.values()



print(f"Exercise 4:\n")

for l in group_by_ip():
   pprint(l)

print('\n\n')

#+++++++++++++++++++++++ Exercise 5 ++++++++++++++++++++++++++
def group_by_ip_threshold(threshold, fun = group_by_ip):
    yield from filter(lambda x: len(x) >= threshold, fun())



print("Exercise 5:\n")

for l in group_by_ip_threshold(3):
    pprint(l)

print('\n\n')

#+++++++++++++++++++++++ Exercise 6 ++++++++++++++++++++++++++
def random_subset(lines = loaded_logs):
    while True:
        value = yield
        if value < 0:
            result = []
        elif value >= len(lines):
            result = lines
        else:
            result = random.sample(lines, value)
        value = yield result


print("Exercise 6:\n")


random_gen = random_subset(loaded_logs)
next(random_gen)

for i in range(-1, 5):
   pprint(random_gen.send(i))
   next(random_gen)



#+++++++++++++++++++++++ Exercise 7+8 ++++++++++++++++++++++++++
def sliding_window(size, lines = loaded_logs):
    n = len(loaded_logs)
    if size <= 0:
        return
    end = min(size, n)
    begin = 0
    while end <= n:
        window = lines[begin:end]
        methods = list(map(lambda x: x["method"], window))
        pages = list(map(lambda x: x["page"], window))
        statuses = list(map(lambda x: x["status"], window))
        method_counts = {}
        page_counts = {}
        status_counts = {}
        for m in methods:
            method_counts[m] = method_counts.get(m, 0) + 1
        for s in pages:
            page_counts[s] = page_counts.get(s, 0) + 1
        for st in statuses:
            status_counts[st] = status_counts.get(st, 0) + 1
        yield {
            "window": (begin, end - 1),
            "method": method_counts,
            "page": page_counts,
            "status": status_counts,
        }
        if size >= n:
            return
        begin += 1
        end += 1


print("Exercise 7:\n")

print("Window size: 6")
for l in sliding_window(6):
   pprint(l)

