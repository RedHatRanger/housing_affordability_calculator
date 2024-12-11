# Housing Income Calculator

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


## **Detailed Description:**
Below is a detailed, step-by-step illustration of how the standard mortgage payment formula works and how we rearrange it to find the principal.
Original Mortgage Payment Formula
For a fixed-rate mortgage, the monthly mortgage payment (M) can be calculated using the formula:
M=P×i(1+i)n(1+i)n−1M = P \times \frac{i(1+i)^n}{(1+i)^n - 1}M=P×(1+i)n−1i(1+i)n
Where:
•	PPP = Principal (the amount borrowed)
•	iii = Monthly interest rate = Annual Interest Rate (in decimal form)12\frac{\text{Annual Interest Rate (in decimal form)}}{12}12Annual Interest Rate (in decimal form)
•	nnn = Total number of monthly payments over the entire term of the loan
(For a 30-year mortgage: n=30×12=360n = 30 \times 12 = 360n=30×12=360)
•	MMM = Monthly mortgage payment
Explanation:
1.	Monthly Interest Rate (i):
If your Annual Percentage Rate (APR) is 5%, then in decimal form it’s 0.050.050.05. Dividing by 12 gives the monthly interest rate:
i=0.0512≈0.0041667.i = \frac{0.05}{12} \approx 0.0041667.i=120.05≈0.0041667.
2.	Term (n):
For a 30-year mortgage, there are 360 monthly payments:
n=30×12=360.n = 30 \times 12 = 360.n=30×12=360.
3.	Growth Factor (1+i)n(1+i)^n(1+i)n:
This represents the growth of a single dollar when compounded monthly for nnn periods at the monthly rate iii. If i=0.0041667i = 0.0041667i=0.0041667, then:
(1+i)n=(1+0.0041667)360.(1+i)^n = (1 + 0.0041667)^{360}.(1+i)n=(1+0.0041667)360.
4.	Putting it Together:
The fraction i(1+i)n(1+i)n−1\frac{i(1+i)^n}{(1+i)^n - 1}(1+i)n−1i(1+i)n is a scaling factor that converts the principal PPP into a monthly payment MMM that, if paid each month for nnn months, will fully amortize the loan (pay it off completely).
Illustration of the Formula:
Imagine you start with the principal PPP:
1.	Multiply PPP by the monthly interest rate factor (1+i)n(1+i)^n(1+i)n to account for the compound growth over nnn months.
2.	Extracting the payment pattern involves balancing this growth with the structured monthly payments, which is why we divide by (1+i)n−1(1+i)^n - 1(1+i)n−1.
3.	Finally, multiplying by iii ensures that each month covers the interest plus a portion of the principal in such a way that after nnn months, the loan balance is zero.
Rearranging to Solve for Principal (P)
If we know MMM, iii, and nnn, and want to find out how large a loan PPP we can afford, we rearrange the formula:
From:
M=P×i(1+i)n(1+i)n−1M = P \times \frac{i(1+i)^n}{(1+i)^n - 1}M=P×(1+i)n−1i(1+i)n
We get:
P=M×((1+i)n−1)i(1+i)nP = M \times \frac{( (1+i)^n - 1 )}{i(1+i)^n}P=M×i(1+i)n((1+i)n−1)
Step-by-Step Rearrangement:
1.	Start with:
M=P×i(1+i)n(1+i)n−1M = P \times \frac{i(1+i)^n}{(1+i)^n - 1}M=P×(1+i)n−1i(1+i)n
2.	Multiply both sides by ((1+i)n−1)( (1+i)^n - 1 )((1+i)n−1):
M((1+i)n−1)=P×i(1+i)nM((1+i)^n - 1) = P \times i(1+i)^nM((1+i)n−1)=P×i(1+i)n
3.	Divide both sides by i(1+i)ni(1+i)^ni(1+i)n:
M((1+i)n−1)i(1+i)n=P\frac{M((1+i)^n - 1)}{i(1+i)^n} = Pi(1+i)nM((1+i)n−1)=P
Now you have PPP in terms of MMM, iii, and nnn. This allows you to plug in a target monthly payment and interest rate to determine how large a principal you can afford.
Putting In Sample Numbers:
•	Suppose M=$2,600M = \$2{,}600M=$2,600, i=0.05/12≈0.0041667i = 0.05/12 \approx 0.0041667i=0.05/12≈0.0041667, and n=360n = 360n=360.
•	First, calculate (1+i)n(1+i)^n(1+i)n:
(1+0.0041667)360≈4.4677(approximate)(1+0.0041667)^{360} \approx 4.4677 \quad (\text{approximate})(1+0.0041667)360≈4.4677(approximate)
•	Then:
P=2600×4.4677−10.0041667×4.4677.P = 2600 \times \frac{4.4677 - 1}{0.0041667 \times 4.4677}.P=2600×0.0041667×4.46774.4677−1.
•	Evaluate the numerator:
4.4677−1=3.4677.4.4677 - 1 = 3.4677.4.4677−1=3.4677.
•	Evaluate the denominator:
0.0041667×4.4677≈0.01861.0.0041667 \times 4.4677 \approx 0.01861.0.0041667×4.4677≈0.01861.
•	Now:
P≈2600×3.46770.01861≈2600×186.3≈484,380.P \approx 2600 \times \frac{3.4677}{0.01861} \approx 2600 \times 186.3 \approx 484,380.P≈2600×0.018613.4677≈2600×186.3≈484,380.
(These numbers are approximate, but they show the process.)
In Summary:
•	The original formula relates monthly payment, interest rate, and principal for an amortizing loan.
•	By rearranging the formula, you can solve for the principal, given a target monthly payment and an interest rate.
•	This allows you to estimate how large a loan you can afford if you know how much you can pay per month.

