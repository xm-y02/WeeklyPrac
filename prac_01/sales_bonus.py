"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
"""Pseudocode
get sales
while sales >= 0
    if sales < 1000
    bonus = sales * 10% 
    else if
    sales >= 1000
    bonus = sales * 15%
else
    display invalid
"""

JUNIOR_RATE = 0.1
SENIOR_RATE = 0.15
VALUE_OF_SALES = 1000


user_sales = float(input("Enter sales: $"))
while user_sales >= 0:
    if user_sales >= VALUE_OF_SALES:
        user_bonus = user_sales * SENIOR_RATE
    else:
        user_bonus = user_sales * JUNIOR_RATE
    print(f"Bonus: {user_bonus:.2f} ")
    user_sales = float(input("Enter sales: $"))
else:
    print("Invalid")






