from Tkinter import *
import tkFont
import thread
import socket
from datetime import datetime

root = Tk()
sock = socket.socket()

chatFrame=Frame(root)

BUFFER_SIZE = 1024
SERV_PORT = 1997
username = ""
servIP = ""
i = 0

ipEntry = Entry(root, width = 30,)
userEntry = Entry(root, width = 30)
msgEntry = Entry(root, width = 40)

chatList = []
chatListBox = Listbox(chatFrame,
                      font = tkFont.Font(size = 10))

chatScrollbar = Scrollbar(chatFrame)

statusLabel = Label(root,
               text = "Status: not connected ",
               relief = "ridge",
               font = tkFont.Font(size = 15))

def main():
    
    root.geometry ("600x500")
    root.title ("FoxChat Client")
    root.resizable(width = False, height = False)
    
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
    discoconnectButton = Button(root, text = "Disconnect", command = disconnect)
    discoconnectButton.grid(row = 3, column = 1)

    chatFrame.grid(row = 4)
    chatListBox.pack(side = "left", fill = "both")
    chatListBox['height'] = 20
    chatListBox['width'] = 50
    chatListBox.config(yscrollcommand=chatScrollbar.set)

    chatScrollbar.pack( side = "right", fill = "y" )
    chatScrollbar.config( command = chatListBox.yview )
    
    msgEntry.grid(row = 5, column = 0)

    chatSendButton = Button(root, text = "Send", command = send)
    chatSendButton.grid(row = 6, column = 0)
    
    statusLabel.grid(row = 4, column = 1)
 
    root.mainloop()

def connect():
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    servIP = ipEntry.get()
    username = userEntry.get()
    print servIP
    print username
    if servIP != "" and username != "":
        try:
            sock.connect((servIP, SERV_PORT))
            
            try:
                thread.start_new_thread(recieve,())
            except:
                print "Error: unable to start thread"
                
        except:
            statusLabel["text"] = "Status: Unable to connect "
            

def recieve():
    time = ""
    statusLabel["text"] = "Status: connected"
    global i
    i = 0
    inp = ""
    while inp != "disconnect":
        if inp != "":
            time = datetime.now().strftime('%H:%M')
            inp = "[%s] %s"%(time, inp)
            chatListBox.insert(i, inp)                            
            chatListBox.yview(END)   
        inp = sock.recv(BUFFER_SIZE)
        i += 1

def send():
    username = userEntry.get()
    msg = msgEntry.get()
    if(msg != ""):
        msg = (username + ": " + msg)
        print msg
        sock.send(msg)
    msgEntry.delete(0, END)

def disconnect():
    statusLabel["text"] = "Status: not connected "
    sock.send("disconnect")
    sock.close()
    global chatListBox
    chatListBox.delete(0, i)
    

if __name__ == "__main__":
  main()
