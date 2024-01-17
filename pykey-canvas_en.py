# Author: Filippvas™ (Philip Vasilakis) 2024
# Project Name: PyKey Canvas (CN n S)

import os
import time
import string
from datetime import date

today = date.today()
d = today.strftime("%Y-%m-%d")

cs = list(string.ascii_uppercase)
ns = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
ss = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "'", '"', ",", ".", "<", ">", "[", "]", "{", "}", "`", "~", ":",
      ";", "|", "-", "_", "=", "+"]
clist = clist = [" " for _ in range(100)]
running = True
cp = "|Cursor: I.Up K.Down J.Left L.Right | S.Show E.Enter|"
pp = 1
cv = 0
t = "U"
px = 1
py = 1
pn = "1"
e = " "
c1 = " "
c2 = " "
c3 = " "
c4 = " "
c5 = " "
c6 = " "
ts = "  "
frs = "  "
c11 = " "
c12 = " "
c13 = " "
c14 = " "
c15 = " "
c21 = " "
c22 = " "
c23 = " "
c24 = " "
c25 = " "
c31 = " "
c32 = " "
c33 = " "
c34 = " "
c35 = " "
c41 = " "
c42 = " "
c43 = " "
c44 = " "
c45 = " "
c51 = " "
c52 = " "
c53 = " "
c54 = " "
c55 = " "


def crash_error(ec):
    global running

    os.system("cls")
    running = False
    print(" ___________________________")
    print("|Software stopped to prevent|")
    print("|the system from crashing.  |")
    print("|Press: P.Proceed Q.Quit    |")
    print(f"|Error Code: {ec}            |")
    print("|Read manual for error code |")
    print("|___________________________|")
    cmd = input("CMD> ")
    if cmd == "P":
        running = True
    elif cmd == "Q":
        quit()
    else:
        crash_error("316")


def tev():
    global t
    global e
    os.system("cls")
    tenv = input("ENTER TYPE> ")
    if tenv == "C" and len(tenv) == 1:
        t = "C"
        e = " "
    elif tenv == "N" and len(tenv) == 1:
        t = "N"
        e = " "
    elif tenv == "S" and len(tenv) == 1:
        t = "S"
        e = " "
    else:
        t = "U"
        e = " "
        crash_error("025")


def eev():
    global e
    global t
    os.system("cls")
    eenv = input("ENTER VALUE> ")
    if t == "C" and eenv in cs and len(eenv) == 1:
        e = eenv
    elif t == "N" and eenv in ns and len(eenv) == 1:
        e = eenv
    elif t == "S" and eenv in ss and len(eenv) == 1:
        e = eenv
    else:
        e = " "
        crash_error("055")


def pxev():
    global px
    os.system("cls")
    pxenv = int(input("ENTER VALUE> "))
    if pxenv < 11 and pxenv >= 1:
        px = pxenv
    else:
        crash_error("254")


def pyev():
    global py
    os.system("cls")
    pyenv = int(input("ENTER VALUE> "))
    if pyenv < 11 and pyenv >= 1:
        py = pyenv
    else:
        crash_error("251")


def pnev():
    global pn
    os.system("cls")
    pnenv = int(input("ENTER VALUE> "))
    if pnenv < 10 and pnenv >= 1:
        pn = pnenv


def up():
    global pp
    if pp >= 3:
        pp = pp - 2
    else:
        pass


def down():
    global pp
    if pp <= 4:
        pp = pp + 2
    else:
        pass


def left():
    global pp
    if pp == 2 or pp == 4 or pp == 6:
        pp = pp - 1
    else:
        pass


def right():
    global pp
    if pp == 1 or pp == 3 or pp == 5:
        pp = pp + 1
    else:
        pass


