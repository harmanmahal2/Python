## excercise 7-8, 7-9

sandwich_orders = ["club sandwich", "pastami", "california sandwich", "egg and cheese", "pastami", "chicken sandwich", "pastami"]
finished_sandwiches = []
print("The deli has run out of pastami sandwiches")

while "pastami" in sandwich_orders:
    sandwich_orders.remove("pastami")

while sandwich_orders:

    current_order = sandwich_orders.pop()
    print(current_order + " is being made")
    finished_sandwiches.append(current_order)

print(finished_sandwiches)


## 7- 10

vacation_spots = {}

while True:
    name = input("What is your name?: ")
    spot = input("What is your favorite vacation spot?: ")
    next = input("do you want next person to answer? ")


    vacation_spots[name] = spot
    if next == "no":
        break

for key, value in vacation_spots.items():
    print(key + "'s favorite vacation sport is " + value)

