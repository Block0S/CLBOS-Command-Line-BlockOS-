import os

path = os.getcwd()
bosver = "clbos-3.0.1"

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
        Line11 = input("11| ")
        Line12 = input("12| ")
        Line13 = input("13| ")
        Line14 = input("14| ")
        Line15 = input("15| ")
        Line16 = input("16| ")
        Line17 = input("17| ")
        Line18 = input("18| ")
        Line19 = input("19| ")
        Line20 = input("20| ")
        Line21 = input("21| ")
        Line22 = input("22| ")
        Line23 = input("23| ")
        Line24 = input("24| ")
        Line25 = input("25| ")
        Line26 = input("26| ")
        Line27 = input("27| ")
        Line28 = input("28| ")
        Line29 = input("29| ")
        Line30 = input("30| ")
        Line31 = input("31| ")
        Line32 = input("32| ")
        Line33 = input("33| ")
        Line34 = input("34| ")
        Line35 = input("35| ")
        Line36 = input("36| ")
        Line37 = input("37| ")
        Line38 = input("38| ")
        Line39 = input("39| ")
        Line40 = input("40| ")
        Line41 = input("41| ")
        Line42 = input("42| ")
        Line43 = input("43| ")
        Line44 = input("44| ")
        Line45 = input("45| ")
        Line46 = input("46| ")
        Line47 = input("47| ")
        Line48 = input("48| ")
        Line49 = input("49| ")
        Line50 = input("50| ")
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
        L11 = open(SaveInDir+"/"+ScriptName+"-line11.clb", "x")
        L11W = open(SaveInDir+"/"+ScriptName+"-line11.clb", "w")
        L11W.write(Line11)
        L12 = open(SaveInDir+"/"+ScriptName+"-line12.clb", "x")
        L12W = open(SaveInDir+"/"+ScriptName+"-line12.clb", "w")
        L12W.write(Line12)
        L13 = open(SaveInDir+"/"+ScriptName+"-line13.clb", "x")
        L13W = open(SaveInDir+"/"+ScriptName+"-line13.clb", "w")
        L13W.write(Line13)
        L14 = open(SaveInDir+"/"+ScriptName+"-line14.clb", "x")
        L14W = open(SaveInDir+"/"+ScriptName+"-line14.clb", "w")
        L14W.write(Line14)
        L15 = open(SaveInDir+"/"+ScriptName+"-line15.clb", "x")
        L15W = open(SaveInDir+"/"+ScriptName+"-line15.clb", "w")
        L15W.write(Line15)
        L16 = open(SaveInDir+"/"+ScriptName+"-line16.clb", "x")
        L16W = open(SaveInDir+"/"+ScriptName+"-line16.clb", "w")
        L16W.write(Line16)
        L17 = open(SaveInDir+"/"+ScriptName+"-line17.clb", "x")
        L17W = open(SaveInDir+"/"+ScriptName+"-line17.clb", "w")
        L17W.write(Line17)
        L18 = open(SaveInDir+"/"+ScriptName+"-line18.clb", "x")
        L18W = open(SaveInDir+"/"+ScriptName+"-line18.clb", "w")
        L18W.write(Line18)
        L19 = open(SaveInDir+"/"+ScriptName+"-line19.clb", "x")
        L19W = open(SaveInDir+"/"+ScriptName+"-line19.clb", "w")
        L19W.write(Line19)
        L20 = open(SaveInDir+"/"+ScriptName+"-line20.clb", "x")
        L20W = open(SaveInDir+"/"+ScriptName+"-line20.clb", "w")
        L20W.write(Line20)
        L21 = open(SaveInDir+"/"+ScriptName+"-line21.clb", "x")
        L21W = open(SaveInDir+"/"+ScriptName+"-line21.clb", "w")
        L21W.write(Line21)
        L22 = open(SaveInDir+"/"+ScriptName+"-line22.clb", "x")
        L22W = open(SaveInDir+"/"+ScriptName+"-line22.clb", "w")
        L22W.write(Line22)
        L23 = open(SaveInDir+"/"+ScriptName+"-line23.clb", "x")
        L23W = open(SaveInDir+"/"+ScriptName+"-line23.clb", "w")
        L23W.write(Line23)
        L24 = open(SaveInDir+"/"+ScriptName+"-line24.clb", "x")
        L24W = open(SaveInDir+"/"+ScriptName+"-line24.clb", "w")
        L24W.write(Line24)
        L25 = open(SaveInDir+"/"+ScriptName+"-line25.clb", "x")
        L25W = open(SaveInDir+"/"+ScriptName+"-line25.clb", "w")
        L25W.write(Line25)
        L26 = open(SaveInDir+"/"+ScriptName+"-line26.clb", "x")
        L26W = open(SaveInDir+"/"+ScriptName+"-line26.clb", "w")
        L26W.write(Line26)
        L27 = open(SaveInDir+"/"+ScriptName+"-line27.clb", "x")
        L27W = open(SaveInDir+"/"+ScriptName+"-line27.clb", "w")
        L27W.write(Line27)
        L28 = open(SaveInDir+"/"+ScriptName+"-line28.clb", "x")
        L28W = open(SaveInDir+"/"+ScriptName+"-line28.clb", "w")
        L28W.write(Line28)
        L29 = open(SaveInDir+"/"+ScriptName+"-line29.clb", "x")
        L29W = open(SaveInDir+"/"+ScriptName+"-line29.clb", "w")
        L29W.write(Line29)
        L30 = open(SaveInDir+"/"+ScriptName+"-line30.clb", "x")
        L30W = open(SaveInDir+"/"+ScriptName+"-line30.clb", "w")
        L30W.write(Line30)
        L31 = open(SaveInDir+"/"+ScriptName+"-line31.clb", "x")
        L31W = open(SaveInDir+"/"+ScriptName+"-line31.clb", "w")
        L31W.write(Line31)
        L32 = open(SaveInDir+"/"+ScriptName+"-line32.clb", "x")
        L32W = open(SaveInDir+"/"+ScriptName+"-line32.clb", "w")
        L32W.write(Line32)
        L33 = open(SaveInDir+"/"+ScriptName+"-line33.clb", "x")
        L33W = open(SaveInDir+"/"+ScriptName+"-line33.clb", "w")
        L33W.write(Line33)
        L34 = open(SaveInDir+"/"+ScriptName+"-line34.clb", "x")
        L34W = open(SaveInDir+"/"+ScriptName+"-line34.clb", "w")
        L34W.write(Line34)
        L35 = open(SaveInDir+"/"+ScriptName+"-line35.clb", "x")
        L35W = open(SaveInDir+"/"+ScriptName+"-line35.clb", "w")
        L35W.write(Line35)
        L36 = open(SaveInDir+"/"+ScriptName+"-line36.clb", "x")
        L36W = open(SaveInDir+"/"+ScriptName+"-line36.clb", "w")
        L36W.write(Line36)
        L37 = open(SaveInDir+"/"+ScriptName+"-line37.clb", "x")
        L37W = open(SaveInDir+"/"+ScriptName+"-line37.clb", "w")
        L37W.write(Line37)
        L38 = open(SaveInDir+"/"+ScriptName+"-line38.clb", "x")
        L38W = open(SaveInDir+"/"+ScriptName+"-line38.clb", "w")
        L38W.write(Line38)
        L39 = open(SaveInDir+"/"+ScriptName+"-line39.clb", "x")
        L39W = open(SaveInDir+"/"+ScriptName+"-line39.clb", "w")
        L39W.write(Line39)
        L40 = open(SaveInDir+"/"+ScriptName+"-line40.clb", "x")
        L40W = open(SaveInDir+"/"+ScriptName+"-line40.clb", "w")
        L40W.write(Line40)
        L41 = open(SaveInDir+"/"+ScriptName+"-line41.clb", "x")
        L41W = open(SaveInDir+"/"+ScriptName+"-line41.clb", "w")
        L41W.write(Line41)
        L42 = open(SaveInDir+"/"+ScriptName+"-line42.clb", "x")
        L42W = open(SaveInDir+"/"+ScriptName+"-line42.clb", "w")
        L42W.write(Line42)
        L43 = open(SaveInDir+"/"+ScriptName+"-line43.clb", "x")
        L43W = open(SaveInDir+"/"+ScriptName+"-line43.clb", "w")
        L43W.write(Line43)
        L44 = open(SaveInDir+"/"+ScriptName+"-line44.clb", "x")
        L44W = open(SaveInDir+"/"+ScriptName+"-line44.clb", "w")
        L44W.write(Line44)
        L45 = open(SaveInDir+"/"+ScriptName+"-line45.clb", "x")
        L45W = open(SaveInDir+"/"+ScriptName+"-line45.clb", "w")
        L45W.write(Line45)
        L46 = open(SaveInDir+"/"+ScriptName+"-line46.clb", "x")
        L46W = open(SaveInDir+"/"+ScriptName+"-line46.clb", "w")
        L46W.write(Line46)
        L47 = open(SaveInDir+"/"+ScriptName+"-line47.clb", "x")
        L47W = open(SaveInDir+"/"+ScriptName+"-line47.clb", "w")
        L47W.write(Line47)
        L48 = open(SaveInDir+"/"+ScriptName+"-line48.clb", "x")
        L48W = open(SaveInDir+"/"+ScriptName+"-line48.clb", "w")
        L48W.write(Line48)
        L49 = open(SaveInDir+"/"+ScriptName+"-line49.clb", "x")
        L49W = open(SaveInDir+"/"+ScriptName+"-line49.clb", "w")
        L49W.write(Line49)
        L50 = open(SaveInDir+"/"+ScriptName+"-line50.clb", "x")
        L50W = open(SaveInDir+"/"+ScriptName+"-line50.clb", "w")
        L50W.write(Line50)

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
        L11R = open(SaveInDir+"/"+ScriptName+"-line11.clb", "r")
        L11R = L11R.read()
        L12R = open(SaveInDir+"/"+ScriptName+"-line12.clb", "r")
        L12R = L12R.read()
        L13R = open(SaveInDir+"/"+ScriptName+"-line13.clb", "r")
        L13R = L13R.read()
        L14R = open(SaveInDir+"/"+ScriptName+"-line14.clb", "r")
        L14R = L14R.read()
        L15R = open(SaveInDir+"/"+ScriptName+"-line15.clb", "r")
        L15R = L15R.read()
        L16R = open(SaveInDir+"/"+ScriptName+"-line16.clb", "r")
        L16R = L16R.read()
        L17R = open(SaveInDir+"/"+ScriptName+"-line17.clb", "r")
        L17R = L17R.read()
        L18R = open(SaveInDir+"/"+ScriptName+"-line18.clb", "r")
        L18R = L18R.read()
        L19R = open(SaveInDir+"/"+ScriptName+"-line19.clb", "r")
        L19R = L19R.read()
        L20R = open(SaveInDir+"/"+ScriptName+"-line20.clb", "r")
        L20R = L20R.read()
        L21R = open(SaveInDir+"/"+ScriptName+"-line21.clb", "r")
        L21R = L21R.read()
        L22R = open(SaveInDir+"/"+ScriptName+"-line22.clb", "r")
        L22R = L22R.read()
        L23R = open(SaveInDir+"/"+ScriptName+"-line23.clb", "r")
        L23R = L23R.read()
        L24R = open(SaveInDir+"/"+ScriptName+"-line24.clb", "r")
        L24R = L24R.read()
        L25R = open(SaveInDir+"/"+ScriptName+"-line25.clb", "r")
        L25R = L25R.read()
        L26R = open(SaveInDir+"/"+ScriptName+"-line26.clb", "r")
        L26R = L26R.read()
        L27R = open(SaveInDir+"/"+ScriptName+"-line27.clb", "r")
        L27R = L27R.read()
        L28R = open(SaveInDir+"/"+ScriptName+"-line28.clb", "r")
        L28R = L28R.read()
        L29R = open(SaveInDir+"/"+ScriptName+"-line29.clb", "r")
        L29R = L29R.read()
        L30R = open(SaveInDir+"/"+ScriptName+"-line30.clb", "r")
        L30R = L30R.read()
        L31R = open(SaveInDir+"/"+ScriptName+"-line31.clb", "r")
        L31R = L31R.read()
        L32R = open(SaveInDir+"/"+ScriptName+"-line32.clb", "r")
        L32R = L32R.read()
        L33R = open(SaveInDir+"/"+ScriptName+"-line33.clb", "r")
        L33R = L33R.read()
        L34R = open(SaveInDir+"/"+ScriptName+"-line34.clb", "r")
        L34R = L34R.read()
        L35R = open(SaveInDir+"/"+ScriptName+"-line35.clb", "r")
        L35R = L35R.read()
        L36R = open(SaveInDir+"/"+ScriptName+"-line36.clb", "r")
        L36R = L36R.read()
        L37R = open(SaveInDir+"/"+ScriptName+"-line37.clb", "r")
        L37R = L37R.read()
        L38R = open(SaveInDir+"/"+ScriptName+"-line38.clb", "r")
        L38R = L38R.read()
        L39R = open(SaveInDir+"/"+ScriptName+"-line39.clb", "r")
        L39R = L39R.read()
        L40R = open(SaveInDir+"/"+ScriptName+"-line40.clb", "r")
        L40R = L40R.read()
        L41R = open(SaveInDir+"/"+ScriptName+"-line41.clb", "r")
        L41R = L41R.read()
        L42R = open(SaveInDir+"/"+ScriptName+"-line42.clb", "r")
        L42R = L42R.read()
        L43R = open(SaveInDir+"/"+ScriptName+"-line43.clb", "r")
        L43R = L43R.read()
        L44R = open(SaveInDir+"/"+ScriptName+"-line44.clb", "r")
        L44R = L44R.read()
        L45R = open(SaveInDir+"/"+ScriptName+"-line45.clb", "r")
        L45R = L45R.read()
        L46R = open(SaveInDir+"/"+ScriptName+"-line46.clb", "r")
        L46R = L46R.read()
        L47R = open(SaveInDir+"/"+ScriptName+"-line47.clb", "r")
        L47R = L47R.read()
        L48R = open(SaveInDir+"/"+ScriptName+"-line48.clb", "r")
        L48R = L48R.read()
        L49R = open(SaveInDir+"/"+ScriptName+"-line49.clb", "r")
        L49R = L49R.read()
        L50R = open(SaveInDir+"/"+ScriptName+"-line50.clb", "r")
        L50R = L50R.read()
        if L1R == "print":
            print(L2R)
        if L1R == "inp":
            a = input(L2R+" $"+" ")
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
            prinp = g
            equals_to_var = L9R
            ipi_then = L10R
            ipi_else = L11R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
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
        if L9R == "ipi":
            prinp = h
            equals_to_var = L10R
            ipi_then = L11R
            ipi_else = L12R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L9R == "svb":
            vn = L10R
            v = L11R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(v)
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
            print(L11R)
        if L10R == "inp":
            j = input(L11R+" $"+" ")
            print(j)
        if L10R == "svb":
            vn = L11R
            v = L12R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(v)
        if L10R == "rvb":
            vs = L11R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L10R == "ipi":
            prinp = i
            equals_to_var = L11R
            ipi_then = L12R
            ipi_else = L13R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L10R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L10R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L10R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L10R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L10R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L11R) + float(fv)
            print(inpsm)
        if L10R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L11R) - float(fv)
            print(inpsm)
        if L10R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L11R) * float(fv)
            print(inpsm)
        if L10R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L11R) / float(fv)
            print(inpsm)
        if L11R == "print":
            print(L12R)
        if L11R == "inp":
            k = input(L12R+" $"+" ")
            print(k)
        if L11R == "svb":
            vn = L12R
            v = L13R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(v)
        if L11R == "rvb":
            vs = L12R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L11R == "ipi":
            prinp = j
            equals_to_var = L12R
            ipi_then = L13R
            ipi_else = L14R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L11R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L11R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L11R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L11R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L11R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L12R) + float(fv)
            print(inpsm)
        if L11R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L12R) - float(fv)
            print(inpsm)
        if L11R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L12R) * float(fv)
            print(inpsm)
        if L11R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L12R) / float(fv)
            print(inpsm)
        if L12R == "print":
            print(L13R)
        if L12R == "inp":
            l = input(L13R+" $"+" ")
            print(l)
        if L12R == "svb":
            vn = L13R
            v = L14R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(v)
        if L12R == "rvb":
            vs = L13R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L12R == "ipi":
            prinp = k
            equals_to_var = L13R
            ipi_then = L14R
            ipi_else = L15R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L12R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L12R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L12R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L12R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L12R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L13R) + float(fv)
            print(inpsm)
        if L12R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L13R) - float(fv)
            print(inpsm)
        if L12R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L13R) * float(fv)
            print(inpsm)
        if L12R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L13R) / float(fv)
            print(inpsm)
        if L13R == "print":
            print(L14R)
        if L13R == "inp":
            m = input(L14R+" $"+" ")
            print(m)
        if L13R == "svb":
            vn = L14R
            v = L15R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(v)
        if L13R == "rvb":
            vs = L14R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L13R == "ipi":
            prinp = l
            equals_to_var = L14R
            ipi_then = L15R
            ipi_else = L16R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L13R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L13R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L13R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L13R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L13R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L13R) + float(fv)
            print(inpsm)
        if L13R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L13R) - float(fv)
            print(inpsm)
        if L13R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L13R) * float(fv)
            print(inpsm)
        if L13R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L13R) / float(fv)
            print(inpsm)
        if L14R == "print":
            print(L15R)
        if L14R == "inp":
            n = input(L15R+" $"+" ")
            print(n)
        if L14R == "svb":
            vn = L15R
            v = L16R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(v)
        if L14R == "rvb":
            vs = L15R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L14R == "ipi":
            prinp = m
            equals_to_var = L15R
            ipi_then = L16R
            ipi_else = L17R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L14R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L14R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L14R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L14R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L14R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L15R) + float(fv)
            print(inpsm)
        if L14R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L15R) - float(fv)
            print(inpsm)
        if L14R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L15R) * float(fv)
            print(inpsm)
        if L14R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L15R) / float(fv)
            print(inpsm)
        if L15R == "print":
            print(L16R)
        if L15R == "inp":
            o = input(L16R+" $"+" ")
            print(o)
        if L15R == "svb":
            vn = L16R
            v = L17R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(v)
        if L15R == "rvb":
            vs = L16R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L15R == "ipi":
            prinp = n
            equals_to_var = L16R
            ipi_then = L17R
            ipi_else = L18R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L15R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L15R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L15R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L15R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L15R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L16R) + float(fv)
            print(inpsm)
        if L15R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L16R) - float(fv)
            print(inpsm)
        if L15R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L16R) * float(fv)
            print(inpsm)
        if L15R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L16R) / float(fv)
            print(inpsm)
        if L16R == "print":
            print(L17R)
        if L16R == "inp":
            p = input(L17R+" $"+" ")
            print(p)
        if L16R == "svb":
            vn = L17R
            v = L18R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(v)
        if L16R == "rvb":
            vs = L17R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L16R == "ipi":
            prinp = o
            equals_to_var = L17R
            ipi_then = L18R
            ipi_else = L19R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L16R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L16R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L16R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L16R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L16R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L17R) + float(fv)
            print(inpsm)
        if L16R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L17R) - float(fv)
            print(inpsm)
        if L16R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L17R) * float(fv)
            print(inpsm)
        if L16R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L17R) / float(fv)
            print(inpsm)
        if L17R == "print":
            print(L18R)
        if L17R == "inp":
            q = input(L18R+" $"+" ")
            print(q)
        if L17R == "svb":
            vn = L18R
            v = L19R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(v)
        if L17R == "rvb":
            vs = L18R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L17R == "ipi":
            prinp = p
            equals_to_var = L18R
            ipi_then = L19R
            ipi_else = L20R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L17R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L17R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L17R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L17R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L17R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L18R) + float(fv)
            print(inpsm)
        if L17R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L18R) - float(fv)
            print(inpsm)
        if L17R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L18R) * float(fv)
            print(inpsm)
        if L17R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L18R) / float(fv)
            print(inpsm)
        if L18R == "print":
            print(L19R)
        if L18R == "inp":
            r = input(L19R+" $"+" ")
            print(r)
        if L18R == "svb":
            vn = L19R
            v = L20R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(v)
        if L18R == "rvb":
            vs = L19R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L18R == "ipi":
            prinp = q
            equals_to_var = L19R
            ipi_then = L20R
            ipi_else = L21R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L18R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L18R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L18R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L18R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L18R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L19R) + float(fv)
            print(inpsm)
        if L18R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L19R) - float(fv)
            print(inpsm)
        if L18R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L19R) * float(fv)
            print(inpsm)
        if L18R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L19R) / float(fv)
            print(inpsm)
        if L19R == "print":
            print(L20R)
        if L19R == "inp":
            s = input(L20R+" $"+" ")
            print(s)
        if L19R == "svb":
            vn = L20R
            v = L21R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(v)
        if L19R == "rvb":
            vs = L20R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L19R == "ipi":
            prinp = r
            equals_to_var = L20R
            ipi_then = L21R
            ipi_else = L22R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L19R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L19R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L19R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L19R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L19R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L20R) + float(fv)
            print(inpsm)
        if L19R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L20R) - float(fv)
            print(inpsm)
        if L19R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L20R) * float(fv)
            print(inpsm)
        if L19R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L20R) / float(fv)
            print(inpsm)
        if L20R == "print":
            print(L21R)
        if L20R == "inp":
            t = input(L21R+" $"+" ")
            print(t)
        if L20R == "svb":
            vn = L21R
            v = L22R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(v)
        if L20R == "rvb":
            vs = L21R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L20R == "ipi":
            prinp = s
            equals_to_var = L21R
            ipi_then = L22R
            ipi_else = L23R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L20R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L20R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L20R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L20R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L20R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L21R) + float(fv)
            print(inpsm)
        if L20R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L21R) - float(fv)
            print(inpsm)
        if L20R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L21R) * float(fv)
            print(inpsm)
        if L20R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L21R) / float(fv)
            print(inpsm)
        if L21R == "print":
            print(L22R)
        if L21R == "inp":
            u = input(L22R+" $"+" ")
            print(u)
        if L21R == "svb":
            vn = L22R
            v = L23R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(v)
        if L21R == "rvb":
            vs = L22R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L21R == "ipi":
            prinp = t
            equals_to_var = L22R
            ipi_then = L23R
            ipi_else = L24R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L21R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L21R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L21R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L21R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L21R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L22R) + float(fv)
            print(inpsm)
        if L21R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L22R) - float(fv)
            print(inpsm)
        if L21R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L22R) * float(fv)
            print(inpsm)
        if L21R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L22R) / float(fv)
            print(inpsm)
        if L22R == "print":
            print(L23R)
        if L22R == "inp":
            v = input(L23R+" $"+" ")
            print(v)
        if L22R == "svb":
            vn = L23R
            vbw = L24R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L22R == "rvb":
            vs = L23R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L22R == "ipi":
            prinp = u
            equals_to_var = L23R
            ipi_then = L24R
            ipi_else = L25R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L22R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L22R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L22R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L22R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L22R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L23R) + float(fv)
            print(inpsm)
        if L22R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L23R) - float(fv)
            print(inpsm)
        if L22R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L23R) * float(fv)
            print(inpsm)
        if L22R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L23R) / float(fv)
            print(inpsm)
        if L23R == "print":
            print(L24R)
        if L23R == "inp":
            w = input(L24R+" $"+" ")
            print(w)
        if L23R == "svb":
            vn = L24R
            vbw = L25R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L23R == "rvb":
            vs = L24R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L23R == "ipi":
            prinp = v
            equals_to_var = L24R
            ipi_then = L25R
            ipi_else = L26R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L23R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L23R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L23R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L23R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L23R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L24R) + float(fv)
            print(inpsm)
        if L23R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L24R) - float(fv)
            print(inpsm)
        if L23R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L24R) * float(fv)
            print(inpsm)
        if L23R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L24R) / float(fv)
            print(inpsm)
        if L24R == "print":
            print(L25R)
        if L24R == "inp":
            x = input(L25R+" $"+" ")
            print(x)
        if L24R == "svb":
            vn = L25R
            vbw = L26R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L24R == "rvb":
            vs = L25R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L24R == "ipi":
            prinp = w
            equals_to_var = L25R
            ipi_then = L26R
            ipi_else = L27R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L24R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L24R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L24R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L24R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L24R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L25R) + float(fv)
            print(inpsm)
        if L24R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L25R) - float(fv)
            print(inpsm)
        if L24R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L25R) * float(fv)
            print(inpsm)
        if L24R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L25R) / float(fv)
            print(inpsm)
        if L25R == "print":
            print(L26R)
        if L25R == "inp":
            y = input(L26R+" $"+" ")
            print(y)
        if L25R == "svb":
            vn = L26R
            vbw = L27R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L25R == "rvb":
            vs = L26R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L25R == "ipi":
            prinp = x
            equals_to_var = L26R
            ipi_then = L27R
            ipi_else = L28R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L25R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L25R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L25R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L25R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L25R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L26R) + float(fv)
            print(inpsm)
        if L25R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L26R) - float(fv)
            print(inpsm)
        if L25R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L26R) * float(fv)
            print(inpsm)
        if L25R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L26R) / float(fv)
            print(inpsm)
        if L26R == "print":
            print(L27R)
        if L26R == "inp":
            z = input(L27R+" $"+" ")
            print(z)
        if L26R == "svb":
            vn = L27R
            vbw = L28R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L26R == "rvb":
            vs = L27R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L26R == "ipi":
            prinp = y
            equals_to_var = L27R
            ipi_then = L28R
            ipi_else = L29R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L26R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L26R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L26R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L26R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L26R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L27R) + float(fv)
            print(inpsm)
        if L26R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L27R) - float(fv)
            print(inpsm)
        if L26R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L27R) * float(fv)
            print(inpsm)
        if L26R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L27R) / float(fv)
            print(inpsm)
        if L27R == "print":
            print(L28R)
        if L27R == "inp":
            aa = input(L28R+" $"+" ")
            print(aa)
        if L27R == "svb":
            vn = L28R
            vbw = L29R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L27R == "rvb":
            vs = L28R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L27R == "ipi":
            prinp = z
            equals_to_var = L28R
            ipi_then = L29R
            ipi_else = L30R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L27R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L27R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L27R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L27R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L27R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L28R) + float(fv)
            print(inpsm)
        if L27R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L28R) - float(fv)
            print(inpsm)
        if L27R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L28R) * float(fv)
            print(inpsm)
        if L27R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L28R) / float(fv)
            print(inpsm)
        if L28R == "print":
            print(L29R)
        if L28R == "inp":
            ab = input(L29R+" $"+" ")
            print(ab)
        if L28R == "svb":
            vn = L29R
            vbw = L30R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L28R == "rvb":
            vs = L29R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L28R == "ipi":
            prinp = aa
            equals_to_var = L29R
            ipi_then = L30R
            ipi_else = L31R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L28R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L28R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L28R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L28R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L28R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L29R) + float(fv)
            print(inpsm)
        if L28R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L29R) - float(fv)
            print(inpsm)
        if L28R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L29R) * float(fv)
            print(inpsm)
        if L28R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L29R) / float(fv)
            print(inpsm)
        if L29R == "print":
            print(L30R)
        if L29R == "inp":
            ab = input(L30R+" $"+" ")
            print(ab)
        if L29R == "svb":
            vn = L30R
            vbw = L31R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L29R == "rvb":
            vs = L30R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L29R == "ipi":
            prinp = aa
            equals_to_var = L30R
            ipi_then = L31R
            ipi_else = L32R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L29R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L29R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L29R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L29R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L29R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L30R) + float(fv)
            print(inpsm)
        if L29R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L30R) - float(fv)
            print(inpsm)
        if L29R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L30R) * float(fv)
            print(inpsm)
        if L29R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L30R) / float(fv)
            print(inpsm)
        if L30R == "print":
            print(L31R)
        if L30R == "inp":
            ac = input(L31R+" $"+" ")
            print(ac)
        if L30R == "svb":
            vn = L31R
            vbw = L32R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L30R == "rvb":
            vs = L31R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L30R == "ipi":
            prinp = ab
            equals_to_var = L31R
            ipi_then = L32R
            ipi_else = L33R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L30R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L30R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L30R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L30R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L30R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L31R) + float(fv)
            print(inpsm)
        if L30R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L31R) - float(fv)
            print(inpsm)
        if L30R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L31R) * float(fv)
            print(inpsm)
        if L30R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L31R) / float(fv)
            print(inpsm)
        if L31R == "print":
            print(L32R)
        if L31R == "inp":
            ac = input(L32R+" $"+" ")
            print(ac)
        if L31R == "svb":
            vn = L32R
            vbw = L33R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L31R == "rvb":
            vs = L32R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L31R == "ipi":
            prinp = ab
            equals_to_var = L32R
            ipi_then = L33R
            ipi_else = L34R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L31R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L31R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L31R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L31R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L31R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L32R) + float(fv)
            print(inpsm)
        if L31R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L32R) - float(fv)
            print(inpsm)
        if L31R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L32R) * float(fv)
            print(inpsm)
        if L31R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L32R) / float(fv)
            print(inpsm)
        if L32R == "print":
            print(L33R)
        if L32R == "inp":
            ad = input(L33R+" $"+" ")
            print(ad)
        if L32R == "svb":
            vn = L33R
            vbw = L34R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L32R == "rvb":
            vs = L33R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L32R == "ipi":
            prinp = ac
            equals_to_var = L33R
            ipi_then = L34R
            ipi_else = L35R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L32R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L32R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L32R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L32R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L32R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L33R) + float(fv)
            print(inpsm)
        if L32R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L33R) - float(fv)
            print(inpsm)
        if L32R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L33R) * float(fv)
            print(inpsm)
        if L32R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L33R) / float(fv)
            print(inpsm)
        if L33R == "print":
            print(L34R)
        if L33R == "inp":
            ae = input(L34R+" $"+" ")
            print(ae)
        if L33R == "svb":
            vn = L34R
            vbw = L35R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L33R == "rvb":
            vs = L34R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L33R == "ipi":
            prinp = ad
            equals_to_var = L34R
            ipi_then = L35R
            ipi_else = L36R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L33R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L33R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L33R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L33R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L33R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L34R) + float(fv)
            print(inpsm)
        if L33R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L34R) - float(fv)
            print(inpsm)
        if L33R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L34R) * float(fv)
            print(inpsm)
        if L33R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L34R) / float(fv)
            print(inpsm)
        if L34R == "print":
            print(L35R)
        if L34R == "inp":
            af = input(L35R+" $"+" ")
            print(af)
        if L34R == "svb":
            vn = L35R
            vbw = L36R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L34R == "rvb":
            vs = L35R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L34R == "ipi":
            prinp = ae
            equals_to_var = L35R
            ipi_then = L36R
            ipi_else = L37R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L34R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L34R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L34R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L34R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L34R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L35R) + float(fv)
            print(inpsm)
        if L34R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L35R) - float(fv)
            print(inpsm)
        if L34R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L35R) * float(fv)
            print(inpsm)
        if L34R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L35R) / float(fv)
            print(inpsm)
        if L35R == "print":
            print(L36R)
        if L35R == "inp":
            ag = input(L36R+" $"+" ")
            print(ag)
        if L35R == "svb":
            vn = L36R
            vbw = L37R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L35R == "rvb":
            vs = L36R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L35R == "ipi":
            prinp = af
            equals_to_var = L36R
            ipi_then = L37R
            ipi_else = L38R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L35R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L35R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L35R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L35R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L35R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L36R) + float(fv)
            print(inpsm)
        if L35R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L36R) - float(fv)
            print(inpsm)
        if L35R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L36R) * float(fv)
            print(inpsm)
        if L35R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L36R) / float(fv)
            print(inpsm)
        if L36R == "print":
            print(L37R)
        if L36R == "inp":
            ah = input(L37R+" $"+" ")
            print(ah)
        if L36R == "svb":
            vn = L37R
            vbw = L38R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L36R == "rvb":
            vs = L37R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L36R == "ipi":
            prinp = ag
            equals_to_var = L37R
            ipi_then = L38R
            ipi_else = L39R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L36R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L36R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L36R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L36R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L36R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L37R) + float(fv)
            print(inpsm)
        if L36R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L37R) - float(fv)
            print(inpsm)
        if L36R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L37R) * float(fv)
            print(inpsm)
        if L36R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L37R) / float(fv)
            print(inpsm)
        if L37R == "print":
            print(L38R)
        if L37R == "inp":
            ai = input(L38R+" $"+" ")
            print(ai)
        if L37R == "svb":
            vn = L38R
            vbw = L39R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L37R == "rvb":            
            vs = L38R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L37R == "ipi":
            prinp = ah
            equals_to_var = L38R
            ipi_then = L39R
            ipi_else = L40R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L37R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L37R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L37R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L37R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L37R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L38R) + float(fv)
            print(inpsm)
        if L37R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L38R) - float(fv)
            print(inpsm)
        if L37R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L38R) * float(fv)
            print(inpsm)
        if L37R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L38R) / float(fv)
            print(inpsm)
        if L38R == "print":
            print(L39R)
        if L38R == "inp":
            aj = input(L39R+" $"+" ")
            print(aj)
        if L38R == "svb":
            vn = L39R
            vbw = L40R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L38R == "rvb":
            vs = L39R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L38R == "ipi":
            prinp = ai
            equals_to_var = L39R
            ipi_then = L40R
            ipi_else = L41R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L38R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L38R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L38R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L38R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L38R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L39R) + float(fv)
            print(inpsm)
        if L38R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L39R) - float(fv)
            print(inpsm)
        if L38R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L39R) * float(fv)
            print(inpsm)
        if L38R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L39R) / float(fv)
            print(inpsm)
        if L39R == "print":
            print(L40R)
        if L39R == "inp":
            ak = input(L40R+" $"+" ")
            print(ak)
        if L39R == "svb":
            vn = L40R
            vbw = L41R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L39R == "rvb":
            vs = L40R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L39R == "ipi":
            prinp = aj
            equals_to_var = L40R
            ipi_then = L41R
            ipi_else = L42R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L39R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L39R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L39R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L39R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L39R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L40R) + float(fv)
            print(inpsm)
        if L39R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L40R) - float(fv)
            print(inpsm)
        if L39R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L40R) * float(fv)
            print(inpsm)
        if L39R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L40R) / float(fv)
            print(inpsm)
        if L40R == "print":
            print(L41R)
        if L40R == "inp":
            al = input(L41R+" $"+" ")
            print(al)
        if L40R == "svb":
            vn = L41R
            vbw = L42R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L40R == "rvb":
            vs = L41R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L40R == "ipi":
            prinp = ak
            equals_to_var = L41R
            ipi_then = L42R
            ipi_else = L43R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L40R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L40R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L40R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L40R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L40R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L41R) + float(fv)
            print(inpsm)
        if L40R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L41R) - float(fv)
            print(inpsm)
        if L40R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L41R) * float(fv)
            print(inpsm)
        if L40R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L41R) / float(fv)
            print(inpsm)
        if L41R == "print":
            print(L42R)
        if L41R == "inp":
            am = input(L42R+" $"+" ")
            print(am)
        if L41R == "svb":
            vn = L42R
            vbw = L43R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L41R == "rvb":
            vs = L42R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L41R == "ipi":
            prinp = al
            equals_to_var = L42R
            ipi_then = L43R
            ipi_else = L44R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L41R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L41R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L41R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L41R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L41R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L42R) + float(fv)
            print(inpsm)
        if L41R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L42R) - float(fv)
            print(inpsm)
        if L41R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L42R) * float(fv)
            print(inpsm)
        if L41R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L42R) / float(fv)
            print(inpsm)
        if L42R == "print":
            print(L43R)
        if L42R == "inp":
            an = input(L43R+" $"+" ")
            print(an)
        if L42R == "svb":
            vn = L43R
            vbw = L44R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L42R == "rvb":
            vs = L43R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L42R == "ipi":
            prinp = am
            equals_to_var = L43R
            ipi_then = L44R
            ipi_else = L45R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L42R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L42R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L42R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L42R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L42R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L43R) + float(fv)
            print(inpsm)
        if L42R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L43R) - float(fv)
            print(inpsm)
        if L42R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L43R) * float(fv)
            print(inpsm)
        if L42R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L43R) / float(fv)
            print(inpsm)
        if L43R == "print":
            print(L44R)
        if L43R == "inp":
            an = input(L44R+" $"+" ")
            print(an)
        if L43R == "svb":
            vn = L44R
            vbw = L45R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L43R == "rvb":
            vs = L44R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L43R == "ipi":
            prinp = am
            equals_to_var = L44R
            ipi_then = L45R
            ipi_else = L46R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L43R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L43R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L43R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L43R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L43R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L44R) + float(fv)
            print(inpsm)
        if L43R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L44R) - float(fv)
            print(inpsm)
        if L43R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L44R) * float(fv)
            print(inpsm)
        if L43R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L44R) / float(fv)
            print(inpsm)
        if L44R == "print":
            print(L45R)
        if L44R == "inp":
            ao = input(L45R+" $"+" ")
            print(ao)
        if L44R == "svb":
            vn = L45R
            vbw = L46R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L44R == "rvb":
            vs = L45R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L44R == "ipi":
            prinp = an
            equals_to_var = L45R
            ipi_then = L46R
            ipi_else = L47R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L44R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L44R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L44R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L44R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L44R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L45R) + float(fv)
            print(inpsm)
        if L44R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L45R) - float(fv)
            print(inpsm)
        if L44R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L45R) * float(fv)
            print(inpsm)
        if L44R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L45R) / float(fv)
            print(inpsm)
        if L45R == "print":
            print(L46R)
        if L45R == "inp":
            ap = input(L46R+" $"+" ")
            print(ap)
        if L45R == "svb":
            vn = L46R
            vbw = L47R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L45R == "rvb":
            vs = L46R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L45R == "ipi":
            prinp = ao
            equals_to_var = L46R
            ipi_then = L47R
            ipi_else = L48R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L45R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L45R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L45R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L45R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L45R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L46R) + float(fv)
            print(inpsm)
        if L45R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L46R) - float(fv)
            print(inpsm)
        if L45R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L46R) * float(fv)
            print(inpsm)
        if L45R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L46R) / float(fv)
            print(inpsm)
        if L46R == "print":
            print(L47R)
        if L46R == "inp":
            aq = input(L47R+" $"+" ")
            print(aq)
        if L46R == "svb":
            vn = L47R
            vbw = L48R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L46R == "rvb":
            vs = L47R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L46R == "ipi":
            prinp = ap
            equals_to_var = L47R
            ipi_then = L48R
            ipi_else = L49R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L46R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L46R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L46R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L46R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L46R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L47R) + float(fv)
            print(inpsm)
        if L46R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L47R) - float(fv)
            print(inpsm)
        if L46R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L47R) * float(fv)
            print(inpsm)
        if L46R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L47R) / float(fv)
            print(inpsm)
        if L47R == "print":
            print(L48R)
        if L47R == "inp":
            ar = input(L48R+" $"+" ")
            print(ar)
        if L47R == "svb":
            vn = L48R
            vbw = L49R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L47R == "rvb":
            vs = L48R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L47R == "ipi":
            prinp = aq
            equals_to_var = L48R
            ipi_then = L49R
            ipi_else = L50R
            if prinp == equals_to_var:
                print(ipi_then)
            if prinp != equals_to_var:
                print(ipi_else)
        if L47R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L47R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L47R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L47R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L47R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L48R) + float(fv)
            print(inpsm)
        if L47R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L48R) - float(fv)
            print(inpsm)
        if L47R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L48R) * float(fv)
            print(inpsm)
        if L47R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L48R) / float(fv)
            print(inpsm)
        if L48R == "print":
            print(L49R)
        if L48R == "inp":
            asa = input(L49R+" $"+" ")
            print(asa)
        if L48R == "svb":
            vn = L49R
            vbw = L50R
            svb = open(vn+".var", "x")
            svb = open(vn+".var", "w")
            svb.write(vbw)
        if L48R == "rvb":
            vs = L49R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L48R == "ipi":
            print("ERROR: No Space Left.")
        if L48R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L48R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L48R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L48R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L48R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L49R) + float(fv)
            print(inpsm)
        if L48R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L49R) - float(fv)
            print(inpsm)
        if L48R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L49R) * float(fv)
            print(inpsm)
        if L48R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L49R) / float(fv)
            print(inpsm)
        if L49R == "print":
            print(L50R)
        if L49R == "inp":
            at = input(L50R+" $"+" ")
            print(at)
        if L49R == "svb":
            print("ERROR: No Space Left.")
        if L49R == "rvb":
            vs = L50R
            vr = open(vs+".var", "r")
            print(vr.read())
        if L49R == "ipi":
            print("ERROR: No Space Left.")
        if L49R == "minpp":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) + float(sv)
            print(inpsm)
        if L49R == "minpm":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) - float(sv)
            print(inpsm)
        if L49R == "minpmu":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) * float(sv)
            print(inpsm)
        if L49R == "minpd":
            fv = input("First $ ")
            sv = input("Second $ ")
            inpsm = float(fv) / float(sv)
            print(inpsm)
        if L49R == "sminpp":
            fv = input("First $ ")
            inpsm = float(L50R) + float(fv)
            print(inpsm)
        if L49R == "sminpm":
            fv = input("First $ ")
            inpsm = float(L50R) - float(fv)
            print(inpsm)
        if L49R == "sminpmu":
            fv = input("First $ ")
            inpsm = float(L50R) * float(fv)
            print(inpsm)
        if L49R == "sminpd":
            fv = input("First $ ")
            inpsm = float(L50R) / float(fv)
            print(inpsm)
        if L50R == "print":
            print("ERROR: No Space Left.")
        if L50R == "inp":
            print("ERROR: No Space Left.")
        if L50R == "svb":
            print("ERROR: No Space Left.")
        if L50R == "rvb":
            print("ERROR: No Space Left.")
        if L50R == "ipi":
	        print("ERROR: No Space Left.")
        if L50R == "minpp":
            print("ERROR: No Space Left.")
        if L50R == "minpm":
            print("ERROR: No Space Left.")
        if L50R == "minpmu":
            print("ERROR: No Space Left.")
        if L50R == "minpd":
            print("ERROR: No Space Left.")
        if L50R == "sminpp":
            print("ERROR: No Space Left.")
        if L50R == "sminpm":
            print("ERROR: No Space Left.")
        if L50R == "sminpmu":
            print("ERROR: No Space Left.")
        if L50R == "sminpd":
            print("ERROR: No Space Left.")
    if cmnd == "py":
        print("=====================================================================================")
        print("Welcome To Python Compiler 3.12.")
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
        Line11 = input("11| ")
        Line12 = input("12| ")
        Line13 = input("13| ")
        Line14 = input("14| ")
        Line15 = input("15| ")
        Line16 = input("16| ")
        Line17 = input("17| ")
        Line18 = input("18| ")
        Line19 = input("19| ")
        Line20 = input("20| ")
        Line21 = input("21| ")
        Line22 = input("22| ")
        Line23 = input("23| ")
        Line24 = input("24| ")
        Line25 = input("25| ")
        Line26 = input("26| ")
        Line27 = input("27| ")
        Line28 = input("28| ")
        Line29 = input("29| ")
        Line30 = input("30| ")
        Line31 = input("31| ")
        Line32 = input("32| ")
        Line33 = input("33| ")
        Line34 = input("34| ")
        Line35 = input("35| ")
        Line36 = input("36| ")
        Line37 = input("37| ")
        Line38 = input("38| ")
        Line39 = input("39| ")
        Line40 = input("40| ")
        Line41 = input("41| ")
        Line42 = input("42| ")
        Line43 = input("43| ")
        Line44 = input("44| ")
        Line45 = input("45| ")
        Line46 = input("46| ")
        Line47 = input("47| ")
        Line48 = input("48| ")
        Line49 = input("49| ")
        Line50 = input("50| ")
        ScriptName = input("Script Name $ ")
        SaveInDir = input("Directory $ ")
        L1 = open(SaveInDir+"/"+ScriptName+"-line1.py", "x")
        L1W = open(SaveInDir+"/"+ScriptName+"-line1.py", "w")
        L1W.write(Line1)
        L2 = open(SaveInDir+"/"+ScriptName+"-line2.py", "x")
        L2W = open(SaveInDir+"/"+ScriptName+"-line2.py", "w")
        L2W.write(Line2)
        L3 = open(SaveInDir+"/"+ScriptName+"-line3.py", "x")
        L3W = open(SaveInDir+"/"+ScriptName+"-line3.py", "w")
        L3W.write(Line3)
        L4 = open(SaveInDir+"/"+ScriptName+"-line4.py", "x")
        L4W = open(SaveInDir+"/"+ScriptName+"-line4.py", "w")
        L4W.write(Line4)
        L5 = open(SaveInDir+"/"+ScriptName+"-line5.py", "x")
        L5W = open(SaveInDir+"/"+ScriptName+"-line5.py", "w")
        L5W.write(Line5)
        L6 = open(SaveInDir+"/"+ScriptName+"-line6.py", "x")
        L6W = open(SaveInDir+"/"+ScriptName+"-line6.py", "w")
        L6W.write(Line6)
        L7 = open(SaveInDir+"/"+ScriptName+"-line7.py", "x")
        L7W = open(SaveInDir+"/"+ScriptName+"-line7.py", "w")
        L7W.write(Line7)
        L8 = open(SaveInDir+"/"+ScriptName+"-line8.py", "x")
        L8W = open(SaveInDir+"/"+ScriptName+"-line8.py", "w")
        L8W.write(Line8)
        L9 = open(SaveInDir+"/"+ScriptName+"-line9.py", "x")
        L9W = open(SaveInDir+"/"+ScriptName+"-line9.py", "w")
        L9W.write(Line9)
        L10 = open(SaveInDir+"/"+ScriptName+"-line10.py", "x")
        L10W = open(SaveInDir+"/"+ScriptName+"-line10.py", "w")
        L10W.write(Line10)
        L11 = open(SaveInDir+"/"+ScriptName+"-line11.py", "x")
        L11W = open(SaveInDir+"/"+ScriptName+"-line11.py", "w")
        L11W.write(Line11)
        L12 = open(SaveInDir+"/"+ScriptName+"-line12.py", "x")
        L12W = open(SaveInDir+"/"+ScriptName+"-line12.py", "w")
        L12W.write(Line12)
        L13 = open(SaveInDir+"/"+ScriptName+"-line13.py", "x")
        L13W = open(SaveInDir+"/"+ScriptName+"-line13.py", "w")
        L13W.write(Line13)
        L14 = open(SaveInDir+"/"+ScriptName+"-line14.py", "x")
        L14W = open(SaveInDir+"/"+ScriptName+"-line14.py", "w")
        L14W.write(Line14)
        L15 = open(SaveInDir+"/"+ScriptName+"-line15.py", "x")
        L15W = open(SaveInDir+"/"+ScriptName+"-line15.py", "w")
        L15W.write(Line15)
        L16 = open(SaveInDir+"/"+ScriptName+"-line16.py", "x")
        L16W = open(SaveInDir+"/"+ScriptName+"-line16.py", "w")
        L16W.write(Line16)
        L17 = open(SaveInDir+"/"+ScriptName+"-line17.py", "x")
        L17W = open(SaveInDir+"/"+ScriptName+"-line17.py", "w")
        L17W.write(Line17)
        L18 = open(SaveInDir+"/"+ScriptName+"-line18.py", "x")
        L18W = open(SaveInDir+"/"+ScriptName+"-line18.py", "w")
        L18W.write(Line18)
        L19 = open(SaveInDir+"/"+ScriptName+"-line19.py", "x")
        L19W = open(SaveInDir+"/"+ScriptName+"-line19.py", "w")
        L19W.write(Line19)
        L20 = open(SaveInDir+"/"+ScriptName+"-line20.py", "x")
        L20W = open(SaveInDir+"/"+ScriptName+"-line20.py", "w")
        L20W.write(Line20)
        L21 = open(SaveInDir+"/"+ScriptName+"-line21.py", "x")
        L21W = open(SaveInDir+"/"+ScriptName+"-line21.py", "w")
        L21W.write(Line21)
        L22 = open(SaveInDir+"/"+ScriptName+"-line22.py", "x")
        L22W = open(SaveInDir+"/"+ScriptName+"-line22.py", "w")
        L22W.write(Line22)
        L23 = open(SaveInDir+"/"+ScriptName+"-line23.py", "x")
        L23W = open(SaveInDir+"/"+ScriptName+"-line23.py", "w")
        L23W.write(Line23)
        L24 = open(SaveInDir+"/"+ScriptName+"-line24.py", "x")
        L24W = open(SaveInDir+"/"+ScriptName+"-line24.py", "w")
        L24W.write(Line24)
        L25 = open(SaveInDir+"/"+ScriptName+"-line25.py", "x")
        L25W = open(SaveInDir+"/"+ScriptName+"-line25.py", "w")
        L25W.write(Line25)
        L26 = open(SaveInDir+"/"+ScriptName+"-line26.py", "x")
        L26W = open(SaveInDir+"/"+ScriptName+"-line26.py", "w")
        L26W.write(Line26)
        L27 = open(SaveInDir+"/"+ScriptName+"-line27.py", "x")
        L27W = open(SaveInDir+"/"+ScriptName+"-line27.py", "w")
        L27W.write(Line27)
        L28 = open(SaveInDir+"/"+ScriptName+"-line28.py", "x")
        L28W = open(SaveInDir+"/"+ScriptName+"-line28.py", "w")
        L28W.write(Line28)
        L29 = open(SaveInDir+"/"+ScriptName+"-line29.py", "x")
        L29W = open(SaveInDir+"/"+ScriptName+"-line29.py", "w")
        L29W.write(Line29)
        L30 = open(SaveInDir+"/"+ScriptName+"-line30.py", "x")
        L30W = open(SaveInDir+"/"+ScriptName+"-line30.py", "w")
        L30W.write(Line30)
        L31 = open(SaveInDir+"/"+ScriptName+"-line31.py", "x")
        L31W = open(SaveInDir+"/"+ScriptName+"-line31.py", "w")
        L31W.write(Line31)
        L32 = open(SaveInDir+"/"+ScriptName+"-line32.py", "x")
        L32W = open(SaveInDir+"/"+ScriptName+"-line32.py", "w")
        L32W.write(Line32)
        L33 = open(SaveInDir+"/"+ScriptName+"-line33.py", "x")
        L33W = open(SaveInDir+"/"+ScriptName+"-line33.py", "w")
        L33W.write(Line33)
        L34 = open(SaveInDir+"/"+ScriptName+"-line34.py", "x")
        L34W = open(SaveInDir+"/"+ScriptName+"-line34.py", "w")
        L34W.write(Line34)
        L35 = open(SaveInDir+"/"+ScriptName+"-line35.py", "x")
        L35W = open(SaveInDir+"/"+ScriptName+"-line35.py", "w")
        L35W.write(Line35)
        L36 = open(SaveInDir+"/"+ScriptName+"-line36.py", "x")
        L36W = open(SaveInDir+"/"+ScriptName+"-line36.py", "w")
        L36W.write(Line36)
        L37 = open(SaveInDir+"/"+ScriptName+"-line37.py", "x")
        L37W = open(SaveInDir+"/"+ScriptName+"-line37.py", "w")
        L37W.write(Line37)
        L38 = open(SaveInDir+"/"+ScriptName+"-line38.py", "x")
        L38W = open(SaveInDir+"/"+ScriptName+"-line38.py", "w")
        L38W.write(Line38)
        L39 = open(SaveInDir+"/"+ScriptName+"-line39.py", "x")
        L39W = open(SaveInDir+"/"+ScriptName+"-line39.py", "w")
        L39W.write(Line39)
        L40 = open(SaveInDir+"/"+ScriptName+"-line40.py", "x")
        L40W = open(SaveInDir+"/"+ScriptName+"-line40.py", "w")
        L40W.write(Line40)
        L41 = open(SaveInDir+"/"+ScriptName+"-line41.py", "x")
        L41W = open(SaveInDir+"/"+ScriptName+"-line41.py", "w")
        L41W.write(Line41)
        L42 = open(SaveInDir+"/"+ScriptName+"-line42.py", "x")
        L42W = open(SaveInDir+"/"+ScriptName+"-line42.py", "w")
        L42W.write(Line42)
        L43 = open(SaveInDir+"/"+ScriptName+"-line43.py", "x")
        L43W = open(SaveInDir+"/"+ScriptName+"-line43.py", "w")
        L43W.write(Line43)
        L44 = open(SaveInDir+"/"+ScriptName+"-line44.py", "x")
        L44W = open(SaveInDir+"/"+ScriptName+"-line44.py", "w")
        L44W.write(Line44)
        L45 = open(SaveInDir+"/"+ScriptName+"-line45.py", "x")
        L45W = open(SaveInDir+"/"+ScriptName+"-line45.py", "w")
        L45W.write(Line45)
        L46 = open(SaveInDir+"/"+ScriptName+"-line46.py", "x")
        L46W = open(SaveInDir+"/"+ScriptName+"-line46.py", "w")
        L46W.write(Line46)
        L47 = open(SaveInDir+"/"+ScriptName+"-line47.py", "x")
        L47W = open(SaveInDir+"/"+ScriptName+"-line47.py", "w")
        L47W.write(Line47)
        L48 = open(SaveInDir+"/"+ScriptName+"-line48.py", "x")
        L48W = open(SaveInDir+"/"+ScriptName+"-line48.py", "w")
        L48W.write(Line48)
        L49 = open(SaveInDir+"/"+ScriptName+"-line49.py", "x")
        L49W = open(SaveInDir+"/"+ScriptName+"-line49.py", "w")
        L49W.write(Line49)
        L50 = open(SaveInDir+"/"+ScriptName+"-line50.py", "x")
        L50W = open(SaveInDir+"/"+ScriptName+"-line50.py", "w")
        L50W.write(Line50)
    if cmnd == "pyrun":
        ScriptName = input("Script Name $ ")
        SaveInDir = input("Directory $ ")
        L1R = open(SaveInDir+"/"+ScriptName+"-line1.py", "r")
        L1R = L1R.read()
        L2R = open(SaveInDir+"/"+ScriptName+"-line2.py", "r")
        L2R = L2R.read()
        L3R = open(SaveInDir+"/"+ScriptName+"-line3.py", "r")
        L3R = L3R.read()
        L4R = open(SaveInDir+"/"+ScriptName+"-line4.py", "r")
        L4R = L4R.read()
        L5R = open(SaveInDir+"/"+ScriptName+"-line5.py", "r")
        L5R = L5R.read()
        L6R = open(SaveInDir+"/"+ScriptName+"-line6.py", "r")
        L6R = L6R.read()
        L7R = open(SaveInDir+"/"+ScriptName+"-line7.py", "r")
        L7R = L7R.read()
        L8R = open(SaveInDir+"/"+ScriptName+"-line8.py", "r")
        L8R = L8R.read()
        L9R = open(SaveInDir+"/"+ScriptName+"-line9.py", "r")
        L9R = L9R.read()
        L10R = open(SaveInDir+"/"+ScriptName+"-line10.py", "r")
        L10R = L10R.read()
        L11R = open(SaveInDir+"/"+ScriptName+"-line11.py", "r")
        L11R = L11R.read()
        L12R = open(SaveInDir+"/"+ScriptName+"-line12.py", "r")
        L12R = L12R.read()
        L13R = open(SaveInDir+"/"+ScriptName+"-line13.py", "r")
        L13R = L13R.read()
        L14R = open(SaveInDir+"/"+ScriptName+"-line14.py", "r")
        L14R = L14R.read()
        L15R = open(SaveInDir+"/"+ScriptName+"-line15.py", "r")
        L15R = L15R.read()
        L16R = open(SaveInDir+"/"+ScriptName+"-line16.py", "r")
        L16R = L16R.read()
        L17R = open(SaveInDir+"/"+ScriptName+"-line17.py", "r")
        L17R = L17R.read()
        L18R = open(SaveInDir+"/"+ScriptName+"-line18.py", "r")
        L18R = L18R.read()
        L19R = open(SaveInDir+"/"+ScriptName+"-line19.py", "r")
        L19R = L19R.read()
        L20R = open(SaveInDir+"/"+ScriptName+"-line20.py", "r")
        L20R = L20R.read()
        L21R = open(SaveInDir+"/"+ScriptName+"-line21.py", "r")
        L21R = L21R.read()
        L22R = open(SaveInDir+"/"+ScriptName+"-line22.py", "r")
        L22R = L22R.read()
        L23R = open(SaveInDir+"/"+ScriptName+"-line23.py", "r")
        L23R = L23R.read()
        L24R = open(SaveInDir+"/"+ScriptName+"-line24.py", "r")
        L24R = L24R.read()
        L25R = open(SaveInDir+"/"+ScriptName+"-line25.py", "r")
        L25R = L25R.read()
        L26R = open(SaveInDir+"/"+ScriptName+"-line26.py", "r")
        L26R = L26R.read()
        L27R = open(SaveInDir+"/"+ScriptName+"-line27.py", "r")
        L27R = L27R.read()
        L28R = open(SaveInDir+"/"+ScriptName+"-line28.py", "r")
        L28R = L28R.read()
        L29R = open(SaveInDir+"/"+ScriptName+"-line29.py", "r")
        L29R = L29R.read()
        L30R = open(SaveInDir+"/"+ScriptName+"-line30.py", "r")
        L30R = L30R.read()
        L31R = open(SaveInDir+"/"+ScriptName+"-line31.py", "r")
        L31R = L31R.read()
        L32R = open(SaveInDir+"/"+ScriptName+"-line32.py", "r")
        L32R = L32R.read()
        L33R = open(SaveInDir+"/"+ScriptName+"-line33.py", "r")
        L33R = L33R.read()
        L34R = open(SaveInDir+"/"+ScriptName+"-line34.py", "r")
        L34R = L34R.read()
        L35R = open(SaveInDir+"/"+ScriptName+"-line35.py", "r")
        L35R = L35R.read()
        L36R = open(SaveInDir+"/"+ScriptName+"-line36.py", "r")
        L36R = L36R.read()
        L37R = open(SaveInDir+"/"+ScriptName+"-line37.py", "r")
        L37R = L37R.read()
        L38R = open(SaveInDir+"/"+ScriptName+"-line38.py", "r")
        L38R = L38R.read()
        L39R = open(SaveInDir+"/"+ScriptName+"-line39.py", "r")
        L39R = L39R.read()
        L40R = open(SaveInDir+"/"+ScriptName+"-line40.py", "r")
        L40R = L40R.read()
        L41R = open(SaveInDir+"/"+ScriptName+"-line41.py", "r")
        L41R = L41R.read()
        L42R = open(SaveInDir+"/"+ScriptName+"-line42.py", "r")
        L42R = L42R.read()
        L43R = open(SaveInDir+"/"+ScriptName+"-line43.py", "r")
        L43R = L43R.read()
        L44R = open(SaveInDir+"/"+ScriptName+"-line44.py", "r")
        L44R = L44R.read()
        L45R = open(SaveInDir+"/"+ScriptName+"-line45.py", "r")
        L45R = L45R.read()
        L46R = open(SaveInDir+"/"+ScriptName+"-line46.py", "r")
        L46R = L46R.read()
        L47R = open(SaveInDir+"/"+ScriptName+"-line47.py", "r")
        L47R = L47R.read()
        L48R = open(SaveInDir+"/"+ScriptName+"-line48.py", "r")
        L48R = L48R.read()
        L49R = open(SaveInDir+"/"+ScriptName+"-line49.py", "r")
        L49R = L49R.read()
        L50R = open(SaveInDir+"/"+ScriptName+"-line50.py", "r")
        L50R = L50R.read()
        exec(f"{L1R}\n{L2R}\n{L3R}\n{L4R}\n{L5R}\n{L6R}\n{L7R}\n{L8R}\n{L9R}\n{L10R}\n{L11R}\n{L12R}\n{L13R}\n{L14R}\n{L15R}\n{L16R}\n{L17R}\n{L18R}\n{L19R}\n{L20R}\n{L21R}\n{L22R}\n{L23R}\n{L24R}\n{L25R}\n{L26R}\n{L27R}\n{L28R}\n{L29R}\n{L30R}\n{L31R}\n{L32R}\n{L33R}\n{L34R}\n{L35R}\n{L36R}\n{L37R}\n{L38R}\n{L39R}\n{L40R}\n{L41R}\n{L42R}\n{L43R}\n{L44R}\n{L45R}\n{L46R}\n{L47R}\n{L48R}\n{L49R}\n{L50R}")
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
