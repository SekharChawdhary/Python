student_name=input("Enter Your Name: ")
student_grade=int(input("Enter Your Garde(1-12): "))
base_tution_fee=float(input("Enter Your Tution fee: "))
academic_topper_states=True
discount=0
# input validation
if student_grade<1 or student_grade>12:
    print("Invalid plese enter valid grade (1-12)")
    exit()
#Discount calculation
if student_grade>=9 or student_grade<=12 and academic_topper_states==True:
    discount=base_tution_fee*0.20
elif student_grade>=9 or student_grade<=12 and academic_topper_states==False:
    discount=base_tution_fee*.10
elif student_grade>=6 or student_grade<=8:
    discount=base_tution_fee*0.5
studen_final_fee=base_tution_fee-discount
print(f"Your name is: {student_name}")
print(f"Your grade is: {student_grade}")
print(f"Your Tution fee is: {base_tution_fee}")
print(f"Student discounted amount is: {discount}")
print(f"Your final tution fee is:{studen_final_fee}")







