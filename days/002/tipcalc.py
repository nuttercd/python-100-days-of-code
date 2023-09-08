print("Welcome to the tip calculator.")
billTotal = float(input("What was the total bill? $"))
billSplit = int(input("How many people to split the bill? "))
percentage= float(input("What percentage tip would you like to give? 10, 12, or 15 ")) /100
total = round(((billTotal * percentage) + billTotal) / billSplit, 2)
print(f"Each person should pay ${total}")
