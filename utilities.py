import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from tkinter import *
from tkinter.ttk import *
from ttkbootstrap import Style

root = tk.Tk()
style = Style(theme='creativeone')
window = style.master
root.iconbitmap('./assets/icons/CreativeOne.ico')
root.title('Creative One® Utilities')
window_width = 823
window_height = 335
root.resizable(False, False)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="QUIT", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

advancedmenu = Menu(menubar, tearoff=0)
def cleartasks():
  import os
  os.startfile(r".\scripts\Clear Pending System Tasks")
advancedmenu.add_command(label="Clear System Tasks", command=cleartasks)
def CMD():
  import os
  os.startfile(r".\scripts\CMD")
advancedmenu.add_command(label="Command Prompt (admin)", command=CMD)
menubar.add_cascade(label="Advanced", menu=advancedmenu)

helpmenu = Menu(menubar, tearoff=0)
def about():
     aboutwin = Toplevel(root)
     aboutwin.iconbitmap('./assets/icons/CreativeOne.ico')
     aboutwin.title('Creative One® Utilities - About...')
     aboutwin.geometry('500x300')
     aboutwin.resizable(False, False)
     licenseLabel=Label(aboutwin, text='Creative One® Utilities - About Program and Develeoper').grid()
     aboutwin.columnconfigure(0, weight=1)
     aboutwin.rowconfigure(1, weight=1)
     message ='''Creative One® Utilities was developed by Steven Klinck of Creative One®.'''
     aboutwin_text=Text(aboutwin, wrap=WORD)
     aboutwin_text.grid(sticky="W",row=1,column=0,pady=2, padx=4)
     aboutwin_text.insert('end', message)
     aboutwin_text["state"] = DISABLED
helpmenu.add_command(label="About...", command=about)
def features():
     featureswin = Toplevel(root)
     featureswin.iconbitmap('./assets/icons/CreativeOne.ico')
     featureswin.title('Creative One® Utilities - Program Features')
     featureswin.geometry('500x300')
     featureswin.resizable(False, False)
     featuresLabel=Label(featureswin, text='Creative One® Utilities - Program Features').grid()
     featureswin.columnconfigure(0, weight=1)
     featureswin.rowconfigure(1, weight=1)
     message ='''- Restart Print Services\n- Force Restart Outlook\n- Network Connection Reset via IPConfig / DNSFlush\n- Check Disk + Repair\n- Check USB + Repair\n- System File Checker\n- Reboot into Advanced Startup Menu\n- Reboot PC'''
     featureswin_text=Text(featureswin, wrap=WORD)
     featureswin_text.grid(sticky="W",row=1,column=0,pady=2, padx=4)
     featureswin_text.insert('end', message)
     featureswin_text["state"] = DISABLED
