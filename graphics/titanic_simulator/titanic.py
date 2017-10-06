"""
Beispiel für eine graphische Oberfläche
mit Tkinter.

Siehe Dokumentation unter 
https://docs.python.org/3/library/tk.html
und
https://docs.python.org/3/library/tkinter.html
"""
import tkinter as tk
from PIL import Image, ImageTk



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.titanic = Image.open("titanic.png")
        self.titanic2 = Image.open("titanic2.png")
        self.pack()
        self.create_widgets()

    def sos(self):
        print("SOS - wir sinken!")

    def kollision_mit_eisberg(self):
        photo = ImageTk.PhotoImage(self.titanic2)
        self.canvas.image = photo
        self.im = self.canvas.create_image(0, 0, image=photo, anchor='nw')
        
    def create_widgets(self):
        photo = ImageTk.PhotoImage(self.titanic)
        self.canvas = tk.Canvas(self, width=700, height=178, bg='black') 
        self.canvas.pack(side='top', fill='both', expand='yes')
        self.canvas.image = photo # keep a reference!
        self.im = self.canvas.create_image(0, 0, image=photo, anchor='nw')

        self.quit = tk.Button(self, text="Von Bord gehen", 
                              command=root.destroy)
        self.quit.pack(side="bottom", fill="both", expand="yes")
        
        self.versenken = tk.Button(self, fg="red")
        self.versenken["text"] = "S.O.S. funken"
        self.versenken["command"] = self.sos
        self.versenken.pack(side="bottom", fill="both", expand="yes")

        self.versenken = tk.Button(self)
        self.versenken["text"] = "Weiterfahren"
        self.versenken["command"] = self.kollision_mit_eisberg
        self.versenken.pack(side="bottom", fill="both", expand="yes")



root = tk.Tk()
app = Application(master=root)
app.master.title("Titanic-Simulator 1.0")
app.mainloop()