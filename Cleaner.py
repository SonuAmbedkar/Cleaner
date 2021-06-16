from os import close
import ctypes, sys
from typing import Counter
import pyrebase
import webbrowser
from tkinter import *
from threading import Timer
import subprocess
import os
import shutil
import time
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
from elevate import elevate
firebaseConfig = {
    'apiKey': "AIzaSyA3bewEw6I4D9eG2Rx858jlnpt-CbYtcds",
    'authDomain': "sonucoolantiban.firebaseapp.com",
    'databaseURL': "https://sonucoolantiban.firebaseio.com",
    'projectId': "sonucoolantiban",
    'storageBucket': "sonucoolantiban.appspot.com",
    'messagingSenderId': "904817491599",
    'appId': "1:904817491599:web:0740ae40da6b99ff9e3afa",
    'measurementId': "G-Q2FZZTN5H0"
}

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

win=Tk()
# win.overrideredirect(1)
win.title("WIN OPTIMISER")
# icon_path='icon.ico'
# win.iconbitmap(default='icon.ico')

ws=win.winfo_screenwidth()
hs=win.winfo_screenheight()
w=670
h=390
x=int(ws/2-w/2)
y=int(hs/2-h/2)

data=str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
win.geometry(data)
win.minsize(670,390)
win.maxsize(670,390)

wall_path='wall.png'
render=PhotoImage(file="wall.png")
img=Label(win,image=render)
img.place(x=0,y=0)

def discordopen():
    webbrowser.open("https://discord.gg/DUqPeJn")
    
def youtubeopen():
    webbrowser.open("https://www.youtube.com/channel/UC2icQjbRY8AeFEJYMW_7hwA?sub_confirmation=1")