helpmenu.add_command(label="Program Features", command=features)
helpmenu.add_separator()
def license():
     licensewin = Toplevel(root)
     licensewin.iconbitmap('./assets/icons/CreativeOne.ico')
     licensewin.title('Creative One® Utilities End User License Agreement')
     licensewin.geometry('500x300')
     licensewin.resizable(False, False)
     licenseLabel=Label(licensewin, text='Creative One® Utilities - End User License Agreement (EULA)').grid()
     licensewin.columnconfigure(0, weight=1)
     licensewin.rowconfigure(1, weight=1)
     message ='''Creative One®\n\nCreative One® Utilities\n\nThis End-User License Agreement (EULA) is a legal agreement between USER and the mentioned author Steven Klinck [Creative One®] of this Software for the software product identified above, which includes computer software and may include associated media, printed materials, and “online” or electronic documentation (“Software Product”).\n\nBy installing, copying, or otherwise using Creative One® Utilities, you agree to be bounded by the terms of this EULA. If you do not agree to the terms of this EULA, do not install or use Creative One® Utilities.\n\nSOFTWARE PRODUCT LICENSE\na) Creative One® Utilities is being distributed as software for commercial use. It may be included with CD-ROM/DVD-ROM, USB, or digital distributions. You are not allowed to make a charge for distributing this Software (either for profit or merely to recover your media and distribution costs) whether as a stand-alone product, or as part of a compilation or anthology, nor to use it for supporting your business or customers. It may not be distributed freely on any website or through any other distribution mechanism.\n\n1. Grant of License.\nThis EULA grants you the following rights:\n\nInstallation and Use.\nYou may install and use one (1) copy of Creative One® Utilities per license.\n\nReproduction and Distribution.\nYou may not reproduce and distribute copies of Creative One® Utilities.\n\n2. Description of Rights and Limitations.\n\nLimitations on Reverse Engineering, Decompilation, Disassembly and change (add, delete or modify) the resources in the compiled the assembly. You may not reverse engineer, decompile, or disassemble Creative One® Utilities, except and only to the extent that such activity is expressly permitted by applicable law notwithstanding this limitation.\n\nSeparation of Components.\nCreative One® Utilities is licensed as a single product. Its component parts may not be separated for use on more than one computer.\n\nSoftware Transfer.\nYou may not transfer any of your rights under this EULA.\n\nTermination.\nWithout prejudice to any other rights, the Author of this Software may terminate this EULA if you fail to comply with the terms and conditions of this EULA. In such event, you must destroy all copies of Creative One® Utilities and all of its component parts.\n\n3. Copyright.\nAll title and copyrights in and to Creative One® Utilities (including but not limited to any images, photographs, clipart, libraries, and examples incorporated into Creative One® Utilities), the accompanying printed materials, and any copies of Creative One® Utilities are owned by the Author of this Software. Creative One® Utilities is protected by copyright laws and international treaty provisions.\n\nTherefore, you must treat Creative One® Utilities like any other copyrighted material. The licensed users or licensed company can use all functions, example, templates, clipart, libraries and symbols in Creative One® Utilities\n\nLIMITED WARRANTY\nNo Warranties. The Author of this Software expressly disclaims any warranty for Creative One® Utilities. Creative One® Utilities and any related documentation is provided “as is” without warranty of any kind, either express or implied, including, without limitation, the implied warranties or merchantability, fitness for a particular purpose, or noninfringement. The entire risk arising out of use or performance of Creative One® Utilities remains with you.\nNo Liability for Damages. In no event shall the author of this Software be liable for any special, consequential, incidental or indirect damages whatsoever (including, without limitation, damages for loss of business profits, business interruption, loss of business information, or any other pecuniary loss) arising out of the use of or inability to use Creative One® Utilities, even if the Author of this Software is aware of the possibility of such damages and known defects. '''
     licensewin_text=Text(licensewin, wrap=WORD)
     licensewin_text.grid(sticky="W",row=1,column=0,pady=2, padx=4)
     licensewin_text.insert('end', message)
     licensewin_text["state"] = DISABLED
helpmenu.add_command(label="License", command=license)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

tabMenu = ttk.Notebook(root)
tab1 = tk.Frame(tabMenu, width=811)
# Propagates the width of tab1 across all tabs
tab1.grid_propagate(0)
tab2 = tk.Frame(tabMenu)
tab3 = tk.Frame(tabMenu)
tab4 = tk.Frame(tabMenu)
tab5 = tk.Frame(tabMenu)
tab6 = tk.Frame(tabMenu)

tabMenu.add(tab1, text ='Quick Fixes')
tabMenu.add(tab2, text ='Advanced PC Tools')
tabMenu.add(tab3, text ='Network Fixes')
tabMenu.add(tab4, text ='Neat Tools')
tabMenu.add(tab5, text ='About My PC!')
tabMenu.add(tab6, text ='Telephone/Remote Support & Record Screen')
tabMenu.grid(rowspan='1', ipadx='1', padx='2', pady='2')

ttk.Label(tab6,
          text ="Need Additional Support?", font = ('Century Gothic', 12, "bold")).grid(
                                    column = 0,
                                    row = 0, 
                                    padx = 5,
                                    pady = 5)
ttk.Label(tab6,
          text ="If you require live assistance from a member of our team call:", font = ('Century Gothic', 12)).grid(
                                    column = 0,
                                    row = 1, 
                                    padx = 5,
                                    pady = 5)
ttk.Label(tab6,
          text ="Creative One® Huntsville: 705-788-3932", font = ('Century Gothic', 12, "bold")).grid(
                                    column = 0,
                                    row = 2, 
                                    padx = 5,
                                    pady = 5,
                                    sticky=W)
ttk.Label(tab6,
          text ="Creative One® Bracebridge: 705-646-3932", font = ('Century Gothic', 12, "bold")).grid(
                                    column = 0,
                                    row = 3, 
                                    padx = 5,
                                    pady = 5,
                                    sticky=W)                                  
