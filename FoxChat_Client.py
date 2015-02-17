from Tkinter import *
import tkFont
import thread
import socket
import pickle

root = Tk()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

BUFFER_SIZE = 1024
SERV_PORT = 1997
username = ""
servIP = ""

ipEntry = Entry(root, width = 30,)
userEntry = Entry(root, width = 30)
msgEntry = Entry(root, width = 40)

chatList = []
chatListBox = Listbox(root)

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
    discoconnectButton = Button(root, text = "Disconnect", command = disconnect)
    discoconnectButton.grid(row = 3, column = 1)

    chatListBox.grid(row = 4)
    chatListBox['height'] = 20
    chatListBox['width'] = 50
    chatListBox.insert(0, "Python")
    chatListBox.delete(0)
    chatListBox.insert(0, "yay")


    msgEntry.grid(row = 5, column = 0)

    chatSendButton = Button(root, text = "Send", command = send)
    chatSendButton.grid(row = 6, column = 0)
    
    root.mainloop()

def connect():
    servIP = ipEntry.get()
    username = userEntry.get()
    if servIP != "" and username != "":
        sock.connect((servIP, SERV_PORT))      
        try:
            thread.start_new_thread(recieve,())
        except:
            print "Error: unable to start thread"

def recieve():
    print "connected"
    while 1:
        chatList = pickle.loads(sock.recv(BUFFER_SIZE))
        i = 0
        for msg in chatList:
            chatListBox.delete(i)
            chatListBox.insert(i, msg)
            i += 1

def send():
    msg = msgEntry.get()
    if(msg != ""):
        msg = username + msg
        print msg
        sock.send(msg)

def disconnect():
    sock.close()
    
		   
if __name__ == "__main__":
  main()
