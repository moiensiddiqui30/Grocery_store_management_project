from tkinter import *
from tkinter import messagebox
import os

class EditItem():
    def __init__(self,b_window):
        self.b_window=b_window
        self.EditWindow=Tk()
        self.EditWindow.config(bg="#19191b")
        self.EditWindow.geometry("300x300")
        
        frame=Frame(self.EditWindow)
        
        product_id_label=Label(frame,text="Product Id. : ",fg="white",bg="#19191b",font="bold")
        product_id_label.grid(row=0,column=0)
        
        self.product_id_text=Text(frame,height=1,width=20)
        self.product_id_text.grid(row=0,column=1)
        
        # self.my_dict={'id':self.product_id_text}
        
        
        frame.pack(pady=20)
        
        frame1=Frame(self.EditWindow,bg="#19191b")
        
        self.check_button=Button(frame1,text="Check",fg="white",bg="#29292c",font="bold",command=self.to_check)
        self.check_button.grid(row=0,column=0,padx=5)
        
        self.clear_button=Button(frame1,text="clear",fg="white",bg="#29292c",font="bold",command=self.clear)
        self.clear_button.grid(row=0,column=1,padx=5)
        
        self.back_button=Button(frame1,text="Back",fg="white",bg="#29292c",font="bold",command=self.back)
        self.back_button.grid(row=0,column=2,padx=5)
        
        frame1.pack(pady=10)
        
        self.EditWindow.mainloop()
        
    def matched(self):
        
        self.EditWindow.withdraw()
        self.EditWindow1=Tk()
        self.EditWindow1.geometry("600x600")
        self.EditWindow1.config(bg="#19191b")
        
        frame2=Frame(self.EditWindow1,bg="#19191b")
        
        EditName_label=Label(frame2,text="1. Edit name",font="bold",fg="white",bg="#19191b")
        EditName_label.grid(row=0,column=0)
        
        EditPrice_label=Label(frame2,text="2. Edit Price",font="bold",fg="white",bg="#19191b")
        EditPrice_label.grid(row=1,column=0)
        
        EditQuantity_label=Label(frame2,text="3. Edit quantity",font="bold",fg="white",bg="#19191b")
        EditQuantity_label.grid(row=2,column=0)
        
        self.EditName_text=Text(frame2,height=1,width=20)
        self.EditName_text.grid(row=0,column=1)
        
        self.EditPrice_text=Text(frame2,height=1,width=20)
        self.EditPrice_text.grid(row=1,column=1)
        
        self.EditQuantity_text=Text(frame2,height=1,width=20)
        self.EditQuantity_text.grid(row=2,column=1)
        
        
        
        # self.myDict={"name":EditName_text,"price":self.EditPrice_text,"quantity":EditQuantity_text}
        
        frame2.pack(pady=20)
        
        frame3=Frame(self.EditWindow1,bg="#19191b")
        
        self.name_button=Button(frame3,text="1",font="bold",fg="white",bg="#29292c",command=self.editname1)
        self.name_button.grid(row=0,column=0)
        
        self.price_button=Button(frame3,text="2",fg="white",font="bold",bg="#29292c",command=self.editprice)
        self.price_button.grid(row=0,column=1)
        
        self.quantity_button=Button(frame3,text="3",fg="White",font="bold",bg="#29292c",command=self.editquantity)
        self.quantity_button.grid(row=0,column=2)
        
        back_button=Button(frame3,text="BACK",fg="black",bg="white",font="bold",command=self.back2)
        back_button.grid(row=1,column=0,pady=10)
        
        frame3.pack()
        
        
        
        #filepath="D:\\file_content\\store_added_product.txt"
        #file=open(filepath,"a+")
        
        
    def editname1(self):
        p_id=self.product_id_text.get("1.0",END).rstrip("\n")
        p_name=self.EditName_text.get("1.0",END).rstrip("\n")
        print(p_name,p_id)
        
        filepath="C:\\python_programs\\file_content\\StoreAddedProducts.txt"
        file=open(filepath,"r+")
        temp_filepath="C:\\python_programs\\file_content\\temp_StoreAddedProducts.txt"
        temp_file=open(temp_filepath,"a")
        
        for line in file:
            tline=line.split("\t")
            print(tline)
            
            if(tline[0]==p_id):
                line=tline[0]+"\t"+p_name+"\t"+tline[2]+"\t"+tline[3]
                print(line)
                
                temp_file.write(line)
            else:
                temp_file.write(line)
            
        file.close()
        temp_file.close()
        
        messagebox.showinfo("Sucessful","Edited sucessfully")
        
        os.remove(filepath)
        os.rename(temp_filepath,filepath)
        
        
       
            
            
            
    def editprice(self):
        product_id_text=self.product_id_text.get("1.0",END).rstrip("\n")
        EditPrice_text=self.EditPrice_text.get("1.0",END).rstrip("\n")
        print(EditPrice_text,product_id_text)
        
        filepath="C:\\python_programs\\file_content\\StoreAddedProducts.txt"
        file=open(filepath,"r+")
        
        temp_filepath="C:\\python_programs\\file_content\\temp_StoreAddedProducts.txt"
        temp_file=open(temp_filepath,"a")
        
        for line in file:
            tline=line.split("\t")

            if(self.product_id_text==tline[0]):
                line=tline[0]+"\t"+tline[1]+"\t"+str(EditPrice_text)+"\t"+tline[3]
                
            temp_file.write(line)
            
        file.close()
        temp_file.close()
        
        os.remove(filepath)
        os.rename(temp_filepath,filepath)
        
        messagebox.showinfo("Sucessful","Edited sucessfully")
       
        
        
    
    def editquantity(self):
        product_id_text=self.product_id_text.get("1.0",END).rstrip("\n")
        EditQuantity_text=self.EditQuantity_text.get("1.0",END).rstrip("\n")
        
        filepath="C:\\python_programs\\file_content\\StoreAddedProducts.txt"
        file=open(filepath,"r+")
        
        temp_filepath="C:\\python_programs\\file_content\\temp_StoreAddedProducts.txt"
        temp_file=open(temp_filepath,"a")
        
        for line in file:
            tline=line.split("\t")
            tline=line.rstrip("\n")

            if(product_id_text==tline[0]):
                line=tline[0]+"\t"+tline[1]+"\t"+tline[2]+"\t"+str(EditQuantity_text)+"\n"
                
            temp_file.write(line)
            
        file.close()
        temp_file.close()
        
        messagebox.showinfo("Sucessful","Edited Sucessfully")
        
        os.remove(filepath)
        os.rename(temp_filepath,filepath)
        
        
        

    def to_check(self):
        
        product_id=self.product_id_text.get("1.0",END).rstrip("\n")
        print(product_id)
        
        filepath="C:\\python_programs\\file_content\\StoreAddedProducts.txt"
        file=open(filepath,"r+")
        flag=False
        for line in file:
            s_line=line.split("\t")
            
            if(s_line[0]==product_id):
                self.win=self.matched()
                flag=True
                
                
        if(flag==False):
            self.product_id_text.delete("1.0",END)
            messagebox.showinfo("Invalid","No such product found")
            
        file.close()
        
        
        
        
    def clear(self):
        self.product_id_text.delete("1.0",END)
        
        
    def back(self):
        self.EditWindow.destroy()
        self.b_window.deiconify()
        
    def back2(self):
        self.EditWindow1.destroy()
        self.EditWindow.deiconify()
        
    