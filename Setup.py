u = open("username.txt", "x")
p = open("password.txt", "x")

Start_Installation = input("Type Y To Start Setup: ")
if Start_Installation == "Y":
    username = input("Username: ")
    password = input("Password: ")
    u = open("username.txt", "a")
    u.write(username)
    u.close()
    p = open("password.txt", "a")
    p.write(password)
    p.close()
input("")