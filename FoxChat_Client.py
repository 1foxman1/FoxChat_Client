from Tkinter import *
import tkFont
import time
import thread

root = Tk()
username = ""
servIP = ""

ipEntry = Entry(root, width = 30,)
userEntry = Entry(root, width = 30)

def main():
    
    root.geometry ("700x500")
    root.title ("FoxChat Client")
    
    ipLabel = Label(root,
               text = "Enter chat server IP: ",
               relief = "ridge",
               font = tkFont.Font(size = 15))
    
    
    ipLabel.grid(row = 0)   
    ipEntry.grid(row = 0, column = 1)

    userLabel = Label(root,
               text = "Enter your chat name: ",
               relief = "ridge",
               font = tkFont.Font(size = 15))
    
    userLabel.grid(row = 1)   
    userEntry.grid(row = 1, column = 1)

    connectButton = Button(root, text = "Connect", command = connect)
    connectButton.grid(row = 2, column = 1)
    
    
    try:
      thread.start_new_thread(rotater,())
    except:
      print "Error: unable to start thread"
      
    root.mainloop()

def connect():
    servIP = ipEntry.get()
    username = userEntry.get()
    print servIP
    print username

def rotater():
    while 1:
        time.sleep(1000)

if __name__ == "__main__":
  main()
