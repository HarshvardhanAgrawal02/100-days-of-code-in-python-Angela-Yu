print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? Rs."))
tip = int(input("What percent tip would you like to give? 6,15, or 20?"))
people = int(input("How many people to split the bill? "))
pay = (tip/100 * bill + bill)/people
total_pay = round(pay, 2)
print(f"Each person should pay: Rs.{total_pay}")