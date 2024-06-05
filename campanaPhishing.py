import time
import os
import sys
import smtplib

#Import templates Spanish
from templates.spanish.bankEs import bank_es
from templates.spanish.onedriveEs import onedrive_es
from templates.spanish.atalasianEs import atlassian_es
from templates.spanish.buildingSellingEs import building_selling_es
from templates.spanish.antivirusEs import antivirus_es
from templates.spanish.docusignEs import docusign_es

#Import templates English
from templates.english.bankEn import bank_en
from templates.english.onedriveEn import onedrive_en
from templates.english.atalasianEn import atalassian_En
from templates.english.awsEn import aws_en
from templates.english.antivirusEn import antivirus_en
from templates.english.docusignEn import docusign_en

#Import helpers
from helper.helper import getPath,generateFolderReport, saveReportAndTemplates

#import flask for portal
Version="0.1"

def main():
    print("Starting CampanaPhishing --> Version: v"+Version+"\nTemplates to deploy:")
    print("\n[1] Bank ")
    print("\n[2] Atalassian")
    print("\n[3] OneDrive")
    print("\n[4] Idealista")
    print("\n[5] Docusign")
    print("\n[6] AWS")
    print("\n[7] Zoom")
    print("\n[8] BitWarden")
    print("\n[9] Antivirus")
    print("\nSelect your option: ")

    #Selection of the lenguage of the attack
    value=int(input())
    languageString="Choose language: \n[0]Spanish \n[1]English"

    #Save path and create directory where the user save the reports
    generateFolderReport()
    
    #Bank Template
    if value == 1:
        print("Bank:\n"+languageString)
        language=int(input())
        if language==0:
            #Template Spanish
            print("Accediendo al modo phishing...\n")
            bank_es()
        elif language==1:
            #Template english
            print("Accessing to phishing mode...\n")
            bank_en()
        else:
            #Fail statement
            print("\nError selection language")
            sys.exit()
            
    #Atalassian
    elif value == 2:
        print("Atalassian:\n"+languageString)
        language=int(input())
        if language==0:
            #Template Spanish
            print("Accediendo al modo phishing...\n")
            atlassian_es()
        elif language==1:
            #Template English
            print("Accessing to phishing mode...\n")
            atalassian_En()
        else:
            #Fail statement
            print("\nError selection language")
            sys.exit()
            

    #Onedrive Template
    elif value == 3:
        print("OneDrive:\n"+languageString)
        language=int(input())
        if language==0:
            #Template Spanish
            print("Accediendo al modo phishing...\n")
            onedrive_es()
        elif language==1:
            #Template English
            print("Accessing to phishing mode...\n")
            onedrive_en()
        else:
            #Fail statement
            print("\nError selection language")
            sys.exit()

    #Idealista Building selling Template
    elif value == 4:
        print("Idealista:\n"+languageString)
        language=int(input())
        if language==0:
            #Template Spanish
            print("Accediendo al modo phishing...\n")
            building_selling_es()
        elif language==1:
            #Template English
            print("\nNot finish english version")
        else:
            #Fail statement
            print("\nError selection language")
            sys.exit()
    
    #Docusign template
    elif value == 5:
        print("Docusign:\n"+languageString)
        language=int(input())
        if language==0:
            #Template Spanish
            print("Accediendo al modo phishing...\n")
            docusign_es()
        elif language==1:
            #Template English
            print("\nAccessing to phishing mode...\n")
            docusign_en()
        else:
            #Fail statement
            print("\nError selection language")
            sys.exit()
    #Aws template
    elif value == 6:
        print("AWS:\n"+languageString)
        language=int(input())
        if language==0:
            #Template Spanish
            print("\nNot finish spanish version")
        elif language==1:
            #Template English
            print("\nAccessing to phishing mode")
            aws_en()
        else:
            #Fail statement
            print("\nError selection language")
            sys.exit()
    #Zoom template
    elif value == 7:
        print("Zoom:\n"+languageString)
        language=int(input())
        if language==0:
            #Template Spanish
            print("\nNot finish spanish version")
        elif language==1:
            #Template English
            print("\nNot finish english version")
            #AwsEn()
        else:
            #Fail statement
            print("\nError selection language")
            sys.exit()
    #Bitwarden template
    elif value == 8:
        print("Bitwarden:\n"+languageString)
        language=int(input())
        if language==0:
            #Template Spanish
            print("\nNot finish spanish version")
        elif language==1:
            #Template English
            print("\nNot finish english version")
            #AwsEn()
        else:
            #Fail statement
            print("\nError selection language")
            sys.exit()
    #Antivirus Template
    elif value == 9:
        print("Antivirus:\n"+languageString)
        language=int(input())
        if language==0:
            #Template Spanish
            print("\nAccediendo al modo phishing...\n")
            antivirus_es()
        elif language==1:
            #Template English
            print("\nAccessing to phishing mode")
            antivirus_en()
        else:
            #Fail statement
            print("\nError selection language")
            sys.exit()

    #More Templates...

    else:
        print("\nInvalid option")
        sys.exit()
        

main()