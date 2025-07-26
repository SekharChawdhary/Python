'''
Assume the correct OTP is already stored in a variable.
Ask the user to input a 4-digit OTP.
If the OTP entered is not 4 digits, display
OTP Must be 4 digit number only
If the OTP is correct, display:
Correct OTP - Success
If the OTP is incorrect, decrease the attempts count.
After 3 incorrect attempts, display
Maximum attempts done, try after 24 Hours

'''
import random
otp = str(random.randint(1000,9999))
print(f"Your opt is: {otp}")
attempts=3
while attempts > 0 :
    user_otp=input("Enter 4 digits otp")
    if len(user_otp) !=4:
        print("Otp should be 4 digit")
        continue
    if user_otp == otp:
        print("Otp seccess")
        break
    else:
        attempts-=1
        if attempts > 0:
            print(f"Invalid otp {attempts} attempts left")
        else:
            print("Maximum attempts reached, try after 24 hours")


