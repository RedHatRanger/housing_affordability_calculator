# Prompt the user for the housing cost (e.g., mortgage payment)
housing_cost = float(input("Enter your monthly housing cost (e.g. 2600): "))

# The percentage factor (30% rule)
percentage = 0.30

# Using the formula:
# 30/100 = housing_cost / monthly_income
# This simplifies to monthly_income = housing_cost / 0.30
monthly_income = housing_cost / percentage

# Calculate the annual income by multiplying by 12
annual_income = monthly_income * 12

# Print the results
print(f"To afford a monthly housing cost of ${housing_cost},")
print(f"you need a monthly gross income of approximately ${monthly_income:,.2f}.")
print(f"This corresponds to an annual gross income of approximately ${annual_income:,.2f}.")
