#importing lib
import subprocess, ctypes, sys
from subprocess import Popen, DEVNULL
import os

#start cmd without termination "cmd /k"
#start cmd with termination "cmd /c"

#Windows Firewall start automatically
os.system('cmd /k "sc config mpssvc start=auto"')

#Start Windows Firewall Service
os.system('cmd /k "net stop mpssvc && net start mpssvc"')

#Enable Windows Firewall profiles
os.system('cmd /k "netsh advfirewall set allprofiles state on"')

#Create a rule to deny input of packets from a specific IP address
os.system('cmd /k "netsh advfirewall firewall add rule name="BLOCK IP ADDRESS - 10.10.10.10" dir=in action=block remoteip=10.10.10.10"')

#Create a firewall rule to deny the output of packets to a specific IP address
os.system('cmd /k "netsh advfirewall firewall add rule name="BLOCK IP ADDRESS - 10.10.10.10" dir=out action=block remoteip=10.10.10.10"')

