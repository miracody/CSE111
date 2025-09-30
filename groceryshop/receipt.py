import csv

def read_dictionary(filename, key_column_index):
    dictionary = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                key = row[key_column_index]
                dictionary[key] = row
    except FileNotFoundError as e:
        print(f"Error: missing file {e}")
    except PermissionError as e:
        print(f"Error: permission denied {e}")
    return dictionary

from datetime import datetime

def main():
    try:
        products_dict = read_dictionary("products.csv", 0)
        total_items = 0
        subtotal = 0

        with open("request.csv", mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header

            print("Inkom Emporium")
            for row in reader:
                prod_num = row[0]
                quantity = int(row[1])
                try:
                    product = products_dict[prod_num]
                    name = product[1]
                    price = float(product[2])
                    print(f"{name}: {quantity} @ {price:.2f}")
                    total_items += quantity
                    subtotal += price * quantity
                except KeyError:
                    print(f"Error: unknown product ID in the request.csv file '{prod_num}'")

        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax

        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        print("Thank you for shopping at the Inkom Emporium.")
        print(datetime.now().strftime("%a %b %d %H:%M:%S %Y"))

    except FileNotFoundError as e:
        print(f"Error: missing file {e}")
    except PermissionError as e:
        print(f"Error: permission denied {e}")
if __name__ == "__main__":
    main()
