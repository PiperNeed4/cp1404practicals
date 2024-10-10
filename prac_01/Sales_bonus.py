"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

LOW_SALES_BONUS = 0.1
HIGH_SALES_BONUS = 0.15
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        salary_bonus = sales * LOW_SALES_BONUS
    else:
        salary_bonus = sales * HIGH_SALES_BONUS
    print(f"Your bonus is ${salary_bonus:.2f}")
    sales = float(input("Enter sales: $"))
