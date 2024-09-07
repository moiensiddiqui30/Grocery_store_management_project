import os
from tkinter import *
from tkinter import messagebox


class DelItem():
    def __init__(self,b_window):
        self.b_window=b_window
        self.DelWindow=Tk()
        self.DelWindow.config(bg="#19191b")
        self.DelWindow.geometry("300x300")
        
        frame=Frame(self.DelWindow,bg="#19191b")
        
        product_id_label=Label(frame,text="Product Id. : ",fg="white",bg="#19191b",font="bold")
        product_id_label.grid(row=0,column=0)
        
        self.product_id_text=Text(frame,height=1,width=20)
        self.product_id_text.grid(row=0,column=1)
        
        
        frame.pack(pady=20)
        
        frame3=Frame(self.DelWindow,bg="#19191b")
        
        self.check_button=Button(frame3,text="Delete",fg="white",bg="#29292c",font="bold",command=self.delete)
        self.check_button.grid(row=0,column=0,padx=5)
        
        self.clear_button=Button(frame3,text="clear",fg="white",bg="#29292c",font="bold",command=self.clear)
        self.clear_button.grid(row=0,column=1,padx=5)
        
        self.back_button=Button(frame3,text="Back",fg="white",bg="#29292c",font="bold",command=self.back)
        self.back_button.grid(row=0,column=2,padx=5)
        
        frame3.pack(pady=10)
        
        self.DelWindow.mainloop()

    def back(self):
        self.DelWindow.destroy()
        self.b_window.deiconify()
    
    
    def clear(self):
        self.product_id_text.delete("1.0",END)
        
        
    def delete(self):
        p_id=self.product_id_text.get("1.0",END).rstrip("\n")
        print(p_id)
        
        filepath="C:\\python_programs\\file_content\\StoreAddedProducts.txt"
        file=open(filepath,"r+")
        
        temp_filepath="C:\\python_programs\\file_content\\temp_StoreAddedProducts.txt"
        temp_file=open(temp_filepath,"a")
        
        for line in file:
            t_line=line.split("\t")
            
            if(t_line[0]==p_id):
                continue
            else:
                temp_file.write(line)
        
        file.close()
        temp_file.close()
        
        os.remove(filepath)
        os.rename(temp_filepath,filepath)
        
        messagebox.showinfo("Sucessfull","Deleted sucessfully")