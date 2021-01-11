import main
import sys
from tkinter import messagebox
import tkinter as tk
from BikeGUI.ADDSTOCK import add_stock_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Add_to_stock (root)
    add_stock_support.init(root, top)
    root.mainloop()
shp = main.BikeRental()

def shop_inst(bikes):
    shop = main.BikeRental(bikes)
    return shop

w = None
def create_Add_to_stock(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Add_to_stock(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Add_to_stock (w)
    add_stock_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Add_to_stock():
    global w
    w.destroy()
    w = None

class Add_to_stock:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("579x466+660+210")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(0,  0)
        top.title("ADD BIKES")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(x=21, y=114, height=42, width=351)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Yu Gothic UI Semibold} -size 12 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Enter the number of Bicycles you want to add''')


        self.bike_stock_Var = tk.StringVar()

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(x=409, y=124, height=30, width=64)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black", textvariable=self.bike_stock_Var)


        self.btn_save = tk.Button(top)
        self.btn_save.place(x=100, y=320, height=44, width=107)
        self.btn_save.configure(activebackground="#ececec")
        self.btn_save.configure(activeforeground="#000000")
        self.btn_save.configure(background="#d9d9d9")
        self.btn_save.configure(disabledforeground="#a3a3a3")
        self.btn_save.configure(foreground="#000000")
        self.btn_save.configure(highlightbackground="#d9d9d9")
        self.btn_save.configure(highlightcolor="black")
        self.btn_save.configure(pady="0")
        self.btn_save.configure(text='''SAVE''', command=self.save_bikes)



        self.Button1 = tk.Button(top)
        self.Button1.place(x=350, y=320, height=44, width=107)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''CANCEL''', command=root.quit)




    def save_bikes(self):
        shp.stock += int(self.bike_stock_Var.get())
        return messagebox.showinfo("SAVED",  f"You've added {self.bike_stock_Var.get()} bike(s)."), destroy_Add_to_stock()

    def stock_value(self):
        pass

if __name__ == '__main__':
    vp_start_gui()





