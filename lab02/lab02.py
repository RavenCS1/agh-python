import sys

#Exercise 1
args = sys.argv[1:]
print(f"Exercise {1}: {args}")

#Exercise 2
args_int = [int(float(_)) for _ in args]
print(f"Exercise {2}: {args_int}")

#Exercise 3
while 7 in args_int:
    args_int.remove(7)
print(f"Exercise {3}: {args_int}")

#Exercise 4
print("Exercise 4: ", end="")
if len(args_int) > 10:
    for i, a in enumerate(args_int):
        if i >= 10:
            break
        print(f"({i}, {a})", end= ", ")
else:
    for i, a in enumerate(args_int):
        print(f"({i}, {a})", end= ", ")
print("")

#Exercise 5
squares = [(a, a ** 2) for a in args_int if a > 0 and a % 2 == 0]
print(f"Exercise {5}: {squares}")


#Exercise 6
squares.sort(key = lambda x: x[1], reverse=True)
print(f"Exercise {6}: {squares}")


#Exercise 7
if(last := len(args_int) - 1) % 2 != 0:
    last -= 1
pairs = []
for i in range(last, -1, -2):
    pairs.append((i, args_int[i]))
print(f"Exercise {7}: {pairs}")

#Exercise 8
pairs = [(i, j) if i > j else (j, i) for i, j in pairs if i*j > 10]
print(f"Exercise {8}: {pairs}")
