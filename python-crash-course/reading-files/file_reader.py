import os

with open(os.path.join(os.path.dirname(__file__),'pi_digits.txt')) as file_object:
    contents = file_object.read()
    print(contents)
