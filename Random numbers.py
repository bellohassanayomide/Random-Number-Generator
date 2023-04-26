import random

print("                RANDOM NUMBER GENERATION                ")
a = float(input("Enter the minimum number: "))
b = float(input("Enter the maximum number: "))
decimal = input("Do you want to generate decimal numbers? (Y/N): ")

if decimal.lower() == 'y':
    num_decimals = int(input("Enter the number of decimal places: "))
    for i in range(100):
        z = round(random.uniform(a, b), num_decimals)
        print(z)
else:
    for i in range(100):
        z = random.randint(int(a), int(b))
        print(z)
