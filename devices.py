import os, time
from colorama import Fore
sys = os.name
winpath='./platform-tools/adb.exe'

#for redmi note 4 / 4x
def mido():
    print('getting rom...')
    if sys == 'posix':
        os.system('wget https://master.dl.sourceforge.net/project/pixelexperiencerom/mido/PixelExperience_Plus_mido-11.0-20211216-1807-OFFICIAL.zip?viasf=1 -O mido-pe11.zip')
        print('check your phone if is on mode sideload')
        print('you have 10 secs...')
        time.sleep(10)
        os.system('adb sideload mido-pe11.zip')
        return
    else:
        os.system('powershell wget https://master.dl.sourceforge.net/project/pixelexperiencerom/mido/PixelExperience_Plus_mido-11.0-20211216-1807-OFFICIAL.zip?viasf=1 -O mido-pe11.zip')
        print('check your phone if is on mode sideload')
        print('you have 10 secs...')
        time.sleep(10)
        os.system(f"powershell {winpath} sideload mido-pe11.zip")
        return

#for redmi note 9s / 9pro
def miatoll():
    print('getting rom...')
    if sys == 'posix':
        os.system('wget https://master.dl.sourceforge.net/project/pixelexperiencerom/miatoll/PixelExperience_miatoll-12.0-20220125-1725-OFFICIAL.zip?viasf=1 -O miatoll-pe12.zip')
        print('check your phone if is on mode sideload')
        print('you have 10 secs...')
        time.sleep(10)
        os.system('adb sideload miatoll-pe12.zip')
        return
    else:
        os.system('powershell wget https://master.dl.sourceforge.net/project/pixelexperiencerom/miatoll/PixelExperience_miatoll-12.0-20220125-1725-OFFICIAL.zip?viasf=1 -O miatoll-pe12.zip')
        print('check your phone if is on mode sideload')
        print('you have 10 secs...')
        time.sleep(10)
        os.system(f"powershell {winpath} sideload miatoll-pe12.zip")
        return

#for redmi note 8 pro
def begonia():
    print('getting rom...')
    if sys == 'posix':
        os.system('wget https://master.dl.sourceforge.net/project/pixelexperiencerom/begonia/PixelExperience_begonia-12.0-20220121-0746-OFFICIAL.zip?viasf=1 -O begonia-pe12.zip')
        print('check your phone if is on mode sideload')
        print('you have 10 secs...')
        time.sleep(10)
        os.system('adb sideload begonia-pe12.zip')
        return
    else:
        os.system('powershell wget https://master.dl.sourceforge.net/project/pixelexperiencerom/begonia/PixelExperience_begonia-12.0-20220121-0746-OFFICIAL.zip?viasf=1 -O begonia-pe12.zip')
        print('check your phone if is on mode sideload')
        print('you have 10 secs...')
        time.sleep(10)
        os.system(f"powershell {winpath} sideload begonia-pe12.zip")
        return

#for Poco X3
def surya():
    print('getting rom...')
    if sys == 'posix':
        os.system('wget https://master.dl.sourceforge.net/project/pixelexperiencerom/surya/PixelExperience_surya-12.0-20220124-0118-OFFICIAL.zip?viasf=1 -O surya-pe12.zip')
        print('check your phone if is on mode sideload')
        print('you have 10 secs...')
        time.sleep(10)
        os.system('adb sideload surya-pe12.zip')
        return
    else:
        os.system('powershell wget https://master.dl.sourceforge.net/project/pixelexperiencerom/surya/PixelExperience_surya-12.0-20220124-0118-OFFICIAL.zip?viasf=1 -O surya-pe12.zip')
        print('check your phone if is on mode sideload')
        print('you have 10 secs...')
        time.sleep(10)
        os.system(f"powershell {winpath} sideload surya-pe12.zip")
        return