def show():
    global running
    os.system("cls")
    running = False
    print("| - - - - - - - - - - |")
    # print(f"| {clist[0]} {clist[1]} {clist[2]} {clist[3]} {clist[4]} {clist[5]} {clist[6]} {clist[7]} {clist[8]} {clist[9]} |")
    # print(f"| {clist[10]} {clist[11]} {clist[12]} {clist[13]} {clist[14]} {clist[15]} {clist[16]} {clist[17]} {clist[18]} {clist[19]} |")
    # print(f"| {clist[20]} {clist[21]} {clist[22]} {clist[23]} {clist[24]} {clist[25]} {clist[26]} {clist[27]} {clist[28]} {clist[29]} |")
    # print(f"| {clist[30]} {clist[31]} {clist[32]} {clist[33]} {clist[34]} {clist[35]} {clist[36]} {clist[37]} {clist[38]} {clist[39]} |")
    # print(f"| {clist[40]} {clist[41]} {clist[42]} {clist[43]} {clist[44]} {clist[45]} {clist[46]} {clist[47]} {clist[48]} {clist[49]} |")
    # print(f"| {clist[50]} {clist[51]} {clist[52]} {clist[53]} {clist[54]} {clist[55]} {clist[56]} {clist[57]} {clist[58]} {clist[59]} |")
    # print(f"| {clist[60]} {clist[61]} {clist[62]} {clist[63]} {clist[64]} {clist[65]} {clist[66]} {clist[67]} {clist[68]} {clist[69]} |")
    # print(f"| {clist[70]} {clist[71]} {clist[72]} {clist[73]} {clist[74]} {clist[75]} {clist[76]} {clist[77]} {clist[78]} {clist[79]} |")
    # print(f"| {clist[80]} {clist[81]} {clist[82]} {clist[83]} {clist[84]} {clist[85]} {clist[86]} {clist[87]} {clist[88]} {clist[89]} |")
    # print(f"| {clist[90]} {clist[91]} {clist[92]} {clist[93]} {clist[94]} {clist[95]} {clist[96]} {clist[97]} {clist[98]} {clist[99]} |")
    for i in range(10):
        print("|", " ".join(clist[i * 10:(i + 1) * 10]), "|")
    print(f"| - - - - - - - - - - |")
    cmd = input("CMD> ")
    if cmd == "B":
        running = True
    else:
        crash_error("316")


def show_done():
    pass


def pt(px, py, e):
    index = (py - 1) * 10 + (px - 1)
    clist[index] = e


while running == True:
    os.system("cls")

    if py < 10:
        frs = "  "
    elif py > 9:
        frs = " "

    if px < 10:
        ts = "  "
    elif px > 9:
        ts = " "

    if pp == 1:
        c1 = "*"
    else:
        c1 = " "

    if pp == 2:
        c2 = "*"
    else:
        c2 = " "

    if pp == 3:
        c3 = "*"
    else:
        c3 = " "

    if pp == 4:
        c4 = "*"
    else:
        c4 = " "

    if pp == 5:
        c5 = "*"
    else:
        c5 = " "

    if pp == 6:
        c6 = "*"
    else:
        c6 = " "

    if pp == 5:
        cp = "|Cursor: I.Up K.Down J.Left L.Right | S.Show        |"
    elif pp != 5:
        cp = "|Cursor: I.Up K.Down J.Left L.Right | S.Show E.Enter|"
    print(" ___________________________________________________")
    print("|*FILIPPVAS™ 2023 - ....*    (PyKey Canvas)   D.Done|")
    print("|                                                   |")
    print(f"|TYPE: {t}{c1}           ENTER: {e}{c2}                       |")
    print("|                                                   |")
    print(f"|POSITION X: {px}{c3}{ts}   POSITION Y: {py}{c4}{frs}                |")
    print("|                                                   |")
    print(f"|DATE: {d}{c5}  PROJECT NUMBER: {pn}{c6}              |")
    print("|                                                   |")
    print("|                                                   |")
    print(cp)
    print("|___________________________________________________|")
    cmd = input("CMD> ")
    if cmd == "I":
        up()
    elif cmd == "K":
        down()
    elif cmd == "J":
        left()
    elif cmd == "L":
        right()
    elif cmd == "E":
        if pp == 1:
            tev()
        elif pp == 2:
            eev()
        elif pp == 3:
            pxev()
        elif pp == 4:
            pyev()
        elif pp == 6:
            pnev()
        elif pp == 5:
            crash_error("348")
    elif cmd == "S":
        show()
    elif cmd == "D":
        pt(px, py, e)
    elif cmd == "Q":
        quit()
    else:
        crash_error("316")

