print("Welcome to Auction!")

auction_bids = {}
more_bids = True

while more_bids:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid amount: $"))
    auction_bids[name] = bid
    repeat = input("Are there any other bidders? Type 'Yes' or 'No: ").lower()
    if repeat == 'no':
        more_bids = False
    else :
        print("\n" * 20)

winner_name = ""
highest_bid = 0

for bidder in auction_bids:
    if auction_bids[bidder] > highest_bid:
        winner_name = bidder
        highest_bid = auction_bids[bidder]

print(f'The winner is {winner_name} with ${highest_bid}.')