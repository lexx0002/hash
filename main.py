import hashlib
import json

def generator_mp5(path_to_file):
    with open(path_to_file) as file:
        generator = (line for line in file)
        text = hashlib.md5(str(generator).encode('utf-8')).hexdigest()


        yield text

print(generator_mp5('countries.json').__next__())
print(generator_mp5('countries.json').__next__())
