from projectsMenu import projectMenu


def userLogin():
    try:
        file = open("info.txt", 'r')
        email = input("Please enter your EMAIL ? ")
        password = input("Please enter your PASSWORD ? ")
        login_success = False
        for line in file:
            record = list(line.split(":"))
            if email.lower() == str(record[2]).lower() and password == str(record[3]):
                print("=              you are logged in successfully             =")
                login_success = True
                break
            else:
                login_success = False

        if login_success:
            projectMenu(email)
        else:
            print("=               Invalid login, please try again.                =")

    except Exception as e:
        print(f"Failed to Open the file its not exist. {e}")


if __name__ == "__main__":
    userLogin()
