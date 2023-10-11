from registration import setData
from login import userLogin


def mainFunction():
    option = input("Please choose registration or login : \n 1) Registration \n 2) Login \n 3) Exit \n")
    while True:
        if option == "1":
            setData()
            mainFunction()
            break
        elif option == "2":
            userLogin()
            mainFunction()
            break
        elif option == "3":
            print("=  Bye  =")
            exit()
        else:
            print("Try")
            option = input("You should choose registration or login : \n 1) Registration \n 2) Login \n 3) Exit")


if __name__ == "__main__":
    mainFunction()
