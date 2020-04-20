from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import pytube

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.original = Image.open('assets/images/logoshock.jpg')
        self.image = ImageTk.PhotoImage(self.original)
        self.display = Canvas(self, bd=0, highlightthickness=0)
        self.display.create_image(0, 0, image=self.image, anchor=NW, tags="IMG")
        self.display.grid(row=0, sticky=W+E+N+S)
        self.pack(fill=BOTH, expand=1)
        self.bind("<Configure>", self.resize)

    def resize(self, event):
        size = (event.width, event.height)
        resized = self.original.resize(size,Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.display.delete("IMG")
        self.display.create_image(0, 0, image=self.image, anchor=NW, tags="IMG")

root = Tk()
app = App(root)
root.iconbitmap(r'assets/images/logoshock.ico')

root.title("SHOCK DOWNLOADER")
font=Label(root,text="Welcome to Shock Downloader!\nThis app helps you to download videos from Youtube.")
font.pack()
font.config(wraplength=450,foreground="red",justify="center")
font.config(font=('Courier',18,'bold'))

def get_info():
	link=entry.get()
	yt = pytube.YouTube(link)

	variable = messagebox.askquestion('Format','Choose video format')
	if variable == 'yes':
		#vids = yt.streams.filter(subtype='mp4').all()
		vids = yt.streams.filter(progressive=True).all()
		selections=[]
		for i in range(len(vids)):
			a=i,'. ',vids[i]
			selections.append(a)
	s=str(selections)
	messagebox.showinfo("vid num",s)
	win=Tk()
	win.title("Hybrid Downloader")
	win.geometry="720x720"
	argument=Label(win,text="Enter vid num:\n ")
	argument.grid(row=0,column=1)
	Enter=Entry(win)
	Enter.grid(row=0,column=2)
	def sub_info():
		value=Enter.get()
		vnum=int(value)
		##save video ###
		messagebox.showinfo('Save Path', 'Please choose directory to save video')
		parent_dir = askdirectory()
		vids[vnum].download(parent_dir)
		messagebox.showinfo('Done!!!', 'Video Downloaded Succesfully')
		sys.exit()
	button=Button(win,text="Validate",command=sub_info)
	button.grid(row=1,column=0)
	

url=Label(root,text="Video Url")
url.pack()
entry=Entry(root)
entry.pack()
button=Button(root,text="Download",command=get_info)
button.pack()
label=Label(root,text="Designed by Taneristique\n version 1.0")
label.pack()
label.config(foreground="green")
count=1
	
	

app.mainloop()
root.destroy()