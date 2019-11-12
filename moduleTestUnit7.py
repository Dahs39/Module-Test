import pyautogui
import os
from time import sleep
import time
from pywinauto.findwindows import find_window
from pywinauto.win32functions import SetForegroundWindow
from PIL import Image
from moduleTestFunctions import *
from moduleTestUnitList import *

pyautogui.FAILSAFE = False

# Gets current date where screenshots will be saved in C:\Python\Script_Pictures\moduleTest\Screenshots\
currentDay = time.strftime('%m-%d-%Y')

# Checks if folder already exists for screenshots, if not, creates it
filepath = 'c:\\Python\\Script_Pictures\\moduleTest\\Screenshots\\Unit7\\%s' %currentDay
if not os.path.exists(filepath):
	os.makedirs('c:\\Python\\Script_Pictures\\moduleTest\\Screenshots\\Unit7\\%s' %currentDay)

def Logout_Frontend():
	btnPos.click_LogOutBtn()
	btnPos.click_LogOutConfirmBtn()
	os.system("taskkill /f /im java.exe")
	Test_Completion_Time = (time.strftime('%m-%d-%Y-%H-%M'))
	Screenshot_with_Paint('testEnd')

def Screenshot_with_Paint(name):
	sleep(5)
	pyautogui.hotkey('printscreen')
	sleep(2)
	os.startfile('c:\\Windows\\system32\\mspaint.exe')
	sleep(20)
	pyautogui.hotkey('ctrl', 'v')
	sleep(3)
	pyautogui.hotkey('ctrl', 's')
	sleep(15)
	pyautogui.typewrite('c:\\Python\\Script_Pictures\\moduleTest\\Screenshots\\Unit7\\')
	sleep(1)
	pyautogui.typewrite(currentDay)
	sleep(1)
	pyautogui.typewrite('\\')
	sleep(1)
	pyautogui.typewrite(name)
	sleep(1)
	pyautogui.hotkey('enter')
	sleep(10)
	os.system("taskkill /f /im mspaint.exe")
	sleep(5)

# Selects module from moduleDataUnit7 and loads it, takes a screenshot after preset sleep time
def injectModule(moduleName):
	selectAllModules(moduleName)
	print('Currently loading: {}'.format(moduleName))
	print(time.strftime('%m-%d-%Y-%H:%M:%S'))
	sleep(moduleDataUnit7[moduleName][0])
	btnPos.click_ContinueBtn(moduleDataUnit7[moduleName][1])
	if moduleDataUnit7[moduleName][2] == True:
		btnPos.click_CallTutorBtn()
	Screenshot_with_Paint(moduleName)

Local_Frontend_Login('dchau_test', 'Cangetin00')

#Iterates through modules in moduleDataUnit7dictionary
for module in moduleDataUnit7:
	injectModule(module)

sleep(300)

Logout_Frontend()

# #Log out of Tutor
# btnPos.click_LogOutBtn()
# btnPos.click_LogOutConfirmBtn()
# os.system("taskkill /f /im java.exe")

# Test_Completion_Time = (time.strftime('%m-%d-%Y-%H-%M'))

# Screenshot_with_Paint('testEnd')


#7/24 Modifying due to preinjection being turned on
# moduleDataUnit7= {
# 			'2K16 Web Server - Introduction': (120, 1, False),
# 			'2K16 Web Server - Managing Websites 1': (630, 1, False),
# 			'2K16 Storage - Mirrored Volumes': (90, 0, True),
# 			'2K16 Print Server - Printer Basics 1': (150, 0, False),
# 			'2K16 Performance Monitor': (120, 0, False),
# 			'2K16 Group Policy Troubleshooting - RSOP': (120, 1, False),
# 			'2K16 Group Policy Deployment - Publish Software': (150, 0, False),
# 			'2K16 Group Policy - Folder Redirection': (120, 1, False),
# 			'2K16 Global Catalog - Schema': (120, 0, False),
# 			'2K16 Global Catalog - Database in the Raw': (120, 1, False),
# 			'2K16 DHCP - MAC Filtering': (120, 0, False),
# 			'2K16 Basic OS - Event Viewer 2': (120, 0, False),
# 			'2K16 Auditing 1': (100, 1, False),
# 			'2K16 Active Directory Restore Basics': (60, 0, False),
# 			'2K16 AD Maintenance': (120, 1, False),
# 			'DNS Server as resolver 2016': (150, 1, False),
# 			'DNS Zones 2016': (45, 1, False),
# 			'Rise and Shine Exercise 2016': (200, 1, False),
# 			'DNS Recursion 2016': (30, 1, False),
# 			'Adding an Alias Record Exercise 2016': (130, 1, False),
# 			'Who Hijacked the Mail Server Exercise 2016': (500, 1, False),
# 			'Introduction to the Domain 2016': (350, 1, False),
# 			'Installing Admin Tools 2016': (390, 0, False),
# 			'User Profiles - Change User Name 2016': (400, 0, False),
# 			'User Profiles - Default User 2016': (120, 1, False),
# 			'User Profiles - Mandatory Profiles 2016': (460, 1, False),
# 			'2K16 Adding Counters': (120, 0 , False),
# 			'2K16 Basic OS - Device Manager': (90, 1, False),
# 			'2K16 DHCP - Scope Options': (600, 0, False),
# 			'2K16 File Server Access Management - Group Types and Scopes': (600, 1, False),
# 			'2K16 Introduction to Active Directory': (600, 1 , False),
# 			'2K16 DSRM - Authoritative Restore': (900, 2, False),
# 			'2K16 DSRM - Non-Authoritative Restore': (900, 0 , False),
# 			'2K16 DHCP - Scopes': (130, 0, False),
# 			'2K16 Auditing 2': (100, 1, False),
# 			'2K16 Directing Authentication': (120, 0, False),
# 			'2K16 Disaster Recovery': (100, 1, False),
# 			'2K16 Group Policy Security - Administrative Templates': (100, 5, False),
# 			'2K16 Active Directory Structure - OU Delegation': (130, 0, False),
# 			'2K16 Web Server - Creating Websites': (615, 1, True),
# 			'2K16 Web Server - Virtual Directories': (715, 0 , False),
# 			'2K16 Active Directory Recycle Bin': (210, 4, False),
# 			'2K16 AD Troubleshooting - ADTD': (160, 4, False),
# 			'2K16 Group Policy Deployment - Assign Software': (160, 2, False),
# 			'2K16 Functional Levels - Domain': (700, 0, False),
# 	}