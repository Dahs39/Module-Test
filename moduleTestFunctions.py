import pyautogui
import os
from time import sleep
import time
from pywinauto.findwindows import find_window
from pywinauto.win32functions import SetForegroundWindow
from PIL import Image
from win32api import GetSystemMetrics

# Get resolution of screen the test is running on
screenWidth = GetSystemMetrics(0)
screenHeight = GetSystemMetrics(1)

currentDay = time.strftime('%m-%d-%Y')

# Positions of buttons in the Tutor based on screen resolution(david-vbox is at 1920x1157)
class btnPos:
	def click_LobbyBtn():
		#Clicks on Lobby Button
		lobbyBtnXPos = screenWidth * (25/1920)
		lobbyBtnYPos = screenHeight * (38/1157)
		pyautogui.click(x=lobbyBtnXPos, y=lobbyBtnYPos)

	def click_DebugBtn():
		#Clicks on Debug menu
		#debugBtnXPos = screenWidth * 0.0505
		#debugBtnYPos = screenHeight * 0.5056
		#New Lobby 4/24
		debugBtnXPos = screenWidth * (84/1920)
		debugBtnYPos = screenHeight * (609/1157)
		pyautogui.click(x=debugBtnXPos, y=debugBtnYPos)

	def click_All_ModulesBtn():
		#Clicks on All Modules
		#allModulesBtnXPos = screenWidth * 0.0500
		#allModulesBtnYPos = screenHeight * 0.5523
		#New Lobby 4/24
		allModulesBtnXPos = screenWidth * (92/1920)
		allModulesBtnYPos = screenHeight * (662/1157)
		pyautogui.click(x=allModulesBtnXPos, y=allModulesBtnYPos)

	def click_Find_Bar():
		#Clicks on Find bar
		findBtnXPos = screenWidth * (363/1920)
		findBtnYPos = screenHeight * (357/1157)
		pyautogui.click(x=findBtnXPos, y=findBtnYPos)

	def click_Find_Search_Bar():
		#Clicks on Find Search bar
		findSearchBtnXPos = screenWidth * (303/1920)
		findSearchBtnYPos = screenHeight * (393/1157)
		pyautogui.doubleClick(x=findSearchBtnXPos, y=findSearchBtnYPos)

	def click_Debug_Start_ModuleBtn():
		#Clicks on Debug Start Module
		debugStartModuleBtnXPos = screenWidth * (430/1920)
		debugStartModuleBtnYPos = screenHeight * (943/1157)
		pyautogui.click(x=debugStartModuleBtnXPos, y=debugStartModuleBtnYPos)

	def click_All_Modules_Start_ModuleBtn():
		#Clicks on All Modules Start Module
		allModstartModuleBtnXPos = screenWidth * (488/1920)
		allModstartModuleBtnYPos = screenHeight * (948/1157)
		pyautogui.click(x=allModstartModuleBtnXPos, y=allModstartModuleBtnYPos)

	def click_LogOutBtn():
		#Clicks on Log Out button
		logOutBtnXPos = screenWidth * 0.9870
		logOutBtnYPos = screenHeight * 0.0337
		pyautogui.click(x=logOutBtnXPos, y=logOutBtnYPos)
		sleep(2)

	def click_LogOutConfirmBtn():
		#Clicks on Log Out Confirmation button
		logOutConfirmBtnXPos = screenWidth * 0.9333
		logOutConfirmBtnYPos = screenHeight * 0.2446
		pyautogui.click(x=logOutConfirmBtnXPos, y=logOutConfirmBtnYPos)
		sleep(20)

	def click_ContinueBtn(num_of_Continues):
		#Clicks on Continue button
		continueBtnXPos = screenWidth * 0.2318
		continueBtnYPos = screenHeight * 0.9430
		count = 0
		while count < num_of_Continues:
			sleep(1)
			pyautogui.click(x=continueBtnXPos, y=continueBtnYPos)
			sleep(2)
			count +=1

	def click_CallTutorBtn():
		#Clicks on Call Tutor button
		callTutorBtnXPos = screenWidth * 0.1693
		callTutorBtnYPos = screenHeight * 0.9378
		sleep(1)
		pyautogui.click(x=callTutorBtnXPos, y=callTutorBtnYPos)
		sleep(2)

	def click_AllModulesSearchBar():
		#Clicks on search bar in All Modules
		allModsSearchBarBtnXPos = screenWidth * (387/1920)
		allModsSearchBarYPos = screenHeight * (903/1157)
		pyautogui.click(x=allModsSearchBarBtnXPos, y=allModsSearchBarYPos)
		sleep(1)

	def click_MaximizeFrontEndBtn():
		# maximizeFrontEndBtnXPos = screenWidth * 0.9688
		# maximizeFrontEndBtnYPos = screenHeight * 0.0147
		maximizeFrontEndBtnXPos = screenWidth * 0.9568
		maximizeFrontEndBtnYPos = screenHeight * 0.0190
		pyautogui.click(x=maximizeFrontEndBtnXPos, y=maximizeFrontEndBtnYPos)
		sleep(1)

	def click_ReportProblemFixed():
		reportProblemFixedBtnXPos = screenWidth * 0.2260
		reportProblemFixedBtnYPos = screenHeight * 0.9408
		pyautogui.click(x=reportProblemFixedBtnXPos, y=reportProblemFixedBtnYPos)
		sleep(3)

	def click_ReportProblemFixedConfirm():
		reportProblemFixedConfirmBtnXPos = screenWidth * 0.2094
		reportProblemFixedConfirmBtnYPos = screenHeight * 0.8408
		pyautogui.click(x=reportProblemFixedConfirmBtnXPos, y=reportProblemFixedConfirmBtnYPos)
		sleep(30)

	def EXTDC_Pos():
		EXTDC_XPos = screenWidth * 0.8906
		EXTDC_YPos = screenHeight * 0.5843
		pyautogui.click(x=EXTDC_XPos, y=EXTDC_YPos)
		sleep(3)

	def click_StartMenu():
		Start_XPos = screenWidth * 0.4760
		Start_YPos = screenHeight * 0.9412
		pyautogui.click(x=Start_XPos, y=Start_YPos)
		sleep(1)

	def click_WinAdminTools():
		AdminTools_XPos = screenWidth * 0.5333
		AdminTools_YPos	= screenHeight * 0.7087
		pyautogui.click(x=AdminTools_XPos, y= AdminTools_YPos)
		sleep(1)

	def DC01_Pos():
		pyautogui.click(1227, 428)
		sleep(3)

	def WKS01_Pos():
		pyautogui.click(1086, 1027)
		sleep(3)

	def Topology_Pos():
		pyautogui.click(1342, 1132)
		sleep(3)

