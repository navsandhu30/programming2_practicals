"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales : $"))
if sales < 1000:
  bonus = sales *0.1
else:
   bonus = sales*0.15
print("your bonus is $" , bonus)
   #part2 addition of loop to same function with condition (0 is vlid sales) and general structure
sales = float(input("Enter your sale :$"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print("your bonus is $", bonus)
    sales = float(input("enter your sale :$"))

