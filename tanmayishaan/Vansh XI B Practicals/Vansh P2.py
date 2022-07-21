item  = 1

while item == 5:
    name = input(" What's the name of the first item? ")
    price = input("What's the price of ", name, "? ")
    data = (name, price)
    print(data)
    item += 1
