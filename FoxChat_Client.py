from Tkinter import *
import time
import thread

root = Tk()
lb = Label(root, text = "1")

def main():
    
    root.geometry ("700x500")
    root.title ("FoxChat Client")
    lb.pack()

    lb.text = "2"
    
    try:
      thread.start_new_thread(rotater,())
    except:
      print "Error: unable to start thread"
      
    root.mainloop()


def rotater():
    print "thread started"
    while 1:
        time.sleep (1)
        print "printing..."
        lb['text'] = "2"
        time.sleep (1)
        print "printing..."
        lb['text'] = "1"


if __name__ == "__main__":
  main()