ttk.Label(tab6,
          text ="Use extension 1 for Brand and Web.", font = ('Century Gothic', 12, "bold")).grid(
                                    column = 0,
                                    row = 4, 
                                    padx = 5,
                                    pady = 5,
                                    sticky=W)
ttk.Label(tab6,
          text ="Use extension 2 for Technical Support.", font = ('Century Gothic', 12, "bold")).grid(
                                    column = 0,
                                    row = 5, 
                                    padx = 5,
                                    pady = 5,
                                    sticky=W)                                 

# RESTART PRINT SERVICES BUTTON
from tkinter.messagebox import *
def run_rps():
  import os
  os.startfile(r".\scripts\Restart Print Services")
rps_icon = tk.PhotoImage(file='./assets/icons/printer32.png')
rps_button = ttk.Button(tab1,
    image=rps_icon,
    text='     Clear Your Print Queue\n     Clear a clogged print queue, and refresh your PCs print services.',
    compound=tk.LEFT,
    command=run_rps)
rps_button.grid(sticky="W",row=1,column=0, ipady=4, ipadx=4, pady=2, padx=4)
# TASK KILL OUTLOOK BUTTON
def run_tko():
  showinfo(title='Outlook not opening?',message='Click "OK" to open a \n stuck Outlook program.')
  import os
  os.system("taskkill /im outlook.exe")
  showinfo(title='Please Wait!',message='Outlook will open shortly, \n you may close this window.')
  import time
  time.sleep(2)
  os.system("start /im outlook.exe")
tko_icon = tk.PhotoImage(file='./assets/icons/outlook32.png')
tkm_icon = tk.PhotoImage(file='./assets/icons/mail32.png')
tko_button = ttk.Button(tab1,
    image=tko_icon,
    text='     Force Restart Outlook\n     Forces Outlook to close and then automatically reopens the program.',
    compound=tk.LEFT,
    command=run_tko)
tko_button.grid(sticky="W",row=3,column=0, ipady=4, ipadx=4, pady=2, padx=4)
# RESTART PC BUTTON
def diskclean():
  import os
  os.startfile(r".\scripts\Disk Cleaner")
diskclean_icon = tk.PhotoImage(file='./assets/icons/clean32.png')
diskclean_button = ttk.Button(tab1,
    image=diskclean_icon,
    text='     Disk Cleaner for Windows\n     Reclaim space on your PC! Scan for junk files, then choose what to remove.',
    compound=tk.LEFT,
    command=diskclean)
diskclean_button.grid(sticky="W",row=4,column=0, ipady=4, ipadx=4, pady=2, padx=4)
# RESTART PC BUTTON
def run_reboot():
  import os
  os.startfile(r".\scripts\Reboot")
reboot_icon = tk.PhotoImage(file='./assets/icons/restart32.png')
reboot_button = ttk.Button(tab1,
    image=reboot_icon,
    text='     Reboot PC\n     Select this option to reboot your computer now.',
    compound=tk.LEFT,
    command=run_reboot)
reboot_button.grid(sticky="W",row=5,column=0, ipady=4, ipadx=4, pady=2, padx=4)
# SYSTEM FILE CHECKER
def switch():
  if sfc_lock_btn['text'] == 'Locked!':
    sfc_button['state'] = DISABLED
  elif sfc_lock_btn['text'] == 'Unlocked!':
    sfc_button['state'] = NORMAL
def run_sfc():
  import os
  os.startfile(r".\scripts\System File Checker")
sfc_icon = tk.PhotoImage(file='./assets/icons/sfc32.png')
sfc_button = ttk.Button(tab2,
    image=sfc_icon,
    text='     System File Checker Tool\n     Run this command to check the integrity of your Windows 10 installation, and attempt to fix any errors.\n     NOTE: This process will take some time to complete.',
    compound=tk.LEFT,
    state=DISABLED,
    command=run_sfc)
