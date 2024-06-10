import os
import zipfile
import time

import requests
import json

#to remove folders
import shutil

#QR lib
import segno
import base64

#email import libraries
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Get actual Path
def getPath():
    currentPath = os.getcwd()

    # generate the aperance of the terminal of the user to make inputs
    print(f"\x1b[91m{os.path.basename(currentPath)}\x1b[0m:", currentPath)
    return currentPath

#Generator of a new folder
def generateFolderReport():
    # Creating new folders for the final report
    reportsFolder = "reportsCampana"
    
    if not os.path.exists(reportsFolder):
        os.makedirs(reportsFolder)
        print(f"Folder " + reportsFolder + " created successfully!---->"+getPath())
    else:
        print(f"Folder " + reportsFolder + " already exists")
    
    file_for_phishing_results = "reportsCampana/dataOfVictims.json"
    with open(file_for_phishing_results, "w+") as file:
        file.write("")
    print("File for make reports generated on: "+getPath()+"reportsCampana/dataOfVictims.json")

#Save the reports on a ZIP and deleting the reports folder to next one create another  
def saveReportAndTemplates():
    #save the results folder in a zip
    print("\nSaving report and templates...")
    counter=1
    while True:
        if counter==1:
            nameOfZip="campanaPhishingResults.zip"
        else:
            nameOfZip=f"campanaPhishingResults_{counter}.zip"
        if not os.path.exists(nameOfZip):
            break
        counter+=1
        
    
    zf=zipfile.ZipFile(nameOfZip,"w")
    for dirname, subdirs, files in os.walk("reportsCampana"):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()
    #delete previous folder
    try:
        shutil.rmtree("reportsCampana")
        print("\nFolder and its contents removed successfully!")
    except OSError as e:
        print(f"\nError removing folder: {e}")

    print("\nProcess finished")

def get_input_es():
    #Información de la victima
    userName = input("Introduce el nombre de la victima-->")
    #organization = input("Introduce el nombre de la organizacion a suplantar-->")
    #userAccount = input("Introduce la cuenta de usuario de tu victima-->")
    url=input("Introduce el URL de phishing-->")
    userEmail=input("Introduce el email de la victima-->")
    
    date=time.localtime()
    currentDate=time.strftime("%D %B %Y, %H:%M:%S",date)
    
    return userName,url,userEmail,currentDate# ,userAccount ,organization

def get_input_en():
    #Info of the victim
    userName = input("Enter the name of your victim-->")
    #organization = input("Enter the organization to spoof-->")
    #userAccount = input("Enter the username of the victim's account-->")
    url=input("Enter the phishing URL-->")
    userEmail=input("Enter the victim's email-->")
    
    #data time
    date=time.localtime()
    currentDate=time.strftime("%D %B %Y, %H:%M:%S",date)
    
    return userName,url,userEmail,currentDate #,userAccount ,organization

##After generate a template save it and send the email
def saveTemplateGenerated(userName,templateName,html,subjectEmail,emailAttacker,userEmail):
    print("\nGuardando correo en carpeta reporte preparado para enviar en "+getPath()+"/reportsCampana...")
    fileNameHtml=userName+templateName+".html"
    htmlFile=open(getPath()+"/reportsCampana/"+str(fileNameHtml),"w+")
    htmlFile.write(html)
    htmlFile.close()
    #Send email
    print("HTML creado y preparado para enviar por correo: "+getPath()+"/reportsCampana/"+str(fileNameHtml))
    sendEmailToVictim(html,subjectEmail,emailAttacker,userEmail)

#Email sender
def sendEmailToVictim(htmlTosend,subject, emailoftheatacker, emailofthevictim, starttls=True):
    # Create a secure connection with the SMTP server
    with smtplib.SMTP('smtp.sendgrid.net', 587) as server:
        print("\n Starting process to send the template selected to the victim\n")
        if starttls:
            server.starttls()
        
        userSMTP="apikey" # set up with your user
        passwordSMTP="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" # Set up with your password
        
        # Login with your email credentials
        server.login(userSMTP, passwordSMTP)
        
        # Create a MIMEMultipart message
        msg = MIMEMultipart('alternative')
        msg['From'] = emailoftheatacker
        msg['To'] = emailofthevictim
        msg['Subject'] = subject
        
        # Create a MIMEText object for HTML content
        html_part = MIMEText(htmlTosend, 'html')
        msg.attach(html_part)
        
        # Send the email
        server.sendmail(emailoftheatacker, emailofthevictim, msg.as_string())
        print("Phishing Email was send\nEnjoy the results....")
        
def urlShorter(url):
    api_url=f"https://tinyurl.com/api-create.php?url={url}"
    # Send GET request to TinyURL API
    response = requests.get(api_url)
    if response.status_code == 200:
        # Extract the shortened URL from the response
        short_url = response.text.strip()
        return short_url
    else:
        print(f"Error shortening URL: {response.status_code}")
        os.abort()

def qrGeneratorbyUrl(url,username):
    #Generate Qr image by an url
    qrFileName='reportsCampana/qr'+username+".png"
    qrcode=segno.make_qr(url)
    qrcode.save(
        qrFileName,
        scale=10,
        border=10
    )
    #Generate html interpreter
    data_uri= base64.b64encode(open(qrFileName,'rb').read()).decode('utf-8')
    img_tag='<img width="195" height="195" src="data:image/png;base64,{0}">'.format(data_uri)
    return img_tag