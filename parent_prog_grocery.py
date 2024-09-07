#window/label=#19191b , buttons= #29292c

from tkinter import *
from tkinter import messagebox

from ParentBranch import *

from sign_up_window import SignUp

from PIL import ImageTk, Image



def click_login():
    
    id_data=employee_text_id.get()
    name_data=employee_text_name.get()
    pass_data=employee_text_pass.get()
    
    id_data=id_data.rstrip("\n")
    name_data=name_data.rstrip("\n")
    pass_data=pass_data.rstrip("\n")    
    
    print(id_data,name_data,pass_data)
    
    filepath="C:\\python_programs\\file_content\\store_id_pass.txt"
    file=open(filepath,"r")
    
    for line in file:
        line=line.rstrip("\n")
        content=line.split("\t")
        print(content)
        flag=False
        
        employee_text_id.delete(0,END)
        employee_text_name.delete(0,END)
        employee_text_pass.delete(0,END)
        
        if(content[0]==id_data and content[1]==name_data and content[2]==pass_data):
            flag=True
            window.withdraw()
            login_window_2()
            print("Matched")
            return

    if(flag==False):
        messagebox.showinfo("wrong id or pass","try again...")
    
    file.close()

def click_signup():
    window.withdraw()
    win=SignUp(window)
    
def click_clear():
    employee_text_id.delete("0",END)
    employee_text_name.delete("0",END)
    employee_text_pass.delete("0",END)


window=Tk()

window.geometry("700x600")
window.config(bg="#19191b")
window.title("grocery program")

frame=Frame(window,bg="#19191b")

img=ImageTk.PhotoImage(Image.open("grocery_store_image.jpg"))
label=Label(window,image=img)

label.pack(pady=10)

employee_id_label=Label(frame,text="Employee Id :",bg="#19191b",fg="white",font="bold")
employee_id_label.grid(row=0,column=0)

employee_name_label=Label(frame,text="Employee name :",bg="#19191b",fg="white",font="bold")
employee_name_label.grid(row=1,column=0)

employee_pass_label=Label(frame,text="Employee password :",bg="#19191b",fg="white",font="bold")
employee_pass_label.grid(row=2,column=0)

employee_text_id=Entry(frame,width=20)
employee_text_id.grid(row=0,column=1,pady=5)

employee_text_name=Entry(frame,width=20)
employee_text_name.grid(row=1,column=1,pady=5)

employee_text_pass=Entry(frame,show="*",width=20)
employee_text_pass.grid(row=2,column=1,pady=5)

frame.pack(pady=20,padx=20)

frame2=Frame(window,bg="#19191b")

login_button=Button(frame2,text="Login",font="bold",fg="white",command=click_login,bg="#29292c")
login_button.grid(row=0,column=0,padx=5)

signup_button=Button(frame2,text="Sign Up",font="bold",fg="white",bg="#29292c",command=click_signup)
signup_button.grid(row=0,column=1,padx=5)

back_button=Button(frame2,text="Clear",font="bold",fg="white",bg="#29292c",command=click_clear)
back_button.grid(row=0,column=2,padx=5)


frame2.pack()
window.mainloop()