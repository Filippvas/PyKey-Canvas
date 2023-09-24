#Author: Filippvas™ (Philip Vasilakis)
#Project Name: PyKey Canvas (CN n S)

import os
import time
import string
from datetime import date

today = date.today()
d = today.strftime("%Y-%m-%d")

cs = list(string.ascii_uppercase)
ns = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
ss = ["!", "@","#","$","%","^","&","*","(",")","'",'"',",",".","<",">","[","]","{","}","`","~",":",";","|","-","_","=","+"]
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
    if pxenv < 6 and pxenv >= 1:
        px = pxenv
    else:
        crash_error("254")

def pyev():
    global py
    os.system("cls")
    pyenv = int(input("ENTER VALUE> "))
    if pyenv < 6 and pyenv >= 1:
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
    print("| - - - - - |")
    print(f"| {c11} {c21} {c31} {c41} {c51} |")
    print(f"| {c12} {c22} {c32} {c42} {c52} |")
    print(f"| {c13} {c23} {c33} {c43} {c53} |")
    print(f"| {c14} {c24} {c34} {c44} {c54} |")
    print(f"| {c15} {c25} {c35} {c45} {c55} |")
    print(f"| - - - - - |")
    cmd = input("CMD> ")
    if cmd == "B":
        running = True
    else:
        crash_error("316")

def show_done():
    pass

def pt():
    global c11, c12, c13, c14, c15, c21, c22, c23, c24, c25, c31, c32, c33, c34, c35, c41, c42, c43, c45, c51, c52, c53, c54, c55
    if px == 1 and py == 1:
        c11 = e
    elif px == 1 and py == 2:
        c12 = e
    elif px == 1 and py == 3:
        c13 = e
    elif px == 1 and py == 4:
        c14 = e
    elif px == 1 and py == 5:
        c15 = e
    elif px == 2 and py == 1:
        c21 = e
    elif px == 2 and py == 2:
        c22 = e
    elif px == 2 and py == 3:
        c23 = e
    elif px == 2 and py == 4:
        c24 = e
    elif px == 2 and py == 5:
        c25 = e
    elif px == 3 and py == 1:
        c31 = e
    elif px == 3 and py == 2:
        c32 = e
    elif px == 3 and py == 3:
        c33 = e
    elif px == 3 and py == 4:
        c34 = e
    elif px == 3 and py == 5:
        c35 = e
    elif px == 4 and py == 1:
        c41 = e
    elif px == 4 and py == 2:
        c42 = e
    elif px == 4 and py == 3:
        c43 = e
    elif px == 4 and py == 4:
        c44 = e
    elif px == 4 and py == 5:
        c45 = e
    elif px == 5 and py == 1:
        c51 = e
    elif px == 5 and py == 2:
        c52 = e
    elif px == 5 and py == 3:
        c53 = e
    elif px == 5 and py == 4:
        c54 = e
    elif px == 5 and py == 5:
        c55 = e


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
        pt()
    elif cmd == "Q":
        quit()
    else:
        crash_error("316")

