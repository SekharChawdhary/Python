id = int(input("Enter Your ID: "))
name = input("Enter Your Name: ")
subjects = int(input("Enter your subjects"))
attendence = float(input("Enter your attendence Percentage"))
if attendence > 100 or attendence < 0:
    print("Attendence should be(1-100 %)")
    exit()
total_marks=0
for i in range (1, subjects+1):
    mark = float(input(f"Enter marks for subject {i}: "))
    if(mark > 100 or mark < 0):
         print("Mraks should be (0-100)") 
         continue
         
    total_marks += mark
    cont = input("Do you want enter another marks (yes/no):")
    if cont.lower() != "yes":
        break
average_marks = total_marks / subjects
print(f"students Id: {id}")
print(f"students Name: {name}")
print(f"students total_marks: {total_marks:.2f}")
print(f"Students Average_marks: {average_marks:.2f}")
# marks conditions
if average_marks >= 85:
    print("Excellent")
elif average_marks >= 75:
    print("Good")
elif average_marks >= 65:
    print("Average")
else:
    print('Needs Improvement')
#attendence condions
if attendence <= 75:
    print("WARNING Low Attendance")
else:
    print("Attendence satishfied")


