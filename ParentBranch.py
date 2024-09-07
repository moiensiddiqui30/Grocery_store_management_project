from tkinter import *
from add_product import Additem
from delete_product import DelItem
from display_product_window import Display_window_product
from edit_product import EditItem
from total_sale import TotalSale


def add_item():
    b_window.withdraw()
    win=Additem(b_window)
    
def edit_item():
    b_window.withdraw()
    win=EditItem(b_window)
    
def display_window():
    b_window.withdraw()
    win=Display_window_product(b_window)
    
def delete_item():
    
    b_window.withdraw()
    win=DelItem(b_window)

def exit_window1():
    b_window.destroy()
    
def Total_sale():
    b_window.withdraw()    
    win=TotalSale(b_window)

def login_window_2():
    global b_window
    
    b_window=Tk()
    b_window.geometry("600x400")
    b_window.config(bg="#19191b")
    b_window.title("branch_1")
    
    frame1=Frame(b_window,bg="#19191b")
    
    common_var=0
    add_product=Radiobutton(frame1,text="Add a new product",variable=common_var,value=1,font="bold",fg="white",bg="#19191b",command=add_item)
    add_product.pack(pady=5)
    
    display_product=Radiobutton(frame1,text="Display products",variable=common_var,value=2,font="bold",fg="white",bg="#19191b",command=display_window)
    display_product.pack(pady=5)
    
    Edit_product=Radiobutton(frame1,text="Edit products",variable=common_var,value=3,font="bold",fg="white",bg="#19191b",command=edit_item)
    Edit_product.pack(pady=5)
    
    delete_product=Radiobutton(frame1,text="Delete products",variable=common_var,value=4,font="bold",fg="white",bg="#19191b",command=delete_item)
    delete_product.pack(pady=5)
    
    total_sale_product=Radiobutton(frame1,text="Total sale of product",variable=common_var,value=5,font="bold",fg="white",bg="#19191b",command=Total_sale)
    total_sale_product.pack(pady=5)
    
    exit=Radiobutton(frame1,text="exit",variable=common_var,value=6,font="bold",fg="white",bg="#19191b",command=exit_window1)
    exit.pack(pady=5)
    
    
    frame1.pack(pady=10)
    
    
    b_window.mainloop()
