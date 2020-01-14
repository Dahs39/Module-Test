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
filepath = 'c:\\Python\\Script_Pictures\\moduleTest\\Screenshots\\moduleDataExchange\\%s' %currentDay
if not os.path.exists(filepath):
	os.makedirs('c:\\Python\\Script_Pictures\\moduleTest\\Screenshots\\moduleDataExchange\\%s' %currentDay)

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
	pyautogui.typewrite('c:\\Python\\Script_Pictures\\moduleTest\\Screenshots\\moduleDataExchange\\')
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

# Selects module from moduleData and loads it, takes a screenshot after preset sleep time
def injectModule(moduleName):
	selectAllModules(moduleName)
	print('Currently loading: {}'.format(moduleName))
	print(time.strftime('%m-%d-%Y-%H:%M:%S'))
	sleep(moduleDataExchange[moduleName][0])
	btnPos.click_ContinueBtn(moduleDataExchange[moduleName][1])
	if moduleDataExchange[moduleName][2] == True:
		btnPos.click_CallTutorBtn()
	Screenshot_with_Paint(moduleName)

Local_Frontend_Login('dchau_test', 'Cangetin00')

#Iterates through modules in moduleData dictionary
for module in moduleDataExchange:
	injectModule(module)

sleep(300)

Logout_Frontend()