import os
import sys
from colorama import init
init()
from colorama import Fore,Back
import settings
import signal
import DroxyFire

def signal_handler(sig, frame):
    print("\nWelcome To Out Of PyPad's World !")
    sys.exit(0)

def ReadFile(path):
    x = open(path,mode)
    d = x.readlines()
    content = ""
    for c in d:
        content += c
    return content

if (__name__ == "__main__"):
    _cls = DroxyFire.DroxyFireV1(settings._SETTINGS_VERSION_).HashStr(2)
    if (_cls == settings._ENCODED_SETTINGS_VERSION_):
        signal.signal(signal.SIGINT,signal_handler)
        if (len(sys.argv) == 3):
            path = sys.argv[1]
            mode = sys.argv[2]
            ext = "Non Ext File"
            _class = DroxyFire.DroxyFireV1(str(path))
            cv = _class.DoesIn('.')
            if (cv == 1):
                x = _class.IndexOf('.')
                ext = path[x + 1:len(path)]

            if (os.path.exists(path)):
                if (mode == "w"):

                    line = 1
                    lines = []

                    if (settings._CLEAR_ON_ACTIONS_):
                        if (settings._SYS_CURRENT_CORE_ == "WINDOWS"):
                            clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[1])
                            clear()
                        else:
                            clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[0])
                            clear()

                    x = open(path,"r")
                    d = x.readlines()
                    
                    for i in range(0,len(d)):
                        if (settings._SHOW_WITH_NUMBER_):
                            if (settings._USE_EDITOR_COLOR_STYLE_):
                                if (settings._USE_EDITOR_COLOR_STYLE_):
                                    print(settings._TEXT_COLOR_ + settings._BACK_COLOR_ + str(i + 1) + "| " + d[i].replace("\n",""))
                            else:
                                print(str(i + 1) + "| " + d[i].replace("\n",""))
                            line += 1
                            if (line > settings._MAX_PAGE_LINE_SIZE_):
                                print(Fore.RED + Back.WHITE + "Can't Handle Lines More Than " + str(settings._MAX_PAGE_LINE_SIZE_))
                                exit(0)
                            else:
                                    lines.append(d[i])
                        else:
                            if (settings._USE_EDITOR_COLOR_STYLE_):
                                if (settings._USE_EDITOR_COLOR_STYLE_):
                                    print(settings._TEXT_COLOR_ + settings._BACK_COLOR_ + str(i + 1) + "| " + d[i].replace("\n",""))
                            else:
                                print("| " + d[i].replace("\n",""))
                            line += 1
                            if (line > settings._MAX_PAGE_LINE_SIZE_):
                                print(Fore.RED + Back.WHITE + "Can't Handle Lines More Than " + str(settings._MAX_PAGE_LINE_SIZE_))
                                exit(0)
                            else:
                                    lines.append(d[i])

                    save = False
                    
                    while(save == False):
                        tline = ""
                        if (settings._SHOW_WITH_NUMBER_):
                            tline = input(str(line) + "| ")
                        else:
                            tline = input("| ")

                        if (tline == "~>SAVE"):
                            c = open(path,mode)
                            v = ""
                            for i in lines:
                                v += i
                            c.write(v)
                            save = True
                            break
                        elif (tline == "~>GTL"):
                            if (settings._CLEAR_ON_ACTIONS_):
                                if (settings._SYS_CURRENT_CORE_ == "WINDOWS"):
                                    clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[1])
                                    clear()
                                else:
                                    clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[0])
                                    clear()
                            x = int(input("enter line number : "))
                            if (settings._SHOW_WITH_NUMBER_):
                                print(str(x) + "| " + lines[x - 1])
                            else:
                                print("| " + lines[x - 1])
                        elif (tline == "~>VERSION"):
                            print("Encoded Settings Version : " + settings._ENCODED_SETTINGS_VERSION_)
                            print("Settings Version : " + settings._SETTINGS_VERSION_)
                        elif (tline == "~>RSF"):
                            if (settings._CLEAR_ON_ACTIONS_):
                                if (settings._SYS_CURRENT_CORE_ == "WINDOWS"):
                                    clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[1])
                                    clear()
                                else:
                                    clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[0])
                                    clear()
                            d = lines
                            for i in range(0,len(d)):
                                if (settings._SHOW_WITH_NUMBER_):
                                    print(str(i + 1) + "| " + d[i].replace("\n",""))
                                else:
                                    print("| " + d[i].replace("\n",""))
                        elif (tline == "~>EL"):
                            if (settings._CLEAR_ON_ACTIONS_):
                                if (settings._SYS_CURRENT_CORE_ == "WINDOWS"):
                                    clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[1])
                                    clear()
                                else:
                                    clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[0])
                                    clear()
                            x = int(input("enter line number : "))
                            if (settings._SHOW_WITH_NUMBER_):
                                print(str(x) + "| " + lines[x - 1])
                            else:
                                print("| " + lines[x - 1])
                            c = input("Enter New Data : ")
                            lines[x - 1] = c + "\n"
                        elif (tline == "~>SLL"):
                            if (settings._CLEAR_ON_ACTIONS_):
                                if (settings._SYS_CURRENT_CORE_ == "WINDOWS"):
                                    clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[1])
                                    clear()
                                else:
                                    clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[0])
                                    clear()
                            start = int(input("Enter Start Line : "))
                            end = int(input("Enter End Line : "))
                            for i in range(start,end + 1):
                                if (settings._SHOW_WITH_NUMBER_):
                                    print(str(i) + "| " + lines[i - 1].replace("\n",""))
                                else:
                                    print("| " + lines[i])
                        elif (tline == "~>FIND"):
                            if (settings._CLEAR_ON_ACTIONS_):
                                if (settings._SYS_CURRENT_CORE_ == "WINDOWS"):
                                    clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[1])
                                    clear()
                                else:
                                    clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[0])
                                    clear()
                            res = ""
                            serach = input("enter your text : ")
                            for i in range(0,len(lines)):
                                if (lines[i].find(serach,0) != -1):
                                    if (settings._SHOW_WITH_NUMBER_):
                                        res += str(i + 1) + "| " + lines[i]
                                    else:
                                        res += "| " + lines[i]
                            print(res)
                        elif (tline == "~>EWOC"):
                            exit(0)
                        else:
                            line += 1
                            if (line > settings._MAX_PAGE_LINE_SIZE_):
                                print(Fore.RED + Back.WHITE + "Can't Handle Lines More Than " + str(settings._MAX_PAGE_LINE_SIZE_))
                                exit(0)
                            else:
                                    lines.append(tline + "\n")
                            
                    if (save):
                        print("\nFile Saved !")
                elif (mode == "r"):
                    if (settings._USE_EDITOR_COLOR_STYLE_):
                        print(settings._TEXT_COLOR_ + settings._BACK_COLOR_ + ReadFile(path))
                    else:
                        print(ReadFile(path))
            else:
                if (mode == "w"):

                    lines = []

                    if (settings._CLEAR_ON_ACTIONS_):
                        if (settings._SYS_CURRENT_CORE_ == "WINDOWS"):
                            clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[1])
                            clear()
                        else:
                            clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[0])
                            clear()

                    save = False
                    line = 1
                    while(save == False):
                        tline = ""
                        if (settings._SHOW_WITH_NUMBER_):
                            if (settings._USE_EDITOR_COLOR_STYLE_):
                                tline = input(settings._TEXT_COLOR_ + settings._BACK_COLOR_ + str(line) + "| ")
                            else:
                                tline = input(str(line) + "| ")
                        else:
                            if (settings._USE_EDITOR_COLOR_STYLE_):
                                tline = input(settings._TEXT_COLOR_ + settings._BACK_COLOR_ + "| ")
                            else:
                                tline = input("| ")
                        if (tline == "~>SAVE"):
                            c = open(path,mode)
                            v = ""
                            for i in lines:
                                v += i
                            c.write(v)
                            save = True
                            break
                        elif (tline == "~>GTL"):
                            if (settings._CLEAR_ON_ACTIONS_):
                                if (settings._SYS_CURRENT_CORE_ == "WINDOWS"):
                                    clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[1])
                                    clear()
                                else:
                                    clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[0])
                                    clear()
                            x = int(input("enter line number : "))
                            if (settings._SHOW_WITH_NUMBER_):
                                print(str(x) + "| " + lines[x - 1])
                            else:
                                print("| " + lines[x - 1])
                        elif (tline == "~>RSF"):
                            if (settings._CLEAR_ON_ACTIONS_):
                                if (settings._SYS_CURRENT_CORE_ == "WINDOWS"):
                                    clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[1])
                                    clear()
                                else:
                                    clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[0])
                                    clear()       
                            d = lines
                            for i in range(0,len(d)):
                                if (settings._SHOW_WITH_NUMBER_):
                                    print(str(i + 1) + "| " + d[i].replace("\n",""))
                                else:
                                    print("| " + d[i].replace("\n",""))
                        elif (tline == "~>EL"):
                            if (settings._CLEAR_ON_ACTIONS_):
                                if (settings._SYS_CURRENT_CORE_ == "WINDOWS"):
                                    clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[1])
                                    clear()
                                else:
                                    clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[0])
                                    clear()
                            x = int(input("enter line number : "))
                            if (settings._SHOW_WITH_NUMBER_):
                                print(str(x) + "| " + lines[x - 1])
                            else:
                                print("| " + lines[x - 1])
                            c = input("Enter New Data : ")
                            lines[x - 1] = c + "\n"
                        elif (tline == "~>SLL"):
                            if (settings._CLEAR_ON_ACTIONS_):
                                if (settings._SYS_CURRENT_CORE_ == "WINDOWS"):
                                    clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[1])
                                    clear()
                                else:
                                    clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[0])
                                    clear()
                            start = int(input("Enter Start Line : "))
                            end = int(input("Enter End Line : "))
                            for i in range(start,end + 1):
                                if (settings._SHOW_WITH_NUMBER_):
                                    print(str(i) + "| " + lines[i - 1].replace("\n",""))
                                else:
                                    print("| " + lines[i])
                        elif (tline == "~>FIND"):
                            if (settings._CLEAR_ON_ACTIONS_):
                                if (settings._SYS_CURRENT_CORE_ == "WINDOWS"):
                                    clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[1])
                                    clear()
                                else:
                                    clear = lambda: os.system(settings._SYS_CLEAR_COMMANDS[0])
                                    clear()
                            res = ""
                            serach = input("enter your text : ")
                            for i in range(0,len(lines)):
                                if (lines[i].find(serach,0) != -1):
                                    if (settings._SHOW_WITH_NUMBER_):
                                        res += str(i + 1) + "| " + lines[i]
                                    else:
                                        res += "| " + lines[i]
                            print(res)
                        elif (tline == "~>EWOC"):
                            exit(0)
                        else:
                            line += 1
                            if (line > settings._MAX_PAGE_LINE_SIZE_):
                                print(Fore.RED + Back.WHITE + "Can't Handle Lines More Than " + str(settings._MAX_PAGE_LINE_SIZE_))
                                exit(0)
                            else:
                                    lines.append(tline + "\n")
                    if (save):
                        print("\nFile Saved !")
                elif (mode == "r"):
                    print(Fore.RED + "File Not Exist !...")
        elif (len(sys.argv) == 1):
            print()
            print("""                     WELCOME TO PYPAD 0.0.2                        """)
            print("""               Created By Armin Asefi On 2020/8/14                 """)
            print("""        For more information , please read ' READ.MD ' File        """)
            print("""    **********************************************************     """)
            print("""      ******************************************************       """)
            print("""         *************************************************         """)
            print("""             ****************************************              """)
            print("""                   ****************************                    """)
            print("""                     *-*-* PyPad 0.0.2 *-*-*                       """)
            print("""                   ****************************                    """)
            print("""             ****************************************              """)
            print("""         *************************************************         """)
            print("""      ******************************************************       """)
            print("""    **********************************************************     """)
            print()
    else:
        print(Fore.RED + "Theft Version Of PyPad Found !")