import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image, ImageOps
from tkinter import font
import webbrowser
import requests
import win32api
import threading

__author__ = 'Steven Klinck'
__copyright__ = 'Copyright (C) 2021, Steven Klinck / Creative One®'
__credits__ = ['Steven Klinck / Victor Santiago']
__version__ = '1.0'
__maintainer__ = 'Steven Klinck'
__email__ = 'steven@creativeone.ca'
__status__ = 'Beta'

_AppName_ = 'Creative One® Utilities'


class Main:
    def __init__(self, parent):
        def check_updates():
            try:
                # -- Online Version File
                # -- Replace the url for your file online with the one below.
                response = requests.get(
                    'https://raw.githubusercontent.com/SKlinck/CreativeOneUtilities/master/version.txt')
                data = response.text

                if float(data) > float(__version__):
                    messagebox.showinfo('Software Update', 'Update Available!')
                    mb1 = messagebox.askyesno('Update!', f'{_AppName_} {__version__} needs to update to version {data}')
                    if mb1 is True:
                        # -- Replace the url for your file online with the one below.
                        webbrowser.open_new_tab('https://github.com/SKlinck/CreativeOneUtilities/blob/9fdbbc8a861673ead61861d8fa5a85c61ff9507c/Creative_One_Utilities_Setup_v1.1.exe?raw=true')
                        parent.destroy()
                    else:
                        pass
                else:
                    messagebox.showinfo('Software Update', 'No Updates are Available.')
            except Exception as e:
                messagebox.showinfo('Software Update', 'Unable to Check for Update, Error:' + str(e))

        def about_me():
            DisplayAboutMe(parent)

        def update_using_manager():
            try:
                # -- Online Version File
                # -- Replace the url for your file online with the one below.
                response = requests.get(
                    'https://raw.githubusercontent.com/SKlinck/CreativeOneUtilities/master/version.txt')
                data = response.text

                if float(data) > float(__version__):
                    messagebox.showinfo('Software Update', 'Update Available!')
                    mb2 = messagebox.askyesno('Update!', f'{_AppName_} {__version__} needs to update to version {data}')
                    if mb2 is True:
                        UpdateManager(parent)
                    elif mb2 == 'No':
                        pass
                else:
                    messagebox.showinfo('Software Update', 'No Updates are Available.')
            except Exception as e:
                print('The Error is here!')
                messagebox.showinfo('Software Update', 'Unable to Check for Update, Error:' + str(e))

        menu_bar = tk.Menu(parent)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='Exit', command=parent.destroy)
        menu_bar.add_cascade(label='File', menu=file_menu)
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label='About', command=about_me)
        menu_bar.add_cascade(label='Help', menu=help_menu)
        parent.config(menu=menu_bar)

        buttons_frame = tk.Frame(parent, bg='#FFFFFF')
        buttons_frame.pack(side='top', fill='x')

        button1 = ttk.Button(parent, text='Check for Updates', command=check_updates)
        button1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        button4 = ttk.Button(parent, text='UpdateManager', command=update_using_manager)
        button4.place(x=-200, relx=1.0, y=60)

class UpdateManager(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)

        self.transient(parent)
        self.result = None
        self.grab_set()
        w = 350
        h = 200
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
        self.resizable(width=False, height=False)
        self.title('Update Manager')
        self.wm_iconbitmap('images/CreativeOne.ico')

        image = Image.open('images/updatemanager.jpg')
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.pack()

        def install_update():
            win32api.ShellExecute(0, 'open', f'tmp\\{_AppName_}.exe', None, None, 10)
            parent.destroy()

        def start_update_manager():
            with requests.get('https://github.com/SKlinck/CreativeOneUtilities/blob/9fdbbc8a861673ead61861d8fa5a85c61ff9507c/Creative_One_Utilities_Setup_v1.1.exe?raw=true', stream=True) as r:
                self.progressbar['maximum'] = int(r.headers.get('Content-Length'))
                r.raise_for_status()
                with open(f'./tmp/{_AppName_}.exe', 'wb') as f:
                    for chunk in r.iter_content(chunk_size=4096):
                        if chunk:  # filter out keep-alive new chunks
                            f.write(chunk)
                            self.progressbar['value'] += 4096
            self.button1.config(text='Install', state=tk.NORMAL)

        self.progressbar = ttk.Progressbar(self,
                                           orient='horizontal',
                                           length=200,
                                           mode='determinate',
                                           value=0,
                                           maximum=0)
        self.progressbar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.button1 = ttk.Button(self, text='Wait!', state=tk.DISABLED, command=install_update)
        self.button1.place(x=-83, relx=1.0, y=-33, rely=1.0)

        self.t1 = threading.Thread(target=start_update_manager)
        self.t1.start()

## ABOUT ME
class DisplayAboutMe(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)

        self.transient(parent)
        self.result = None
        self.grab_set()
        w = 285
        h = 273
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
        self.resizable(width=False, height=False)
        self.title('About')
        self.wm_iconbitmap('images/CreativeOne.ico')

        self.image = Image.open('./images/CreativeOne.ico')
        self.size = (100, 100)
        self.thumb = ImageOps.fit(self.image, self.size, Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.thumb)
        logo_label = tk.Label(self, image=self.photo)
        logo_label.pack(side=tk.TOP, pady=10)

        f1 = tk.Frame(self)
        f1.pack()
        f2 = tk.Frame(self)
        f2.pack(pady=10)
        f3 = tk.Frame(f2)
        f3.pack()

        def call_link(*args):
            webbrowser.open_new_tab('https://www.creativeone.ca')

        tk.Label(f1, text=_AppName_ + ' ' + str(__version__)).pack()
        tk.Label(f1, text='Copyright (C) 2021 Creative One®').pack()
        tk.Label(f1, text='All rights reserved').pack()

        f = font.Font(size=10, slant='italic', underline=True)
        label1 = tk.Label(f3, text='Creative One®', font=f, cursor='hand2')
        label1['foreground'] = 'blue'
        label1.pack(side=tk.LEFT)
        label1.bind('<Button-1>', call_link)
        ttk.Button(self, text='OK', command=self.destroy).pack(pady=5)

## ROOT WINDOW
def main():
    root = tk.Tk()
    root.title(_AppName_ + ' ' + str(__version__))
    w = 310
    h = 310
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    root.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
    root.resizable(width=False, height=False)
    root.wm_iconbitmap('images/CreativeOne.ico')
    Main(root)
    root.mainloop()


if __name__ == '__main__':
    main()
