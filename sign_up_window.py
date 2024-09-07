
from tkinter import *
from tkinter import messagebox

class SignUp:
    def __init__(self,window) -> None:
        self.window=window
        self.sign_window=Tk()
        self.sign_window.config(bg="#19191b")
        self.sign_window.geometry("500x400")
        
        
        frame=Frame(self.sign_window)
        frame.config(bg="#19191b")
        
        
        employee_id_label=Label(frame,text="Employee ID. ",font="bold",fg="white",bg="#19191b")
        employee_id_label.grid(row=0,column=0)
        
        
        employee_name_label=Label(frame,text="Employee Name ",fg="white",bg="#19191b",font="bold")
        employee_name_label.grid(row=1,column=0)
        
        
        employee_passward_label=Label(frame,text="Employee Passward  ",font="bold",fg="white",bg="#19191b")
        employee_passward_label.grid(row=2,column=0)
        
        self.employee_name_text=Entry(frame,width=20)
        self.employee_name_text.grid(row=1,column=1)
        
        self.employee_passward_text=Entry(frame,width=20)
        self.employee_passward_text.grid(row=2,column=1)
        
        self.employee_id_text=Entry(frame,width=20)
        self.employee_id_text.grid(row=0,column=1)
        
        frame.pack(pady=50)
        
        frame1=Frame(self.sign_window)
        
        sign_up_button=Button(frame1,text="Sign Up",font="bold",bg="black",fg="white",command=self.signup)
        sign_up_button.grid(row=0,column=1)
        
        clear_button=Button(frame1,text="Clear",font="bold",bg="black",fg="white",command=self.clear)
        clear_button.grid(row=0,column=0)
        
        back_button=Button(frame1,text="Back",font="bold",bg="black",fg="white",command=self.back)
        back_button.grid(row=0,column=2)
        
        
        
        frame1.pack(pady=10)
        
        self.sign_window.mainloop()

    def signup(self):
        E_id=self.employee_id_text.get().rstrip("\n")
        E_name=self.employee_name_text.get().rstrip("\n")
        E_pass=self.employee_passward_text.get().rstrip("\n")
        
        filepath="C:\\python_programs\\file_content\\store_id_pass.txt"
        file=open(filepath,"a+")
        
        t_line=[E_id,E_name,E_pass]
        
        for i in range(0,3,1):
            if(i==1):
                file.write(t_line[i]+"\t")
            elif(i==0):
                file.write(t_line[i]+"\t")
            else:
                file.write(t_line[i]+"\n")
                
        messagebox.showinfo("sucessful","Signed up sucessfully")

        file.close()

    def clear(self):
        self.employee_name_text.delete("0",END)
        self.employee_passward_text.delete("0",END)
        self.employee_id_text.delete("0",END)

    def back(self):
        self.sign_window.destroy()
        self.window.deiconify()
    
        
        
    