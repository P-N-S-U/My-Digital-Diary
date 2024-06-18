import os
from tkinter import * 
from tkinter import colorchooser
from tkinter import filedialog
import pyttsx3
import speech_recognition as sr
import time


class file_fncs():

    def __init__(self):
        self.current_file = None

    def new_file(self,text_widget):
        text_widget.delete(1.0,END)
        self.current_file = None
        print("new file")



    def save_file(self,text_widget,window):
        if self.current_file:
            try:
                with open(self.current_file,"w") as file:
                    file.write(text_widget.get(1.0,END))
                    print("you save current known file")
                window.title("My diary")
            except EXCEPTION as e :
                print("couldn't save the file:",e)
        else:
            file = filedialog.asksaveasfilename(initialfile=time.strftime("%Y-%b-%d",time.localtime()),defaultextension=".txt", file=[("All files","*.*"), ("Text file","*.txt")])
            if file:
                try:
                    with open(file,"w") as file:
                        file.write(text_widget.get(1.0,END))
                    self.current_file=file.name
                    window.title("My diary")
                except Exception as e:
                    print("couldn't save this file: ",e)

    def open_file(self,text_widget):
        file = filedialog.askopenfilename(defaultextension=".txt", file=[("All files", "*.*"), ("Text file", "*.txt")])
        if file:
            try:
                text_widget.delete(1.0, 'end')
                with open(file, "r") as file:
                    text_widget.insert(1.0, file.read())
                self.current_file = file.name
            except Exception as e:
                print("Couldn't read file:", e)
        
        print("you open a file")
   
    #-----------------------------------------------

    def copy(self,Text_widget):
        Text_widget.event_generate("<<Copy>>")

    def cut(self,Text_widget):
        Text_widget.event_generate("<<Cut>>")

    def paste(self,Text_widget):
        Text_widget.event_generate("<<Paste>>")

class view_MENU():

    def __init__(self):
        self.COLOR = "light yellow"
    
    def Change_Font(self,Text_widget,font_family,):
       Text_widget.config(font=(font_family))


    def Default_fg(seld,Text_widget):
        Text_widget.config(fg="black")

    def more_color_fg(self,Text_widget):
        color = colorchooser.askcolor(title='pick a color')
        Text_widget.config(fg=color[1])
    
    def Default_bg(self,Text_widget,F1,L1,B1):
        Text_widget.config(bg="light yellow")
        F1.config(bg="light yellow")
        L1.config(bg="light yellow")
        B1.configure(bg="light yellow")

    def presets (self,text_widget,choice,F1,L1,B1):
        if choice==1:
            text_widget.config(bg="light blue")
            self.COLOR = "light blue"
        elif choice==2:
            text_widget.config(bg="light pink")
            self.COLOR = "light pink"
        elif choice ==3:
            text_widget.config(bg="#f08080")
            self.COLOR = "#f08080"
        elif choice==4:
            text_widget.config(bg="light Green")
            self.COLOR = "light Green"

        F1.config(bg=self.COLOR)
        L1.config(bg=self.COLOR)
        B1.configure(bg=self.COLOR)


    def more_color_bg(self,Text_widget,F1,L1,B1):
        color = colorchooser.askcolor(title='pick a color')
        Text_widget.config(bg=color[1])
        F1.config(bg=color[1])
        L1.config(bg=color[1])
        B1.configure(bg=color[1])

    def Dark_mode(self,Text_widget,F1,L1,B1):
        Text_widget.config(bg="#1E1E1E",fg="#008B8B")
        self.COLOR = "#1E1E1E"
        F1.config(bg=self.COLOR)
        L1.config(bg=self.COLOR)
        B1.configure(bg=self.COLOR,fg="#008B8B")

class Tools_MENU():
    
    
    def text_to_speech(self,text_widget):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text_widget.get(1.0,END))
        engine.runAndWait()

    def speech_to_text(self,text_widget,curr_file):
        
        r=sr.Recognizer()

        with sr.Microphone() as source:
            print("\nstart speaking \nnow:...")
            audio_text = r.listen(source)
            print("time over")
        
        try:
            print("text:"+ r.recognize_google(audio_text))
        except:
            print("cannot listen properly")

        try:
            with open(curr_file,"a") as f:
                f.write(r.recognize_google(audio_text)+"\n")
        except Exception as e:
            print("some error occured",e)

        with open(curr_file,"r") as f:
            text_widget.delete(1.0,END)
            text_widget.insert(1.0,f.read())
                 