sfc_button.grid(sticky="W",row=1,column=0, ipady=4, ipadx=4, pady=2, padx=4)
sfc_lock = StringVar()
sfc_lock.set('Locked!')
sfc_lock_btn = ttk.Checkbutton(tab2, style='warning.Roundtoggle.Toolbutton', text='Locked!', textvariable=sfc_lock, variable=sfc_lock, onvalue='Unlocked!', offvalue='Locked!', command=switch)
sfc_lock_btn.grid(sticky="W",row=1,column=1, ipady=4, ipadx=4, pady=2, padx=4)
# CHECK DISK + FIX SWITCH BUTTONS
def chkdskfix_switch():
  if chkdsk_fix_btn['text'] == 'Just Scan':
    chkdsk_button['command'] = chkdsk
    chkdsk_button['text'] = '     Scan Disk (C:)\n     Verifies the file system integrity of the C: drive. Flip the switch to scan and repair.\n     NOTE: This process will take some time to complete.'
  elif chkdsk_fix_btn['text'] == 'Scan & Fix':
    chkdsk_button['command'] = chkdskfix
    chkdsk_button['text'] = '     Scan Disk & Fix (C:)\n     Verifies the file system integrity of the C: drive. Flip the switch to scan and repair.\n     NOTE: This process will take some time to complete.'
def chkdsk_switch():
  if chkdsk_lock_btn['text'] == 'Locked!':
    chkdsk_button['state'] = DISABLED
  elif chkdsk_lock_btn['text'] == 'Unlocked!':
    chkdsk_button['state'] = NORMAL
def chkdsk():
  import os
  os.startfile(r".\scripts\Check Disk")
def chkdskfix():
  import os
  os.startfile(r".\scripts\Check & Fix Disk")
chkdsk_icon = tk.PhotoImage(file='./assets/icons/chkdsk32.png')
chkdsk_button = ttk.Button(tab2,
    image=chkdsk_icon,
    text='     Scan Disk (C:)\n     Verifies the file system integrity of the C: drive. Flip the switch to scan and repair.\n     NOTE: This process will take some time to complete.',
    compound=tk.LEFT,
    state=DISABLED,
    command=chkdsk)
chkdsk_button.grid(sticky="W",row=2,column=0, ipady=4, ipadx=4, pady=2, padx=4)
chkdsk_fix = StringVar()
chkdsk_fix.set('Just Scan')
chkdsk_fix_btn = ttk.Checkbutton(tab2, style='warning.Roundtoggle.Toolbutton', text='Scan & Fix', textvariable=chkdsk_fix, variable=chkdsk_fix, onvalue='Scan & Fix', offvalue='Just Scan', command=chkdskfix_switch)
chkdsk_fix_btn.grid(sticky="E",row=2,column=0, ipady=4, ipadx=4, pady=2, padx=4)
chkdsk_lock = StringVar()
chkdsk_lock.set('Locked!')
chkdsk_lock_btn = ttk.Checkbutton(tab2, style='warning.Roundtoggle.Toolbutton', text='Locked!', textvariable=chkdsk_lock, variable=chkdsk_lock, onvalue='Unlocked!', offvalue='Locked!', command=chkdsk_switch)
chkdsk_lock_btn.grid(sticky="W",row=2,column=1, ipady=4, ipadx=4, pady=2, padx=4)
# CHECK USB + FIX SWITCH BUTTONS
def chkUSBfix_switch():
  if chkUSB_fix_btn['text'] == 'Just Scan':
    chkUSB_button['command'] = chkUSB
    chkUSB_button['text'] = '     Scan USB (E:)\n     Verifies the file system integrity of the E: drive. Flip the switch to scan and repair.\n     NOTE: This process will take some time to complete.'
  elif chkUSB_fix_btn['text'] == 'Scan & Fix':
    chkUSB_button['command'] = chkUSBF
    chkUSB_button['text'] = '     Scan USB & Fix (E:)\n     Verifies the file system integrity of the E: drive. Flip the switch to scan and repair.\n     NOTE: This process will take some time to complete.'
def chkUSB_switch():
  if chkUSB_lock_btn['text'] == 'Locked!':
    chkUSB_button['state'] = DISABLED
  elif chkUSB_lock_btn['text'] == 'Unlocked!':
    chkUSB_button['state'] = NORMAL
def chkUSB():
  import os
  os.startfile(r".\scripts\Check USB")
def chkUSBF():
  import os
  os.startfile(r".\scripts\Check & Fix USB")
chkUSB_icon = tk.PhotoImage(file='./assets/icons/USB32.png')
chkUSB_button = ttk.Button(tab2,
    image=chkUSB_icon,
    text='     Scan USB (E:)\n     Verifies the file system integrity of the E: drive. Flip the switch to scan and repair.\n     NOTE: This process will take some time to complete.',
    compound=tk.LEFT,
    state=DISABLED,
    command=chkUSB)
