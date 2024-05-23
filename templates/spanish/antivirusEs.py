import os
import sys
from helper.helper import get_input_es,saveTemplateGenerated,urlShorter

def antivirus_es():
    #Información de la victima
    userName,url,userEmail,currentDate=get_input_es()
    
    ##HTML que se enviara a la victima
    av = int(input("Introduce el antivirus que quieres suplantar\n[0]Bitdefender\n[1]Otro\n-->"))
    if av==0:
        bitdefender_es(userName,userEmail,url,currentDate)
    elif av==1:
        print("Implementación no finalizada")
        sys.exit()
        #santander_es(userName,userEmail,url)
    else:
      print("El antivirus que quieres suplantar no esta en la lista, intentalo de nuevo")
      antivirus_es()


def bitdefender_es(userName,userEmail,url,currentDate):
    ##HTML suplantacion bbva
    print("\nGenerando suplantanción bitdefender...")
    print("\nLos datos de la victima usados para este ataque:\n[Usuario]:"+userName+"\n[Email]:"+userEmail)
    urlShort=urlShorter(url+userName)
    print("\n[Url Maliciosa]:"+url+userName+"\n[Url Acortada]:"+urlShort)
    
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
                            data-ogsc="black">Pasos de la Instalación</h1>
                        <p style="color: rgb(200, 200, 200) !important; font-family: Arial, Helvetica; font-size: 14px; line-height: 21px; padding: 0px; margin: 0px 0px 40px;"
                            data-ogsc="rgb(68, 68, 68)">Instalar Endpoint Security de Bitdefender</p>
                    </div>
                </div>
                <div style="font-family: Arial, Helvetica; font-size: 14px; line-height: 21px; color: rgb(200, 200, 200) !important;"
                    data-ogsc="rgb(68, 68, 68)">
                    <div style="margin:0 60px">
                        <div style="margin-top:16px">
                            <h5 style="margin: 32px 0px 16px; padding: 0px; font-size: 16px; line-height: 20px; color: rgb(200, 200, 200) !important; font-weight: 600; font-family: Roboto, Helvetica;"
                                data-ogsc="rgb(68, 68, 68)">¡Hola!</h5>
                            <p style="margin-top:24px">Su administrador de red le invita a instalar <strong
                                    style="font-weight:bold">Bitdefender Endpoint Security Tools </strong>en su equipo.
                            </p>
                            <p style="margin-top:24px">Haga clic en el enlace que corresponda a su sistema operativo
                                para descargar y ejecutar al instalador. <br><br><a
                                    href="{}"
                                    target="_blank" rel="noopener noreferrer" data-auth="NotApplicable"
                                    data-linkindex="0" data-ogsc=""
                                    style="color: rgb(219, 151, 255) !important;">Instalador para Windows</a> <br><a
                                    href="{}"
                                    target="_blank" rel="noopener noreferrer" data-auth="NotApplicable"
                                    data-linkindex="1" data-ogsc=""
                                    style="color: rgb(219, 151, 255) !important;">Instalador para Linux</a> <br><a
                                    href="{}"
                                    target="_blank" rel="noopener noreferrer" data-auth="NotApplicable"
                                    data-linkindex="2" data-ogsc=""
                                    style="color: rgb(219, 151, 255) !important;">Instalador para macOS</a> </p>
                            <hr
                                style="margin:40px 0 32px 0; height:1px; background-color:#000000; opacity:0.1; border:none">
                            <p style="margin-top:24px"><strong style="font-weight:bold">Bitdefender Endpoint Security
                                </strong>protege discretamente cualquier número de equipos usando la tecnología
                                antimalware número uno combinada con un cortafuego, detección de intrusiones, control de
                                acceso Web y filtrado, protección de datos sensibles y control de aplicaciones. La
                                productividad de los empleados se asegura con un consumo mínimo de recursos, análisis
                                optimizado del sistema y seguridad automatizada que no requiere la actuación del usuario
                                final. </p>
                            <p style="margin-top:24px">El paquete de instalación está diseñado solo para el uso de
                                <strong style="font-weight:bold"> {} </strong> No trate de ejecutarlo en
                                dispositivos que no formen parte de su empresa. </p>
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
                        data-ogsc="rgb(118, 118, 118)" data-ogsb="rgb(248, 248, 248)">Por favor, no responda a este
                        mensaje. Este mensaje se ha generado automáticamente.</p>
                    <p style="background-color: rgb(44, 44, 44) !important; font-size: 18px; line-height: 17.5px; margin: 0px;"
                        aria-hidden="true" data-ogsb="rgb(248, 248, 248)">&nbsp;</p>
                </div>
            </div>
        </div>
    </div>
</div>

</html>
                   """.format(urlShort,urlShort,urlShort,"Movicoders S.L."))
    saveTemplateGenerated(userName,"Bitdefender",bitdefenderHtml,"Instalación de Bitdefender Endpoint Security","notificaciones@movicoders.link",userEmail)
    

#Desarrollando...