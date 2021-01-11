from BikeGUI.ADDSTOCK.add_stock import shp
import main
import bike_gui
import sys
from tkinter import messagebox

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from BikeGUI.RETURNBIKE import return_bike_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = return_bike (root)
    return_bike_support.init(root, top)
    root.mainloop()

w = None
def create_return_bike(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_return_bike(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = return_bike (w)
    return_bike_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_return_bike():
    global w
    w.destroy()
    w = None



class return_bike:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'


        top.geometry("600x450+660+210")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1,  1)
        top.title("RETURN BIKE")
        top.configure(background="#d9d9d9")

        self.Listbox1 = tk.Listbox(top)
        self.Listbox1.place(relx=0.067, rely=0.133, relheight=0.76
                , relwidth=0.44)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")

        for v in bike_gui.names:
            self.Listbox1.insert(tk.END, f"{v.codename}")
        
        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.633, rely=0.422, height=44, width=127)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Return Bike''', command=self.bikeReturn)

    def bikeReturn(self):
        for cus in bike_gui.names:
            bike_gui.names.remove(cus)
            shp.returnBike(cus.returnBike())
            self.Listbox1.delete(tk.ANCHOR)



if __name__ == '__main__':
    vp_start_gui()





