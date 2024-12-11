def required_income_from_housing_cost(housing_cost):
    """
    Given a monthly housing cost, calculate the gross monthly and annual income 
    required so the housing cost does not exceed 30% of income.
    """
    percentage = 0.30
    monthly_income = housing_cost / percentage
    annual_income = monthly_income * 12
    return monthly_income, annual_income

def mortgage_principal_from_payment(monthly_payment, annual_interest_rate):
    """
    Given a desired monthly mortgage payment and an annual interest rate (APR),
    calculate the approximate principal you can afford for a 30-year fixed mortgage.
    
    Formula:
    M = P * [ i*(1+i)^n ] / [ (1+i)^n - 1 ]

    Where:
    M = Monthly Payment
    P = Principal (what we want to find)
    i = monthly interest rate = APR/12
    n = number of monthly payments = 360 (30 years * 12)
    
    Rearranged to solve for P:
    P = M * [ ((1+i)^n - 1) / ( i*(1+i)^n ) ]
    """
    n = 360  # 30 years * 12 months
    i = annual_interest_rate / 12.0  # monthly interest rate
    if i == 0:
        # If interest rate is 0%, principal is simply monthly_payment * 360
        return monthly_payment * n

    # Compute (1+i)^n
    factor = (1 + i) ** n

    # Principal calculation
    principal = monthly_payment * ((factor - 1) / (i * factor))
    return principal

# ----------------------------
# Main Execution
# ----------------------------

# 1. Prompt user for monthly housing cost (e.g. $2,600)
housing_cost_input = input("Enter your desired monthly housing cost (Example: 2600 for $2,600 a month): ")
try:
    housing_cost = float(housing_cost_input)
except ValueError:
    print("Invalid input. Please enter a numeric value.")
    exit(1)

# Calculate required income using the 30% rule
monthly_income_needed, annual_income_needed = required_income_from_housing_cost(housing_cost)

# Print the income results
print(f"\nTo afford a monthly housing cost of ${housing_cost:,.2f}:")
print(f" - You need a monthly gross income of: ${monthly_income_needed:,.2f}")
print(f" - Which corresponds to an annual gross income of: ${annual_income_needed:,.2f}")

# 2. Prompt user for APR to estimate mortgage principal
apr_input = input("\nEnter the Annual Percentage Rate (APR) without the `%` (Example: 5 for 5%): ")
try:
    apr = float(apr_input) / 100.0  # convert percentage to decimal
except ValueError:
    print("Invalid input. Please enter a numeric value.")
    exit(1)

# Calculate the principal amount using the given APR and monthly payment
principal_affordable = mortgage_principal_from_payment(housing_cost, apr)

# Print the principal result
print(f"\nWith a {apr_input}% APR 30-year fixed mortgage and a monthly payment of ${housing_cost:,.2f}:")
print(f" - You could afford an approximate principal of: ${principal_affordable:,.2f}")
