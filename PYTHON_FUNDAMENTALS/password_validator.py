def validate_password(password):
    if len(password) < 8:
        print("Invalid password!!")
    else:
        for char in password:
            if char.isdigit() == True:
                print("Valid password!")
                break
            elif char.isupper() == True:
                print("Valid password!")
                break
            elif char.islower() == True:
                print("Valid password!")
                break
            else:
                print("Invalid password!")

password = input("Enter password :")
validate_password(password)