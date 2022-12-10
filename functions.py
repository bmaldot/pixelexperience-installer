import os, time, devices
from colorama import Fore
from zipfile import ZipFile
sys=os.name
linpath='platform-tools/adb'
winpath='./platform-tools/adb.exe'
##functions necessary to make the script work

##clear terminal
def clc():
    if sys == 'posix':
        os.system('clear')
    else: 
        os.system('cls')

##clean directories/temporalfiles/files
def clean():
    options=["y","n"]
    if sys == 'posix':
        os.system('rm extractme.zip')
    else:
        os.system('del extractme.zip')
    while True:
            yesorno=input('Do you want to remove adb? (y/n) ')
            yesornocheck=yesorno in options
            if len(yesorno) == 0:
                print(f"{Fore.RED}Insert something!{Fore.RESET}")
            if yesornocheck == False:
                print(f"{Fore.RED}Insert some valid option!{Fore.RESET}")
            else: 
                if yesorno != options[0]:
                    pass
                else:
                    os.system('RD platform-tools\ /s ')
                    pass
            yesorno2=input('Do you want to remove zip flashables? (y/n) ')
            yesornocheck2=yesorno2 in options
            if len(yesorno2) == 0:
                print(f"{Fore.RED}Insert something!{Fore.RESET}")
            if yesornocheck2 == False:
                print(f"{Fore.RED}Insert some valid option!{Fore.RESET}")
            else: 
                if yesorno2 != options[0]:
                    return
                else:
                    if sys == 'posix':
                        os.system('rm surya-pe12.zip')
                        os.system('rm mido-pe11.zip')
                        os.system('rm begonia-pe12.zip')
                        os.system('rm miatoll-pe12.zip')
                    else:
                        os.system('del surya-pe12.zip')
                        os.system('del mido-pe11.zip')
                        os.system('del begonia-pe12.zip')
                        os.system('del miatoll-pe12.zip')    
                    return            

##get what do you want to do    
def __init__():
    eschema="""
    What do you want to do?
    
    1)Install adb and fastboot (win, debian)
    2)Install Pixel Experience

    """
    options=["1","2"]
    print(eschema)
    while True:
        quehacerunchecked=input(f'{Fore.BLUE}Put here what do you want to do: {Fore.RESET}')
        quehacerchecker= quehacerunchecked in options
        if len(quehacerunchecked) == 0:
            print(f"{Fore.RED}Insert something!{Fore.RESET}")
        if quehacerchecker == False:
            print(f"{Fore.RED}Insert some valid option!{Fore.RESET}")
        else: 
            return quehacerunchecked
            break

##installer of adb and fastboot        
def installer():
    sis=os.name
    options=["y","n"]
    print(f"Your os is: {Fore.GREEN}{sis}{Fore.RESET}")
    while True:
        yesorno=input('Do you want to proceed? (y/n)')
        yesornocheck=yesorno in options
        if len(yesorno) == 0:
            print(f"{Fore.RED}Insert something!{Fore.RESET}")
        if yesornocheck == False:
            print(f"{Fore.RED}Insert some valid option!{Fore.RESET}")
        if yesorno == 'n':
            print(Fore.RED+'closing installer...'+Fore.RESET)
            return
        else:
            break
    while True:    
        if sis=="posix":
            answer=input('Are you in debian? (y/n)')
            answercheck=answer in options
            if len(answer) == 0:
                print(f"{Fore.RED}Insert something!{Fore.RESET}")
            if answercheck == False:
                print(f"{Fore.RED}Insert some valid option!{Fore.RESET}")
            if answer != options[0]:
                    print(f"{Fore.RED}closing installer...{Fore.RESET}")
                    time.sleep(0.5)
                    return
            else:
                print('installing adb and fastboot...')
                os.system('wget https://dl.google.com/android/repository/platform-tools_r33.0.3-linux.zip -O extractme.zip')
                with ZipFile('extractme.zip', 'r') as zip:
                    zip.extractall()
                print('installed!')
                return
        else:
            print('installing adb and fastboot...')
            os.system('powershell wget https://dl.google.com/android/repository/platform-tools-latest-windows.zip -O extractme.zip')
            with ZipFile('extractme.zip', 'r') as zip:
                zip.extractall()
                print(f'{Fore.GREEN}Installed!{Fore.RESET}')    
            return 1

#installer
def inst():
    options=['mido', 'miatoll','begonia','surya']
    print(f'{Fore.LIGHTBLACK_EX}This script is only working for 4 dispositives: mido, miatoll, begonia and surya {Fore.RESET}')
    device=input("What is the codename of your device?\ninput: ")
    checkdevice=device in options
    while True:
        if len(device)==0:
            Fore.RED
            print('wrong input')
            Fore.RESET
        if checkdevice != True:
            Fore.RED
            print('wrong input')
            Fore.RESET
        if device==options[0]:
            devices.mido()
            return
        if device==options[1]:
            devices.miatoll()
            return
        if device==options[2]:
            devices.begonia()
            return
        if device==options[3]:
            devices.surya()
            return
            