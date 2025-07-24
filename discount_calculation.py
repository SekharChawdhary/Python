student_name=input("Enter Your Name: ")
student_grade=int(input("Enter Your Garde(1-12): "))
base_tution_fee=float(input("Enter Your Tution fee: "))
academic_topper_states=input("Are You Topper (Yes/No)")
discount=0
if student_grade<1 or student_grade>12:
        print("Invalid  (Garde should be (1-12):")
        exit()
match student_grade:
    # For grade 10
  
    case 10:
        if student_grade==10:
            percent=3
            discount=base_tution_fee*(percent/100)
        print(f"Name : {student_name}")
        print(f"Grade : {student_grade}")
        print(f"Topper Status: {academic_topper_states}")
        print(f"Tution Fees: {base_tution_fee}")
        print(f"Discounted: {discount} (({percent})%) Applied")
        print(f"Final Tution Fees{base_tution_fee-discount}")

    # for grade 12
    case 12:
        percent=5
        if student_grade==12:
            discount=base_tution_fee*(percent/100)
        print(f"Name : {student_name}")
        print(f"Grade : {student_grade}")
        print(f"Topper Status: {academic_topper_states}")
        print(f"Tution Fees: {base_tution_fee}")
        print(f"Discounted: {discount}({percent}%) applied")
        print(f"Final Tution Fees{base_tution_fee-discount}")
    # Other academics
    case _:
        percent=0
        print(f"Name : {student_name}")
        print(f"Grade : {student_grade}")
        print(f"Topper Status: {academic_topper_states}")
        print(f"Tution Fees: {base_tution_fee}")
        print(f"Discounted : {discount} ({percent}%)")
        print(f"Final Tution Fees{base_tution_fee-discount}")

           
