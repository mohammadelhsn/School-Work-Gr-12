usd = lambda amt: round(amt * 0.725, 3)
euro = lambda amt: round(amt * 0.75, 3)
peso = lambda amt: round(amt * 14.54, 3)
pound = lambda amt: round(amt * 0.66, 3)

while True:
    try:
        amt = float(input("What amount would you like to convert? "))
        currency = int(
            input(
                "Which currency would you like to convert to?\n1) U.S.D\n2) Euros\n3) Pesos\n4) Pound\n "
            )
        )

        if currency == 1:
            print(
                f"Your amount {amt} CAD converted to U.S.D would be {usd(amt)} U.S Dollar(s)"
            )
        if currency == 2:
            print(
                f"Your amount {amt} CAD converted to Euros would be {euro(amt)} euro(s)"
            )
        if currency == 3:
            print(
                f"Your amount {amt} CAD converted to Pesos would be {peso(amt)} peso(s)"
            )
        if currency == 4:
            print(
                f"Your amount {amt} CAD converted to Pounds would be {pound(amt)} pound(s)"
            )
        else:
            print("Not a valid choice!")
        bye = int(input("Would you like to 1) continue or would you like to 2) exit? "))
        if (bye == 2): break
        continue
    except Exception as e:
        print(e)
        continue
