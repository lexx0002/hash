import hashlib

def generator_mp5(path_to_file):
    with open(path_to_file) as file:
        for line in file:
            text = hashlib.md5(str(line).encode('utf-8')).hexdigest()
            yield text

for item in generator_mp5('countries.json'):
    print(item)
