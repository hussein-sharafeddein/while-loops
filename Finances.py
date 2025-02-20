finances = []

# Get Nabiha's input
month = input("Enter the month: ")
while month != "stop":
  
  income = float(input("Enter your income: "))
  rent_pct = float(input("Enter the rent percentage: "))
  electricity_pct = float(input("Enter the electricity percentage: "))
  savings_pct = float(input("Enter the savings percentage: "))
  
  # Create a dictionary for the finance
  finance = {
  "month": month,
  "income": income,
  "rent": rent_pct,
  "electricity": electricity_pct,
  "savings": savings_pct,
  }
  finances.append(finance)
