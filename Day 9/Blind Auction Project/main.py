import art
print(art.logo)
# TODO-1: Ask the user for input
bid_player ={}
continue_to_bid = True
highest_bid = 0
highest_player = ""
while continue_to_bid:
    name = input("Enter your Name: ")
    bid = int(input("Enter your Bid: $"))
    # TODO-2: Save data into dictionary {name: price}
    bid_player[name] = bid
    # TODO-3: Whether if new bids need to be added
    user_choice = input("Other Players to bid? (y/n): ")
    if user_choice == "y":
        print("\n"*20)
    else:
        for key in bid_player:
            # TODO-4: Compare bids in dictionary
            if bid_player[key] > highest_bid:
                highest_bid = bid_player[key]
                highest_player = key
        print(bid_player)
        print(f"The highest bid is {highest_bid} from {highest_player}")
        continue_to_bid = False





