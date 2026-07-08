import sys

path = " ".join(sys.argv[1:])
parts = path.split('/')

# Exercise 1
dir_count = path.count('/') if not path.startswith('/') else path.count('/') - 1
print(f"Exercise {1}: {dir_count}")


# Exercise 2
folder_path = '/'.join(parts[:-1]) + '/'
print(f"Exercise {2}: {folder_path}")


# Exercise 3
normalized_name = parts[-1].lower()
print(f"Exercise {3}: {normalized_name}")


# Exercise 4
normalized_name = normalized_name.replace(' ', '_')
print(f"Exercise {4}: {normalized_name}")


# Exercise 5
first = 'dokumenty' in parts
extension = "." + str(parts[-1].split('.')[1])
second = extension in [".txt", ".docx", ".pdf", ".odt"]
result = first and second
print(f"Exercise {5}: {result}")

# Exercise 6
file_name = parts[-1]
accumulate = ''
for i in range(10):
    accumulate = accumulate + '{fld}{nam}_copy_{num}.{ext}'.format(fld = folder_path,
                                                                    nam = file_name,
                                                                    num = i,
                                                                    ext = extension.strip('.')) + '\n'
print(f"Exercise {6}: \n{accumulate}")

# Exercise 7
shortened = ''
if len(path) > 60 and dir_count > 2:
    if path.startswith('/'):
        shortened = '/' + parts[1] + '/.../' + parts[-2] + '/' + parts[-1]
    else:
        shortened = parts[0] + '/.../' + parts[-2] + '/' + parts[-1]
print(f"Exercise {7}: {shortened}")


# Exercise 8
prefix = normalized_name[:3]
for i in normalized_name.split('_'):
    if i.isdigit() and len(i) == 4:
        year = i
        break
else:
    year = '0000'
number = []
digits = ''
for char in normalized_name:
    if char.isdigit():
        digits += char
    else:
        if digits != '':
            number.append(digits)
        digits = ''
number = '0' if not number else number[len(number) - 1]
identifier = prefix + '-' + year + '-' + number + extension
print(f"Exercise {8}: {identifier}")
