from os import name
from sys import argv

print(f"OS: {name}\n")

for index, arg in enumerate(argv):
    print(index, arg, sep=": ")

input()
