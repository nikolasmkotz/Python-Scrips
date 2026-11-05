#exercise : Calculate total bill

#Get user input and convert to float

meal = float(input("whats the meal bill? "))
tax = float(input("how much tax payed (porcentage)"))
tip = float(input("what is the tip given(porcentage)"))

# Calculate tax amount and add to bill

tax_amount = (meal * tax) / 100
total = tax_amount + meal

# Calculate tip amount and add to total

tip_amount = (tip * meal) / 100
total= tip_amount + total



# Round total to two decimal places

total = round(total, 2)



# Print the final total bill

print("the final bill will be $", total)
