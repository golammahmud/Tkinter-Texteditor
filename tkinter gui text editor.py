from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
from django.contrib.sessions.backends import file


root=Tk(className='Tkinter text editor')
root.title("Untitled - Notepad")
root.geometry('700x800')

def save_file():
    pass
def new_file():
    global file
    root.title("Untitled -Notepad")
    file=None
    TextArea.delete(1.0, END)

def openfile():
    global file
    file=askopenfilename(defaultextension="*.txt",filetypes=[('All Files','*.*'),('text document','*.txt')])

    if file =="":
        file=None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        TextArea.delete(1.0,END)
        f=open(file,'r')
        TextArea.insert(1.0,f.read())
        f.close()
def savefile():
    global file
    if file is None:
        file=asksaveasfilename(initialfile='Unititle.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"),('Python Files', '*.py'),('html Files', '*.html'),
                                      ('java script Files', '*.js'),('pdf Files', '*.pdf'),('doc Files', '*.doc'),
                                     ("Text Documents", "*.txt")])
        
        if file =="":
            file=None
        else:
            f=open(file,'w')
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    
def about():
    pass

def copy_file():
    TextArea.event_generate(("<<Copy>>"))
def cut_file():
    TextArea.event_generate(("<<Cut>>"))
def paste_file():
    TextArea.event_generate(("<<Paste>>"))

TextArea = Text(root, font="lucida 13")
file = None
TextArea.pack(expand=True, fill=BOTH)



menu=Menu(root)

#file menu
my_file=Menu(menu,tearoff=0)
menu.add_cascade(label='File',menu=my_file)
my_file.add_command(label='New File',command=new_file)
my_file.add_command(label='New Folder',command=new_file)
my_file.add_command(label='New Project',command=new_file)
my_file.add_separator()
my_file.add_command(label='open File',command=openfile)
my_file.add_command(label='open Folder',command=new_file)

recent_file=Menu(my_file,tearoff=0)
recent_file.add_command(label='python gui',command=new_file)
recent_file.add_command(label='tkinter menu bar',command=new_file)
my_file.add_cascade(label='open recent File',menu=recent_file)
#file menu

#edit  menu
my_file=Menu(menu,tearoff=0)
menu.add_cascade(label='Edit',menu=my_file)
my_file.add_command(label='copy',command=copy_file)
my_file.add_command(label='cut',command=cut_file)
my_file.add_command(label='paste',command=paste_file)
my_file.add_separator()
my_file.add_command(label='save as',command=savefile)
my_file.add_command(label='edit File',command=new_file)
my_file.add_command(label='open Folder',command=new_file)

# Help Menu Starts
HelpMenu = Menu(menu, tearoff=0)
HelpMenu.add_command(label="About Notepad", command=about)
menu.add_cascade(label="Help", menu=HelpMenu)

root.configure(menu=menu)


  #Adding Scrollbar using rules from Tkinter lecture no 22
Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT,  fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

root.mainloop()