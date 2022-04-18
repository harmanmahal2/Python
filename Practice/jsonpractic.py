import json

#numbers = [1,2,3,4,5,6,6]

#file = 'files/numbers.json'

#with open(file, 'w') as f:
  #  json.dump(numbers, f)


#with open(file) as f:
    #number = json.load(f)

#print(number)



## 10-11

path = 'files/fav_number.json'

if path:
    with open(path) as j:
        fav = json.load(j)
        print(fav)
else:
    fav_number = input("What is yur fav number")
    with open(path, 'w') as f:
        json.dump(fav_number, f)

