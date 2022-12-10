import functions, os, time
from colorama import Fore

def somethingelse():
    options=["y","n"]
    while True:
            yesorno=input('Do you want to do something else? (y/n)')
            yesornocheck=yesorno in options
            if len(yesorno) == 0:
                print(f"{Fore.RED}Insert something!{Fore.RESET}")
            if yesornocheck == False:
                print(f"{Fore.RED}Insert some valid option!{Fore.RESET}")
            else: 
                if yesorno != options[0]:
                    print(f"{Fore.RED}closing...{Fore.RESET}")
                    time.sleep(0.5)
                    functions.clean()
                    exit()
                else:
                    break

## Here is displayed all the code
while True:
    functions.clc()
    whattodo=(functions.__init__())
    if whattodo == "1":
        functions.installer()
        somethingelse()

    else:
        functions.inst()
        somethingelse()


