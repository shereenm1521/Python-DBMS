def edit_Project():
    old = input("Enter data you want to edit it :")
    new = input("Enter new data want to add it :")
    with open("projectInfo.txt", "r") as file_obj_r:
        new_line = []
        for word in file_obj_r.readlines():
            new_line.append(word.replace(old, new))
            print("data updated successfully")
            with open("projectInfo.txt", "w") as file_obj_w:
                for line in new_line:
                    file_obj_w.writelines(line)
