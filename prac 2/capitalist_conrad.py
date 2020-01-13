import random
Maximum_increase = 0.175
Maximum_decrease = 0.05
Min_price = 1
Maximum_price = 100
Initial_value = 10.0
OUTPUT_FILE="CAP.TXT"

out_file = open(OUTPUT_FILE,'w')
price = Initial_value
day=1;
while ((price<Maximum_price and price>Min_price)):
    chance=random.randint(1, 2)
    if (chance == 1):
        price_change = random.uniform(0, Maximum_increase)
        price = price + price * price_change
    else:
        price_change = random.uniform(Maximum_decrease, 0)
        price = price - price*price_change
    print("on day {} price is ${:,.2f}".format(day,price), file=out_file)
    day=day+1

out_file.close()