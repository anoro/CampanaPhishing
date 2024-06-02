import os
import sys
from helper.helper import get_input_es,saveTemplateGenerated,urlShorter

def giveaway_es():
    #Información de la victima
    userName,url,userEmail,currentDate=get_input_es()
    ##HTML suplantacion bbva
    print("\nGenerando suplantanción bitdefender...")
    print("\nLos datos de la victima usados para este ataque:\n[Usuario]:"+userName+"\n[Email]:"+userEmail)
    urlShort=urlShorter(url+userName)
    print("\n[Url Maliciosa]:"+url+userName+"\n[Url Acortada]:"+urlShort)
    
    giveawayHtml=("""
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
</head>
<body>
<center>
  <div>
    <h1>Enhorabuena {} por detectar el correo phishing!</h1>
    <p>Accede para ganar una tarjeta regalo.</p>

    <img src="https://pluspng.com/img-png/png-regalo-packs-regalo-888.png" width="100" height="100" alt="Price Image">

    <div>
      <p>Sorteamos una tarjeta regalo entre los que han detectado la campaña phishing:</p>
      <p>Tarjeta regalo 25€</p>
    </div>

    <div>
      <p>Haz click aqui abajo para apuntarte al sorteo:</p>
      <a width="100" height="100" href="{}" type="submit">Haz click</button>
    </div>
    <br></br>
    
  </div>
  </center>
</body>
</html>
                   """.format(userName,urlShort))
    saveTemplateGenerated(userName,"GiveAway",giveawayHtml,"Enhorabuena por detectar la campaña phishing","notificaciones@movicoders.link",userEmail)
    

