# CampanaPhishing

Open project for automatize the phishing campaigns attacks for organizations and intern campaigns

by Guillermo Anoro (ganoro)

## Legal Disclaimer

I don´t make responsible of the uses of this tools, this tool is prepared for Educational proposes or to medium-small enterprises can use to make campaigns of phishing to train their employees

## Features

The program is able to send this kind of phishing emails templates to spoofing:
- Antivirus (BitDefender)
- Atalassian
- Adobe (developing)
- AWS
- Banks
- Bitwarden
- DocuSign
- Giveaway Phishing
- OneDrive/Office
    - Recovery account
    - MFA-QR
- Zones to rent an office 
- Zoom (developing)

And developing...

**Note** The application does not intend to use the brand image to steal information from the impersonated companies, remember that its use is internal for awareness purposes.

Also the program will be able to recollect information from the users that are phished
- Name of the user
- IP
- Browser information

## Installation

You need to install the following tools

- Python3

First Clone The Repository:
```bash
git clone https://www.github.com/anoro/CampanaPhishing
```
Then access to CampanaPhishing folder and provide permission to your user:
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
If you want to put the flask app in background for persistance:

```bash
nohup flask run --host=0.0.0.0 --port=5000 &
```
and close the terminal, the task will find it with, to close it:
```bash
ps aux | grep flask #get pid
kill <pid>
```

- Docker

For deploy persistance flask page with docker
```bash
sudo docker build . -t campanaphishing
sudo docker run -p 5000:5000 -it campanaphishing
```

prune dockers
```bash
docker system prune
```

Once the program will ask the following question:
- Enter the name of your victim--> (Name) 
- Enter the phishing URL--> (url)
- Enter the victim's email--> email

and will send the custom email from flask 

Implement in the code the url shorter and qr generator by a url (QRhishing)
The HTML Templates are done to extract more info of the user to add more you need to add endpoints on the app.py for deploy the flask app properly

Important Steps:
- Set up the SMTP (User/password), and make the need changes if them are needed

