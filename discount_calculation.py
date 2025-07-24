student_name=input("Enter Your Name: ")
student_grade=int(input("Enter Your Garde(1-12): "))
base_tution_fee=float(input("Enter Your Tution fee: "))
academic_topper_states=input("Enter academic sates (Yes/No)")
discount=0
if student_grade<=1 or student_grade>12:
        print("Invalid your Garde should be (1-12):")
        exit()
match student_grade:
    # For grade 10
  
    case 10:
        if student_grade==10:
            discount=base_tution_fee*0.03
        print(f"Your name is: {student_name}")
        print(f"Your grade is: {student_grade}")
        print(f"Your acdemic states: {academic_topper_states}")
        print(f"Your Tution fee is: {base_tution_fee}")
        print(f"Student discounted amount is: {discount}")
        print(f"Your final tution fee is{base_tution_fee-discount}")

    # for grade 12
    case 12:
        if student_grade==12:
            discount=base_tution_fee*0.05
        print(f"Your name is: {student_name}")
        print(f"Your grade is: {student_grade}")
        print(f"Your acdemic states: {academic_topper_states}")
        print(f"Your Tution fee is: {base_tution_fee}")
        print(f"Student discounted amount is: {discount}")
        print(f"Your final tution fee is{base_tution_fee-discount}")
    # Other academics
    case _:
        print(f"Your name is: {student_name}")
        print(f"Your grade is: {student_grade}")
        print(f"Your acdemic states: {academic_topper_states}")
        print(f"Your Tution fee is: {base_tution_fee}")
        print(f"Student discounted amount is: {discount}")
        print(f"Your final tution fee is{base_tution_fee-discount}")

           
