from tkinter import *
from turtle import title

class TotalSale():
    def __init__(self,b_window):
        self.b_window=b_window
        self.window=Tk()
        self.window.config(bg="#19191b")
        self.window.geometry("400x400")
        
        frame=Frame(self.window,bg="#19191b")
        
        def totalsale2():
            filepath="C:\\python_programs\\file_content\\StoreAddedProducts.txt"
            file=open(filepath,"r+")
        
            sum=0
            for line in file:
                line.rstrip("\n")
                line=line.split("\t")
                sum+= (float(line[2])*float(line[3]))
            
            file.close()

            
            mylabel.config(text=sum)
            
        totalsale=Label(frame,text="Total Sale=",font="bold",bg="#19191b",fg="white")
        totalsale.grid(row=0,column=0)
        
        global mylabel
        mylabel=Label(frame,text="0.00",bg="#19191b",fg="white",font="bold")
        mylabel.grid(row=0,column=1)
        
        totalsale_update=Button(frame,text="Update",font="bold",bg="#29292c",fg="white",command=totalsale2)
        totalsale_update.grid(row=1,column=0)
        
        back_button=Button(frame,text="Back",font="bold",bg="#29292c",fg="white",command=self.back)
        back_button.grid(row=1,column=2,columnspan=2,pady=20)
        
        frame.pack(pady=50)
        
        self.window.mainloop()

        
    def back(self):
        self.window.destroy()
        self.b_window.deiconify()

    
            
            