chkUSB_button.grid(sticky="W",row=4,column=0, ipady=4, ipadx=4, pady=2, padx=4)
chkUSB_fix = StringVar()
chkUSB_fix.set('Just Scan')
chkUSB_fix_btn = ttk.Checkbutton(tab2, style='warning.Roundtoggle.Toolbutton', text='Scan & Fix', textvariable=chkUSB_fix, variable=chkUSB_fix, onvalue='Scan & Fix', offvalue='Just Scan', command=chkUSBfix_switch)
chkUSB_fix_btn.grid(sticky="E",row=4,column=0, ipady=4, ipadx=4, pady=2, padx=4)
chkUSB_lock = StringVar()
chkUSB_lock.set('Locked!')
chkUSB_lock_btn = ttk.Checkbutton(tab2, style='warning.Roundtoggle.Toolbutton', text='Locked!', textvariable=chkUSB_lock, variable=chkUSB_lock, onvalue='Unlocked!', offvalue='Locked!', command=chkUSB_switch)
chkUSB_lock_btn.grid(sticky="W",row=4,column=1, ipady=4, ipadx=4, pady=2, padx=4)
# ADVANCED BOOT MENU BUTTON
def ASu_switch():
  if ASu_lock_btn['text'] == 'Locked!':
    rebootASu_button['state'] = DISABLED
  elif ASu_lock_btn['text'] == 'Unlocked!':
    rebootASu_button['state'] = NORMAL
def run_rebootASu():
  import os
  os.startfile(r".\scripts\Reboot Advanced Startup")
rebootASu_icon = tk.PhotoImage(file='./assets/icons/pcrepair32.png')
rebootASu_button = ttk.Button(tab2,
    image=rebootASu_icon,
    text='     Reboot into the Advanced Startup Menu.\n     Reboot into safe mode, the BiOS menu or into a PC recovery environment. Knowledgable Users Only.',
    compound=tk.LEFT,
    state=DISABLED,
    command=run_rebootASu)
rebootASu_button.grid(sticky="W",row=6,column=0, ipady=4, ipadx=4, pady=2, padx=4)
ASu_lock = StringVar()
ASu_lock.set('Locked!')
ASu_lock_btn = ttk.Checkbutton(tab2, style='warning.Roundtoggle.Toolbutton', text='Locked!', textvariable=ASu_lock, variable=ASu_lock, onvalue='Unlocked!', offvalue='Locked!', command=ASu_switch)
ASu_lock_btn.grid(sticky="W",row=6,column=1, ipady=4, ipadx=4, pady=2, padx=4)
# IPCONFIG BUTTON
def refreshNetwork_switch():
  if refreshNetwork_lock_btn['text'] == 'Locked!':
    refreshNetwork_button['state'] = DISABLED
  elif refreshNetwork_lock_btn['text'] == 'Unlocked!':
    refreshNetwork_button['state'] = NORMAL
def run_refreshNetwork():
  showinfo(title='Please Wait!',message='Press "OK" to refresh your network connection. Another pop-up will appear when the script is complete. You may close this window.')
  import os
  os.startfile(r".\scripts\refresh-network.bat")
  import time
  time.sleep(20)
  showinfo(title='Thank you for waiting!',message='The script has completed!')
refreshNetwork_icon = tk.PhotoImage(file='./assets/icons/router32.png')
refreshNetwork_button = ttk.Button(tab3,
    image=refreshNetwork_icon,
    text='     Release & Renew IP + DNS Flush\n     Refresh your network connection by grabbing a new IP address from your router and flushing your DNS.',
    compound=tk.LEFT,
    state=DISABLED,
    command=run_refreshNetwork)
refreshNetwork_button.grid(sticky="W",row=1,column=0, ipady=4, ipadx=4, pady=2, padx=4)
refreshNetwork_lock = StringVar()
refreshNetwork_lock.set('Locked!')
refreshNetwork_lock_btn = ttk.Checkbutton(tab3, style='warning.Roundtoggle.Toolbutton', text='Locked!', textvariable=refreshNetwork_lock, variable=refreshNetwork_lock, onvalue='Unlocked!', offvalue='Locked!', command=refreshNetwork_switch)
refreshNetwork_lock_btn.grid(sticky="W",row=1,column=1, ipady=4, ipadx=4, pady=2, padx=4)
# CHARACTER MAP BUTTON
def run_charmap():
  import os
  os.startfile(r".\scripts\charmap.bat")
