from Tkinter import *
import tkFont
import time
import thread
import socket

root = Tk()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

BUFFER_SIZE = 5120
SERV_PORT = 1740
username = ""
servIP = ""

ipEntry = Entry(root, width = 30,)
userEntry = Entry(root, width = 30)

chatList = []

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



      
    root.mainloop()

def connect():
    servIP = ipEntry.get()
    username = userEntry.get()
    if servIP != "" and username != "":
        sock.connect(servIP, SERV_PORT)      
        try:
            thread.start_new_thread(chat,())
        except:
            print "Error: unable to start thread"

def chat():
    while 1:
        chatList = array.fromstring(conn.recv(BUFFER_SIZE).fromString())
        
        
        
if __name__ == "__main__":
  main()
