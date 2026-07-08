import sys
import random
from collections import defaultdict

if len(sys.argv) <= 1:
    sys.exit()

numbers = [int(l) for l in sys.argv[1:]]
print(f"numbers: {numbers}")

frequency = defaultdict(int)
for n in numbers:
    frequency[n] = numbers.count(n)
print(f"Exercise 1: {dict(frequency)}")

drawn_numbers = random.choices(numbers, k=2)
for w in set(drawn_numbers):
    if w in frequency:
        del frequency[w]

numbers = list(frequency)
print(f"Exercise 2: {drawn_numbers}, {numbers}, {dict(frequency)}")


split_numbers = {
    "even" : [numbers[i] for i in range(0, len(numbers), 2)],
    "odd"  : [numbers[i] for i in range(1, len(numbers), 2)]
}
print(f"Exercise 3: {split_numbers}")

split_frequency = {
    "even": {i: frequency[i] for i in split_numbers["even"]},
    "odd" : {i: frequency[i] for i in split_numbers["odd"]},
}
print(f"Exercise 4: {split_frequency}")

differences = {(i, i + 1): numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)}
print(f"Exercise 5: {differences}")

differences.update({k: (1 if v > 0 else (-1 if v < 0 else 0)) for k, v in differences.items()})
print(f"Exercise 6: {differences}")

unique = list(sorted(set(numbers)))

def rand_perm(unique):
    perm = unique[:]
    random.shuffle(perm)
    return {unique[i]: perm[i] for i in range(len(unique))}

s1 = rand_perm(unique)
s2 = rand_perm(unique)
s3 = rand_perm(unique)

composition = {k: s3[s2[v]] for k, v in s1.items()}

visited = set()
cycles = {"permutation": composition}
for start in composition:
    if start in visited:
        continue
    cycle = []
    current = start
    while current not in visited:
        visited.add(current)
        cycle.append(current)
        current = composition[current]
    length = len(cycle)
    if length not in cycles:
        cycles[length] = []
    cycles[length].append(tuple(cycle))
print(f"Exercise 7: {cycles}")
