import time
import os
import sys
import smtplib

Version="0.1"

def main():
    print("Starting CampanaPhishing --> Version: v"+Version+"\n Templates to deploy:")
    print("\n[1] Bank ")
    print("\n[2] Atalasian")
    print("\n[3] OneDrive")
    print("\nSelect your option: \n")

    value=int(input())

    if value == 1:
        print("\nBank:\n")
    elif value ==2:
        print("\nAtalasian:\n")
    elif value ==3:
        print("\nOneDrive:\n")
    else:
        print("\nInvalid option")
        sys.exit()