charmap_icon = tk.PhotoImage(file='./assets/icons/symbol32.png')
charmap_button = ttk.Button(tab4,
    image=charmap_icon,
    text='     Open the Character Map\n     Browse a HUGE library of special text symbols and letters (Ex. æ, ©, ®,™, ֎, ♠ ♥ ♣ ♦, ₿) ',
    compound=tk.LEFT,
    command=run_charmap)
charmap_button.grid(sticky="W",row=1,column=0, ipady=4, ipadx=4, pady=2, padx=4)
# MAGNIFIER
def run_magnifier():
  import os
  os.startfile(r".\scripts\Magnifier")
magnifier_icon = tk.PhotoImage(file='./assets/icons/magnify32.png')
magnifier_button = ttk.Button(tab4,
    image=magnifier_icon,
    text='     Open the Magnifier Tool\n     Adjust the zoom level on your computer, great for reading fine print.',
    compound=tk.LEFT,
    command=run_magnifier)
magnifier_button.grid(sticky="W",row=2,column=0, ipady=4, ipadx=4, pady=2, padx=4)
# SYSTEM INFO BUTTON
def sysinfo():
  import os
  os.startfile(r".\scripts\System Information")
sysinfo_icon = tk.PhotoImage(file='./assets/icons/info32.png')
sysinfo_button = ttk.Button(tab5,
    image=sysinfo_icon,
    text='     System Information\n     Gather information on your computer system from the command terminal automatically.',
    compound=tk.LEFT,
    command=sysinfo)
sysinfo_button.grid(sticky="W",row=1,column=0, ipady=4, ipadx=4, pady=2, padx=4)
# DX DIAG BUTTON
def dxdiag():
  import os
  os.startfile(r".\scripts\dxdiag.bat")
dxdiag_icon = tk.PhotoImage(file='./assets/icons/dxdiag32.png')
dxdiag_button = ttk.Button(tab5,
    image=dxdiag_icon,
    text='     Direct X Diagnostic\n     Gather information on your computer system, display, sound, and input devices.',
    compound=tk.LEFT,
    command=dxdiag)
dxdiag_button.grid(sticky="W",row=3,column=0, ipady=4, ipadx=4, pady=2, padx=4)
# MSINFO32 BUTTON
def msinfo():
  import os
  os.startfile(r".\scripts\msinfo32.bat")
msinfo_icon = tk.PhotoImage(file='./assets/icons/windows32.png')
msinfo_button = ttk.Button(tab5,
    image=msinfo_icon,
    text='     System Information for Windows (msinfo32)\n     Gather detailed information on your computer system, hardware, and configurations.',
    compound=tk.LEFT,
    command=msinfo)
msinfo_button.grid(sticky="W",row=5,column=0, ipady=4, ipadx=4, pady=2, padx=4)
# EVENT VIEWER
def eventvwr():
  import os
  os.startfile(r".\scripts\Event Viewer")
eventvwr_icon = tk.PhotoImage(file='./assets/icons/event32.png')
eventvwr_button = ttk.Button(tab5,
    image=eventvwr_icon,
    text='     Event Viewer\n     Review computer system events for errors with software or hardware.',
    compound=tk.LEFT,
    command=eventvwr)
eventvwr_button.grid(sticky="W",row=6,column=0, ipady=4, ipadx=4, pady=2, padx=4)
# SCREEN RECORDING
def record():
  import os
  os.startfile(r".\main.py")
record_icon = tk.PhotoImage(file='./assets/icons/record32.png')
record_button = ttk.Button(tab6,
    image=record_icon,
    text='     Screen Recording\n     Record an on screen issue to show our technical team.',
    compound=tk.LEFT,
    command=record)
record_button.grid(sticky="W",row=6,column=0, ipady=4, ipadx=4, pady=2, padx=4)
# VIDEO OUTPUT FOLDER
def videoOutput():
  import os
  os.startfile(r".\Outputs")
videos_icon = tk.PhotoImage(file='./assets/icons/output32.png')
videos_button = ttk.Button(tab6,
    image=videos_icon,
    text='     Screen Recording Output Folder\n     Review all your screen recording files.',
    compound=tk.LEFT,
    command=videoOutput)
videos_button.grid(sticky="W",row=6,column=1, ipady=4, ipadx=4, pady=2, padx=4)
###############
window.mainloop()