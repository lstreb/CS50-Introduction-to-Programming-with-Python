price = 50
amount_due = price
accepted_coins = [25, 10, 5]

while amount_due > 0:
    print(f"Amount Due: {amount_due} cents")
    coin = int(input("Insert Coin: "))
    if coin in accepted_coins:
        amount_due -= coin
    else:
        print(f"{coin} is not an accepted denomination.")

change_owed = abs(amount_due)
if change_owed > 0:
    print(f"Change Owed: {change_owed} cents")
else:
    print("No change owed.")