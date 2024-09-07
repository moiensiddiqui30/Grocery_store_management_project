from tkinter import *

class Display_window_product:
    def __init__(self,b_window):
        self.b_window=b_window
        self.display_window=Tk()
        self.display_window.config(bg="#19191b")
        self.display_window.geometry("900x400")
        
        self.frame_a=Frame(self.display_window)
        
        self.productId_label=Label(self.frame_a,text="Product Id",width=20,font="bold",bg="#19191b",fg="white")
        self.productId_label.grid(row=0,column=0)
        
        self.productName_label=Label(self.frame_a,text="Product Name",width=20,font="bold",bg="#19191b",fg="white")
        self.productName_label.grid(row=0,column=1)
        
        self.productPrice_label=Label(self.frame_a,text="Product Price",width=20,font="bold",bg="#19191b",fg="white")
        self.productPrice_label.grid(row=0,column=2)
        
        self.productQuantity_label=Label(self.frame_a,text="Product Quantity",width=20,font="bold",bg="#19191b",fg="white")
        self.productQuantity_label.grid(row=0,column=3)
        
        
        file=open("C:\\python_programs\\file_content\\StoreAddedProducts.txt","r+")
        r=0
        for line in file:
            r+=1
            line=line.rstrip("\n")
            list_line=line.split("\t")
            
            product_id_t=Entry(self.frame_a,width=20,font="bold")
            product_id_t.insert(0,str(list_line[0]))
            product_id_t.grid(row=r,column=0)
        
        
            product_name_t=Entry(self.frame_a,width=20,font="bold")
            product_name_t.insert(0,str(list_line[1]))
            product_name_t.grid(row=r,column=1)
        
        
            product_price_t=Entry(self.frame_a,width=20,font="bold")
            product_price_t.insert(0,str(list_line[2]))
            product_price_t.grid(row=r,column=2)
        
        
            product_quantity_t=Entry(self.frame_a,width=20,font="bold")
            product_quantity_t.insert(0,str(list_line[3]))
            product_quantity_t.grid(row=r,column=3)
            
        file.close()
            
        
        self.frame_a.pack(pady=20)
        
        self.frame_b1=Frame(self.display_window)
        
        self.back=Button(self.frame_b1,text="BACK",font="bold",bg="#29292c",fg="white",command=self.back)
        self.back.grid(row=0,column=0,columnspan=1)

        self.frame_b1.pack(pady=20)
        
        self.display_window.mainloop()
        
    def back(self):
        self.display_window.destroy()
        self.b_window.deiconify()
