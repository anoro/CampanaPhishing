import os
import sys
from helper.helper import get_input_en,saveTemplateGenerated,urlShorter

def giveaway_en():
    #Información de la victima
    userName,url,userEmail,currentDate=get_input_en()
    ##HTML suplantacion bbva
    print("\nGenerating giveaway spoof...")
    print("\nData of the victim:\n[User]:"+userName+"\n[Email]:"+userEmail)
    urlShort=urlShorter(url+userName)
    print("\n[Malicious Url]:"+url+userName+"\n[Short Url]:"+urlShort)
    
    giveawayHtml=("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<center>
  <div>
    <h1>Congratulation {} for detect the phishing campaign! Win a Gift Card!</h1>
    <p>Enter for a chance to win an amazing Gift Card.</p>

    <img src="https://pluspng.com/img-png/png-regalo-packs-regalo-888.png" width="100" height="100" alt="Price Image">

    <div>
      <p>This is your chance to win a fantastic Gift Card!  Here's what you can win:</p>
      <p>Gift card of 25$</p>
    </div>

    <div>
      <p>Click right here to access to the giveaway:</p>
      <a width="100" height="100" href="{}" type="submit">Enter now</button>
    </div>
  </div>
  </center>
</body>
</html>
                   """.format(userName,urlShort))
    saveTemplateGenerated(userName,"GiveAway",giveawayHtml,"Enhorabuena por detectar la campaña phishing","notificaciones@movicoders.link",userEmail)
    

