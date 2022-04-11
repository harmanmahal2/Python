import json

#numbers = [1,2,3,4,5,6,6]

file = 'files/numbers.json'

#with open(file, 'w') as f:
  #  json.dump(numbers, f)


with open(file) as f:
    number = json.load(f)

print(number)