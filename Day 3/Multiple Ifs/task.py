print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    bill = 0
    if age <= 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    else:
        print("Adult tickets are $12.")
        bill = 12
    # Asking for photo independent of age
    wants_photo = input("Do you want to have a photo taken? Type y for Yes and n for No ")
    if wants_photo == "y":
        bill += 3
    print(f"You have to pay: ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
