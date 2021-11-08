from tkinter import *
import os
from glob import glob
from tkinter import filedialog, ttk, messagebox, simpledialog
from pathlib import Path
import shutil

"""
- press open folder button can open folder, file will no response
- press back button can go to previous folder
"""

class EditPage(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        # self.keyboard = virtual_keyboard.Virtual_Keyboard(self)
        self.currently_working = os.path.join(os.getcwd(),"videos")
        self.files = os.listdir(self.currently_working) # glob(r"C:\Users\ASUSuser\PiRecorder\videos\*")
        self.copy_item = ""
        self.copy_item_path = ""
        self.paste_item_path = ""
        self.user_input = ""
        self.mode = None

    def show_editpage(self):
        top = Toplevel(self)
        top.title("Edit Page")
        top.geometry("800x440+0+0")

        self.main_frame = Frame(top,width=800,height=440)
        self.main_frame.pack(expand=True, fill=BOTH)

        self.canvas = Canvas(self.main_frame, borderwidth=0, background="blue",scrollregion=(0,0,800,440))
        self.canvas.pack(side="left", fill="both", expand=True)

        self.frame = Frame(self.canvas, background="blue")
        self.frame2 = Frame(self.canvas, background="white")

        self.canvas.create_window((50,50), window=self.frame, anchor="nw",
                                  tags="self.frame")
        self.canvas.create_window((50,20), window=self.frame2, anchor="nw",
                                  tags="self.frame2")


        self.vbar=Scrollbar(self.frame)
        self.vbar.pack(side=RIGHT,fill=Y)

        for row,file in enumerate(self.files):
            self.listbox = Listbox(self.frame,yscrollcommand = self.vbar.set,height=20,width=100,selectmode='extended')
            for file in self.files:
                self.listbox.insert('end', os.path.basename(file))
        self.listbox.pack(side=LEFT,fill=BOTH)

        self.vbar.config(command=self.listbox.yview )

        self.buttons = [
                        '~','`','!','@','#','$','%','^','&','*','(',')','-','_','ENTER',
                        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p','\\','7','8','9','BACK',
                        'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','[',']','4','5','6'
                        ,'TAB',
                        'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.','?','/','1','2','3','SPACE',
                        ]

        self.button_open_folder = Button(self.frame,text="Open Folder", command=lambda: self.open_folder())
        self.button_open_folder.pack(fill="x",padx=5,pady=5)

        self.button_back = Button(self.frame,text="Back", command=lambda: self.back())
        self.button_back.pack(fill="x",padx=5,pady=5)

        self.button_create_folder = Button(self.frame,text="Create Folder", command=lambda: self.create_folder())
        self.button_create_folder.pack(fill="x",padx=5,pady=5)

        self.button_delete = Button(self.frame,text="Delete", command=lambda: self.delete())
        self.button_delete.pack(fill="x",padx=5,pady=5)

        self.button_rename = Button(self.frame,text="Rename", command=lambda: self.rename())
        self.button_rename.pack(fill="x",padx=5,pady=5)

        self.button_copy = Button(self.frame,text="Copy", command=lambda: self.copy())
        self.button_copy.pack(fill="x",padx=5,pady=5)

        self.button_paste = Button(self.frame,text="Paste", command=lambda: self.paste())
        self.button_paste.pack(fill="x",padx=5,pady=5) 

        self.button_update = Button(self.frame,text="Update", command=lambda: self.update())
        self.button_update.pack(fill="x",padx=5,pady=5) 

        self.path_label = Label(self.frame2,text=self.currently_working)
        self.path_label.config(text=self.currently_working, width=85)
        self.path_label.pack(fill="x") 

    def open_folder(self):
        try:
            self.folder = self.listbox.get( self.listbox.curselection())
        
            if Path(os.path.join(str(self.currently_working),str(self.folder))).is_dir():
                # self.old_files = self.files
                self.currently_working = os.path.join(str(self.currently_working),str(self.folder))
                os.chdir(self.currently_working)
                self.files = os.listdir(self.currently_working)
                self.update_listbox()
        

        # change directory into the folder and display in listbox is the cursor selection is folder instead of file
        
        except Exception as e:
            messagebox.showinfo( "Warning" , "Please select a folder/file")

    def create_folder(self):

        self.mode = "create_folder"
        self.show_keyboard(question="New folder name:")

    def delete(self):

        self.target_delete_item = self.listbox.get( self.listbox.curselection())

        self.target_delete_item_path = os.path.join(self.currently_working,self.target_delete_item)
        try:
            if os.path.isdir(self.target_delete_item_path):
                shutil.rmtree(self.target_delete_item_path)
            elif os.path.isfile(self.target_delete_item_path):
                os.remove(self.target_delete_item_path)
        except:
            pass
        self.files = os.listdir(self.currently_working)
        self.update_listbox()

    def rename(self):

        self.mode = "rename"

        self.old_name = self.listbox.get( self.listbox.curselection())
        self.show_keyboard(question="Rename:")
        

    def copy(self):

        self.copy_item = self.listbox.get( self.listbox.curselection())
        self.copy_item_path = os.path.join(self.currently_working,self.copy_item)
        

    def paste(self):
        self.paste_item_path = os.path.join(self.currently_working,self.copy_item)
    
        if os.path.isfile(self.copy_item_path):
            shutil.copy(self.copy_item_path,self.paste_item_path)
        elif os.path.isdir(self.copy_item_path):
            shutil.copytree(self.copy_item_path,self.paste_item_path)
        self.files = os.listdir(self.currently_working)
        
        self.update_listbox
        self.update_listbox

    def back(self):
       
        self.old_files = self.files
        os.chdir("..")
        self.files = os.listdir()
        self.currently_working = os.path.dirname(self.currently_working)
        self.update_listbox()
    
    def update_listbox(self):

        self.listbox.delete(0, END)

        if self.files == []:
            self.listbox.insert("end","The folder is empty")
        else:
            for row,file in enumerate(self.files):
                self.listbox.insert('end', os.path.basename(file))
        
        self.listbox.pack(side=LEFT,fill=BOTH)
        self.path_label.config(text=self.currently_working, width=85)

    def update(self):
        self.files = os.listdir(self.currently_working)
        self.update_listbox()

    ######################### virtual keyboard ################################

    def select(self,value):
        if value == "BACK":
            # allText = entry.get()[:-1]
            # entry.delete(0, tkinter,END)
            # entry.insert(0,allText)

            self.entry.delete(len(self.entry.get())-1,END)
            
        elif value == "SPACE":
            self.entry.insert(END, ' ')
        elif value == "ENTER":
            self.user_input = self.entry.get()
            if self.mode == "create_folder":
                os.mkdir(os.path.join(self.currently_working,self.user_input))
                self.keyboard.destroy()
            elif self.mode == "rename":
                os.rename(os.path.join(self.currently_working,self.old_name),os.path.join(self.currently_working,self.user_input))
                self.keyboard.destroy()
        elif value == "TAB":
            self.entry.insert(END, '  ')
        else :
            self.entry.insert(END,value)

    def HosoPop(self):

        varRow = 2
        varColumn = 0

        for button in self.buttons:

            command = lambda x=button: self.select(x)
            
            if button == "SPACE" or button == "TAB" or button == "BACK" or button == "ENTER":
                Button(self.frame,text= button,width=10,height=3, bg="#3c4987", fg="#ffffff",
                    activebackground = "#ffffff", activeforeground="#3c4987", relief='raised', padx=1,
                    pady=1, bd=1,command=command).grid(row=varRow,column=varColumn)

            else:
                Button(self.frame,text= button,width=5,height=3, bg="#3c4987", fg="#ffffff",
                    activebackground = "#ffffff", activeforeground="#3c4987", relief='raised', padx=1,
                    pady=1, bd=1,command=command).grid(row=varRow,column=varColumn)


            varColumn +=1 

            if varColumn > 14 and varRow == 2:
                varColumn = 0
                varRow+=1
            if varColumn > 14 and varRow == 3:
                varColumn = 0
                varRow+=1
            if varColumn > 14 and varRow == 4:
                varColumn = 0
                varRow+=1

    def show_keyboard(self,question):
        self.keyboard = Toplevel(self)
        self.keyboard.resizable(0,0)
        self.frame = Frame(self.keyboard,width=800,height=440)
        self.keyboard.title("virtual keyboard")
        self.frame.pack(expand=True, fill=BOTH)
        
        self.label1 = Label(self.frame,text=question).grid(row=0,columnspan=15)

        self.entry = Entry(self.frame,width=50)
        self.entry.grid(row=1,columnspan=15)
        # entry.pack()

        self.entry.bind("<Button-1>", lambda e: self.HosoPop())

    #####################################################################################
        
if __name__ == "__main__":
    root = Tk()
    EditPage(root).pack(side="top", fill="both", expand=True)
    root.mainloop()