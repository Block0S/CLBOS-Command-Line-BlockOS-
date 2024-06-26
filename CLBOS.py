import os

path = os.getcwd()
bosver = "clbos-2.0"
directory = os.getcwd()
user = open("username.sf", "r")
password = open("password.sf", "r")


def cmnds():
    if cmnd == "dfn":
        print(path)
    if cmnd == "help":
        print("dfn / Directory Full Name / Get full name of the directory CLBOS is located in.")
        print("help / Help / Get all commands.")
        print("cun / Change Username / Replace existing Username with another one.")
        print("cpw / Change Password / Replace existing Password with another one.")
        print("cnf / Create New File / Create a file, with file type and name.")
        print("wdtf / Write data to File / Write text to a file you have created.")
        print("rdff / Read data from File / Read text from a file you have created.")
        print("echo / Echo / Echo a message to the system.")
        print("add / Add / Add 2 Numbers together.")
        print("sub / Subtract / Subtract 2 Numbers together.")
        print("mul / Multiply / Multiply 2 Numbers together.")
        print("div / Divide / Divide 2 Numbers together.")
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
    if cmnd == "clbasic":
        print("=====================================================================================")
        print("Welcome To CLBasic 1.0, For Elements; Read 'README' File.")
        print("=====================================================================================")
        Line1 = input("")
        Line2 = input("")
        Line3 = input("")
        Line4 = input("")
        Line5 = input("")
        Line6 = input("")
        Line7 = input("")
        Line8 = input("")
        Line9 = input("")
        Line10 = input("")
        ScriptName = input("Script Name $ ")
        L1 = open(ScriptName+"-line1.clb", "x")
        L1W = open(ScriptName+"-line1.clb", "w")
        L1W.write(Line1)
        L2 = open(ScriptName+"-line2.clb", "x")
        L2W = open(ScriptName+"-line2.clb", "w")
        L2W.write(Line2)
        L3 = open(ScriptName+"-line3.clb", "x")
        L3W = open(ScriptName+"-line3.clb", "w")
        L3W.write(Line3)
        L4 = open(ScriptName+"-line4.clb", "x")
        L4W = open(ScriptName+"-line4.clb", "w")
        L4W.write(Line4)
        L5 = open(ScriptName+"-line5.clb", "x")
        L5W = open(ScriptName+"-line5.clb", "w")
        L5W.write(Line5)
        L6 = open(ScriptName+"-line6.clb", "x")
        L6W = open(ScriptName+"-line6.clb", "w")
        L6W.write(Line6)
        L7 = open(ScriptName+"-line7.clb", "x")
        L7W = open(ScriptName+"-line7.clb", "w")
        L7W.write(Line7)
        L8 = open(ScriptName+"-line8.clb", "x")
        L8W = open(ScriptName+"-line8.clb", "w")
        L8W.write(Line8)
        L9 = open(ScriptName+"-line9.clb", "x")
        L9W = open(ScriptName+"-line9.clb", "w")
        L9W.write(Line9)
        L10 = open(ScriptName+"-line10.clb", "x")
        L10W = open(ScriptName+"-line10.clb", "w")
        L10W.write(Line10)
        print("To Execute script, Use the command 'clbasrun'.")
    if cmnd == "clbasrun":
        ScriptName = input("Script Name $ ")
        L1R = open(ScriptName+"-line1.clb", "r")
        L1R = L1R.read()
        L2R = open(ScriptName+"-line2.clb", "r")
        L2R = L2R.read()
        L3R = open(ScriptName+"-line3.clb", "r")
        L3R = L3R.read()
        L4R = open(ScriptName+"-line4.clb", "r")
        L4R = L4R.read()
        L5R = open(ScriptName+"-line5.clb", "r")
        L5R = L5R.read()
        L6R = open(ScriptName+"-line6.clb", "r")
        L6R = L6R.read()
        L7R = open(ScriptName+"-line7.clb", "r")
        L7R = L7R.read()
        L8R = open(ScriptName+"-line8.clb", "r")
        L8R = L8R.read()
        L9R = open(ScriptName+"-line9.clb", "r")
        L9R = L9R.read()
        L10R = open(ScriptName+"-line10.clb", "r")
        L10R = L10R.read()
        if L1R == "print":
            print(L2R)
        if L1R == "inp":
            a = input(L2R+" $"+" ")
            print(a)
        if L1R == "svb":
            vn = L2R
            v = L3R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(v)
        if L1R == "rvb":
            vs = L2R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L1R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L1R == "minpm":
            fv = input("First $ ")
            sv = input("Second $" )
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L1R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L1R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L1R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L2R) + float(fv)
            print(inpsm)
        if L1R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L2R) - float(fv)
            print(inpsm)
        if L1R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L2R) * float(fv)
            print(inpsm)
        if L1R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L2R) / float(fv)
            print(inpsm)
        if L2R == "print":
            print(L3R)
        if L2R == "inp":
            b = input(L3R+" $"+" ")
            print(b)
        if L2R == "svb":
            vn = L3R
            v = L4R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(v)
        if L2R == "rvb":
            vs = L3R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L2R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L2R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L2R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L2R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L2R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L3R) + float(fv)
            print(inpsm)
        if L2R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L3R) - float(fv)
            print(inpsm)
        if L2R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L3R) * float(fv)
            print(inpsm)
        if L2R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L3R) / float(fv)
            print(inpsm)
        if L3R == "print":
            print(L4R)
        if L3R == "inp":
            c = input(L4R+" $"+" ")
            print(c)
        if L3R == "svb":
            vn = L4R
            v = L5R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(v)
        if L3R == "rvb":
            vs = L4R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L3R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L3R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L3R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L3R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L3R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L4R) + float(fv)
            print(inpsm)
        if L3R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L4R) - float(fv)
            print(inpsm)
        if L3R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L4R) * float(fv)
            print(inpsm)
        if L3R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L4R) / float(fv)
            print(inpsm)
        if L4R == "print":
            print(L5R)
        if L4R == "inp":
            d = input(L5R+" $"+" ")
            print(d)
        if L4R == "svb":
            vn = L5R
            v = L6R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(v)
        if L4R == "rvb":
            vs = L5R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L4R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L4R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L4R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L4R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L4R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L5R) + float(fv)
            print(inpsm)
        if L4R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L5R) - float(fv)
            print(inpsm)
        if L4R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L5R) * float(fv)
            print(inpsm)
        if L4R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L5R) / float(fv)
            print(inpsm)
        if L5R == "print":
            print(L6R)
        if L5R == "inp":
            e = input(L6R+" $"+" ")
            print(e)
        if L5R == "svb":
            vn = L6R
            v = L7R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(v)
        if L5R == "rvb":
            vs = L6R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L5R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L5R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L5R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L5R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L5R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L6R) + float(fv)
            print(inpsm)
        if L5R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L6R) - float(fv)
            print(inpsm)
        if L5R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L6R) * float(fv)
            print(inpsm)
        if L5R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L6R) / float(fv)
            print(inpsm)
        if L6R == "print":
            print(L7R)
        if L6R == "inp":
            f = input(L7R+" $"+" ")
            print(f)
        if L6R == "svb":
            vn = L7R
            v = L8R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(v)
        if L6R == "rvb":
            vs = L7R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L6R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L6R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L6R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L6R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L6R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L7R) + float(fv)
            print(inpsm)
        if L6R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L7R) - float(fv)
            print(inpsm)
        if L6R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L7R) * float(fv)
            print(inpsm)
        if L6R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L7R) / float(fv)
            print(inpsm)
        if L7R == "print":
            print(L8R)
        if L7R == "inp":
            g = input(L8R+" $"+"")
        if L7R == "svb":
            vn = L8R
            v = L9R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(v)
        if L7R == "rvb":
            vs = L8R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L7R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L7R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L7R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L7R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L7R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L8R) + float(fv)
            print(inpsm)
        if L7R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L8R) - float(fv)
            print(inpsm)
        if L7R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L8R) * float(fv)
            print(inpsm)
        if L7R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L8R) / float(fv)
            print(inpsm)
        if L8R == "print":
            print(L9R)
        if L8R == "inp":
            h = input(L9R+" $"+" ")
            print(h)
        if L8R == "svb":
            vn = L9R
            v = L10R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(v)
        if L8R == "rvb":
            vs = L9R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L8R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L8R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L8R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L8R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L8R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L9R) + float(fv)
            print(inpsm)
        if L8R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L9R) - float(fv)
            print(inpsm)
        if L8R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L9R) * float(fv)
            print(inpsm)
        if L8R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L9R) / float(fv)
            print(inpsm)
        if L9R == "print":
            print(L10R)
        if L9R == "inp":
            i = input(L10R+" $"+" ")
            print(i)
        if L9R == "svb":
            print("ERROR: No Space Left.")
        if L9R == "rvb":
            vs = L10R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L9R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L9R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L9R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L9R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L9R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L10R) + float(fv)
            print(inpsm)
        if L9R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L10R) - float(fv)
            print(inpsm)
        if L9R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L10R) * float(fv)
            print(inpsm)
        if L9R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L10R) / float(fv)
            print(inpsm)
        if L10R == "print":
            print("ERROR: No Space Left.")
        if L10R == "inp":
            print("ERROR: No Space Left.")
        if L10R == "svb":
            print("ERROR: No Space Left.")
        if L10R == "rvb":
            print("ERROR: No Space Left.")
        if L10R == "print":
            print("ERROR: No Space Left.")
        if L10R == "inp":
            print("ERROR: No Space Left.")
        if L10R == "svb":
            print("ERROR: No Space Left.")
        if L10R == "rvb":
            print("ERROR: No Space Left.")
        if L10R == "minpp":
            print("ERROR: No Space Left.")
        if L10R == "minpm":
            print("ERROR: No Space Left.")
        if L10R == "minpmu":
            print("ERROR: No Space Left.")
        if L10R == "minpd":
            print("ERROR: No Space Left.")
        if L10R == "sminpp":
            print("ERROR: No Space Left.")
        if L10R == "sminpm":
            print("ERROR: No Space Left.")
        if L10R == "sminpmu":
            print("ERROR: No Space Left.")
        if L10R == "sminpd":
            print("ERROR: No Space Left.")
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
    
PIN = input("Password $ ")
if PIN == password.read():
    print(user.read(), "@", bosver ,"/ dir $",directory)
    cmnd = input("$ ")
    cmnds()
