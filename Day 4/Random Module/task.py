import random
# import my_module

# random_integer = random.randint(1,10)
# print(random_integer)

# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)
#
# random_float = random.uniform(1,10)
# print(random_float)

random_coin_number = random.randint(1,2)

if random_coin_number == 1:
    print(f"Heads {random_coin_number}")
else:
    print(f"Tails {random_coin_number}")
