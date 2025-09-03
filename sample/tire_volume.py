#this program calculates the volume of a tire based on user input and results are saved to a file.
#i added feature to ask user if they want to buy tires and collect their phone number to send them price and help with the purchase.


import math
from datetime import datetime

tire_prices = {
    (185, 50, 14): 77.99,
    (205, 60, 15): 89.99,
    (225, 65, 17): 84.99,
    (245, 70, 16): 94.99,
}

width = int(input("enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("enter the diameter of the wheel in inches (ex 15): "))


volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
print(f"the approximate volume is {volume:.2f} liters")

price = tire_prices.get(("width, aspect_ratio, diameter"))
if price is not None:
    print(f"the price of the tire is ${price:.2f}")
else:
    print("sorry, the price of the tire is not available right now.")

buy = input("do you want to buy tires with these dismentions? (yes/no):").strip().lower() 
phone_number = ""  
if buy == "yes":
    phone_number = input("enter your phone number: ")
    print("thank you, we will contact you soon to arrange the purchase.")

current_date = datetime.now().strftime("%Y-%m-%d")
with open("volumes.txt", "at") as file:
    log_entry = f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}"
    if phone_number:
        log_entry += (phone_number)
    print(log_entry, file=file)


