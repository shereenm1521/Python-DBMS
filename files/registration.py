import re
def setFirstName():
    firstname = input("What is your FIRST NAME ? ")
    while True:
        if firstname.isalpha():
            return firstname
        else:
            firstname = input("Invalid NAME, What is your FIRST NAME ? ")


def setLastName():
    lastname = input("What is your LAST NAME ? ")
    while True:
        if lastname.isalpha():
            return lastname
        else:
            lastname = input("Invalid NAME What is your LAST NAME ? ")


def setEmail():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email = input("What is your EMAIL ? ")
    while True:
        if re.fullmatch(regex, email):
            return email
        else:
            email = input("Invalid EMAIL, What is your EMAIL ? ")


def setPassword():
    regex_password = r'^(?=.*[a-z])(?=.*[A-Z])(?!.*\s).{8,}$'
    while True:
        password = input("What is your password? ")
        conf_password = input("Please confirm your password? ")
        if re.fullmatch(regex_password, password) and conf_password == password:
            return password
        else:
            if not re.fullmatch(regex_password, password):
                print("Invalid password. Password must be at least 8 characters long, contain both lowercase and uppercase letters, and have no spaces.")
            else:
                print("Passwords do not match.")
                conf_password = input("Please confirm your password? ")

def setMobile():
    mobile_regex = '^01[0-2,5]{1}[0-9]{8}$'
    mobile = input("What is your MOBILE PHONE ? ")
    while True:
        if re.match(mobile_regex, mobile):
            return mobile
        else:
            mobile = input("Invalid MOBILE PHONE, What is your MOBILE PHONE ? ")


def setData():
    firstname = setFirstName()
    lastname = setLastName()
    email = setEmail()
    password = setPassword()
    mobile = setMobile()

    try:
        fileobj = open("info.txt", "a")
        fileobj.write(f"{firstname}:{lastname}:{email}:{password}:{mobile}\n")
        fileobj.close()
        print("=      Registration Done Successfully     =")
    except Exception as e:
        print(f"Registration Failed {e}")


if __name__ == "__main__":
    setData()