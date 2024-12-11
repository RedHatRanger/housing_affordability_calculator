# Housing Affordability Calculator

## **Overview:**  
This script, **`housing_income_calculator.py`**, helps you determine the amount of gross monthly and annual income required to afford a given monthly housing expense under the commonly used "30% rule." The 30% rule suggests that total housing costs—such as rent or a mortgage payment—should not exceed 30% of your gross monthly income. Adhering to this guideline can help ensure you maintain a balanced budget and stay on track financially.

**How It Works:**  
1. **User Input:**  
   The script prompts you to enter your monthly housing cost (for example, your expected rent or mortgage payment).

2. **Calculation Using the 30% Rule:**  
   The script applies the following formula:

## Monthly Income = Housing Cost / 0.30

This calculation determines the gross monthly income required so that your housing cost remains at or below the 30% threshold.

3. **Annual Income Estimation:**  
After calculating the required gross monthly income, the script multiplies that amount by 12 to provide an estimated annual gross income. This gives you a clear target for your yearly earnings.

**Intended Use Cases:**
- **Mortgage and Loan Qualification:**  
Before applying for a home loan, determine the annual gross income needed to comfortably afford the monthly mortgage payment you have in mind.

- **Rental Budgeting:**  
If you’re apartment hunting and know the monthly rent, quickly find out the monthly and annual incomes you’ll need to stay within the 30% guideline.

- **Financial Planning:**  
Use this tool for long-term financial planning to understand how housing expenses fit into your overall budget and financial goals.

By using **`housing_income_calculator.py`**, you can make more informed decisions about housing expenses, helping you maintain financial health and balance.


## **Detailed Workflow:**
```
         ┌────────────────────────────────────────────────────────────────┐
         │                      Inputs                                    │
         │                                                                │
         │   P = Principal (The Outut Result)                             │
         │   M = Monthly Payment (Input the Desired Payment)              │
         │   APR = Annual % Rate (Input the APR)                          │
         │   i = APR/12 = Monthly Interest Rate (Calculated from Input)   │
         │   n = 360 (for a 30-year loan)                                 │
         └─────────────────────┬──────────────────────────────────────────┘
                               │
                               │  Use the Mortgage Formula:
                               │
                               v
                 ┌─────────────────────────────────┐
                 │ M = P * [ i*(1+i)^n ]            │
                 │            ──────────            │
                 │            (1+i)^n - 1           │
                 └─────────────────────────────────┘
                               │
                               │  We know M, i, n; solve for P
                               v
                 ┌─────────────────────────────────┐
                 │ Rearranging the formula:         │
                 │                                  │
                 │ P = M * [((1+i)^n - 1) / (i*(1+i)^n)] │
                 └─────────────────────────────────┘
                               │
                               │  Substitute your values
                               v
            ┌────────────────────────────────────────────────┐
            │        Compute (1+i)^n                          │
            │        Compute ((1+i)^n - 1)                    │
            │        Divide by [i*(1+i)^n]                    │
            │        Multiply by M                            │
            └────────────────────────────────────────────────┘
                               │
                               v
               ┌──────────────────────────────────┐
               │            Output: P              │
               │   Principal = Amount You Can Afford│
               └──────────────────────────────────┘
```
