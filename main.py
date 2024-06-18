from tkinter import *
from functions import *
from tkinter import font


a = file_fncs()
b = view_MENU()
c = Tools_MENU()
d = help_MENU()
e = TODO()
global num
default_open_file = "files\\default.txt"
a.current_file = default_open_file
fonts = [
    ("Ink Free", 19),("Comic Sans MS", 15),("Consolas", 15),("Brush Script MT", 19),("Papyrus", 18),
    ("Segoe Script", 20),("Kristen ITC", 22),("Chalkduster", 26),("Viner Hand ITC", 18),("Segoe Print", 18),
    ("Ravie", 18),("Harrington", 18),("Snap ITC", 17),("Jokerman", 20),("Magneto", 20),("Stencil", 20),
    ("Wide Latin", 21),("Gigi", 25)
]

def Keybindings():
    root.bind("<Control-s>",lambda event: a.save_file(Text, root))     #saving short cut
    root.bind("<Control-o>", lambda event: a.open_file(Text))       # Ctrl + O for opening
    root.bind("<Control-n>", lambda event: a.new_file(Text))        #new pge shortcut
    root.bind("<Alt-Return>", lambda event: c.text_to_speech(Text))
    root.bind("<Shift-Return>", lambda event: c.speech_to_text(Text,a.current_file))    #for speech to text
    

def File_menubar():
    filemenu = Menu(menubar, tearoff=1,activebackground="pink")
    menubar.add_cascade(label="File",menu=filemenu)

    filemenu.add_command(label="New",command=lambda: a.new_file(Text),activebackground="black",activeforeground="blue")    #you new
    filemenu.add_command(label="Open",command=lambda: a.open_file(Text))  #you open
    filemenu.add_command(label="Save",command=lambda: a.save_file(Text,root))  #you save  
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=quit)         #you quit

def edit_menubar():
    editmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Edit",menu=editmenu)

    editmenu.add_command(label="copy",command=lambda: a.copy(Text))     #cutting
    editmenu.add_command(label="cut",command=lambda:a.cut(Text))        #copying
    editmenu.add_command(label="paste",command=lambda:a.paste(Text))    #pasting

def view_menubar():
    viewmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="View",menu=viewmenu) #created a menu for view

    fontmenu = Menu(viewmenu,tearoff=0)             #creates a sub menu for all fonts
    viewmenu.add_cascade(label="Font Style",menu=fontmenu)  
    num=0
    for i in fonts:               
        fontmenu.add_command(label=fonts[num][0],command=lambda font_family=i: b.Change_Font(Text, font_family))     #adding fonts to dropdown menu
        num+=1

    fg_menu = Menu(viewmenu,tearoff=0)                              #create a sub-menu for text color options
    viewmenu.add_cascade(label="Font Color",menu=fg_menu)
    fg_menu.add_command(label="Default",command=lambda:b.Default_fg(Text))
    fg_menu.add_command(label="More Color",command= lambda:b.more_color_fg(Text))

    bg_menu = Menu(viewmenu,tearoff=0)                          #creating a sub-menu for bg color options
    viewmenu.add_cascade(label="Bg Color",menu=bg_menu)
    bg_menu.add_command(label="Default",command=lambda:b.Default_bg(Text,F1,L1,B1))

    presets_menu = Menu(bg_menu,tearoff=0)
    bg_menu.add_cascade(label="Devlopers choice",menu=presets_menu)
    presets_menu.add_command(label="C1",command=lambda:b.presets(Text,1,F1,L1,B1))
    presets_menu.add_command(label="C2",command=lambda:b.presets(Text,2,F1,L1,B1))
    presets_menu.add_command(label="C3",command=lambda:b.presets(Text,3,F1,L1,B1))
    presets_menu.add_command(label="C4",command=lambda:b.presets(Text,4,F1,L1,B1))

    bg_menu.add_command(label="More Color",command=lambda: b.more_color_bg(Text,F1,L1,B1))

    viewmenu.add_command(label="Dark Mode",command=lambda: b.Dark_mode(Text,F1,L1,B1))

def tools_menubar():
    toolsmenu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Tools",menu=toolsmenu)

    toolsmenu.add_command(label="Text to Speech",command=lambda: c.text_to_speech(Text))
    toolsmenu.add_command(label="speech to text",command=lambda: c.speech_to_text(Text,a.current_file))

def help_menubar():
    helpmenu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="help",menu=helpmenu)

    helpmenu.add_command(label="Keyboard Shortcuts",command=lambda: d.shorcuts())
    helpmenu.add_command(label="About Us",command=lambda: d.About_us())


root = Tk()
root.title("My Digitalz Diary")
root.geometry("450x400")
root.resizable(0,0)

F1 = Frame(root,width=10,height=50,bg="light Yellow")                           
L1 = Label(F1,width=5,height=5,relief="flat",bg="light Yellow")
L1.pack(side=RIGHT)
B1= Button(L1,text='TO-DO',font=("Ink Free",10,"bold"),
            padx=7,pady=2,relief="flat",bg="light Yellow",activebackground="black",
            activeforeground="#008B8B",command=lambda:e.Open_Todo(root,B1))
B1.pack(side=RIGHT)

F2 = Frame(root,width=400,height=50,)

Keybindings()

Text = Text(F2,bg="light yellow",padx=15,pady=5,font=("Ink Free",19),relief="flat")
Text.pack(side=TOP,fill=X)

with open(default_open_file) as file:
    Text.insert(1.0,file.read())
    print("the content on screen is \n"+Text.get(1.0,END))


menubar = Menu(root)
root.config(menu=menubar)
File_menubar()
edit_menubar()
view_menubar()
tools_menubar()
help_menubar()


F1.pack(side=BOTTOM, fill=BOTH)                 
F2.pack(side=TOP, fill=BOTH, expand=True)
root.mainloop()


