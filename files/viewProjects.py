"""
view all projects function
"""
import projectsMenu

def getUserProjects():
    projects = []
    file = open("projectInfo.txt", "r")
    for line in file:
        projects.append(list(line.split(":")))
    file.close()
    return projects

def viewAllProjects(user_id):
    try:
        check_for_empty = getUserProjects()
        if len(check_for_empty) != 0:
            for item in check_for_empty:
                print(f"        Project Id             :       {item[0]}")
                print(f"        Project Title          :       {item[1]}")
                print(f"        Project Details        :       {item[2]}")
                print(f"        Project Total Target   :       {item[3]}")
                print(f"        Project Start Date     :       {item[4]}")
                print(f"        Project Dnd Date       :       {item[5]}")
                print(f"        Project User Id        :       {item[6]}")
        else:
            print("There are no Projects for view, The file is Empty.")

    except Exception as e:
        print(f"Failed to Open the file its not exist. {e}")
    projectsMenu.projectMenu(user_id)
