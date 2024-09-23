import pyqrcode
from pyqrcode import QRCode

print("Welcome to STEP_IN SHOP!!!!!")

# Dictionary of value pairs
data = {
    'note_book': 10,
    'pen': 5,
    'pencil': 3,
    'chips': 5,
    'water_bottle': 10,
    'milk': 30,
    'bread': 30,
    'egg': 60,
    'butter': 25,
    'chocolate': 1
}

for x, y in data.items():
    print(x, y)

# Get user input for keys
keys = input("What do you want to buy? Choose any (comma-separated): ").split(',')

# Calculate the sum of values for the provided keys
total_sum = sum(data[key] for key in keys if key in data)

print("Total bill is:", total_sum, "rupees")
selected_items = ', '.join([f"{key}: {data[key]} " for key in keys if key in data])
s = f"Bill: {total_sum} rupees\nItems: {selected_items} "

url = pyqrcode.create(s)
url.png("bill.png", scale=10)