# def Screenshot_with_Paint(name):
# 	sleep(5)
# 	pyautogui.hotkey('printscreen')
# 	sleep(2)
# 	os.startfile('c:\\Windows\\system32\\mspaint.exe')
# 	sleep(20)
# 	pyautogui.hotkey('ctrl', 'v')
# 	sleep(3)
# 	pyautogui.hotkey('ctrl', 's')
# 	sleep(15)
# 	pyautogui.typewrite('c:\\Python\\Script_Pictures\\moduleTest\\Screenshots\\Unit5\\')
# 	sleep(1)
# 	pyautogui.typewrite(currentDay)
# 	sleep(1)
# 	pyautogui.typewrite('\\')
# 	sleep(1)
# 	pyautogui.typewrite(name)
# 	sleep(1)
# 	pyautogui.hotkey('enter')
# 	sleep(10)
# 	os.system("taskkill /f /im mspaint.exe")
# 	sleep(5)

# Logs in to a local frontend with username and password passed through, default is dtl registrar.
def Local_Frontend_Login(user, password):
	os.startfile('c:\\runtime\\loginfrontend.bat')
	sleep(60)
	btnPos.click_MaximizeFrontEndBtn()
	pyautogui.typewrite(['f1'])
	pyautogui.typewrite(user)
	pyautogui.hotkey('tab'); pyautogui.typewrite(password)
	pyautogui.typewrite(['enter'])
	sleep(120)

# def Logout_Frontend():
# 	btnPos.click_LogOutBtn()
# 	btnPos.click_LogOutConfirmBtn()
# 	os.system("taskkill /f /im java.exe")
# 	Test_Completion_Time = (time.strftime('%m-%d-%Y-%H-%M'))
# 	Screenshot_with_Paint('testEnd')

# Logs into DC01
def DC01_Login():
	btnPos.DC01_Pos()
	pyautogui.hotkey('ctrl', 'alt', 'backspace')
	sleep(1)
	pyautogui.typewrite('student')
	pyautogui.hotkey('tab'); pyautogui.typewrite('Cangetin00')
	pyautogui.hotkey('enter')
	sleep(30)
	pyautogui.hotkey('ctrl', 'alt', 'backspace')
	sleep(3)
	print('Clicking on Task Manager')
	pyautogui.click(1370, 721)
	sleep(3)
	print('Clicking on More Details')
	pyautogui.click(1020, 734)
	sleep(3)
	print('Clicking on CPU Usage Column')
	pyautogui.click(1212, 501)
	sleep(3)

