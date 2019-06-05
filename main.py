import hashlib
import json

def generator_mp5(path_to_file):
    with open(path_to_file) as file:
        file = json.load(file)
        for line in file:
            print(hashlib.md5(str(line).encode('utf-8')).hexdigest())

generator_mp5('countries.json')
