import datetime


def setProjectId():
    project_id = input("What is your PROJECT ID? ")
    while True:
        if project_id.isdigit():
            return project_id
        else:
            project_id = input("Invalid ID. What is your ID? ")


def setTitle():
    title = input("What is your PROJECT TITLE? ")
    while True:
        if title.isalpha():
            return title
        else:
            title = input("Invalid NAME. What is your PROJECT TITLE? ")


def setDetails():
    details = input("What is your PROJECT DETAILS? ")
    return details


def setTotalTarget():
    total_target = input("What is your TOTAL TARGET? ")
    while True:
        if total_target.isdigit():
            return total_target
        else:
            total_target = input("Invalid TARGET. What is your TOTAL TARGET? ")


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d-%m-%Y')
        return date_text
    except ValueError:
        return None


def setStartDate():
    while True:
        start_date = input("Enter the START DATE in the format DD-MM-YYYY: ")
        if validate(start_date):
            return start_date
        else:
            print("Invalid date format. Please enter the START DATE in the format DD-MM-YYYY.")


def setEndDate():
    while True:
        end_date = input("Enter the END DATE in the format DD-MM-YYYY: ")
        if validate(end_date):
            return end_date
        else:
            print("Invalid date format. Please enter the END DATE in the format DD-MM-YYYY.")


def setData(userid):
    project_id = setProjectId()
    title = setTitle()
    details = setDetails()
    total_target = setTotalTarget()
    start_date = setStartDate()
    end_date = setEndDate()
    project_userid = userid

    try:
        with open("projectInfo.txt", "a") as file_obj:
            file_obj.write(f"{project_id}:{title}:{details}:{total_target}:{start_date}:{end_date}:{project_userid}\n")

        print("=      Project Created Successfully       =")
    except Exception as e:
        print(e)