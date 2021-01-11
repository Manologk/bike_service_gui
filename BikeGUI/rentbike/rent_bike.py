from tkinter import messagebox
import main, bike_gui
import datetime
from BikeGUI.ADDSTOCK.add_stock import shp


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

from BikeGUI.rentbike import rent_bike_support

# customer = main.Customer()
#
# customer.rentalTime = datetime.datetime.now()

def addcus(nam, bik, rntB):
    bike_gui.namer()
    bike_gui.names[-1] = main.Customer(nam, bik, rntB)
    return (bike_gui.names[-1])


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    rent_bike_support.set_Tk_var()
    top = Rent_Bike (root)
    rent_bike_support.init(root, top)
    root.mainloop()

w = None
def create_Rent_Bike(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Rent_Bike(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    rent_bike_support.set_Tk_var()
    top = Rent_Bike (w)
    rent_bike_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Rent_Bike():
    global w
    w.destroy()
    w = None

class Rent_Bike:
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
        top.title("RENT A BIKE")
        top.configure(background="#d9d9d9")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.05, rely=0.156, height=31, width=74)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''CodeName:''')

        #tkinter varible
        self.customername = tk.StringVar()

        self.codename = tk.Entry(top)
        self.codename.place(relx=0.25, rely=0.156, height=30, relwidth=0.423)
        self.codename.configure(background="white")
        self.codename.configure(disabledforeground="#a3a3a3")
        self.codename.configure(font="TkFixedFont")
        self.codename.configure(foreground="#000000")
        self.codename.configure(insertbackground="black", textvariable=self.customername)


        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.05, rely=0.311, height=21, width=94)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Number of Bikes:''')

        self.num_of_bikes = tk.StringVar()
        #number of bikes


        self.price = tk.Entry(top)
        self.price.place(relx=0.25, rely=0.311, height=20, relwidth=0.09)
        self.price.configure(background="white")
        self.price.configure(disabledforeground="#a3a3a3")
        self.price.configure(font="TkFixedFont")
        self.price.configure(foreground="#000000")
        self.price.configure(insertbackground="black", textvariable=self.num_of_bikes)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.05, rely=0.489, height=21, width=104)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Select Your Service:''')

        self.Radiobutton1 = tk.Radiobutton(top)
        self.Radiobutton1.place(relx=0.217, rely=0.489, relheight=0.056
                , relwidth=0.197)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#d9d9d9")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(text='''hourly    @5$''')
        self.Radiobutton1.configure(variable=rent_bike_support.selected, value=1)

        self.Radiobutton2 = tk.Radiobutton(top)
        self.Radiobutton2.place(relx=0.217, rely=0.556, relheight=0.056
                , relwidth=0.197)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#d9d9d9")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify='left')
        self.Radiobutton2.configure(text='''Daily    @20$''')
        self.Radiobutton2.configure(variable=rent_bike_support.selected, value=2)

        self.Radiobutton3 = tk.Radiobutton(top)
        self.Radiobutton3.place(relx=0.2, rely=0.622, relheight=0.056
                , relwidth=0.247)
        self.Radiobutton3.configure(activebackground="#ececec")
        self.Radiobutton3.configure(activeforeground="#000000")
        self.Radiobutton3.configure(background="#d9d9d9")
        self.Radiobutton3.configure(disabledforeground="#a3a3a3")
        self.Radiobutton3.configure(foreground="#000000")
        self.Radiobutton3.configure(highlightbackground="#d9d9d9")
        self.Radiobutton3.configure(highlightcolor="black")
        self.Radiobutton3.configure(justify='left')
        self.Radiobutton3.configure(text='''Weekly   @60$''')
        self.Radiobutton3.configure(variable=rent_bike_support.selected, value=3)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.35, rely=0.844, height=34, width=147)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Confirm''', command=self.confirm_hour)



    def confirm_hour(self):
        customer = addcus(self.customername.get(), self.num_of_bikes.get(), rent_bike_support.selected.get())
        #get number of bikes from entry
        customer.bikes = int(self.num_of_bikes.get())
        customer.rentalBasis = rent_bike_support.selected.get()
        customer.codename = self.customername.get()

        if customer.rentalBasis == 1:
            if shp.stock < int(customer.bikes):
                messagebox.showinfo("Sorry", "Sorry we don't have enough bikes.")
            else:
                # shp.rentBikeOnHourlyBasis(int(customer.bikes))
                customer.rentalTime = shp.rentBikeOnHourlyBasis(int(customer.requestBike()))
                customer.rentalBasis = 1
                return messagebox.showinfo("confirm", f"You have rented {customer.bikes} bikes"
                                                   f" on an hourly basis and you will be charged 5$ per bike\n"
                                                   f" hope you enjoy our services"), destroy_Rent_Bike()
        elif customer.rentalBasis == 2:
            if shp.stock < int(customer.bikes):
                messagebox.showinfo("Sorry", "Sorry we don't have enough bikes.")
            else:
                customer.rentalTime = shp.rentBikeOnHourlyBasis(int(customer.requestBike()))
                customer.rentalBasis = 2
                return messagebox.showinfo("confirm", f"You have rented {customer.bikes} bikes"
                                                   f" on a weekly basis and you will be charged 20$ per bike\n"
                                                   f" hope you enjoy our services"), destroy_Rent_Bike()
        elif customer.rentalBasis == 3:
            if shp.stock < int(customer.bikes):
                messagebox.showinfo("Sorry", "Sorry we don't have enough bikes.")
            else:
                customer.rentalTime = shp.rentBikeOnHourlyBasis(int(customer.requestBike()))
                customer.rentalBasis = 3
                return messagebox.showinfo("confirm", f"You have rented {customer.bikes} bikes"
                                                   f" on a weekly basis and you will be charged 60$ per bike\n"
                                                   f" hope you enjoy our services"), destroy_Rent_Bike()
        else:
            return "Please enter choose a plan"



if __name__ == '__main__':
    vp_start_gui()





