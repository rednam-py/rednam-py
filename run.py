#!/bin/python 

import os 

# cmd is a String  ex command("last")
def command(cmd):
  """ Simple Funcation for runing System Commands """
  os.system(cmd)
  print ("[+] Commmad excuted ") 
  

# Checking For Updates And Install Apache2 
command("sudo apt-get update && sudo apt-get install apache2 -y ")


# Starting Apache2 Server 
command("sudo services apache2 start")

# Start Browser 
command("firefox 127.0.0.1:80")

