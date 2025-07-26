#Emi calculater
car_price=1753560
down_payment=int(input("Enter down Payment Amount"))
bank_intrest=9.0
loan_period=float(input("Enter Loan peroid"))
loan_amount=car_price - down_payment
monthly_emi=bank_intrest /(12*100)
num_monthes=int(loan_period*12)

emi=loan_amount * monthly_emi * ((1 + monthly_emi) ** num_monthes /(1+monthly_emi) ** num_monthes-1)
print(loan_amount)
print(monthly_emi)