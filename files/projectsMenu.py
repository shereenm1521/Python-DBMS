"""
main menu for projects function
"""
from createProject import setData
from viewProjects import viewAllProjects
from deleteProject import delete_Project
from editProject import edit_Project
from searchProject import search_Project


def projectMenu(userid):
    while True:
        choice = input("Please choose from the following menu : "
                       "\n 1) Create Project"
                       "\n 2) View All projects"
                       "\n 3) Edit your project"
                       "\n 4) Delete your project"
                       "\n 5) Search for a project"
                       "\n 6) Log Out"
                       "\n 7) Exit"
                       "\n")
        if choice == "1":
            # 1) Create Project
            setData(userid)
            projectMenu(userid)
            break
        elif choice == "2":
            # 2) View All projects
            viewAllProjects(userid)
            projectMenu(userid)
            break
        elif choice == "3":
            # 3) Edit your project
            edit_Project()  # still not scripted
            projectMenu(userid)
            break
        elif choice == "4":
            # 4) Delete your project
            delete_Project(userid)
            projectMenu(userid)
            break
        elif choice == "5":
            # 5) Search for a project
            search_Project()  # still not scripted
            projectMenu(userid)
            break
        elif choice == "6":
            # 6) Log Out
            print("=  Logged out  =")
            break
        elif choice == "7":
            # 7) Exit
            print("=  Bye  =")
            exit()
        else:
            print("Invalid Entry, please select again ...")
            projectMenu(userid)
