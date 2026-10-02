# This program converts an amount from one currency to another based on the provided exchange rate.

amount = float(input("Enter the amount: "))
rate = float(input("Enter the exchange rate: "))

converted_amount = amount * rate

print("Converted amount:", converted_amount)
