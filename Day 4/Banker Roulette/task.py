import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#Option 1
print(f"\"{random.choice(friends)}\" will pay the bill")

# Option 2
rand_number = random.randint(0,4)
print(f"\"{friends[rand_number]}\" will pay the bill")