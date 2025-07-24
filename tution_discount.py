# Variables
student_name=input("Enter Your Name: ")
student_grade=int(input("Enter Your Garde(1-12): "))
base_tution_fee=float(input("Enter Your Tution fee: "))
academic_topper_states=input("Are You Topper (Yes/No)")
discount=0
# input validation
if student_grade<1 or student_grade>12:
    print("Invalid plese enter valid grade (1-12)")
    exit()
#Discount calculation
if student_grade>=9 or student_grade<=12 and academic_topper_states=="Yes":
    discount=base_tution_fee*0.20
elif student_grade>=9 or student_grade<=12 and academic_topper_states=="No":
    discount=base_tution_fee*.10
elif student_grade>=6 or student_grade<=8:
    discount=base_tution_fee*0.5
studen_final_fee=base_tution_fee-discount
print(f"Name: {student_name}")
print(f"Grade: {student_grade}")
print(f"Tution Fees: {base_tution_fee}")
print(f"Discount: {discount}")
print(f"Final Fees:{studen_final_fee}")







