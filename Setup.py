u = open("username.sf", "x")
p = open("password.sf", "x")

Start_Installation = input("Type Y To Start Setup: ")
if Start_Installation == "Y":
    username = input("Username $ ")
    password = input("Password $ ")
    u = open("username.sf", "a")
    u.write(username)
    u.close()
    p = open("password.sf", "a")
    p.write(password)
    p.close()
input("")