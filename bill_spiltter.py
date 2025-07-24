total_bill = int(input("Enter bill amount: "))
num_people = int(input("Enter number of people: "))

if total_bill >= 5000:
    discount = total_bill * 0.10
    final_amount = total_bill - discount
    print(f"Discount of 10% applied: ₹{discount}")
else:
    final_amount = total_bill
    print("No discount applied.")

per_person = final_amount / num_people
print(f"Total amount to be paid: ₹{final_amount}")
print(f"Each person should pay: ₹{per_person:.1f}")
