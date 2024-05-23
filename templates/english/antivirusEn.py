import os
import sys
from helper.helper import get_input_en,saveTemplateGenerated,urlShorter

def antivirus_en():
    #Data of the victim
    userName,url,userEmail,currentDate=get_input_en()
    #Selection
    av = int(input("Enter the antivirus you want to spoof\n[0]Bitdefender\n[1]Other\n-->"))
    if av==0:
        bitdefender_en(userName,userEmail,url,currentDate)
    elif av==1:
        print("Not finish to implement")
        sys.exit()
        #santander_es(userName,userEmail,url)
    else:
      print("The antivirus that you want to spoof is not on the list, try again...")
      antivirus_en()


def bitdefender_en(userName,userEmail,url,currentDate):
    ##HTML suplantacion bbva
    print("\nGenerating spoof of bitdefender...")
    print("\nVictim data used for this attack:\n[User]:"+userName+"\n[Email]:"+userEmail)
    urlShort=urlShorter(url+userName)
    print("\n[Malicious Url]:"+url+userName+"\n[Short Url]:"+urlShort)
    ##HTML that will be send to the victim
    bitdefenderHtml=("""
<!DOCTYPE html>
<html>
<div>
    <div>
        <div style="background-color: rgb(48, 48, 48) !important; padding: 50px 0px; height: 100% !important;"
            data-ogsb="rgb(241, 241, 241)">
            <div style="background-color: rgb(41, 41, 41) !important; margin: 0px auto; width: 600px; box-sizing: border-box;"
                data-ogsb="white">
                <div>
                    <div style="margin:0px 60px 0px 60px"><img 
                            naturalheight="0" naturalwidth="0"
                            src="https://s3testbucketganoro.s3.eu-west-1.amazonaws.com/image/Bitdefender.png"
                            style="width: 180px; margin-top: 40px; min-width: auto; min-height: auto; cursor: pointer;"
                            fetchpriority="high" class="Do8Zj">
                        <h1 style="color: rgb(255, 255, 255) !important; font-family: Roboto, Helvetica; margin: 60px 0px 24px; padding: 0px; font-size: 30px; line-height: 51px;"
                            data-ogsc="black">Steps of the installation</h1>
                        <p style="color: rgb(200, 200, 200) !important; font-family: Arial, Helvetica; font-size: 14px; line-height: 21px; padding: 0px; margin: 0px 0px 40px;"
                            data-ogsc="rgb(68, 68, 68)">Install Bitdefender Endpoint Security</p>
                    </div>
                </div>
                <div style="font-family: Arial, Helvetica; font-size: 14px; line-height: 21px; color: rgb(200, 200, 200) !important;"
                    data-ogsc="rgb(68, 68, 68)">
                    <div style="margin:0 60px">
                        <div style="margin-top:16px">
                            <h5 style="margin: 32px 0px 16px; padding: 0px; font-size: 16px; line-height: 20px; color: rgb(200, 200, 200) !important; font-weight: 600; font-family: Roboto, Helvetica;"
                                data-ogsc="rgb(68, 68, 68)">¡Hello!</h5>
                            <p style="margin-top:24px">Your network administrator invites you to install <strong
                                    style="font-weight:bold">Bitdefender Endpoint Security Tools </strong>on your computer.
                            </p>
                            <p style="margin-top:24px">Click on the link that corresponds to your 
								operating system to download and run the installer. <br><br><a
                                    href="{}"
                                    target="_blank" rel="noopener noreferrer" data-auth="NotApplicable"
                                    data-linkindex="0" data-ogsc=""
                                    style="color: rgb(219, 151, 255) !important;">Windows Installer</a> <br><a
                                    href="{}"
                                    target="_blank" rel="noopener noreferrer" data-auth="NotApplicable"
                                    data-linkindex="1" data-ogsc=""
                                    style="color: rgb(219, 151, 255) !important;">Linux Installer</a> <br><a
                                    href="{}"
                                    target="_blank" rel="noopener noreferrer" data-auth="NotApplicable"
                                    data-linkindex="2" data-ogsc=""
                                    style="color: rgb(219, 151, 255) !important;">MacOS Installer</a> </p>
                            <hr
                                style="margin:40px 0 32px 0; height:1px; background-color:#000000; opacity:0.1; border:none">
                            <p style="margin-top:24px"><strong style="font-weight:bold">Bitdefender Endpoint Security
                                </strong>Bitdefender discreetly protects any number of computers using the number one anti-malware 
								technology combined with firewall, intrusion detection, web access control and filtering, 
								sensitive data protection and application control. Employee productivity is ensured with minimal 
								resource consumption, optimised system scanning and automated security that does not require 
								end-user action. </p>
                            <p style="margin-top:24px">The installation package is designed only for use by
                                <strong style="font-weight:bold"> {} </strong>. 
								Do not try to run it on devices that are not part of your company.</p>
                        </div>
                    </div>
                </div>
                <div>
                    <div style="margin:40px 60px 0 60px">
                        <p style="color: rgb(200, 200, 200) !important; font-family: Arial, Helvetica; font-size: 14px; line-height: 21px; margin: 0px 0px 16px; padding: 0px; font-style: italic;"
                            data-ogsc="rgb(68, 68, 68)">Thank you for trusting Bitdefender!</p>
                        <p style="color: rgb(200, 200, 200) !important; font-family: Arial, Helvetica; font-size: 14px; line-height: 21px; margin: 0px; padding: 0px; font-style: italic;"
                            data-ogsc="rgb(68, 68, 68)">Kind regards, <br>Bitdefender Team</p>
                    </div>
                </div>
                <div style="font-family: Roboto, Helvetica; margin: 80px 0px 0px; text-align: center; background-color: rgb(44, 44, 44) !important; width: 100%;"
                    data-ogsb="rgb(248, 248, 248)">
                    <p style="background-color: rgb(44, 44, 44) !important; font-size: 18px; line-height: 17.5px; margin: 0px;"
                        aria-hidden="true" data-ogsb="rgb(248, 248, 248)">&nbsp;</p>
                    <p style="font-size: 12px; background-color: rgb(44, 44, 44) !important; color: rgb(163, 163, 163) !important; line-height: 15px; margin: 0px; vertical-align: middle;"
                        data-ogsc="rgb(118, 118, 118)" data-ogsb="rgb(248, 248, 248)">Please do not reply to this message. 
						This message has been generated automatically.</p>
                    <p style="background-color: rgb(44, 44, 44) !important; font-size: 18px; line-height: 17.5px; margin: 0px;"
                        aria-hidden="true" data-ogsb="rgb(248, 248, 248)">&nbsp;</p>
                </div>
            </div>
        </div>
    </div>
</div>

</html>
                   """.format(urlShort,urlShort,urlShort,"Movicoders S.L."))
    saveTemplateGenerated(userName,"Bitdefender",bitdefenderHtml,"Instalation of Bitdefender Endpoint Security","notify@movicoders.link",userEmail)
    

#Desarrollando...