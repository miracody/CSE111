from datetime import datetime
discount_days=[1,2]
discount_rate=.1
tax_rate=.06
today=datetime.now()
dayofweek=today.weekday()
subtotal=0
quantity=1
while quantity !=0:
    quantity=int(input("enter the quantity of the items: "))
    if quantity !=0:
        price=float(input("enter the price of items: "))
        subtotal +=quantity * price
print(f"total order {subtotal:.2f}")
discount=0
if dayofweek in discount_days:
    if subtotal > 50:
        discount=subtotal * discount_rate
        print(f"discount {discount:.2f}")
    else:
        short=50-subtotal
        print(f"you can get a discount by ordering {short:.2f} more.")
subtotal -=discount
tax=subtotal * tax_rate
total=subtotal + tax
print(f"tax {tax :.2f}")
print(f"total due {total :.2f}")
