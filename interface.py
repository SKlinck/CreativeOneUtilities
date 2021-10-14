#Run main.py!!!

import tkinter
from tkinter import ttk
from tkinter import *

def on_closing():
    global running
    running = False

# GUI
root = tkinter.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.resizable(False, False)
root.title("Screen Recorder")
root.geometry("800x400+500+100")
root.iconbitmap('./assets/CreativeOne.ico')
root.title('Creative One® Screen Recorder')
canvas = Canvas(root, bg="#4392F1", height=400, width=800, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)
background_img = PhotoImage(file=f"assets/background.png")
background = canvas.create_image(400.0, 200.0, image=background_img)
header = canvas.create_text(400.0, 91.0, text="Screen Recorder", fill="#ECE8EF", font=("Roboto-Bold", int(30.0)))
create_label = canvas.create_text(300, 174.5, text="create a", fill="#ECE8EF", font=("Roboto-Bold", int(16.0)))
video_label = canvas.create_text(500, 174.5, text="fps video", fill="#ECE8EF", font=("Roboto-Medium", int(16.0)))
switch = tkinter.Scale(from_=10, to=30, orient=tkinter.HORIZONTAL, length=90, activebackground="#cb0e17"
                       , bg="#cb0e17", highlightcolor="#cb0e17", highlightbackground="#cb0e17", fg="white",
                       troughcolor="white")
create_label = canvas.create_text(400, 140, text="(playback speed)", fill="#ECE8EF", font=("Roboto-Bold", int(12.0)))

menubar = Menu(root)
fileMenu = Menu(menubar, tearoff=0)
Output = Menu(menubar, tearoff=0)
video_format = Menu(menubar, tearoff=0)

mp4_format = tkinter.BooleanVar()
mp4_format.set(True)
avi_format = tkinter.BooleanVar()

fileMenu.add_cascade(label='Video Format', menu=video_format)

menubar.add_cascade(label='Video Settings', menu=fileMenu)
menubar.add_cascade(label="Output", menu=Output)

start_img = PhotoImage(file=f"assets/start.png")
start = Button(image=start_img, borderwidth=0, highlightthickness=0, relief="raised")
pause_img = PhotoImage(file=f"assets/pause.png")
pause = Button(image=pause_img, borderwidth=0, highlightthickness=0, relief="raised")
end_img = PhotoImage(file=f"assets/end.png")
end = Button(image=end_img, borderwidth=0, highlightthickness=0, relief="raised")
info = canvas.create_text(400.0, 342.5, text="Start Recording", fill="#ECE8EF", font=("Roboto-Medium", int(16.0)))

# When started
end["state"] = "disabled"
pause["state"] = "disabled"