import time
import os
import sys
import smtplib
from helper.helper import getPath,get_input_en

def atalassian_En():
    
    get_input_en()
    
    ##HTML que se enviara a la victima
    atalasianHtml=("""
                   
                   """.format(currentDate,userEmail,userName,userEmail))
    fileNameHtml=userName+"Atalasian.html"
    htmlFile=open("./reportFolder/"+fileNameHtml,"w")
    htmlFile.write(atalasianHtml)
    htmlFile.close()
    print("HTML creado y preparado para enviar")
    getPath()