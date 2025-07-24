#Decalre varibles

student_id=1
student_name="Sekhar"
student_age=25
quiz_score=88
assement_score=81
exam_score=79
student_attendence=89

#Arithmetic operaters to calculate

total_score=quiz_score + assement_score + exam_score
average_score=total_score/3

#Relational oersaters to determine

is_passing =average_score>=75
student_attendence+=1
is_eligible_for_award= (student_attendence>=90 )and is_passing

#display results

print("Student information")
print(f"Student id is: {student_id}")
print(f"Student id is: {student_name}")
print(f"Student id is: {student_age}")

print(f"Total score is: {total_score}")
print(f"Average score is: {average_score}")
print(f"Awarrd eligibility: {'Eligible' if is_eligible_for_award else 'Not eligible'}")





