def delete_Project(userid):
    print("-------------- Delete Project ---------------------")
    project_title = input("Project Title: ")
    project_id = input("Project ID: ")

    try:
        with open("projectInfo.txt", "r") as file_obj:
            lines = file_obj.readlines()

        new_lines = []
        for line in lines:
            project_info = line.split(":")
            if (
                len(project_info) >= 7
                and project_info[0] == project_id
                and project_info[1] == project_title
            ):
                continue
            new_lines.append(line)

        with open("projectInfo.txt", "w") as file_obj:
            file_obj.writelines(new_lines)

        print("=      Project Deleted Successfully       =")
    except Exception as e:
        print(e)
