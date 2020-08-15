import socket              

s = socket.socket()        
host = '13.127.139.196' 
port = 5006               

s.connect((host, port))
while True: 
    try:
        print ("From Server: ", s.recv(1024))
        s.send(raw_input("Client please type: "))
    except:
        break
s.close()
