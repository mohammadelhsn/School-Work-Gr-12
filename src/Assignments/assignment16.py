import random

inventory = {
    "cash": random.randrange(0, 500, 10),
    "items": ["candy", "car", "bike", "scooter"],
}
guild = {
    "car": {"sell": 1000, "buy": 250},
    "bike": {"sell": 400, "buy": 50},
    "scooter": {"sell": 500, "buy": 65},
    "candy": {"sell": 20, "buy": 5},
}
while True:
    inv_cash = inventory["cash"]
    print(f"💵 | You have ${inv_cash}")
    inv_items = inventory["items"]
    print(f"🎒 | You own {inv_items}")
    action = input("What would you like to do? (Buy/Sell) ")
    if action.lower() == "sell":
        if len(inventory["items"]) == 0:
            print("❌ | You don't have anything to sell!")
            continue
        print(f"🎒 | Your inventory is {inv_items}")
        print(f"🛒 | The guild rates are {guild}")
        item = input("What would you like to sell? ")
        if item in inventory["items"]:
            guild_item = guild.get(item)
            inventory["cash"] = inventory["cash"] + guild_item["sell"]
            cash = inventory["cash"]
            sold_for = guild_item["sell"]
            print(
                f"✅ | You have now sold {item} for ${sold_for}. You now have ${cash} total."
            )
            inventory["items"].remove(item)
            continue
        else:
            print("❌ | This item doesn't exist or isn't in your inventory!")
            continue
    elif action.lower() == "buy":
        print(f"🛒 | The guild has {guild}")
        item = input("What would you like to buy? ")
        if item not in guild:
            print("❌ | This item doesn't exist!")
            continue
        if item in inventory["items"]:
            print("❌ | You already own this item!!!")
            continue
        guild_item = guild.get(item)
        buy_value = guild_item["sell"]
        if buy_value > inventory["cash"]:
            print("❌ | You don't have the money for this!")
            continue
        inventory["cash"] = inventory["cash"] - buy_value
        inventory["items"].append(item)
        cash = inventory["cash"]
        print(
            f"✅ | You have purchased {item} for {buy_value} and now your cash amount is {cash}"
        )
        continue
    else:
        print(f"❌ | {action.lower()} is not a valid option my dude! Restart!!!")
        continue
