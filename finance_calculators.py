#this program runs two financial calculator models
#users input their financial data then receive a calculation

import math

print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan")

while True: 
    try:
        user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
        if user_input == "investment" or user_input == "bond":
          break
    except:
        print("Please enter either 'investment' or 'bond'")

finance_calculator = str(user_input.lower())
print("You have entered:", finance_calculator)

#using float for variables r and i, in case interest rates include decimal
if finance_calculator == "investment":
    p = int(input("Deposit amount:"))
    r = float(input("Interest rate:")) / 100
    t = int(input("Number of years investing:"))
    interest = input("Please choose simple or compound interest:")

    if interest == "simple":
        a = p*(1 +r*t)
        print("Your interest amount will be: ", a)

    elif interest == "compound":
        a = p * math.pow((1+r), t)
        print("Your interest amount will be: ", a)

elif finance_calculator == "bond":
    p = int(input("Present value of house:"))
    i = (float(input("Interest rate:")) / 100) / 12
    n = int(input("Number of repayments in months:"))

    monthly_repayment = (i * p)/(1 - (1 + i)**(-n))
    print("Your monthly repayment is: ", monthly_repayment)