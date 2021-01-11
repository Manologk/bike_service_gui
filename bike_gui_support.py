import sys
from BikeGUI.ADDSTOCK import add_stock
from BikeGUI.rentbike import rent_bike
from BikeGUI.RETURNBIKE import return_bike

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

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def addstock():
    add_stock.create_Add_to_stock(root)

def rentbikes():
    rent_bike.create_Rent_Bike(root)

def returnbike():
    return_bike.create_return_bike(root)

if __name__ == '__main__':
    import bike_gui
    bike_gui.vp_start_gui()





