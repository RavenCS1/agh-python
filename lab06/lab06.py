from functools import reduce


def pprint(struct):

    print()

    if isinstance(struct, (list, tuple)):

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

user_db = {
    1: {"name": "Tomek", "age": 30, "email": "tomek@example.com", "status": "employee"},
    2: {"name": "Kasia", "age": 25, "email": "kasia@mydomain.com", "status": "student"},
    3: {"name": "Alicja", "age": 22, "email": "alicja@gmail.com", "status": "student"},
    4: {"name": "Jan", "age": 35, "email": "jan@yahoo.com", "status": "employee"},
    5: {"name": "Marek", "age": 40, "email": "marek@company.org", "status": "employee"},
    6: {"name": "Ola", "age": 28, "email": "ola@hotmail.com", "status": "unemployed"},
    7: {"name": "Piotr", "age": 33, "email": "piotr@example.com", "status": "employee"},
    8: {"name": "Ania", "age": 27, "email": "ania@mydomain.com", "status": "employee"},
    9: {"name": "Michał", "age": 21, "email": "michal@gmail.com", "status": "student"},
    10: {"name": "Katarzyna", "age": 26, "email": "katarzyna@mydomain.com", "status": "employee"},
    11: {"name": "Adam", "age": 31, "email": "adam@yahoo.com", "status": "employee"},
    12: {"name": "Zuzanna", "age": 29, "email": "zuzanna@hotmail.com", "status": "unemployed"},
    13: {"name": "Jakub", "age": 32, "email": "jakub@example.com", "status": "employee"},
    14: {"name": "Wojtek", "age": 38, "email": "wojtek@company.org", "status": "employee"},
    15: {"name": "Ewa", "age": 34, "email": "ewa@gmail.com", "status": "retired"},
    16: {"name": "Monika", "age": 33, "email": "monika@example.com", "status": "employee"},
    17: {"name": "Paweł", "age": 27, "email": "pawel@mydomain.com", "status": "employee"},
    18: {"name": "Lena", "age": 22, "email": "lena@gmail.com", "status": "student"},
    19: {"name": "Marek", "age": 33, "email": "marek@yahoo.com", "status": "employee"},
    20: {"name": "Kamil", "age": 29, "email": "kamil@company.org", "status": "employee"},
}

friend_groups = [
    (1, 2, 3, 4, 5),
    (6, 7, 8),
    (9, 10, 11, 12, 13),
    (14, 15, 16, 17, 18, 19),
    (1, 7, 10, 13, 14),
    (2, 3, 6, 11, 18),
    (4, 5, 8, 9, 16),
    (14, 17, 19),
    (15, 12, 20),
    (3, 8, 13, 16),
    (1, 2, 12, 15, 17),
    (4, 6, 9, 14, 18),
    (5, 7, 10, 20),
    (6, 11, 19),
    (3, 13, 17, 19)
]


#+++++++++++++++++++++++ Exercise 1 ++++++++++++++++++++++++++
def names(db=user_db):
    return list(map(lambda u: u["name"], db.values()))

print()
print("Exercise 1:")
pprint(names())

#+++++++++++++++++++++++ Exercise 2 ++++++++++++++++++++++++++
def filter_by_domain(domain, db=user_db):
    return dict(filter(lambda kv: kv[1]["email"].endswith(domain), db.items()))

print("Exercise 2:")
pprint(filter_by_domain('gmail.com'))

#+++++++++++++++++++++++ Exercise 3 ++++++++++++++++++++++++++
def select_ids_by_age_and_status(min_age, max_age, status, db=user_db):
    return list(map(
        lambda kv: kv[0],
        filter(lambda kv: min_age <= kv[1]["age"] < max_age and kv[1]["status"] == status, db.items())
    ))

print("Exercise 3:")
pprint(select_ids_by_age_and_status(20, 30, 'student'))

#+++++++++++++++++++++++ Exercise 4 ++++++++++++++++++++++++++
def youngest_oldest(db=user_db):
    youngest = min(db.values(), key=lambda u: u["age"])["name"]
    oldest  = max(db.values(), key=lambda u: u["age"])["name"]
    return [youngest, oldest]

print(f"Exercise 4:")
pprint(youngest_oldest())

#+++++++++++++++++++++++ Exercise 5 ++++++++++++++++++++++++++
def average_age(db=user_db):
    ages = list(map(lambda u: u["age"], db.values()))
    return reduce(lambda acc, w: acc + w, ages) / len(ages)

print("Exercise 5:")
pprint(average_age())

#+++++++++++++++++++++++ Exercise 6 ++++++++++++++++++++++++++
def sort_db(db=user_db):
    return dict(sorted(db.items(), key=lambda kv: (kv[1]["status"], kv[1]["age"], kv[1]["name"])))

print("Exercise 6:\n")
print("before sorting:")
pprint(user_db)
print("after sorting:")
pprint(sort_db())

#+++++++++++++++++++++++ Exercise 7 and 8 ++++++++++++++++++++++++++
def influence(groups=friend_groups, db=user_db):

    results = {}

    all_p = set(p for g in groups for p in g)

    for group in groups:
        group_influence = []

        for person in group:
            total_mutual = 0
            for other in group:
                if other == person:
                    continue
                mutual = sum(
                    1 for third in all_p
                    if third != person and third != other
                    and any(person in g and other in g and third in g for g in groups)
                )
                total_mutual += mutual
            group_influence.append(round(total_mutual / len(group), 2))

        average = round(sum(group_influence) / len(group_influence), 2)
        results[group] = {"influence": group_influence, "average": average}

    col1 = max(len(str(g)) for g in results)
    col2 = max(len(str(v["influence"])) for v in results.values())
    header = f"{'id':<{col1}}  {'influence':<{col2}}  {'avg influence'}"
    print(header)
    print("-" * len(header))
    for group, data in results.items():
        print(f"{str(group):<{col1}}  {str(data['influence']):<{col2}}  {data['average']}")

    global_average = round(sum(data["average"] for data in results.values()) / len(results), 2)
    print(f"\nGlobal average influence: {global_average}")

    def influence_of_person_in_group(person_id, group):
        pos = list(group).index(person_id)
        return results[group]["influence"][pos]

    everyone = list(db.keys())

    above_global = [
        (uid, db[uid]["name"]) for uid in everyone
        if all(
            influence_of_person_in_group(uid, g) > global_average
            for g in groups if uid in g
        )
        and any(uid in g for g in groups)
    ]

    above_local = [
        (uid, db[uid]["name"]) for uid in everyone
        if all(
            influence_of_person_in_group(uid, g) > results[g]["average"]
            for g in groups if uid in g
        )
        and any(uid in g for g in groups)
    ]

    set_a = set(uid for uid, _ in above_global)
    set_b = set(uid for uid, _ in above_local)
    both = [(uid, db[uid]["name"]) for uid in set_a & set_b]

    print("\nPeople with influence greater than the global average in all their groups:")
    for entry in above_global:
        print(entry)

    print("\nPeople with influence greater than the local average in all their groups:")
    for entry in above_local:
        print(entry)

    print("\nPeople in both:")
    for entry in both:
        print(entry)

print("Exercise 7 and 8:")
influence()
