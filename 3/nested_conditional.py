name = ''
phone = ''

if(len(name)==0 or len(phone)==0):
    print("All fields need to be required")
else:
    if(len(name)<2):
        print("The name length must be minimum 2")
    elif(len(phone)!=11):
        print("The phone length must be minimum 11")
    else:
        otp = "otp send"
        generated_otp = '1234'
        if(otp!=generated_otp):
            print("otp does not match")
        else:
            print("registration successful")
