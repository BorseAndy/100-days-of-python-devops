capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#Nested List in Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Munich", "Berlin"]
# }

# Print Lille
# print(travel_log["France"][1])

# Print D from nested list
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"]

    },
    "Germany": {
        "num_times_visited": 5,
        "cities_visited": ["Berlin", "Munich", "Stuttgart"]

    },
}

print(travel_log["France"]["cities_visited"][2])