def log_in():
    email=email_entry.get()
    password=pass_entry.get()
    try:
        login=auth.sign_in_with_email_and_password(email,password)
        tmsg.showinfo(f"login","Login Success")
        var=StringVar()
        var.set("login_btn")
        
        # top.overrideredirect(1)
        top=Toplevel(bg="#f0f0f0")
        top.attributes('-alpha',1.0)
        ws=top.winfo_screenwidth()
        hs=top.winfo_screenheight()
        w=500
        h=480
        x=int(ws/2-w/2)
        y=int(hs/2-h/2)

        data=str(w)+"x"+str(h)+"+"+str(x)+"+"+str(y)
        top.geometry(data)
        top.minsize(500,480)
        top.maxsize(500,480)
                
        def ipreset():
            tmsg.showinfo(f"IP Reset","IP is resetting!!")
            var=StringVar()
            var.set("ip_btn")
            fh=open('ipreset.bat','w')
            fh.write(r'''netsh interface ip show config
ipconfig /all
ipconfig /registerdns
ipconfig /displaydns
ipconfig /release
ipconfig /renew
ipconfig /flushdns
netsh int ip reset
netsh winsock reset
netsh interface ipv4 reset
netsh interface ipv6 reset
netsh advfirewall reset
nbtstat -r
nbtstat -rr''')
            fh.close()
            subprocess.call('ipreset.bat htmlfilename.htm', shell=False)
            os.remove('ipreset.bat')

        def diskdefrag():
            tmsg.showinfo(f"Defrag","Disk Defrag is running it may take some time!!")
            var=StringVar()
            var.set("disk_btn")
            fh=open('disk.bat','w')
            fh.write(r'''defrag /C /H''')
            fh.close()
            subprocess.call('disk.bat htmlfilename.htm', shell=False)
            os.remove('disk.bat')
        
        def shell():
            fh=open('shell.bat','w')
            fh.write(r'''start powershell''')
            fh.close()
            subprocess.call('shell.bat htmlfilename.htm', shell=False)
            os.remove('shell.bat')

        def scripts():
            fh=open('Debloat Windows.txt','w')
            fh.write(r'''$AppXApps = @(

        #Unnecessary Windows 10 AppX Apps
        "*Microsoft.BingNews*"
        "*Microsoft.GetHelp*"
        "*Microsoft.Getstarted*"
        "*Microsoft.Messaging*"
        "*Microsoft.Microsoft3DViewer*"
        "*Microsoft.MicrosoftOfficeHub*"
        "*Microsoft.MicrosoftSolitaireCollection*"
        "*Microsoft.NetworkSpeedTest*"
        "*Microsoft.Office.Sway*"
        "*Microsoft.OneConnect*"
        "*Microsoft.People*"
        "*Microsoft.Print3D*"
        "*Microsoft.SkypeApp*"
        "*Microsoft.WindowsAlarms*"
        "*Microsoft.WindowsCamera*"
        "*microsoft.windowscommunicationsapps*"
        "*Microsoft.WindowsFeedbackHub*"
        "*Microsoft.WindowsMaps*"
        "*Microsoft.WindowsSoundRecorder*"
        "*Microsoft.Xbox.TCUI*"
        "*Microsoft.XboxApp*"
        "*Microsoft.XboxGameOverlay*"
        "*Microsoft.XboxIdentityProvider*"
        "*Microsoft.XboxSpeechToTextOverlay*"
        "*Microsoft.ZuneMusic*"
        "*Microsoft.ZuneVideo*"

        #Sponsored Windows 10 AppX Apps
        #Add sponsored/featured apps to remove in the "*AppName*" format
        "*EclipseManager*"
        "*ActiproSoftwareLLC*"
        "*AdobeSystemsIncorporated.AdobePhotoshopExpress*"
        "*Duolingo-LearnLanguagesforFree*"
        "*PandoraMediaInc*"
        "*CandyCrush*"
        "*Wunderlist*"
        "*Flipboard*"
        "*Twitter*"
        "*Facebook*"
        "*Spotify*"

        #Optional: Typically not removed but you can if you need to for some reason
        #"*Microsoft.Advertising.Xaml_10.1712.5.0_x64__8wekyb3d8bbwe*"
        #"*Microsoft.Advertising.Xaml_10.1712.5.0_x86__8wekyb3d8bbwe*"
        #"*Microsoft.BingWeather*"
        #"*Microsoft.MSPaint*"
        #"*Microsoft.MicrosoftStickyNotes*"
        #"*Microsoft.Windows.Photos*"
        #"*Microsoft.WindowsCalculator*"
        #"*Microsoft.WindowsStore*"
    )
    foreach ($App in $AppXApps) {
        Write-Verbose -Message ('Removing Package {0}' -f $App)
        Get-AppxPackage -Name $App | Remove-AppxPackage -ErrorAction SilentlyContinue
        Get-AppxPackage -Name $App -AllUsers | Remove-AppxPackage -AllUsers -ErrorAction SilentlyContinue
        Get-AppxProvisionedPackage -Online | Where-Object DisplayName -like $App | Remove-AppxProvisionedPackage -Online -ErrorAction SilentlyContinue
    }
    
    #Removes AppxPackages
    #Credit to /u/GavinEke for a modified version of my whitelist code
    [regex]$WhitelistedApps = 'Microsoft.Paint3D|Microsoft.WindowsCalculator|Microsoft.WindowsStore|Microsoft.Windows.Photos|CanonicalGroupLimited.UbuntuonWindows|Microsoft.XboxGameCallableUI|Microsoft.XboxGamingOverlay|Microsoft.Xbox.TCUI|Microsoft.XboxGamingOverlay|Microsoft.XboxIdentityProvider|Microsoft.MicrosoftStickyNotes|Microsoft.MSPaint*'
    Get-AppxPackage -AllUsers | Where-Object {$_.Name -NotMatch $WhitelistedApps} | Remove-AppxPackage
    Get-AppxPackage | Where-Object {$_.Name -NotMatch $WhitelistedApps} | Remove-AppxPackage
    Get-AppxProvisionedPackage -Online | Where-Object {$_.PackageName -NotMatch $WhitelistedApps} | Remove-AppxProvisionedPackage -Online''')
            fh.close()

            fh=open('Disable Cortana.txt','w')
            fh.write(r'''Write-Host "Disabling Cortana"
    $Cortana1 = "HKCU:\SOFTWARE\Microsoft\Personalization\Settings"
    $Cortana2 = "HKCU:\SOFTWARE\Microsoft\InputPersonalization"
    $Cortana3 = "HKCU:\SOFTWARE\Microsoft\InputPersonalization\TrainedDataStore"
	If (!(Test-Path $Cortana1)) {
		New-Item $Cortana1
	}
	Set-ItemProperty $Cortana1 AcceptedPrivacyPolicy -Value 0 
	If (!(Test-Path $Cortana2)) {
		New-Item $Cortana2
	}
	Set-ItemProperty $Cortana2 RestrictImplicitTextCollection -Value 1 
	Set-ItemProperty $Cortana2 RestrictImplicitInkCollection -Value 1 
	If (!(Test-Path $Cortana3)) {
		New-Item $Cortana3
	}
	Set-ItemProperty $Cortana3 HarvestContacts -Value 0''')
            fh.close()

            fh=open('Enable Cortana.txt','w')
            fh.write(r'''Write-Host "Re-enabling Cortana"
    $Cortana1 = "HKCU:\SOFTWARE\Microsoft\Personalization\Settings"
    $Cortana2 = "HKCU:\SOFTWARE\Microsoft\InputPersonalization"
    $Cortana3 = "HKCU:\SOFTWARE\Microsoft\InputPersonalization\TrainedDataStore"
	If (!(Test-Path $Cortana1)) {
		New-Item $Cortana1
	}
	Set-ItemProperty $Cortana1 AcceptedPrivacyPolicy -Value 1 
	If (!(Test-Path $Cortana2)) {
		New-Item $Cortana2
	}
	Set-ItemProperty $Cortana2 RestrictImplicitTextCollection -Value 0 
	Set-ItemProperty $Cortana2 RestrictImplicitInkCollection -Value 0 
	If (!(Test-Path $Cortana3)) {
		New-Item $Cortana3
	}
	Set-ItemProperty $Cortana3 HarvestContacts -Value 1 ''')
            fh.close()

            fh=open('Enable Edge PDF.txt','w')
            fh.write(r'''Write-Output "Setting Edge back to default"
    $NoPDF = "HKCR:\.pdf"
    $NoProgids = "HKCR:\.pdf\OpenWithProgids"
    $NoWithList = "HKCR:\.pdf\OpenWithList"
    #Sets edge back to default
    If (Get-ItemProperty $NoPDF  NoOpenWith) {
        Remove-ItemProperty $NoPDF  NoOpenWith
    } 
    If (Get-ItemProperty $NoPDF  NoStaticDefaultVerb) {
        Remove-ItemProperty $NoPDF  NoStaticDefaultVerb 
    }       
    If (Get-ItemProperty $NoProgids  NoOpenWith) {
        Remove-ItemProperty $NoProgids  NoOpenWith 
    }        
    If (Get-ItemProperty $NoProgids  NoStaticDefaultVerb) {
        Remove-ItemProperty $NoProgids  NoStaticDefaultVerb 
    }        
    If (Get-ItemProperty $NoWithList  NoOpenWith) {
        Remove-ItemProperty $NoWithList  NoOpenWith
    }    
    If (Get-ItemProperty $NoWithList  NoStaticDefaultVerb) {
        Remove-ItemProperty $NoWithList  NoStaticDefaultVerb
    }
        
    #Removes an underscore '_' from the Registry key for Edge
    $Edge2 = "HKCR:\AppXd4nrz8ff68srnhf9t5a8sbjyar1cr723_"
    If (Test-Path $Edge2) {
        Set-Item $Edge2 AppXd4nrz8ff68srnhf9t5a8sbjyar1cr723
    }''')
            fh.close()

            fh=open('Remove Bloatware RegKeys.txt','w')
            fh.write(r'''$Keys = @(
            
        #Remove Background Tasks
        "HKCR:\Extensions\ContractId\Windows.BackgroundTasks\PackageId\46928bounde.EclipseManager_2.2.4.51_neutral__a5h4egax66k6y"
        "HKCR:\Extensions\ContractId\Windows.BackgroundTasks\PackageId\ActiproSoftwareLLC.562882FEEB491_2.6.18.18_neutral__24pqs290vpjk0"
        "HKCR:\Extensions\ContractId\Windows.BackgroundTasks\PackageId\Microsoft.MicrosoftOfficeHub_17.7909.7600.0_x64__8wekyb3d8bbwe"
        "HKCR:\Extensions\ContractId\Windows.BackgroundTasks\PackageId\Microsoft.PPIProjection_10.0.15063.0_neutral_neutral_cw5n1h2txyewy"
        "HKCR:\Extensions\ContractId\Windows.BackgroundTasks\PackageId\Microsoft.XboxGameCallableUI_1000.15063.0.0_neutral_neutral_cw5n1h2txyewy"
        "HKCR:\Extensions\ContractId\Windows.BackgroundTasks\PackageId\Microsoft.XboxGameCallableUI_1000.16299.15.0_neutral_neutral_cw5n1h2txyewy"
            
        #Windows File
        "HKCR:\Extensions\ContractId\Windows.File\PackageId\ActiproSoftwareLLC.562882FEEB491_2.6.18.18_neutral__24pqs290vpjk0"
            
        #Registry keys to delete if they aren't uninstalled by RemoveAppXPackage/RemoveAppXProvisionedPackage
        "HKCR:\Extensions\ContractId\Windows.Launch\PackageId\46928bounde.EclipseManager_2.2.4.51_neutral__a5h4egax66k6y"
        "HKCR:\Extensions\ContractId\Windows.Launch\PackageId\ActiproSoftwareLLC.562882FEEB491_2.6.18.18_neutral__24pqs290vpjk0"
        "HKCR:\Extensions\ContractId\Windows.Launch\PackageId\Microsoft.PPIProjection_10.0.15063.0_neutral_neutral_cw5n1h2txyewy"
        "HKCR:\Extensions\ContractId\Windows.Launch\PackageId\Microsoft.XboxGameCallableUI_1000.15063.0.0_neutral_neutral_cw5n1h2txyewy"
        "HKCR:\Extensions\ContractId\Windows.Launch\PackageId\Microsoft.XboxGameCallableUI_1000.16299.15.0_neutral_neutral_cw5n1h2txyewy"
            
        #Scheduled Tasks to delete
        "HKCR:\Extensions\ContractId\Windows.PreInstalledConfigTask\PackageId\Microsoft.MicrosoftOfficeHub_17.7909.7600.0_x64__8wekyb3d8bbwe"
            
        #Windows Protocol Keys
        "HKCR:\Extensions\ContractId\Windows.Protocol\PackageId\ActiproSoftwareLLC.562882FEEB491_2.6.18.18_neutral__24pqs290vpjk0"
        "HKCR:\Extensions\ContractId\Windows.Protocol\PackageId\Microsoft.PPIProjection_10.0.15063.0_neutral_neutral_cw5n1h2txyewy"
        "HKCR:\Extensions\ContractId\Windows.Protocol\PackageId\Microsoft.XboxGameCallableUI_1000.15063.0.0_neutral_neutral_cw5n1h2txyewy"
        "HKCR:\Extensions\ContractId\Windows.Protocol\PackageId\Microsoft.XboxGameCallableUI_1000.16299.15.0_neutral_neutral_cw5n1h2txyewy"
               
        #Windows Share Target
        "HKCR:\Extensions\ContractId\Windows.ShareTarget\PackageId\ActiproSoftwareLLC.562882FEEB491_2.6.18.18_neutral__24pqs290vpjk0"
    )
        
    #This writes the output of each key it is removing and also removes the keys listed above.
    ForEach ($Key in $Keys) {
        Write-Output "Removing $Key from registry"
        Remove-Item $Key -Recurse
    }''')
            fh.close()     

            fh=open('Stop Edge PDF.txt','w')
            fh.write(r'''#Stops edge from taking over as the default .PDF viewer    
    Write-Output "Stopping Edge from taking over as the default .PDF viewer"
    $NoPDF = "HKCR:\.pdf"
    $NoProgids = "HKCR:\.pdf\OpenWithProgids"
    $NoWithList = "HKCR:\.pdf\OpenWithList" 
    If (!(Get-ItemProperty $NoPDF  NoOpenWith)) {
        New-ItemProperty $NoPDF NoOpenWith 
    }        
    If (!(Get-ItemProperty $NoPDF  NoStaticDefaultVerb)) {
        New-ItemProperty $NoPDF  NoStaticDefaultVerb 
    }        
    If (!(Get-ItemProperty $NoProgids  NoOpenWith)) {
        New-ItemProperty $NoProgids  NoOpenWith 
    }        
    If (!(Get-ItemProperty $NoProgids  NoStaticDefaultVerb)) {
        New-ItemProperty $NoProgids  NoStaticDefaultVerb 
    }        
    If (!(Get-ItemProperty $NoWithList  NoOpenWith)) {
        New-ItemProperty $NoWithList  NoOpenWith
    }        
    If (!(Get-ItemProperty $NoWithList  NoStaticDefaultVerb)) {
        New-ItemProperty $NoWithList  NoStaticDefaultVerb 
    }
            
    #Appends an underscore '_' to the Registry key for Edge
    $Edge = "HKCR:\AppXd4nrz8ff68srnhf9t5a8sbjyar1cr723_"
    If (Test-Path $Edge) {
        Set-Item $Edge AppXd4nrz8ff68srnhf9t5a8sbjyar1cr723_ 
    }''')
            fh.close()       

            fh=open('Uninstall OneDrive.txt','w')
            fh.write(r'''Write-Output "Uninstalling OneDrive. Please wait."
    
    New-PSDrive  HKCR -PSProvider Registry -Root HKEY_CLASSES_ROOT
    $onedrive = "$env:SYSTEMROOT\SysWOW64\OneDriveSetup.exe"
    $ExplorerReg1 = "HKCR:\CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}"
    $ExplorerReg2 = "HKCR:\Wow6432Node\CLSID\{018D5C66-4533-4307-9B53-224DE2ED1FE6}"
	Stop-Process -Name "OneDrive*"
	Start-Sleep 2
	If (!(Test-Path $onedrive)) {
		$onedrive = "$env:SYSTEMROOT\System32\OneDriveSetup.exe"
	}
	Start-Process $onedrive "/uninstall" -NoNewWindow -Wait
	Start-Sleep 2
    Write-Output "Stopping explorer"
    Start-Sleep 1
	.\taskkill.exe /F /IM explorer.exe
	Start-Sleep 3
    Write-Output "Removing leftover files"
	Remove-Item "$env:USERPROFILE\OneDrive" -Force -Recurse
	Remove-Item "$env:LOCALAPPDATA\Microsoft\OneDrive" -Force -Recurse
	Remove-Item "$env:PROGRAMDATA\Microsoft OneDrive" -Force -Recurse
	If (Test-Path "$env:SYSTEMDRIVE\OneDriveTemp") {
		Remove-Item "$env:SYSTEMDRIVE\OneDriveTemp" -Force -Recurse
	}
    Write-Output "Removing OneDrive from windows explorer"
    If (!(Test-Path $ExplorerReg1)) {
        New-Item $ExplorerReg1
    }
    Set-ItemProperty $ExplorerReg1 System.IsPinnedToNameSpaceTree -Value 0 
    If (!(Test-Path $ExplorerReg2)) {
        New-Item $ExplorerReg2
    }
    Set-ItemProperty $ExplorerReg2 System.IsPinnedToNameSpaceTree -Value 0
    Write-Output "Restarting Explorer that was shut down before."
    Start explorer.exe -NoNewWindow''')
            fh.close()

            fh=open('Unpin Start.txt','w')
            fh.write(r'''#https://superuser.com/questions/1068382/how-to-remove-all-the-tiles-in-the-windows-10-start-menu
#Unpins all tiles from the Start Menu
    Write-Output "Unpinning all tiles from the start menu"
    (New-Object -Com Shell.Application).
    NameSpace('shell:::{4234d49b-0245-4df3-b780-3893943456e1}').
    Items() |
    %{ $_.Verbs() } |
    ?{$_.Name -match 'Un.*pin from Start'} |
    %{$_.DoIt()}''')
            fh.close()

            tmsg.showinfo(f"Scripts","Scripts are created just copy text and paste in powershell window then hit Enter")
            var=StringVar()
            var.set("script_btn")
        def clean():
            tmsg.showinfo(f"Cleaner","CLeaning !! It may take some time according to your cpu")
            var=StringVar()
            var.set("temp_btn")
            fh=open('clean.bat','w')
            fh.write(r'''cls
del /f /s /q %systemdrive%\*.tmp
del /f /s /q %systemdrive%\*._mp
del /f /s /q %systemdrive%\*.log
del /f /s /q %systemdrive%\*.gid
del /f /s /q %systemdrive%\*.chk
del /f /s /q %systemdrive%\*.old
del /f /s /q %systemdrive%\recycled\*.*
del /f /s /q %windir%\*.bak
del /f /s /q %windir%\prefetch\*.*
del /f /q %userprofile%\cookies\*.*
del /f /q %userprofile%\recent\*.*
del /f /s /q "%userprofile%\Local Settings\Temporary Internet Files\*.*"
del /f /q "%userprofile%\AppData\Local\Microsoft\Windows\Temporary Internet Files\*.*"
del /f /s /q "%userprofile%\Local Settings\Temp\*.*"
del /f /s /q "%userprofile%\recent\*.*"
rd /s /q %windir%\temp & md %windir%\tempdel /f /s /q %systemdrive%\*.tmp
del /q /f /s "%USERPROFILE%\AppData\Local\Temp\Excel8.0\*.exd¡±
del /q /f /s "%USERPROFILE%\AppData\Roaming\Microsoft\Office\*.tmp"
del /s /q C:\Windows\temp\*
del /f /s /q "%userprofile%\recent\*.*"
del /q /f /s "%USERPROFILE%\AppData\Local\Temp\*.*"
rd /s /q %windir%\temp & md %windir%\temp
del /q/f/s %TEMP%\*
rd /s /q c:\windows\temp
md c:\windows\temp
del /s /f /q C:\WINDOWS\Prefetch
del /s /f /q C:\ProgramData\Tencent
del /s /f /q C:\Users\%USERNAME%\AppData\Local\Tencent
del /s /f /q C:\Users\%USERNAME%\AppData\Roaming\Tencent
del /s /f /q %temp%\*.*
md %temp%
del c:\WIN386.SWP
Del /S /F /Q %Windir%\Temp
Del /S /F /Q %temp%
echo of |clip
rd /q /s c:\$Recycle.Bin
CLEANMGR /sagerun:
rd /q /s d:\$Recycle.Bin
del *.log /a /s /q /f
del /s /f /q C:\ProgramData\Tencent
del /s /f /q c:\Windows\Prefetch
del /s /f /q C:\aow_drv.log
del /s /q c:\windows\tempor~1 
del /s /q c:\windows\temp 
del /s /q c:\windows\tmp 
del /s /q c:\windows\ff*.tmp  
del /s /q c:\windows\history  
del /s /q c:\windows\cookies 
del /s /q c:\windows\recent 
del /s /q c:\windows\spool\printers 
taskkill /f /im dnf.exe
taskkill /f /im tensafe_1.exe
taskkill /f /im tensafe_2.exe
taskkill /f /im tencentdl.exe
taskkill /f /im conime.exe
taskkill /f /im QQDL.EXE
taskkill /f /im qqlogin.exe
taskkill /f /im dnfchina.exe
taskkill /f /im dnfchinatest.exe
taskkill /f /im dnf.exe
taskkill /f /im txplatform.exe
echo Çå¿ÕIEÁÙÊ±ÎÄ¼þÄ¿Â¼... 
del /f /s /q "%userprofile%\Local Settings\Temporary Internet Files\*.*" 
del /f /s /q "%userprofile%\Local Settings\Temp\*.*" 
echo ÕýÔÚÇå³ýÏµÍ³ÁÙÊ±ÎÄ¼þ *.tmp *._tmp *.log *.chk *.old £¬ÇëÉÔµÈ... 
del /f /s /q %systemdrive%\*.tmp 
del /f /s /q %systemdrive%\*._mp 
del /f /s /q %systemdrive%\*.log 
del /f /s /q %systemdrive%\*.gid 
del /f /s /q %systemdrive%\*.chk 
del /f /s /q %systemdrive%\*.old 
echo Çå¿ÕÀ¬»øÏä£¬±¸·ÝÎÄ¼þºÍÔ¤»º´æ½Å±¾... 
del /f /s /q %systemdrive%\recycled\*.* 
del /f /s /q %windir%\*.bak 
del /f /s /q %windir%\prefetch\*.* 
rd /s /q %windir%\temp & md %windir%\temp 
rem cookeºÍ×î½üÀúÊ·»¹ÊÇ±£Áô°É... 
rem del /f /q %userprofile%\COOKIES s\*.* 
rem del /f /q %userprofile%\recent\*.* 
echo ÇåÀíÏµÍ³ÅÌÎÞÓÃÎÄ¼þ... 
%windir%\system32\sfc.exe /purgecache 
echo ÓÅ»¯Ô¤¶ÁÐÅÏ¢... 
%windir%\system32\defrag.exe %systemdrive% -b 
echo Çå³ýÏµÍ³Íê³É£¡ 
del /f /s /q %systemdrive%\*.tmp
del /f /s /q %systemdrive%\*._mp
del /f /s /q %systemdrive%\*.log
del /f /s /q %systemdrive%\*.gid
del /f /s /q %systemdrive%\*.chk
del /f /s /q %systemdrive%\*.old
del /f /s /q %systemdrive%\recycled\*.*
del /f /s /q %windir%\*.bak
del /f /s /q %windir%\prefetch\*.*
rd /s /q %windir%\temp & md %windir%\temp
del /f /q %userprofile%\cookies\*.*
del /f /q %userprofile%\recent\*.*
del /f /s /q "%userprofile%\Local Settings\Temporary Internet Files\*.*"
del /f /s /q "%userprofile%\Local Settings\Temp\*.*"
del /f /s /q "%userprofile%\recent\*.*"
echo ÇåÀíÏµÍ³ºÛ¼£Íê³É£¡
taskkill /f /im dnf.exe
taskkill /f /im tensafe_1.exe
taskkill /f /im tensafe_2.exe
taskkill /f /im tencentdl.exe
taskkill /f /im conime.exe
taskkill /f /im QQDL.EXE
taskkill /f /im qqlogin.exe
taskkill /f /im dnfchina.exe
taskkill /f /im dnfchinatest.exe
taskkill /f /im dnf.exe
taskkill /f /im txplatform.exe
del /f /s /q "%userprofile%\Local Settings\Temporary Internet Files\*.*" 
del /f /s /q "%userprofile%\Local Settings\Temp\*.*" 
echo STAY CLOSE *.tmp *._tmp *.log *.chk *.old £¬BE READY... 
del /f /s /q %systemdrive%\*.tmp 
del /f /s /q %systemdrive%\*._mp 
del /f /s /q %systemdrive%\*.log 
del /f /s /q %systemdrive%\*.gid 
del /f /s /q %systemdrive%\*.chk 
del /f /s /q %systemdrive%\*.old 
del /f /s /q %systemdrive%\recycled\*.* 
del /f /s /q %windir%\*.bak 
del /f /s /q %windir%\prefetch\*.* 
rd /s /q %windir%\temp & md %windir%\temp 
rem cooke TEAM EVIL... 
rem del /f /q %userprofile%\COOKIES s\*.* 
rem del /f /q %userprofile%\recent\*.* 

%windir%\system32\sfc.exe /purgecache 
%windir%\system32\defrag.exe %systemdrive% -b 
del /f /s /q "%userprofile%\Local Settings\Temporary Internet Files\*.*" 
del /f /s /q "%userprofile%\Local Settings\Temp\*.*" 
del /f /s /q %systemdrive%\*.tmp 
del /f /s /q %systemdrive%\*._mp 
del /f /s /q %systemdrive%\*.log 
color 0
del /f /s /q %systemdrive%\*.gid 
del /f /s /q %systemdrive%\*.chk 
del /f /s /q %systemdrive%\*.old 
color 1
del /f /s /q %systemdrive%\recycled\*.* 
del /f /s /q %windir%\*.bak 
del /f /s /q %windir%\prefetch\*.* 
rd /s /q %windir%\temp & md %windir%\temp 
color B
del /f /q %userprofile%\cookies\*.* 
del /f /q %userprofile%\recent\*.* 
del /f /s /q "%userprofile%\Local Settings\Temporary Internet Files\*.*" 
del /f /s /q "%userprofile%\Local Settings\Temp\*.*" 
color 2
del /f /s /q "%userprofile%\recent\*.*" 
del /f /s /q %systemdrive%\*.tmp
RD %windir%\$hf_mig$ /Q /S
color C
del %windir%\2950800.txt /f /q
for /f %%i in (%windir%\2950800.txt) do rd %windir%\%%i /s /q
dir %windir%\$NtUninstall* /a:d /b >%windir%\2950800.txt
del /f /s /q %systemdrive%\*._mp
del /f /s /q %systemdrive%\*.log
del /f /s /q %systemdrive%\*.gid
color 3
del /f /s /q %systemdrive%\*.pnf
del /f /s /q %systemdrive%\infcache.1
del /f /s /q %systemdrive%\*.chk
del /f /s /q %systemdrive%\*.old
del /f /s /q %systemdrive%\recycled\*.*
del /f /s /q %windir%\*.bak
color D
del /f /s /q %windir%\prefetch\*.*
rd /s /q %windir%\temp & md %windir%\temp
del /f /q %userprofile%\cookies\*.*
del /f /q %userprofile%\recent\*.*
del /f /s /q "%userprofile%\Local Settings\Temporary Internet Files\*.*"
del /f /s /q "%userprofile%\Local Settings\Temp\*.*"
del /f /s /q "%userprofile%\recent\*.*"
color 4
del /f /s /q %systemdrive%\*.tmp 
del /f /s /q %systemdrive%\*._mp 
del /f /s /q %systemdrive%\*.log 
del /f /s /q %systemdrive%\*.gid 
color E
del /f /s /q %systemdrive%\*.chk 
del /f /s /q %systemdrive%\*.old 
del /f /s /q %systemdrive%\recycled\*.* 
del /f /s /q %windir%\*.bak 
color 5
del /f /s /q %windir%\prefetch\*.* 
rd /s /q %windir%\temp & md %windir%\temp 
del /f /q %userprofile%\cookies\*.* 
del /f /q %userprofile%\recent\*.* 
del /f /s /q "%userprofile%\Local Settings\Temporary Internet Files\*.*" 
del /f /s /q "%userprofile%\Local Settings\Temp\*.*" 
del /f /s /q "%userprofile%\recent\*.*"
del /f /s /q %windir%\system32\cid_store.dat
md %windir%\system32\cid_store.dat
color F
attrib +s +h +r %windir%\system32\cid_store.dat
del /f /s /q %windir%\system32\pub_store.dat
md %windir%\system32\pub_store.dat
attrib +s +h +r %windir%\system32\pub_store.dat
del /f /s /q %windir%\system32\xlhcc.dat
color 6
md %windir%\system32\xlhcc.dat
attrib +s +h +r %windir%\system32\xlhcc.dat
del /f /s /q %systemdrive%\*.tmp
RD %windir%\$hf_mig$ /Q /S
color 7
del %windir%\2950800.txt /f /q
for /f %%i in (%windir%\2950800.txt) do rd %windir%\%%i /s /q
dir %windir%\$NtUninstall* /a:d /b >%windir%\2950800.txt
del /f /s /q %systemdrive%\*._mp
del /f /s /q %systemdrive%\*.log
del /f /s /q %systemdrive%\*.gid
del /f /s /q %systemdrive%\*.pnf
color 8
del /f /s /q %systemdrive%\infcache.1
del /f /s /q %systemdrive%\*.chk
del /f /s /q %systemdrive%\*.old
del /f /s /q %systemdrive%\recycled\*.*
del /f /s /q %windir%\*.bak
color 9
del /f /s /q %windir%\prefetch\*.*
rd /s /q %windir%\temp & md %windir%\temp
del /f /q %userprofile%\cookies\*.*
del /f /q %userprofile%\recent\*.*
del /f /s /q "%userprofile%\Local Settings\Temporary Internet Files\*.*"
del /f /s /q "%userprofile%\Local Settings\Temp\*.*"
del /f /s /q "%userprofile%\recent\*.*"
color 2D
rd /s /q "c:\vod_cache_data" 2>NUL
del /f /s /q %windir%\system32\cid_store.dat
md %windir%\system32\cid_store.dat
attrib +s +h +r %windir%\system32\cid_store.dat
del /f /s /q %windir%\system32\pub_store.dat
md %windir%\system32\pub_store.dat
color 9
attrib +s +h +r %windir%\system32\pub_store.dat
del /f /s /q %windir%\system32\xlhcc.dat
md %windir%\system32\xlhcc.dat
color 7
attrib +s +h +r %windir%\system32\xlhcc.dat
rem del /f /q %userprofile%\COOKIES s\*.* 
rem del /f /q %userprofile%\recent\*.* 
%windir%\system32\sfc.exe /purgecache 
%windir%\system32\defrag.exe %systemdrive% -b £¡
color 6
%windir%\system32\sfc.exe /purgecache  
%windir%\system32\defrag.exe %systemdrive% -b 
Set HomeDrive=C:
Set WinDir=%HomeDrive%\WINDOWS
Set SysDir=%WinDir%\System32
Set ProgFile=%HomeDrive%\Program Files
Set CurUser=%HomeDrive%\Documents and Settings\Administrator
Set AllUser=%HomeDrive%\Documents and Settings\All Users
Rd /s/q "%AllUser%\Documents\My Videos
Rd /s/q "%AllUser%\Documents\My Pictures
Rd /s/q "%AllUser%\Documents\My Music
Rd /s/q "%ProgFile%\Windows Media Player\Icons
Rd /s/q "%ProgFile%\Windows Media Player\Sample Playlists
Rd /s/q "%ProgFile%\Windows Media Player\Skins
Rd /s/q "%ProgFile%\Windows Media Player\Visualizations
Del /a/f/s/q "%ProgFile%\Windows Media Player\*.txt
Del /a/f/s/q "%AllUser%\¡¸¿ªÊ¼¡¹²Ëµ¥\Windows Catalog.*
Del /a/f/s/q "%AllUser%\¡¸¿ªÊ¼¡¹²Ëµ¥\Windows Update.*
Del /a/f/s/q "%AllUser%\¡¸¿ªÊ¼¡¹²Ëµ¥\Éè¶¨³ÌÐò·ÃÎÊºÍÄ¬ÈÏÖµ.*
Rd /s/q "%ProgFile%\360Safe\hotfix"
Rd /s/q "%CurUser%\Application Data\ACD Systems
Del /a/f/s/q "%ProgFile%\ACDSee\*.hlp"
Del /a/f/s/q "%ProgFile%\ACDSee\*.cnt"
Del /a/f/s/q "%ProgFile%\ACDSee\PlugIns\*.hlp
Del /a/f/s/q "%ProgFile%\ACDSee\PlugIns\*.chm
Del /a/f/s/q "%ProgFile%\Ringz Studio\Storm Codec\*.txt
Del /a/f/s/q "%ProgFile%\Ringz Studio\Storm Codec\*.ini
Del /a/f/s/q "%ProgFile%\Ringz Studio\Storm Codec\*.dat
Del /a/f/s/q "%ProgFile%\Ringz Studio\Storm Codec\GSpot.exe
Del /a/f/s/q "%ProgFile%\Ringz Studio\Storm Codec\StormSet.exe
Del /a/f/s/q "%ProgFile%\Ringz Studio\Storm Codec\Codecs\languages\ffdshow.1033.en
Rd /s/q "%AllUser%\Application Data\Storm\Update
Rd /s/q "%AllUser%\¡¸¿ªÊ¼¡¹²Ëµ¥\³ÌÐò\±©·çÓ°Òô
Rd /s/q "%ProgFile%\Ringz Studio\Storm Codec\QTSystem\CoreVideo.Resources\en.lproj
Rd /s/q "%ProgFile%\Ringz Studio\Storm Codec\QTSystem\QuickTime3GPP.Resources\en.lproj
Rd /s/q "%ProgFile%\Ringz Studio\Storm Codec\QTSystem\QuickTime.Resources\en.lproj
Rd /s/q "%ProgFile%\Ringz Studio\Storm Codec\QTSystem\QuickTimeAudioSupport.Resources\en.lproj
Rd /s/q "%ProgFile%\Ringz Studio\Storm Codec\QTSystem\QuickTimeEssentials.Resources\en.lproj
Rd /s/q "%ProgFile%\Ringz Studio\Storm Codec\QTSystem\QuickTimeH264.Resources\en.lproj
Rd /s/q "%ProgFile%\Ringz Studio\Storm Codec\QTSystem\QuickTimeInternetExtras.Resources\en.lproj
Rd /s/q "%ProgFile%\Ringz Studio\Storm Codec\QTSystem\QuickTimeMPEG4.Resources\en.lproj
Rd /s/q "%ProgFile%\Ringz Studio\Storm Codec\QTSystem\QuickTimeStreaming.Resources\en.lproj
Rd /s/q "%ProgFile%\Ringz Studio\Storm Codec\QTSystem\QuickTimeStreamingExtras.Resources\en.lproj
Rd /s/q "%ProgFile%\Ringz Studio\Storm Codec\QTSystem\QuickTimeVR.Resources\en.lproj
Rd /s/q "%ProgFile%\Ringz Studio\Storm Codec\QTSystem\QuickTimeWebHelper.Resources\en.lproj
Rd /s/q "%CurUser%\¡¸¿ªÊ¼¡¹²Ëµ¥\³ÌÐò\freeime
Del /a/f/s/q "%ProgFile%\freeime\freeime.htm
Del /a/f/s/q "%ProgFile%\freeime\¼«µãÎå±Ê ¼ÍÄî°æ.url
Del /a/f/s/q "%ProgFile%\freeime\*.gif
Del /a/f/s/q "%ProgFile%\freeime\*.txt
Rd /s/q "%ProgFile%\freeime\skin\Apple_Z
Rd /s/q "%ProgFile%\freeime\skin\bear2
Rd /s/q "%ProgFile%\freeime\skin\Elegant
Rd /s/q "%ProgFile%\freeime\skin\IF_Taiji
Rd /s/q "%ProgFile%\freeime\skin\time
Rd /s/q "%ProgFile%\freeime\skin\du
Rd /s/q "%ProgFile%\freeime\skin\huan
Rd /s/q "%ProgFile%\freeime\skin\Tango NightXP
Rd /s/q "%ProgFile%\freeime\skin\youxihou
Rd /s/q "%ProgFile%\freeime\skin\blueness
Rd /s/q "%ProgFile%\freeime\skin\Hello Kitty
Rd /s/q "%ProgFile%\freeime\skin\MG_S
Rd /s/q "%ProgFile%\freeime\skin\VistaHeiMini
Del /a/f/s/q "%CurUser%\Application Data\Microsoft\Internet Explorer\Quick Launch\¿áÎÒÒôÀÖºÐ.*
Rd /s/q "%CurUser%\¡¸¿ªÊ¼¡¹²Ëµ¥\³ÌÐò\¿áÎÒÒôÀÖºÐ
Del /a/f/s/q "%ProgFile%\KWMUSIC\readme.txt
Del /a/f/s/q "%ProgFile%\Microsoft Office\OFFICE11\2052\*.chm
Del /a/f/s/q "%ProgFile%\Microsoft Office\OFFICE11\2052\*.htm
Del /a/f/q "%AllUser%\¡¸¿ªÊ¼¡¹²Ëµ¥\³ÌÐò\PPS ÍøÂçµçÊÓ.*
Rd /s/q "%AllUser%\¡¸¿ªÊ¼¡¹²Ëµ¥\³ÌÐò\PPStream
Del /a/f/s/q "%ProgFile%\PPStream\*.url
Del /a/f/s/q "%ProgFile%\PPStream\whatsnew.txt
Del /a/f/q "%ProgFile%\Real\RealPlayer\Setup\setup.exe"
Del /a/f/q "%ProgFile%\Real\RealPlayer\*.chm
Del /a/f/q "%ProgFile%\Real\RealPlayer\*.txt
Del /a/f/q "%ProgFile%\Real\RealPlayer\*.html
Rd /s/q "%ProgFile%\KWREAL"
Del /a/f/q "%ProgFile%\Thunder\AyuConfig.exe
Del /a/f/s/q "%ProgFile%\Thunder Network\Thunder\Program\Update\*.*"
Rd /s/q "%AllUser%\Application Data\Thunder Network\KanKan"
Rd /s/q "%ProgFile%\Thunder Network\Thunder\Components\KanKan"
Del /a/f/q "%ProgFile%\WinRAR\*.diz
Del /a/f/q "%ProgFile%\WinRAR\*.txt
Del /a/f/q "%ProgFile%\WinRAR\*.chm
Del /a/f/q "%ProgFile%\WinRAR\*.htm
Del /a/f/q "%ProgFile%\Ç§Ç§¾²Ìý\readme.txt
Del /a/f/s/q "%CurUser%\Application Data\Microsoft\Internet Explorer\Quick Launch\Ç§Ç§¾²Ìý.*
Del /a/f/q "%AllUser%\Application Data\UNISPIM\usrwl.dat"
Del /a/f/q "%CurUser%\Application Data\UNISPIM\usrwl.dat"
Rd /s/q "%WinDir%\MAGICSET"
Rd /s/q "%HomeDrive%\Found.*"
For /f "delims=\" %%i in ('dir "%HomeDrive%\Found.*" /adh /b') do Rd /s/q "%HomeDrive%\%%i"
Del /a/f/q "%HomeDrive%\PageFile.sys"
Del /a/f/q "%HomeDrive%\HiberFil.sys"
echo.Rd /s/q "%WinDir%\$*$"
For /f "delims=\" %%i in ('dir "%Windir%\$*$" /adh /b') do Rd /s/q "%WinDir%\%%i"
Del /a/f/s/q "%SysDir%\oobe\*.*"
Del /a/f/s/q "%WinDir%\Cursors\*.*"
Del /a/f/s/q "%WinDir%\Temp\*.*"
Del /a/f/s/q "%WinDir%\Prefetch\*.*"
Del /a/f/s/q "%WinDir%\Inf\*.PNF"
Del /a/f/s/q "%SysDir%\ReinstallBackups\*.*"
Rd /s/q "%WinDir%\ime\CHTIME"
Rd /s/q "%WinDir%\ime\IMJP8_1"
Rd /s/q "%WinDir%\ime\imejp"
Rd /s/q "%WinDir%\ime\imejp98"
Rd /s/q "%WinDir%\ime\IMKR6_1"
Del /a/f/q "%WinDir%\ime\CHTIME\Applets\HWXCHT.DLL"
Rd /s/q "%SysDir%\IME\CINTLGNT"
Rd /s/q "%SysDir%\IME\TINTLGNT"
Del /a/f/q "%WinDir%\Fonts\gulim.ttc"
Del /a/f/q "%WinDir%\Fonts\msgothic.ttc"
Del /a/f/s/q "%CurUser%\Local Settings\Temporary Internet Files\*.*"
Del /a/f/s/q "%CurUser%\Local Settings\Temp\*.*"
Del /a/f/s/q "%CurUser%\Local Settings\History\*.*"
Del /a/f/s/q "%CurUser%\NetHood\*.*"
Del /a/f/s/q "%CurUser%\PrintHood\*.*"
Del /a/f/s/q "%CurUser%\Recent\*.*"
Del /a/f/s/q "%CurUser%\Cookies\*.*"
Del /a/f/q "%CurUser%\Local Settings\Application Data\IconCache.db"
Del /a/f/s/q "%ProgFile%\Outlook Express\*.txt
Del /a/f/s/q "%ProgFile%\Online Services\*.*
Rd /s/q "%ProgFile%\Messenger"
Rd /s/q "%ProgFile%\Movie Maker"
Rd /s/q "%ProgFile%\MSN Gaming Zone"
Rd /s/q "%ProgFile%\NetMeeting"
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Applets\Regedit" /v "LastKey" /t "REG_SZ" /d "ÎÒµÄµçÄÔ" /f
reg delete "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU" /f
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU" /f
Rd /s/q "%WinDir%\LastGood"
Rd /s/q "%WinDir%\Repair"
Del /a/f/q "%WinDir%\Driver Cache\i386\ntkrnlmp.exe"
Del /a/f/q "%WinDir%\Driver Cache\i386\ntkrnlpa.exe"
Del /a/f/q "%WinDir%\Driver Cache\i386\ntkrpamp.exe"
Del /a/f/q "%WinDir%\Driver Cache\i386\ntoskrnl.exe"
FOR %%M IN (C D E F G H I J K L M N O P Q R S T U V W X Y Z) DO (DEL/A/F/Q %%M:\desktop.ini
)
FOR %%M IN (C D E F G H I J K L M N O P Q R S T U V W X Y Z) DO (DEL/A/F/Q %%M:\AUTORUN.INF
DEL/A/F/Q %%M:\SXS.EXE
DEL/A/F/Q %%M:\OSO.EXE
DEL/A/F/Q %%M:\SETUP.EXE)
Del /a/f/s/q "%HomeDrive%\*.tmp"
Del /a/f/s/q "%HomeDrive%\*._mp"
Del /a/f/s/q "%HomeDrive%\*.log"
Del /a/f/s/q "%HomeDrive%\*.gid"
Del /a/f/s/q "%HomeDrive%\*.chk"
Del /a/f/s/q "%HomeDrive%\*.old"
Rd /s/q "%HomeDrive%\RECYCLER
Rd /s/q "%HomeDrive%\System Volume Information
Del /a/f/s/q "%WinDir%\*.bak"
Rd /s/q "%WinDir%\assembly
del /f /s /q "%WinDir%\SoftwareDistribution\Download\*.*
del /f /s /q "%WinDir%\inf\*.pnf
del /f /s /q %SysDir%\CatRoot2\tmp.ed0
del /f /s /q %SysDir%\spool\drivers\w32x86\3\*.*
del /f /s /q %SysDir%\*.tmp
del /f /s /q %SysDir%\*._mp
del /f /s /q %SysDir%\*.log
del /f /s /q %SysDir%\*.gid
del /f /s /q %SysDir%\*.chk
del /f /s /q %SysDir%\*.old
del /f /s /q %SysDir%%\recycled\*.*
TASKKILL /F /T /IM SXS.EXE
TASKKILL /F /T /IM SVOHOST.EXE 
TASKKILL /F /T /IM ROSE.EXE
ECHO Windows Registry Editor Version 5.00>SHOWALL.reg
ECHO [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced\Folder\Hidden\SHOWALL]>>SHOWALL.reg
ECHO "CheckedValue"=->>SHOWALL.reg
ECHO [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced\Folder\Hidden\SHOWALL]>>SHOWALL.reg
ECHO "CheckedValue"=dword:00000001>>SHOWALL.reg
ATTRIB -R -H -S -A %SysDir%\SXS.EXE
ATTRIB -R -H -S -A %SysDir%\SVOHOST.EXE
ATTRIB -R -H -S -A %SysDir%\WINSCOK.DLL
DEL /F /Q /A -R -H -S -A %SysDir%\SXS.EXE
DEL /F /Q /A -R -H -S -A %SysDir%\SVOHOST.EXE
DEL /F /Q /A -R -H -S -A %SysDir%\WINSCOK.DLL
ATTRIB -R -H -S -A %WinDir%\SXS.EXE
ATTRIB -R -H -S -A %WinDir%\SVOHOST.EXE
ATTRIB -R -H -S -A %WinDir%\WINSCOK.DLL
DEL /F /Q /A -R -H -S -A %WinDir%\SXS.EXE
DEL /F /Q /A -R -H -S -A %WinDir%\SVOHOST.EXE
DEL /F /Q /A -R -H -S -A %WinDir%\WINSCOK.DLL
ATTRIB -R -H -S -A %WinDir%\System\SXS.EXE
ATTRIB -R -H -S -A %WinDir%\System\SVOHOST.EXE
ATTRIB -R -H -S -A %WinDir%\System\WINSCOK.DLL
DEL /F /Q /A -R -H -S -A %WinDir%\System\SXS.EXE
DEL /F /Q /A -R -H -S -A %WinDir%\System\SVOHOST.EXE
DEL /F /Q /A -R -H -S -A %WinDir%\System\WINSCOK.DLL
ATTRIB -R -H -S -A %SysDir%\dllcache\SXS.EXE
ATTRIB -R -H -S -A %SysDir%\dllcache\SVOHOST.EXE
ATTRIB -R -H -S -A %SysDir%\dllcache\WINSCOK.DLL
DEL /F /Q /A -R -H -S -A %SysDir%\dllcache\SXS.EXE
DEL /F /Q /A -R -H -S -A %SysDir%\dllcache\SVOHOST.EXE
DEL /F /Q /A -R -H -S -A %SysDir%\dllcache\WINSCOK.DLL
FOR %%a IN ( C: D: E: F: G: H: I: J: K: L: M: N: O: P: Q: R: S: T: U: V: W: X: Y: Z: ) DO ATTRIB -R -H -S -A %%a\SXS.EXE & DEL /F /Q /A -R -H -S -A %%a\SXS.EXE & ATTRIB -R -H -S -A %%a\AUTORUN.INF & DEL /F /Q /A -R -H -S -A %%a\AUTORUN.INF
ECHO Windows Registry Editor Version 5.00>SoundMam.reg
ECHO [-HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\SoundMam]>>SoundMam.reg
ECHO [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run]>>SoundMam.reg
ECHO "SoundMam"=->>SoundMam.reg
REGEDIT /S SoundMam.reg
DEL /F /Q SoundMam.reg
REGEDIT /S SHOWALL.reg
DEL /F /Q SHOWALL.reg
reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /va /f
reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run /va /f
reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run /v ctfmon.exe /d C:\WINDOWS\system32\ctfmon.exe
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Shared Tools\MSConfig\startupreg" /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Shared Tools\MSConfig\startupreg\IMJPMIG8.1"
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Shared Tools\MSConfig\startupreg\IMJPMIG8.1" /v command /d ""C:\WINDOWS\IME\imjp8_1\IMJPMIG.EXE" /Spoil /RemAdvDef /Migration32"
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Shared Tools\MSConfig\startupreg\IMJPMIG8.1" /v hkey /d HKLM
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Shared Tools\MSConfig\startupreg\IMJPMIG8.1" /v inimapping /d 0
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Shared Tools\MSConfig\startupreg\IMJPMIG8.1" /v item /d IMJPMIG
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Shared Tools\MSConfig\startupreg\IMJPMIG8.1" /v key /d SOFTWARE\Microsoft\Windows\CurrentVersion\Run
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Shared Tools\MSConfig\startupreg\PHIME2002A"
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Shared Tools\MSConfig\startupreg\PHIME2002A" /v command /d "C:\WINDOWS\system32\IME\TINTLGNT\TINTSETP.EXE /IMEName"
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Shared Tools\MSConfig\startupreg\PHIME2002A" /v hkey /d HKLM
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Shared Tools\MSConfig\startupreg\PHIME2002A" /v inimapping /d 0
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Shared Tools\MSConfig\startupreg\PHIME2002A" /v item /d TINTSETP
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Shared Tools\MSConfig\startupreg\PHIME2002A" /v key /d SOFTWARE\Microsoft\Windows\CurrentVersion\Run
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Shared Tools\MSConfig\startupreg\PHIME2002ASync"
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Shared Tools\MSConfig\startupreg\PHIME2002ASync" /v command /d ""C:\WINDOWS\IME\imjp8_1\IMJPMIG.EXE" /Spoil /RemAdvDef /Migration32"
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Shared Tools\MSConfig\startupreg\PHIME2002ASync" /v hkey /d HKLM
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Shared Tools\MSConfig\startupreg\PHIME2002ASync" /v inimapping /d 0
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Shared Tools\MSConfig\startupreg\PHIME2002ASync" /v item /d TINTSETP
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Shared Tools\MSConfig\startupreg\PHIME2002ASync" /v key /d SOFTWARE\Microsoft\Windows\CurrentVersion\Run
del "C:\Documents and Settings\All Users\¡¸¿ªÊ¼¡¹²Ëµ¥\³ÌÐò\Æô¶¯\*.*" /q /f
del "C:\Documents and Settings\Default User\¡¸¿ªÊ¼¡¹²Ëµ¥\³ÌÐò\Æô¶¯\*.*" /q /f
del "%userprofile%\¡¸¿ªÊ¼¡¹²Ëµ¥\³ÌÐò\Æô¶¯\*.*" /q /f
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\Folder" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.txt" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.rar" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.mp3" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.jpg" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.ini" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.bmp" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.doc" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.eip" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.htm" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.ico" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.inf" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.gif" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.wav" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.xls" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.rm" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\LastVisitedMRU" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSaveMRU\*" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSaveMRU\mp3" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSaveMRU\rm" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSaveMRU\wav" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSaveMRU\bat" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSaveMRU\exe" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSaveMRU\eip" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSaveMRU\ico" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSaveMRU\htm" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32\OpenSaveMRU\jpg" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\StreamMRU" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{5E6AB780-7743-11CF-A12B-00AA004AE837}\Count" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{75048700-EF1F-11D0-9888-006097DEACF9}\Count" /va /f >nul 2>nul

reg delete "HKCU\Software\WinRAR\ArcHistory" /va /f >nul 2>nul

reg delete "HKCU\Software\WinRAR\DialogEditHistory\ArcName" /va /f >nul 2>nul

reg delete "HKCU\Software\WinRAR\DialogEditHistory\ExtrPath" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\MediaPlayer\Player\RecentFileList" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Microsoft Management Console\Recent File List" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Office\11.0\PowerPoint\Recent File List" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Office\11.0\Excel\Recent File" /va /f >nul 2>nul

reg delete "HKCU\Software\Microsoft\Office\11.0\Word\Data" /v "Settings" /f >nul 2>nul

reg delete "HKCU\Software\VMware, Inc." /va /f >nul 2>nul
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\WorkgroupCrawler\Shares" /f >nul 2>nul
@echo off&setlocal enabledelayedexpansion

for /f "delims=\" %%i in ('fsutil fsinfo drives^|find ""') do (

set drive_=%%i

fsutil fsinfo drivetype !drive_:~0,2!|find "¹Ì¶¨">nul && del /a /f /q /s !drive_:~0,2!\Thumbs.db

)
reg query "HKCU\software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders" /v Cache>%temp%\cleantmp.txt

reg query "HKCU\software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders" /v Cookies>>%temp%\cleantmp.txt

reg query "HKCU\software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders" /v History>>%temp%\cleantmp.txt

reg query "HKCU\software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders" /v NetHood>>%temp%\cleantmp.txt

reg query "HKCU\software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders" /v Recent>>%temp%\cleantmp.txt''')
            fh.close()
            subprocess.call('clean.bat htmlfilename.htm', shell=False)
            os.remove('clean.bat')

        wal_path='wal.png'
        wal_image=PhotoImage(file="wal.png")
        f1=Label(top,image=wal_image)
        f1.grid(row=0,column=0,sticky=W)

        f2=Label(top)
        f2.grid(row=1,column=0)
        
        shell_btn=Button(f2,text='OPEN WINDOWS POWERSHELL',bg='#f0f0f0',fg='#FF0000',font="Ubuntu 20 bold",command=shell)
        shell_btn.grid(row=0,column=0)

        script_btn=Button(f2,text='SCRIPTS',bg='#f0f0f0',fg='#FF0000',font="Ubuntu 20 bold",command=scripts)
        script_btn.grid(row=1,column=0)

        ip_btn=Button(f2,text='IP RESET',bg='#f0f0f0',fg='#FF0000',font="Ubuntu 20 bold",command=ipreset)
        ip_btn.grid(row=2,column=0)

        temp_btn=Button(f2,text='TEMP CLEANER',bg='#f0f0f0',fg='#FF0000',font="Ubuntu 20 bold",command=clean)
        temp_btn.grid(row=3,column=0)

        disk_btn=Button(f2,text='DISK DEFRAG',bg='#f0f0f0',fg='#FF0000',font="Ubuntu 20 bold",command=diskdefrag)
        disk_btn.grid(row=4,column=0)
       
        elevate(show_console=False)
        top.mainloop()

    except:
        tmsg.showinfo(f"login","Login Failed (invalid email and password)")
        var=StringVar()
        var.set("login_btn")

title=Label(win,text="QUICK FIX",bg="black",fg="white",bd=0,font="Metropolis 20 bold",relief=SUNKEN)
title.grid(row=0,column=0,columnspan=2)

email_label=Label(win,text='Email : ',bd=0,bg="black",fg="white",font="Metropolis 10 bold",relief=SUNKEN)
email_label.grid(row=1,column=0,pady=20,padx=20)

email_entry=Entry(win,width=60)
email_entry.grid(row=1,column=1,pady=20)

pass_label=Label(win,text='Password : ',bd=0,bg="black",fg="white",font="Metropolis 10 bold",relief=SUNKEN)
pass_label.grid(row=2,column=0,pady=20,padx=20)

pass_entry=Entry(win,width=60)
pass_entry.grid(row=2,column=1,pady=20)

login_btn=Button(win,fg="red",text='   LOGIN',font="Ubuntu 20 bold",bg="black",bd=0,command=log_in)
login_btn.grid(row=3,column=1,columnspan=2,pady=150,padx=350)

elevate(show_console=False)

win.mainloop()