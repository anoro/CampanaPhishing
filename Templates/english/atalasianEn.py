import time
import os
import sys
import smtplib
from helper.helper import getPath

def AtalassianEn():
    
    #Información de la victima
    userName = input("Introduce el nombre de tu victima-->")
    userAccount = input("Introduce la cuenta de usuario de tu victima-->")
    url=("Introduce el url de phishing-->")
    userEmail=("Introduce el email de la victima-->")
    
    date=time.localtime()
    currentDate=time.strftime("%D %B %Y, %H:%M:%S",date)
    
    ##HTML que se enviara a la victima
    atalasianHtml=("""
                   
                   """.format(currentDate,userEmail,userName,userEmail))
    fileNameHtml=userName+"Atalasian.html"
    htmlFile=open("./reportFolder/"+fileNameHtml,"w")
    htmlFile.write(atalasianHtml)
    htmlFile.close()
    print("HTML creado y preparado para enviar")
    getPath()