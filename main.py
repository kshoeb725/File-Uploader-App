from tkinter import *
from tkinter import messagebox,filedialog
import file_uploader

def selectfile():
    files=(("Text files","*.txt"),("All files","*.*"))
    file=filedialog.askopenfilename(initialdir='./',title="upload files",filetypes=files,defaultextension=files)
    if file:
        file_uploader.upload(filename=file)
        messagebox.showinfo("Uploaded",file+"uploaded Successfully")

root=Tk()
root.title("File Uploader Example")
root.geometry("900x320")
root['bg']='blue3'
Label(text="File Uploader Example",bg='black',fg='white',font=15).pack(padx=2,pady=2,fill=X)
uButton=Button(root,text="Upload File",relief=GROOVE,width=20,bd=3,command=selectfile)
uButton.pack(side=LEFT,padx=150)

dButton=Button(root,text="Download File",relief=GROOVE,width=20,bd=3,command=file_uploader.download)
dButton.pack(side=RIGHT,padx=150)
root.mainloop()