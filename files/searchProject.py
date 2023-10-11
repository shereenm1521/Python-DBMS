def search_Project():

    string = input("Enter any information about the Project you want to search : ")
    with open("projectInfo.txt", "r+") as f:
        s = f.readlines()
        found = ''
    for line in s:
        if string in line:
            print("The project is found : ")
            print(line)
            found = 'yes'
            break
    if found == 'yes':
        pass
    else:
        print("The project is not found !")
