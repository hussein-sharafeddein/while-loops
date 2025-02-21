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

  # Calculate amounts
  amount_savings = (savings_pct / 100) * income
  amount_rent = (rent_pct / 100) * income
  amount_electricity = (electricity_pct / 100) * income

  # Total expenses
  total_expenses = amount_savings + amount_rent + amount_electricity

  # Remainder of salary
  remainder_salary = income - total_expenses

  # Yearly rent and electricity costs
  yearly_rent = amount_rent * 12
  yearly_electricity = amount_electricity * 12

  # Total salary squared
  salary_squared = income ** 2

  # Display results
  print(f"amount allocated to savings: {amount_savings}")
  print(f"amount allocated to rent: {amount_rent}")
  print(f"amount allocated to electricity: {amount_electricity}")
  print(f"Total expenses: {total_expenses}")
  print(f"Remainder of salary: {remainder_salary}")
  print(f"Yearly rent cost: {yearly_rent}")
  print(f"Yearly electricity cost: {yearly_electricity}")
  print(f"Total salary squared: {salary_squared}")

  # Ask if Nabiha wants to update savings
  update_savings = input("Do you want to update savings? (yes/no): ")
  while update_savings == "yes":
    additional_savings = float(input("Enter the additional savings amount: "))
    additional_savings_pct = (additional_savings / income) * 100
    finance["savings"] += additional_savings_pct
    savings_pct = finance["savings"]

    # Recalculation
    amount_savings = (savings_pct / 100) * income
    total_expenses = amount_savings + amount_rent + amount_electricity
    remainder_salary = income - total_expenses
    yearly_rent = amount_rent * 12
    yearly_electricity = amount_electricity * 12
    salary_squared = income ** 2

    # Display updated results
    print(f"Updated amount allocated to savings: {amount_savings}")
    print(f"Updated total expenses: {total_expenses}")
    print(f"Updated remainder of salary: {remainder_salary}")
    print(f"Updated yearly rent cost: {yearly_rent}")
    print(f"Updated yearly electricity cost: {yearly_electricity}")
    print(f"Updated total salary squared: {salary_squared}")
    
    update_savings = input("Do you want to update savings again? (yes/no): ")

  month = input("Enter the month (or write stop to stop): ")

print(finances)