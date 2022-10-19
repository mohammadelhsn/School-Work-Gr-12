import math

paintBuckets = lambda num: True if (num >= 1.50) else False
labour = lambda time: time * 8
labourcost = lambda time: time * 20
paintcost = lambda buckets, cost: buckets * cost
total = lambda labour, paint: labour + paint

while True:
    try:
        squareFeet = float(input("How much square feed needs to be painted? "))
        pricePerGallon = float(input("What is the price per gallon of paint? "))
        b = squareFeet / 115
        res = paintBuckets(b)
        buckets = (math.ceil(b) + 1) if (b >= 1.50) else (math.floor(b) + 1)
        costPaint = paintcost(buckets=buckets, cost=pricePerGallon)
        print(f"The cost of paint is {buckets} * ${pricePerGallon} = ${costPaint}")
        work = labour(time=b)
        print(f"Labour time is {work} hour")
        labourCost = labourcost(time=work)
        print(f"The labour cost is ${labourCost}")
        totalCost = total(labourCost, costPaint)
        print(f"The total cost is ${totalCost}")
    except Exception as e:
        print(e)
