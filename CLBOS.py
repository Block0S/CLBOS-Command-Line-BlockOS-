import os

path = os.getcwd()
directory = "~"
user = open("username.txt", "r")
password = open("password.txt", "r")
def cmnds():
    if cmnd == "dfn":
        print(path)
    if cmnd == "help":
        print("dfn - Directory Full Name - Get full name of the directory CLBOS is located in.")
        print("help - Help - Get all commands.")
        print("cun - Change Username - Replace existing Username with another one.")
        print("cpw - Change Password - Replace existing Password with another one.")
        print("cnf - Create New File - Create a file, with file type and name.")
        print("wdtf - Write data to File - Write text to a file you have created.")
        print("echo - Echo - Echo a message to the system.")
        print("add - Add - Add 2 Numbers together.")
        print("sub - Subtract - Subtract 2 Numbers together.")
        print("mul - Multiply - Multiply 2 Numbers together.")
        print("div - Divide - Divide 2 Numbers together.")

    if cmnd == "cun":
        username = input("Overwrite Username $ ") 
        u = open("username.txt", "w")
        u.write(username)
        u.close()
    if cmnd == "cpw":
        nwpw = input("New Password $ ")
        p = open("password.txt", "w")
        p.write(nwpw)
        p.close()
    if cmnd == "cnf":
        cnf = input("File Name $ ")
        cnf = open(cnf, "x")
    if cmnd == "wdtf":
        cf = input("File Name $ ")
        wdtf = input("Text/Data $ ")
        p = open(cf, "w")
        p.write(wdtf)
        p.close()
    if cmnd == "rdff":
        file_selected = input("File Name $ ")
        file_readed = open(file_selected, "r")
        print(file_readed.read())
    if cmnd == "echo":
        eh = input("Echo $ ")
        print(eh)
    if cmnd == "add":
        First = float(input("First $ "))
        Second = float(input("Second $ "))
        sum = Second + First
        print("sum $ " + str(sum))
    if cmnd == "sub":
        First = float(input("First $ "))
        Second = float(input("Second $ "))
        sum = Second - First
        print("sum $ " + str(sum))
    if cmnd == "mul":
        First = float(input("First $ "))
        Second = float(input("Second $ "))
        sum = Second * First
        print("sum $ " + str(sum))
    if cmnd == "div":
        First = float(input("First $ "))
        Second = float(input("Second $ "))
        sum = Second / First
        print("sum $ " + str(sum))
    
    
print(user.read(), "@ clbos-1.0" ,"/ dir:",directory)
PIN = input("Password: ")
if PIN == password.read():
    cmnd = input("$ ")
    cmnds()
