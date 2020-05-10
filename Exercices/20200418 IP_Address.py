import socket    
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Le hostname de ta machine:" + hostname)    
print("L'adresse IP de ta machine:" + IPAddr)