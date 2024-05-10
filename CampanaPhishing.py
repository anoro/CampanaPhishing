import time
import os
import sys
import smtplib

#Import templates Spanish
from Templates.spanish.bankEs import bank_es
from Templates.spanish.onedriveEs import onedrive_es
from Templates.spanish.atalasianEs import atlassian_es
from Templates.spanish.buildingSellingEs import building_selling_es

#Import templates English
from Templates.english.bankEn import bank_en
from Templates.english.onedriveEn import onedrive_en
from Templates.english.atalasianEn import atalassian_En
from Templates.english.awsEn import AwsEn

#Import helpers
from helper.helper import getPath,generateFolderReport,generateUrlAccess



Version="0.1"

def main():
    print("Starting CampanaPhishing --> Version: v"+Version+"\n Templates to deploy:")
    print("\n[1] Bank ")
    print("\n[2] Atalassian")
    print("\n[3] OneDrive")
    print("\n[4] Idealista")
    print
    print("\n\nSelect your option: \n")

    #Selection of the lenguage of the attack
    value=int(input())
    languageString="Choose language: \n[0]Spanish \n[1]English"+getPath()

    #Save path and create directory where the user save the reports
    generateFolderReport()

    #generate url to access by the victim
    generateUrlAccess()

    #Bank Template
    if value == 1:
        print("\nBank:\n"+languageString)
        language=int(input())
        while language!=0|language!=1:
            if language==0:
                #Template Spanish
                bank_es()
            else:
                #Template English
                bank_en()
    #Atalassian
    elif value == 2:
        print("\nAtalassian:\n"+languageString)
        language=int(input())
        while language!=0|language!=1:
            if language==0:
                #Template Spanish
                atlassian_es()
            else:
                #Template English
                atalassian_En()
                
    #Onedrive Template
    elif value == 3:
        print("\nOneDrive:\n"+languageString)
        language=int(input())
        while language!=0|language!=1:
            if language==0:
                #Template Spanish
                onedrive_es()
            else:
                #Template English
                onedrive_en()

    #
    elif value == 4:
        print("\Idealista:\n"+languageString)
        language=int(input())
        while language!=0|language!=1:
            if language==0:
                #Template Spanish
                building_selling_es()
            else:
                #Template English
                print("\nNot finish")
                
    elif value == 5:
        print("\AWS:\n"+languageString)
        language=int(input())
        while language!=0|language!=1:
            if language==0:
                #Template Spanish
                print("\nNot finish")
            else:
                #Template English
                AwsEn()
                
                
                
    #More Templates...

    else:
        print("\nInvalid option")
        sys.exit()

main()