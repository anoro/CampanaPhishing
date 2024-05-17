# CampanaPhishing

Open proyect for automatize the phishing campaigns attacks for organizations and intern campains

by Guillermo Anoro (ganoro)

## Legal Disclaimer

I don´t make responsable of the uses of this tools, this tool is propared for Educational porpouses or to medium-small enterprises can use to make campaigns of phishing to train their employees

## Features

The program is able to send 3 kind of phishing emails

- Banks
- Atalasian
- OneDrive
- Zones to rent an office
- Adobe
- AWS
- DocuSign

And developing...

Also the program will be able to recolect information from the users that are phishinged

## Installation

You need to install the following tools

- Python3

First Clone The Repository:
```bash
git clone https://www.github.com/anoro/CampanaPhishing
```
Then access to CampanaPhishing folder and provide permision to your user:
```bash
cd CampanaPhishing
sudo chmod +x CampanaPhishing.py
```
Then execute the main code:
```bash
python3 CampanaPhishing.py
```

*In other terminal* to deploy the portal to access the victims and register it is need to have install Flask and deploy the app
```bash
flask run --host=0.0.0.0
```

Once the program will ask the following question:
- Enter the name of your victim--> (Name) 
- Enter the phishing URL--> (url)
- Enter the victim's email--> email

and will send the custom email from flask 

Implementing the url shorter like the next page: https://url.gratis/en/ 
