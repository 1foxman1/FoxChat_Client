from Tkinter import *
import time

root = Tk()
root.geometry ("700x500")
root.title ("FoxChat Client")
lb = Label(root, text = "1")
lb.pack()

while 1:
    time.sleep (1000)
    lb.text = "2"
    time.sleep (1000)
    lb.text = "1"
    
    

root.mainloop()