# Logs into WKS01
def WKS01_Login():
	btnPos.WKS01_Pos()
	pyautogui.hotkey('ctrl', 'alt', 'backspace')
	sleep(1)
	pyautogui.typewrite('student')
	pyautogui.hotkey('tab'); pyautogui.typewrite('Cangetin00')
	pyautogui.hotkey('enter')
	sleep(30)
	pyautogui.hotkey('ctrl', 'alt', 'backspace')
	sleep(3)
	print('Clicking on Task Manager')
	pyautogui.click(1370, 721)
	sleep(3)
	print('Clicking on More Details')
	pyautogui.click(1020, 734)
	sleep(3)
	print('Clicking on CPU Usage Column')
	pyautogui.click(1212, 501)
	sleep(3)

# Logs into EXTDC
def EXTDC_Login():
	btnPos.EXTDC_Pos()
	pyautogui.hotkey('ctrl', 'alt', 'backspace')
	sleep(1)
	pyautogui.typewrite('student')
	pyautogui.hotkey('tab'); pyautogui.typewrite('Cangetin00')
	pyautogui.hotkey('enter')
	sleep(30)
	pyautogui.hotkey('ctrl', 'alt', 'backspace')
	sleep(10)
	print('Clicking on Task Manager')
	pyautogui.click(1370, 721)
	sleep(10)
	print('Clicking on More Details')
	pyautogui.click(1065, 787)
	sleep(10)
	print('Clicking on CPU Usage Column')
	pyautogui.click(1276, 553)
	sleep(3)

# Opens lobby and inputs name of the module in the All Modules search bar
def selectAllModules(moduleName):
	sleep(3)
	btnPos.click_LobbyBtn()
	sleep(7)
	btnPos.click_All_ModulesBtn()
	sleep(2)
	btnPos.click_AllModulesSearchBar()
	pyautogui.hotkey('ctrl', 'a'); pyautogui.typewrite(moduleName); pyautogui.hotkey('enter')

# Opens lobby and inputs name of the module in the DEBUG find bar(avoids loading D16 content)
# Only needed for initial DEBUG one due to FIND bar needing to be expanded
def firstModule(moduleName):
	sleep(7)
	btnPos.click_DebugBtn()
	sleep(2)
	btnPos.click_Find_Bar()
	sleep(2)
	btnPos.click_Find_Search_Bar()
	pyautogui.hotkey('ctrl', 'a'); pyautogui.typewrite(moduleName); pyautogui.hotkey('enter')
	btnPos.click_Debug_Start_ModuleBtn()

# Opens lobby and inputs name of the module in the All Modules find bar
# Workaround due to not wanting to DEBUG for D16 content
def firstAllModule(moduleName):
	sleep(7)
	btnPos.click_All_ModulesBtn()
	sleep(2)
	btnPos.click_AllModulesSearchBar()
	sleep(2)
	pyautogui.hotkey('ctrl', 'a'); pyautogui.typewrite(moduleName); pyautogui.hotkey('enter')
	#btnPos.click_All_Modules_Start_ModuleBtn()

# Opens lobby and inputs name of the module in the DEBUG find bar(avoids loading D16 content)
def selectAllModules(moduleName):
	sleep(3)
	btnPos.click_LobbyBtn()
	sleep(7)
	btnPos.click_All_ModulesBtn()
	sleep(1)
	btnPos.click_AllModulesSearchBar()
	pyautogui.hotkey('ctrl', 'a'); pyautogui.typewrite(moduleName); pyautogui.hotkey('enter')
	#btnPos.click_All_Modules_Start_ModuleBtn()

# Prints screen of current window that is focused, opens paint, and saves it in C:\Script_Pictures with the string that was passed.  Kills the MSPaint process afterwards.
# def Screenshot_with_Paint(name):
# 	sleep(5)
# 	pyautogui.hotkey('printscreen')
# 	sleep(2)
# 	os.startfile('c:\\Windows\\system32\\mspaint.exe')
# 	sleep(20)
# 	pyautogui.hotkey('ctrl', 'v')
# 	sleep(3)
# 	pyautogui.hotkey('ctrl', 's')
# 	sleep(15)
# 	pyautogui.typewrite('c:\\Python\\Script_Pictures\\moduleTest\\Screenshots\\EXTDC_Black_Screen_Test\\')
# 	sleep(1)
# 	pyautogui.typewrite(currentDay)
# 	sleep(1)
# 	pyautogui.typewrite('\\')
# 	sleep(1)
# 	pyautogui.typewrite(name)
# 	sleep(1)
# 	pyautogui.hotkey('enter')
# 	sleep(10)
# 	os.system("taskkill /f /im mspaint.exe")
# 	sleep(5)


def selectEXTDC(moduleName):
	selectAllModules(moduleName)
	print('Currently loading: {}'.format(moduleName))
	print(time.strftime('%m-%d-%Y-%H:%M:%S'))
	sleep(420)
	print('Done Sleeping')
	btnPos.click_ContinueBtn(1)
	Screenshot_with_Paint(moduleName + count)
