import os

path = os.getcwd()
bosver = "clbos-3.0"

dfdr = "~"
directory = dfdr
user = open("username.sf", "r")
password = open("password.sf", "r")
running = 1

def cmnds():
    if cmnd == "dfn":
        print(path)
    if cmnd == "help":
        print("clbasic / CLBasic / Code a Program in CLBasic")
        print("clbasrun / Run CLBasic / Run A CLBasic Script.")
        print("dfn / Directory Full Name / Get full name of the directory CLBOS is located in.")
        print("cdr / Change Directory / See the files of a different directory.")
        print("help / Help / Get all commands.")
        print("cun / Change Username / Replace existing Username with another one.")
        print("cpw / Change Password / Replace existing Password with another one.")
        print("cnf / Create New File / Create a file, with file type and name.")
        print("wdtf / Write data to File / Write text to a file you have created.")
        print("rdff / Read data from File / Read text from a file you have created.")
        print("del / Delete / Delete a specific file you have created.")
        print("echo / Echo / Echo a message to the system.")
        print("add / Add / Add 2 Numbers together.")
        print("sub / Subtract / Subtract 2 Numbers together.")
        print("mul / Multiply / Multiply 2 Numbers together.")
        print("div / Divide / Divide 2 Numbers together.")
        print("cls / Clear Screen / Clear Everything From The Screen/Terminal.")
    if cmnd == "cun":
        username = input("Overwrite Username $ ") 
        u = open("username.txt", "w")
        u.write(username)
        u.close()
    if cmnd == "cdr":
        dtct = input("Directory $ ")
        print(os.listdir(dtct))

    if cmnd == "cpw":
        nwpw = input("New Password $ ")
        p = open("password.txt", "w")
        p.write(nwpw)
        p.close()
    if cmnd == "clbasic":
        print("=====================================================================================")
        print("Welcome To CLBasic 1.1, For Elements; Read 'README' File.")
        print("=====================================================================================")
        Line1 = input("1 | ")
        Line2 = input("2 | ")
        Line3 = input("3 | ")
        Line4 = input("4 | ")
        Line5 = input("5 | ")
        Line6 = input("6 | ")
        Line7 = input("7 | ")
        Line8 = input("8 | ")
        Line9 = input("9 | ")
        Line10 = input("10| ")
        ScriptName = input("Script Name $ ")
        SaveInDir = input("Directory $ ")
        L1 = open(SaveInDir+"/"+ScriptName+"-line1.clb", "x")
        L1W = open(SaveInDir+"/"+ScriptName+"-line1.clb", "w")
        L1W.write(Line1)
        L2 = open(SaveInDir+"/"+ScriptName+"-line2.clb", "x")
        L2W = open(SaveInDir+"/"+ScriptName+"-line2.clb", "w")
        L2W.write(Line2)
        L3 = open(SaveInDir+"/"+ScriptName+"-line3.clb", "x")
        L3W = open(SaveInDir+"/"+ScriptName+"-line3.clb", "w")
        L3W.write(Line3)
        L4 = open(SaveInDir+"/"+ScriptName+"-line4.clb", "x")
        L4W = open(SaveInDir+"/"+ScriptName+"-line4.clb", "w")
        L4W.write(Line4)
        L5 = open(SaveInDir+"/"+ScriptName+"-line5.clb", "x")
        L5W = open(SaveInDir+"/"+ScriptName+"-line5.clb", "w")
        L5W.write(Line5)
        L6 = open(SaveInDir+"/"+ScriptName+"-line6.clb", "x")
        L6W = open(SaveInDir+"/"+ScriptName+"-line6.clb", "w")
        L6W.write(Line6)
        L7 = open(SaveInDir+"/"+ScriptName+"-line7.clb", "x")
        L7W = open(SaveInDir+"/"+ScriptName+"-line7.clb", "w")
        L7W.write(Line7)
        L8 = open(SaveInDir+"/"+ScriptName+"-line8.clb", "x")
        L8W = open(SaveInDir+"/"+ScriptName+"-line8.clb", "w")
        L8W.write(Line8)
        L9 = open(SaveInDir+"/"+ScriptName+"-line9.clb", "x")
        L9W = open(SaveInDir+"/"+ScriptName+"-line9.clb", "w")
        L9W.write(Line9)
        L10 = open(SaveInDir+"/"+ScriptName+"-line10.clb", "x")
        L10W = open(SaveInDir+"/"+ScriptName+"-line10.clb", "w")
        L10W.write(Line10)
        print("To Execute script, Use the command 'clbasrun'.")
    if cmnd == "clbasrun":
        ScriptName = input("Script Name $ ")
        SaveInDir = input("Directory $ ")
        L1R = open(SaveInDir+"/"+ScriptName+"-line1.clb", "r")
        L1R = L1R.read()
        L2R = open(SaveInDir+"/"+ScriptName+"-line2.clb", "r")
        L2R = L2R.read()
        L3R = open(SaveInDir+"/"+ScriptName+"-line3.clb", "r")
        L3R = L3R.read()
        L4R = open(SaveInDir+"/"+ScriptName+"-line4.clb", "r")
        L4R = L4R.read()
        L5R = open(SaveInDir+"/"+ScriptName+"-line5.clb", "r")
        L5R = L5R.read()
        L6R = open(SaveInDir+"/"+ScriptName+"-line6.clb", "r")
        L6R = L6R.read()
        L7R = open(SaveInDir+"/"+ScriptName+"-line7.clb", "r")
        L7R = L7R.read()
        L8R = open(SaveInDir+"/"+ScriptName+"-line8.clb", "r")
        L8R = L8R.read()
        L9R = open(SaveInDir+"/"+ScriptName+"-line9.clb", "r")
        L9R = L9R.read()
        L10R = open(SaveInDir+"/"+ScriptName+"-line10.clb", "r")
        L10R = L10R.read()
        if L1R == "print":
            print(L2R)
        if L1R == "inp":
            a = input(L2R+" $"+" ")
            print(a)
        if L1R == "ipi":
            print("ERROR: No Previous Input.")
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
        if L2R == "ipi":
            prinp = a
            equals_to_var = L3R
            ipi_then = L4R
            ipi_else = L5R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
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
        if L3R == "ipi":
            prinp = b
            equals_to_var = L4R
            ipi_then = L5R
            ipi_else = L6R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
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
        if L4R == "ipi":
            prinp = c
            equals_to_var = L5R
            ipi_then = L6R
            ipi_else = L7R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
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
        if L5R == "ipi":
            prinp = d
            equals_to_var = L6R
            ipi_then = L7R
            ipi_else = L8R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
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
        if L6R == "ipi":
            prinp = e
            equals_to_var = L7R
            ipi_then = L8R
            ipi_else = L9R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
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
        if L7R == "ipi":
            prinp = f
            equals_to_var = L8R
            ipi_then = L9R
            ipi_else = L10R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
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
        if L8R == "ipi":
            print("ERROR: No Space Left.")
        if L8R == "svb":
            vn = L9R
            v = L10R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(v)
        if L8R == "svfpi":
            vn = L9R
            prinps = g
            open(vn+".var", "x")
            svbf = open(vn+".var", "w")
            svbf.write(prinps)
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
        if L9R == "ipi":
            print("ERROR: No Space Left.")
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
        if L9R == "tap":
            program = L10R
            L1R2 = open(program+"-line1.clb", "r")
            L1R2 = L1R2.read()
            L2R2 = open(program+"-line2.clb", "r")
            L2R2 = L2R2.read()
            L3R2 = open(program+"-line3.clb", "r")
            L3R2 = L3R2.read()
            L4R2 = open(program+"-line4.clb", "r")
            L4R2 = L4R2.read()
            L5R2 = open(program+"-line5.clb", "r")
            L5R2 = L5R2.read()
            L6R2 = open(program+"-line6.clb", "r")
            L6R2 = L6R2.read()
            L7R2 = open(program+"-line7.clb", "r")
            L7R2 = L7R2.read()
            L8R2 = open(program+"-line8.clb", "r")
            L8R2 = L8R2.read()
            L9R2 = open(program+"-line9.clb", "r")
            L9R2 = L9R2.read()
            L10R2 = open(program+"-line10.clb", "r")
            L10R2 = L10R2.read()
            if L1R2 == "print":
                print(L2R2)
            if L1R2 == "inp":
                aa = input(L2R2+" $"+" ")
                print(aa)
            if L1R2 == "ipi":
                print("ERROR: No Previous Input.")
            if L1R2 == "svb":
                vn = L2R2
                v = L3R2
                svb = open(vn+".var", "x")
                svb = open(vn+".var", "w")
                svb.write(v)
            if L1R2 == "rvb":
                vs = L2R2
                vr = open(vs+".var", "r")
                print(vr.read())
            if L1R2 == "minpp":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) + float(sv)
                print(inpsm)
            if L1R2 == "minpm":
                fv = input("First $ ")
                sv = input("Second $" )
                inpsm = float(fv) - float(sv)
                print(inpsm)
            if L1R2 == "minpmu":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) * float(sv)
                print(inpsm)
            if L1R2 == "minpd":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) / float(sv)
                print(inpsm)
            if L1R2 == "sminpp":
                fv = input("First $ ")
                inpsm = float(L2R2) + float(fv)
                print(inpsm)
            if L1R2 == "sminpm":
                fv = input("First $ ")
                inpsm = float(L2R2) - float(fv)
                print(inpsm)
            if L1R2 == "sminpmu":
                fv = input("First $ ")
                inpsm = float(L2R2) * float(fv)
                print(inpsm)
            if L1R2 == "sminpd":
                fv = input("First $ ")
                inpsm = float(L2R2) / float(fv)
                print(inpsm)
            if L2R2 == "print":
                print(L3R2)
            if L2R2 == "inp":
                ba = input(L3R2+" $"+" ")
                print(ba)
            if L2R2 == "ipi":
                prinp = aa
                equals_to_var = L3R2
                ipi_then = L4R2
                ipi_else = L5R2
                if prinp == equals_to_var:
                    print(ipi_then)
                if prinp != equals_to_var:
                    print(ipi_else)
            if L2R2 == "svb":
                vn = L3R
                v = L4R
                svb = open(vn+".var", "x")
                svb = open(vn+".var", "w")
                svb.write(v)
            if L2R2 == "rvb":
                vs = L3R2
                vr = open(vs+".var", "r")
                print(vr.read())
            if L2R2 == "minpp":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) + float(sv)
                print(inpsm)
            if L2R2 == "minpm":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) - float(sv)
                print(inpsm)
            if L2R2 == "minpmu":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) * float(sv)
                print(inpsm)
            if L2R2 == "minpd":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) / float(sv)
                print(inpsm)
            if L2R2 == "sminpp":
                fv = input("First $ ")
                inpsm = float(L3R2) + float(fv)
                print(inpsm)
            if L2R2 == "sminpm":
                fv = input("First $ ")
                inpsm = float(L3R2) - float(fv)
                print(inpsm)
            if L2R2 == "sminpmu":
                fv = input("First $ ")
                inpsm = float(L3R2) * float(fv)
                print(inpsm)
            if L2R2 == "sminpd":
                fv = input("First $ ")
                inpsm = float(L3R2) / float(fv)
                print(inpsm)
            if L3R2 == "print":
                print(L4R2)
            if L3R2 == "inp":
                ca = input(L4R2+" $"+" ")
                print(ca)
            if L3R2 == "ipi":
                prinp = ba
                equals_to_var = L4R2
                ipi_then = L5R2
                ipi_else = L6R2
                if prinp == equals_to_var:
                    print(ipi_then)
                if prinp != equals_to_var:
                    print(ipi_else)
            if L3R2 == "svb":
                vn = L4R2
                v = L5R2
                svb = open(vn+".var", "x")
                svb = open(vn+".var", "w")
                svb.write(v)
            if L3R2 == "rvb":
                vs = L4R2
                vr = open(vs+".var", "r")
                print(vr.read())
            if L3R2 == "minpp":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) + float(sv)
                print(inpsm)
            if L3R2 == "minpm":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) - float(sv)
                print(inpsm)
            if L3R2 == "minpmu":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) * float(sv)
                print(inpsm)
            if L3R2 == "minpd":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) / float(sv)
                print(inpsm)
            if L3R2 == "sminpp":
                fv = input("First $ ")
                inpsm = float(L4R2) + float(fv)
                print(inpsm)
            if L3R2 == "sminpm":
                fv = input("First $ ")
                inpsm = float(L4R2) - float(fv)
                print(inpsm)
            if L3R2 == "sminpmu":
                fv = input("First $ ")
                inpsm = float(L4R2) * float(fv)
                print(inpsm)
            if L3R2 == "sminpd":
                fv = input("First $ ")
                inpsm = float(L4R2) / float(fv)
                print(inpsm)
            if L4R2 == "print":
                print(L5R2)
            if L4R2 == "inp":
                da = input(L5R2+" $"+" ")
                print(da)
            if L4R2 == "ipi":
                prinp = ca
                equals_to_var = L5R2
                ipi_then = L6R2
                ipi_else = L7R2
                if prinp == equals_to_var:
                    print(ipi_then)
                if prinp != equals_to_var:
                    print(ipi_else)
            if L4R2 == "svb":
                vn = L5R2
                v = L6R2
                svb = open(vn+".var", "x")
                svb = open(vn+".var", "w")
                svb.write(v)
            if L4R2 == "rvb":
                vs = L5R2
                vr = open(vs+".var", "r")
                print(vr.read())
            if L4R2 == "minpp":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) + float(sv)
                print(inpsm)
            if L4R2 == "minpm":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) - float(sv)
                print(inpsm)
            if L4R2 == "minpmu":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) * float(sv)
                print(inpsm)
            if L4R2 == "minpd":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) / float(sv)
                print(inpsm)
            if L4R2 == "sminpp":
                fv = input("First $ ")
                inpsm = float(L5R2) + float(fv)
                print(inpsm)
            if L4R2 == "sminpm":
                fv = input("First $ ")
                inpsm = float(L5R2) - float(fv)
                print(inpsm)
            if L4R2 == "sminpmu":
                fv = input("First $ ")
                inpsm = float(L5R2) * float(fv)
                print(inpsm)
            if L4R2 == "sminpd":
                fv = input("First $ ")
                inpsm = float(L5R2) / float(fv)
                print(inpsm)
            if L5R2 == "print":
                print(L6R2)
            if L5R2 == "inp":
                ea = input(L6R2+" $"+" ")
                print(ea)
            if L5R2 == "ipi":
                prinp = da
                equals_to_var = L6R2
                ipi_then = L7R2
                ipi_else = L8R2
                if prinp == equals_to_var:
                    print(ipi_then)
                if prinp != equals_to_var:
                    print(ipi_else)
            if L5R2 == "svb":
                vn = L6R2
                v = L7R2
                svb = open(vn+".var", "x")
                svb = open(vn+".var", "w")
                svb.write(v)
            if L5R2 == "rvb":
                vs = L6R2
                vr = open(vs+".var", "r")
                print(vr.read())
            if L5R2 == "minpp":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) + float(sv)
                print(inpsm)
            if L5R2 == "minpm":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) - float(sv)
                print(inpsm)
            if L5R2 == "minpmu":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) * float(sv)
                print(inpsm)
            if L5R2 == "minpd":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) / float(sv)
                print(inpsm)
            if L5R2 == "sminpp":
                fv = input("First $ ")
                inpsm = float(L6R2) + float(fv)
                print(inpsm)
            if L5R2 == "sminpm":
                fv = input("First $ ")
                inpsm = float(L6R2) - float(fv)
                print(inpsm)
            if L5R2 == "sminpmu":
                fv = input("First $ ")
                inpsm = float(L6R2) * float(fv)
                print(inpsm)
            if L5R2 == "sminpd":
                fv = input("First $ ")
                inpsm = float(L6R2) / float(fv)
                print(inpsm)
            if L6R2 == "print":
                print(L7R2)
            if L6R2 == "inp":
                fa = input(L7R2+" $"+" ")
                print(fa)
            if L6R2 == "ipi":
                prinp = ea
                equals_to_var = L7R2
                ipi_then = L8R2
                ipi_else = L9R2
                if prinp == equals_to_var:
                    print(ipi_then)
                if prinp != equals_to_var:
                    print(ipi_else)
            if L6R2 == "svb":
                vn = L7R2
                v = L8R2
                svb = open(vn+".var", "x")
                svb = open(vn+".var", "w")
                svb.write(v)
            if L6R2 == "rvb":
                vs = L7R2
                vr = open(vs+".var", "r")
                print(vr.read())
            if L6R2 == "minpp":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) + float(sv)
                print(inpsm)
            if L6R2 == "minpm":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) - float(sv)
                print(inpsm)
            if L6R2 == "minpmu":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) * float(sv)
                print(inpsm)
            if L6R2 == "minpd":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) / float(sv)
                print(inpsm)
            if L6R2 == "sminpp":
                fv = input("First $ ")
                inpsm = float(L7R2) + float(fv)
                print(inpsm)
            if L6R2 == "sminpm":
                fv = input("First $ ")
                inpsm = float(L7R2) - float(fv)
                print(inpsm)
            if L6R2 == "sminpmu":
                fv = input("First $ ")
                inpsm = float(L7R2) * float(fv)
                print(inpsm)
            if L6R2 == "sminpd":
                fv = input("First $ ")
                inpsm = float(L7R2) / float(fv)
                print(inpsm)
            if L7R2 == "print":
                print(L8R2)
            if L7R2 == "inp":
                ga = input(L8R2+" $"+"")
            if L7R2 == "ipi":
                prinp = fa
                equals_to_var = L8R2
                ipi_then = L9R2
                ipi_else = L10R2
                if prinp == equals_to_var:
                    print(ipi_then)
                if prinp != equals_to_var:
                    print(ipi_else)
            if L7R2 == "svb":
                vn = L8R2
                v = L9R2
                svb = open(vn+".var", "x")
                svb = open(vn+".var", "w")
                svb.write(v)
            if L7R2 == "rvb":
                vs = L8R2
                vr = open(vs+".var", "r")
                print(vr.read())
            if L7R2 == "minpp":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) + float(sv)
                print(inpsm)
            if L7R2 == "minpm":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) - float(sv)
                print(inpsm)
            if L7R2 == "minpmu":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) * float(sv)
                print(inpsm)
            if L7R2 == "minpd":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) / float(sv)
                print(inpsm)
            if L7R2 == "sminpp":
                fv = input("First $ ")
                inpsm = float(L8R2) + float(fv)
                print(inpsm)
            if L7R2 == "sminpm":
                fv = input("First $ ")
                inpsm = float(L8R2) - float(fv)
                print(inpsm)
            if L7R2 == "sminpmu":
                fv = input("First $ ")
                inpsm = float(L8R2) * float(fv)
                print(inpsm)
            if L7R2 == "sminpd":
                fv = input("First $ ")
                inpsm = float(L8R2) / float(fv)
                print(inpsm)
            if L8R2 == "print":
                print(L9R2)
            if L8R2 == "inp":
                h = input(L9R2+" $"+" ")
                print(h)
            if L8R2 == "ipi":
                print("ERROR: No Space Left.")
            if L8R2 == "svb":
                vn = L9R2
                v = L10R2
                svb = open(vn+".var", "x")
                svb = open(vn+".var", "w")
                svb.write(v)
            if L8R2 == "rvb":
                vs = L9R2
                vr = open(vs+".var", "r")
                print(vr.read())
            if L8R2 == "minpp":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) + float(sv)
                print(inpsm)
            if L8R2 == "minpm":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) - float(sv)
                print(inpsm)
            if L8R2 == "minpmu":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) * float(sv)
                print(inpsm)
            if L8R2 == "minpd":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) / float(sv)
                print(inpsm)
            if L8R2 == "sminpp":
                fv = input("First $ ")
                inpsm = float(L9R2) + float(fv)
                print(inpsm)
            if L8R2 == "sminpm":
                fv = input("First $ ")
                inpsm = float(L9R2) - float(fv)
                print(inpsm)
            if L8R2 == "sminpmu":
                fv = input("First $ ")
                inpsm = float(L9R2) * float(fv)
                print(inpsm)
            if L8R2 == "sminpd":
                fv = input("First $ ")
                inpsm = float(L9R2) / float(fv)
                print(inpsm)
            if L9R2 == "print":
                print(L10R2)
            if L9R2 == "inp":
                i = input(L10R2+" $"+" ")
                print(i)
            if L9R2 == "ipi":
                print("ERROR: No Space Left.")
            if L9R2 == "svb":
                print("ERROR: No Space Left.")
            if L9R2 == "rvb":
                vs = L10R2
                vr = open(vs+".var", "r")
                print(vr.read())
            if L9R2 == "minpp":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) + float(sv)
                print(inpsm)
            if L9R2 == "minpm":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) - float(sv)
                print(inpsm)
            if L9R2 == "minpmu":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) * float(sv)
                print(inpsm)
            if L9R2 == "minpd":
                fv = input("First $ ")
                sv = input("Second $ ")
                inpsm = float(fv) / float(sv)
                print(inpsm)
            if L9R2 == "sminpp":
                fv = input("First $ ")
                inpsm = float(L10R2) + float(fv)
                print(inpsm)
            if L9R2 == "sminpm":
                fv = input("First $ ")
                inpsm = float(L10R2) - float(fv)
                print(inpsm)
            if L9R2 == "sminpmu":
                fv = input("First $ ")
                inpsm = float(L10R2) * float(fv)
                print(inpsm)
            if L9R2 == "sminpd":
                fv = input("First $ ")
                inpsm = float(L10R2) / float(fv)
                print(inpsm)
            if L9R2 == "tap":
                print("ERROR: Cannot Do Multiple 'tap' Commands.")
            if L10R2 == "print":
                print("ERROR: No Space Left.")
            if L10R2 == "inp":
                print("ERROR: No Space Left.")
            if L10R2 == "ipi":
                print("ERROR: No Space Left.")
            if L10R2 == "svb":
                print("ERROR: No Space Left.")
            if L10R2 == "rvb":
                print("ERROR: No Space Left.")
            if L10R2 == "print":
                print("ERROR: No Space Left.")
            if L10R2 == "inp":
                print("ERROR: No Space Left.")
            if L10R2 == "svb":
                print("ERROR: No Space Left.")
            if L10R2 == "rvb":
                print("ERROR: No Space Left.")
            if L10R2 == "minpp":
                print("ERROR: No Space Left.")
            if L10R2 == "minpm":
                print("ERROR: No Space Left.")
            if L10R2 == "minpmu":
                print("ERROR: No Space Left.")
            if L10R2 == "minpd":
                print("ERROR: No Space Left.")
            if L10R2 == "sminpp":
                print("ERROR: No Space Left.")
            if L10R2 == "sminpm":
                print("ERROR: No Space Left.")
            if L10R2 == "sminpmu":
                print("ERROR: No Space Left.")
            if L10R2 == "sminpd":
                print("ERROR: No Space Left.")
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
        if L10R == "ipi":
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
    if cmnd == "del":
        dlf = input("File Name $ ")
        if dlf != "CLBOS.py":
            os.remove(dlf)
    if cmnd == "cls":
        os.system('cls')
    
PIN = input("Password $ ")
if PIN == password.read():
    while running == 1:
        user = open("username.sf", "r")
        print(user.read(), "@", bosver ,"/ dir $",directory)
        cmnd = input("$ ")
        cmnds()
