import os
import re
from pprint import pprint

filepath = r'file path here'

pattern = b'names{U.netplaySU.(.*)U.codeSU.(.*#\d+)'

nameset = set()

for file in os.listdir(filepath):
    print(f'Doing {file}...')
    if os.path.splitext(file)[1] == '.slp':
        fullpath = os.path.join(filepath, file)

        with open(fullpath, 'rb') as f:
            s = f.read()
            matches = re.findall(pattern, s)
            # print(matches)
            for el in matches:
                nameset.add(el)
                print(el)


with open('fullnames.txt', 'w+') as f:
    pprint(nameset, stream=f)