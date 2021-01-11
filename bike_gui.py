import tkinter as tk
import main
import bike_gui_support
from BikeGUI.ADDSTOCK import add_stock
from tkinter import messagebox
from BikeGUI.RETURNBIKE import return_bike


names = list()
def namer():
    i = 0
    while True:
        i += 1
        name = f"customer_{i}"
        #print(name)
        if name not in names:
            names.append(name)
            break
    return name

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1(root)
    bike_gui_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    bike_gui_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("738x749+410+110")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1, 1)
        top.title("bike rental")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=-0.014, rely=-0.013, relheight=1.04
                          , relwidth=1.057)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.0, rely=0.0, height=156, width=778)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#bc4639")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Showcard Gothic} -size 24 -weight bold -underline 1")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Happy Bikes''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.154, rely=0.321, height=54, width=187)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#5c2018")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''ADD STOCK''', command=bike_gui_support.addstock)


        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.526, rely=0.321, height=54, width=187)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#5c2018")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''RENT A BIKE''', command=bike_gui_support.rentbikes)

        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.154, rely=0.565, height=54, width=187)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#5c2018")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#ffffff")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''CHECK STOCK''', command=self.stck_disp)

        self.Button4 = tk.Button(self.Frame1)
        self.Button4.place(relx=0.526, rely=0.565, height=54, width=187)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#5c2018")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#ffffff")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''RETURN A BIKE''', command=bike_gui_support.returnbike)

    def stck_disp(self):
        return messagebox.showinfo("STOCK",f"{add_stock.shp.displaystock()}")

if __name__ == '__main__':
    vp_start_gui()