class help_MENU():
    
    def shorcuts(self):
        Shortcut ="""
        1. Copy \t\t Ctrl+C
        2. Cut \t\t Ctrl+X
        3. Paste \t\t Ctrl+V
        ---------------------------------------
        4. New Page \t\t Ctrl+N
        5. Open Page \t\t Ctrl+O
        6. Save Page \t\t Ctrl+S
        ---------------------------------------
        7. Text to Speech \t Alt+Enter
        7. Speech to Text \t Shift+Enter
        """
        new_window = Toplevel()
        new_window.geometry("450x310")
        new_window.title("Shortcut Keys")
        L1 = Label(new_window,text=Shortcut,font=("Papyrus", 15),justify="left",bg="light Cyan",fg="dark Blue")
        L1.pack(fill=BOTH)
        

    def About_us(self):
        About=""" Team mates: 1. Mitali Salunke
        \t2. Archi Patil
        \t3. Swaraj Pasilkar
        \t4. Priyanshu Malusare
        Contributions:
        - Morale Support by : \n\tMitali,Archi,Swaraj
        """
        new_window = Toplevel()
        new_window.geometry("280x250")
        new_window.title("About Us")
        L1 = Label(new_window,text=About,font=("Papyrus", 15),justify="left")
        L1.pack(fill=BOTH)
           
class TODO():
    def Open_Todo(self,root,B1):                    #new to add in the main py
        global new_todo
        new_todo = Toplevel(root,bg="light blue")
        new_todo.title("Todo List")
        new_todo.geometry("220x250")
        new_todo.resizable(0,0)
        B1.config(state=DISABLED)
        new_todo.protocol("WM_DELETE_WINDOW",lambda: self.close_todo(B1))
        self.todo_design()
    
    def close_todo(self,B1):                   #new to add in main py
        new_todo.destroy()
        B1.config(state=NORMAL)

    def todo_design(self):
        TODO = Listbox(new_todo,bg="sky blue",height=9,width=23,relief="flat",activestyle = "none",cursor="cross",font=("Consolas",12))
        TODO.grid(row=0,padx=3,pady=2,columnspan=2)

        add_todo = Entry(new_todo,width=28)
        add_todo.insert(0,"Enter Tasks")
        add_todo.bind("<FocusOut>", lambda event: add_todo.insert(0, "Enter Tasks") if add_todo.get()=="" else None)
        add_todo.bind("<FocusIn>", lambda event: add_todo.delete(0, END) if add_todo.get() == "Enter Tasks" else None)
        add_todo.bind("<Return>", lambda event : self.add_tasks(add_todo,TODO))
        
        add_todo.grid(row=1,column=0,padx=5,pady=5)

        save_B = Button(new_todo,text="✅",command= lambda: self.add_tasks(add_todo,TODO))
        save_B.grid(row=1,column=1,padx=5,pady=5)

        complete_B = Button(new_todo,text="Task Completed",width=28,font=("Consolas", 9),command= lambda: self.complete_task(TODO))
        complete_B.grid(row=2,columnspan=2)
        self.load_tasks(TODO)

    def add_tasks(self,entry,listbox):
            print("task added to the todo")
            task = entry.get()
            if task:
                listbox.insert(END, task)
                entry.delete(0,END)  
                self.save_tasks(listbox)

    def complete_task(self,listbox):
        try:
            task_index = listbox.curselection()[0]
            listbox.delete(task_index)
            self.save_tasks(listbox)
            print("you completed task")
        except IndexError:
            pass
    
    def save_tasks(self,listbox):
        with open("files\\TODO", "w") as file:
            tasks = listbox.get(0,END)
            for task in tasks:
                file.write(task + "\n")

    def load_tasks(self,listbox):
        try:
            with open("files\\TODO", "r") as file:
                tasks = file.readlines()
                for task in tasks:
                    listbox.insert(END, task.strip())
        except FileNotFoundError:
            pass
