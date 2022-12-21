import sys
from time import sleep as timeout

import requests
from tkinter import *
from tkinter import messagebox
import webbrowser
import win32api
import wget as d

cfu = Tk()
cfu.title("Update Checker")
# cfu.iconbitmap(PhotoImage("icon.ico")) # here, put the path to the icon! EXAMPLE => ./icon/update.ico

__version__ = "1.1" # Each update, change this to the version of that update
__AppName__ = "Writer" # Here, put the name of the app that you are putting this code (Update Checker) in.

def check_updates():
    try:
        # -- Online Version File
        # -- Replace the url for your file online with the one below.
        response = requests.get(
            'https://raw.githubusercontent.com/cho-amh-programmerExpert/writer.app/main/VERSION.writer') # In version.txt, just put the latest version of the app after each update you make!
        data = response.text

        if float(data) > float(__version__):
            messagebox.showinfo('Software Update', 'Update Available!')
            mb1 = messagebox.askyesno('Update!', f'{__AppName__} {__version__} needs to update to version {data}!\n Do you want to download the new update?')
            if mb1 is True:
                try:
                    messagebox.showinfo("Software Update", "Click \"ok\" To Start downloading!")
                    URL = "https://github.com/cho-amh-programmerExpert/terminal_version/blob/main/Update_Checker.py" # Here Put The Updated App  File URL (GITHUB Is Recommended!)
                    d.download(URL, "Update_Checker.py") # And Except "Update Checker.exe" Put The Same File URL But This Time Only The File Name!
                    # An EXE File Is Recommend For THis System
                    messagebox.showinfo("Software Update", "Successfully Downloaded The Update!\nYou Can Delete This File And Use The New Downloaded File!")
                    cfu.destroy()

                except:
                    Md = messagebox.askyesno("Software Update", "Something Went Wrong!\nDo You Want To Download The Update Manually?")

                    if Md is True:
                        # -- Replace the url for your file online with the one below.
                        webbrowser.open_new_tab('https://raw.githubusercontent.com/cho-amh-programmerExpert/terminal_version/main/Update%20Checker.py')  # Here, put the direct (Raw) link of the updated app for download!
                        cfu.destroy()

                    else:
                        cfu.destroy()


            else:
                pass
        else:
            messagebox.showinfo('Software Update', 'The App Is Up To Date!')
            cfu.destroy()
            app()


    except Exception as e:
        messagebox.showinfo('Software Update', 'Unable to Check for Update, Error:' + str(e))

check_updates()

cfu.mainloop()

def app():
    while 1:
        sys.stdout.write("\r" + "I")
        sys.stdout.flush()
        timeout(1.5)
        sys.stdout.write("\r" + "WILL PURCHASE")
        sys.stdout.flush()
        timeout(1.5)
        sys.stdout.write("\r" + "EVERY ITEM")
        sys.stdout.flush()
        timeout(1.5)
        sys.stdout.write("\r" + "IN THE SSB2's NEW UPDATE")
        sys.stdout.flush()
        timeout(1.5)
        sys.stdout.write("\r" + "AS")
        sys.stdout.flush()
        timeout(1.5)
        sys.stdout.write("\r" + "IT RELEASES")
        sys.stdout.flush()
        timeout(1.5)

        sys.stdout.write("\r" + "I")
        sys.stdout.flush()
        timeout(1.5)
        sys.stdout.write(" WILL PURCHASE")
        sys.stdout.flush()
        timeout(1.5)
        sys.stdout.write(" EVERY ITEM")
        sys.stdout.flush()
        timeout(1.5)
        sys.stdout.write(" IN SSB2's NEW UPDATE")
        sys.stdout.flush()
        timeout(1.5)
        sys.stdout.write(" AS")
        sys.stdout.flush()
        timeout(1.5)
        sys.stdout.write(" IT RELEASES")
        sys.stdout.flush()
        timeout(5)
