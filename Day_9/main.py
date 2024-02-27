auction programfrom replit import clear

#HINT: You can call clear() to clear the output in the console.
bids = {}

def cal_highest_bid(bids):
    winner = ''
    highest_bid = 0
    for bider in bids:
        bider_amount = bids[bider]

        if highest_bid < bider_amount:
            highest_bid = bids[bider]
            winner = bider

    print(f"\nBid Winner is {winner} with bid of ${highest_bid}")


choice = "yes"
while (choice == 'yes'):
    name = input("Enter your name: ")
    bid_price = int(input("Enter Bid Price: $"))
    bids[name] = bid_price

    choice = input("Do you wanna enter more user entries?: ")
    if choice == 'no':
        cal_highest_bid(bids)
        break

    elif choice == 'yes':
        clear()
