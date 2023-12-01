print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
participants = int(input("How many people to split the bill? "))
tip_pct = float(input("What percantege tip would you like to give? "))
result = (bill + bill * tip_pct/100) / participants
print(f"Each person should pay: ${result}")
