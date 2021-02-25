  #i
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):
   serverSocket = socket(AF_INET, SOCK_STREAM)

   #Prepare a server socket
   #Fill in start
   serverSocket.bind(('',port))
   serverSocket.listen(1)
  #print('the web server is up on port:'+ port)
   #Fill in end

   while True:
       #Establish the connection
       print('Ready to serve...')
       connectionSocket, addr = serverSocket.accept()
       try:
           message = connectionSocket.recv(1024)
           filename = message.split()[1]
           f = open(filename[1:])
           outputdata = f.read()
           #Send one HTTP header line into socket
           #Fill in start
           connectionSocket.send(b'HTTP/.1.1 200 OK\r\nContent-Type: text/html\r\n\r\n')

           #Send the content of the requested file to the client
           for i in range(0, len(outputdata)):
               connectionSocket.send(outputdata[i].encode())

           connectionSocket.send("\r\n".encode())
           connectionSocket.close()
       except IOError:
           #Send response message for file not found (404)
           connectionSocket.send(b'HTTP/1.1 404 Not found\r\n\r\n')
           

           #Close client socket
           connectionSocket.close()


   serverSocket.close()
   sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
   webServer(13331)
