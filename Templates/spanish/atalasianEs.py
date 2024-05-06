import time
import os
import sys
import smtplib
from helper.helper import getPath

def AtalassianEs():
    
    #Información de la victima
    userName = input("Introduce el nombre de tu victima-->")
    userAccount = input("Introduce la cuenta de usuario de tu victima-->")
    url=("Introduce el url de phishing-->")
    userEmail=("Introduce el email de la victima-->")
    
    date=time.localtime()
    currentDate=time.strftime("%H:%M:%S , %",date)
    
    ##HTML que se enviara a la victima
    atalasianHtml=("""
                   <div class="maincontent">
                      <table width="100%" cellpadding="0" cellspacing="0" border="0">
                        <tbody>
                          <tr>
                            <td>
                              <font size="+1"
                                ><b>Establece tu nueva contraseña de Atlassian</b></font
                              ><br /><font size="-1" color="#777">1 mensaje</font>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                      <hr />
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
                                ><b>Atlassian </b
                                >&lt;noreply+e069804af0da71dbe878fe78ee260e524d73c7541d53769015b1ce64@am.atlassian.com&gt;</font
                              >
                            </td>
                            <td align="right"><font size="-1">{}</font></td>
                          </tr>
                          <tr>
                            <td colspan="2" style="padding-bottom: 4px">
                              <font size="-1" class="recipient"
                                ><div class="replyto">
                                  Responder a: Atlassian
                                  &lt;noreply+e069804af0da71dbe878fe78ee260e524d73c7541d53769015b1ce64@am.atlassian.com&gt;
                                </div>
                                <div>Para: {}</div></font
                              >
                            </td>
                          </tr>
                          <tr>
                            <td colspan="2">
                              <table width="100%" cellpadding="12" cellspacing="0" border="0">
                                <tbody>
                                  <tr>
                                    <td>
                                      <div style="overflow: hidden">
                                        <font size="-1"
                                          ><u></u>
                                          <div
                                            style="
                                              margin: 0;
                                              padding: 0;
                                              font-family: -apple-system, BlinkMacSystemFont,
                                                Segoe UI, Roboto, Oxygen, Ubuntu, Fira Sans,
                                                Droid Sans, Helvetica Neue, sans-serif;
                                              font-size: 14px;
                                              font-weight: 400;
                                              letter-spacing: -0.005em;
                                              color: #091e42;
                                              line-height: 20px;
                                              background: #ffffff;
                                              height: 100%;
                                              width: 100%;
                                            "
                                          >
                                            <table
                                              width="100%"
                                              border="0"
                                              cellspacing="0"
                                              cellpadding="0"
                                              style="border-collapse: collapse"
                                            >
                                              <tbody>
                                                <tr>
                                                  <td align="center">
                                                    <div style="max-width: 520px; margin: 0 auto">
                                                      <div
                                                        style="
                                                          vertical-align: top;
                                                          text-align: left;
                                                          font-family: -apple-system,
                                                            BlinkMacSystemFont, Segoe UI, Roboto,
                                                            Oxygen, Ubuntu, Fira Sans, Droid Sans,
                                                            Helvetica Neue, sans-serif;
                                                          font-size: 14px;
                                                          font-weight: 400;
                                                          letter-spacing: -0.005em;
                                                          color: #091e42;
                                                          line-height: 20px;
                                                        "
                                                      >
                                                        <div
                                                          style="
                                                            padding-top: 30px;
                                                            padding-bottom: 20px;
                                                            vertical-align: top;
                                                            text-align: center;
                                                          "
                                                        >
                                                          <a
                                                            href="https://www.atlassian.com"
                                                            target="_blank"
                                                            data-saferedirecturl="https://www.google.com/url?hl=es&amp;q=https://www.atlassian.com&amp;source=gmail&amp;ust=1715064449755000&amp;usg=AOvVaw3MYrMzUEv1vSlhVRzDJe88"
                                                            ><img
                                                              src="https://ci3.googleusercontent.com/meips/ADKq_Na6XzjWLy087GFD9hbEVqXoklvXJNS90Id5N9MxbfEi4xqTyfVUuwJG-PPQvOSGaaoV_Hmp8_0sVuzpjjCAg-gS-OyuVLoCZvj9xOIyPeNjBlvbaMKaPJf9qjvRQErEmAZ9QNIYV4u4H0B49K_9zg=s0-d-e1-ft#https://id-mail-assets.atlassian.com/shared/id-summit/id-summit-email_logo_360x80_NEW.png"
                                                              height="30"
                                                              alt="Atlassian"
                                                              style="
                                                                line-height: 100%;
                                                                outline: none;
                                                                text-decoration: none;
                                                                border: 0px;
                                                                filter: invert(0);
                                                              "
                                                          /></a>
                                                        </div>
                                                        <hr
                                                          style="
                                                            margin-top: 24px;
                                                            margin-bottom: 24px;
                                                            border: 0;
                                                            border-bottom: 1px solid #c1c7d0;
                                                          "
                                                        />
                                                        <table
                                                          width="100%"
                                                          border="0"
                                                          cellspacing="0"
                                                          cellpadding="0"
                                                          style="border-collapse: collapse"
                                                        >
                                                          <tbody>
                                                            <tr>
                                                              <td align="center">
                                                                <img
                                                                  src="https://ci3.googleusercontent.com/meips/ADKq_NbpMMFqVi5tm5CYGs09iCodBybQn5XOrIqo7OBYG2ziU88GBH3yuWVNWpqVza_CprxKcOgjhCX-RcABOWvK9YkH9uMi_oW4jVYtxVqfRi_2buB7KI6iqnkDSh1M9yqArbStd1WW5GlDReF4tw=s0-d-e1-ft#https://id-mail-assets.atlassian.com/template/aid_signup_welcome_verify_adg/people.png"
                                                                  height="175"
                                                                  border="0"
                                                                  alt=""
                                                                  style="
                                                                    border: 0px;
                                                                    line-height: 100%;
                                                                    outline: none;
                                                                    text-decoration: none;
                                                                    filter: invert(0);
                                                                  "
                                                                />
                                                              </td>
                                                            </tr>
                                                          </tbody>
                                                        </table>
                                                        <p
                                                          style="
                                                            font-family: -apple-system,
                                                              BlinkMacSystemFont, Segoe UI, Roboto,
                                                              Oxygen, Ubuntu, Fira Sans, Droid Sans,
                                                              Helvetica Neue, sans-serif;
                                                            font-size: 14px;
                                                            font-weight: 400;
                                                            letter-spacing: -0.005em;
                                                            color: #091e42;
                                                            line-height: 20px;
                                                            margin-top: 12px;
                                                          "
                                                        >
                                                          Hola,{}:
                                                        </p>
                                                        <p
                                                          style="
                                                            font-family: -apple-system,
                                                              BlinkMacSystemFont, Segoe UI, Roboto,
                                                              Oxygen, Ubuntu, Fira Sans, Droid Sans,
                                                              Helvetica Neue, sans-serif;
                                                            font-size: 14px;
                                                            font-weight: 400;
                                                            letter-spacing: -0.005em;
                                                            color: #091e42;
                                                            line-height: 20px;
                                                            margin-top: 12px;
                                                          "
                                                        >
                                                          Hemos recibido una solicitud para
                                                          establecer una nueva contraseña para esta
                                                          cuenta de Atlassian:
                                                          <b
                                                            ><a
                                                              style="
                                                                text-decoration: none;
                                                                color: inherit;
                                                              "
                                                              >{}</a
                                                            ></b
                                                          >.
                                                        </p>
                                                        <div
                                                          style="
                                                            margin-top: 24px;
                                                            margin-bottom: 24px;
                                                          "
                                                        >
                                                          <a
                                                            href="https://id.atlassian.com/login/changepassword?continue=https%3A%2F%2Fwww.atlassian.com%2Fgateway%2Fapi%2Fstart%2Fauthredirect&amp;signature=eyJraWQiOiJtaWNyb3MvYWlkLWFjY291bnQvOTlkYmc1ZDA3aXJwZXF1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJndWlsbGVybW9hYzIyQGdtYWlsLmNvbSIsImF1ZCI6Imxpbmstc2lnbmF0dXJlLXZhbGlkYXRvciIsIm5iZiI6MTcxNDk3NzgwNCwic2NvcGUiOiJjaGFuZ2VQYXNzd29yZCIsImlzcyI6Im1pY3Jvcy9haWQtYWNjb3VudCIsImV4cCI6MTcxNDk4MTQwNCwidXNlcklkIjoiNWE3YzA2M2E0YjAzZGQ1N2IwMWE3MTA0IiwiaWF0IjoxNzE0OTc3ODA0LCJqdGkiOiI1MDY3NzZlNC02MzFkLTQyNjktOGJmZi03YmFiZmU0YzE0MDYifQ.SHp_IGC25eHdsxvIYis1E9GV4FJC-aAC58_uVllKpOlRwycHyVZXx8So82n5EDE-UxAeDvU-nb1uP3AtLEEv3cgewBIxIXkgw2v6aYUAG1GW0clllNwRJp3GHhQGVb6562yXizx-KCzI33pmGq0EhPBQ8urdDTtHl3HWSZBRqNFEglZiolJCmznemuLK0yNfdaX04lOXkt87v9Wlf2awjSZi2AYlwiqnSgWEJEqcljZSGc5K2JSHybtf_LsWJOhq6szoWCz0sJSLyD6gMnzS-Qqdq7t8eszuBSoZLfn1uZ1hnrVPe-sIPYSwq6DsDHy_JZqUdVL4Dmnr82oeOITJaQ&amp;source=9607060d97aac19f42cc5c59b0ec4a1d"
                                                            style="
                                                              box-sizing: border-box;
                                                              border-radius: 3px;
                                                              border-width: 0;
                                                              border: none;
                                                              display: inline-flex;
                                                              font-style: normal;
                                                              font-size: inherit;
                                                              line-height: 24px;
                                                              margin: 0;
                                                              outline: none;
                                                              padding: 4px 12px;
                                                              text-align: center;
                                                              vertical-align: middle;
                                                              white-space: nowrap;
                                                              text-decoration: none;
                                                              background: #0052cc;
                                                              color: #ffffff;
                                                            "
                                                            target="_blank"
                                                            data-saferedirecturl="https://www.google.com/url?hl=es&amp;q=https://id.atlassian.com/login/changepassword?continue%3Dhttps%253A%252F%252Fwww.atlassian.com%252Fgateway%252Fapi%252Fstart%252Fauthredirect%26signature%3DeyJraWQiOiJtaWNyb3MvYWlkLWFjY291bnQvOTlkYmc1ZDA3aXJwZXF1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJndWlsbGVybW9hYzIyQGdtYWlsLmNvbSIsImF1ZCI6Imxpbmstc2lnbmF0dXJlLXZhbGlkYXRvciIsIm5iZiI6MTcxNDk3NzgwNCwic2NvcGUiOiJjaGFuZ2VQYXNzd29yZCIsImlzcyI6Im1pY3Jvcy9haWQtYWNjb3VudCIsImV4cCI6MTcxNDk4MTQwNCwidXNlcklkIjoiNWE3YzA2M2E0YjAzZGQ1N2IwMWE3MTA0IiwiaWF0IjoxNzE0OTc3ODA0LCJqdGkiOiI1MDY3NzZlNC02MzFkLTQyNjktOGJmZi03YmFiZmU0YzE0MDYifQ.SHp_IGC25eHdsxvIYis1E9GV4FJC-aAC58_uVllKpOlRwycHyVZXx8So82n5EDE-UxAeDvU-nb1uP3AtLEEv3cgewBIxIXkgw2v6aYUAG1GW0clllNwRJp3GHhQGVb6562yXizx-KCzI33pmGq0EhPBQ8urdDTtHl3HWSZBRqNFEglZiolJCmznemuLK0yNfdaX04lOXkt87v9Wlf2awjSZi2AYlwiqnSgWEJEqcljZSGc5K2JSHybtf_LsWJOhq6szoWCz0sJSLyD6gMnzS-Qqdq7t8eszuBSoZLfn1uZ1hnrVPe-sIPYSwq6DsDHy_JZqUdVL4Dmnr82oeOITJaQ%26source%3D9607060d97aac19f42cc5c59b0ec4a1d&amp;source=gmail&amp;ust=1715064449755000&amp;usg=AOvVaw0DCKLCLCmjCr-zOL2-m2ed"
                                                            >Establecer contraseña</a
                                                          >
                                                        </div>
                                                        <p
                                                          style="
                                                            font-family: -apple-system,
                                                              BlinkMacSystemFont, Segoe UI, Roboto,
                                                              Oxygen, Ubuntu, Fira Sans, Droid Sans,
                                                              Helvetica Neue, sans-serif;
                                                            font-size: 14px;
                                                            font-weight: 400;
                                                            letter-spacing: -0.005em;
                                                            color: #091e42;
                                                            line-height: 20px;
                                                            margin-top: 12px;
                                                          "
                                                        >
                                                          <span style="color: #5e6c84"
                                                            >Si no lo has solicitado, contacta con tu servicio tecnico medinate el siguiente 
                                                            <a
                                                            href="https://id.atlassian.com/login/changepassword?continue=https%3A%2F%2Fwww.atlassian.com%2Fgateway%2Fapi%2Fstart%2Fauthredirect&amp;signature=eyJraWQiOiJtaWNyb3MvYWlkLWFjY291bnQvOTlkYmc1ZDA3aXJwZXF1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJndWlsbGVybW9hYzIyQGdtYWlsLmNvbSIsImF1ZCI6Imxpbmstc2lnbmF0dXJlLXZhbGlkYXRvciIsIm5iZiI6MTcxNDk3NzgwNCwic2NvcGUiOiJjaGFuZ2VQYXNzd29yZCIsImlzcyI6Im1pY3Jvcy9haWQtYWNjb3VudCIsImV4cCI6MTcxNDk4MTQwNCwidXNlcklkIjoiNWE3YzA2M2E0YjAzZGQ1N2IwMWE3MTA0IiwiaWF0IjoxNzE0OTc3ODA0LCJqdGkiOiI1MDY3NzZlNC02MzFkLTQyNjktOGJmZi03YmFiZmU0YzE0MDYifQ.SHp_IGC25eHdsxvIYis1E9GV4FJC-aAC58_uVllKpOlRwycHyVZXx8So82n5EDE-UxAeDvU-nb1uP3AtLEEv3cgewBIxIXkgw2v6aYUAG1GW0clllNwRJp3GHhQGVb6562yXizx-KCzI33pmGq0EhPBQ8urdDTtHl3HWSZBRqNFEglZiolJCmznemuLK0yNfdaX04lOXkt87v9Wlf2awjSZi2AYlwiqnSgWEJEqcljZSGc5K2JSHybtf_LsWJOhq6szoWCz0sJSLyD6gMnzS-Qqdq7t8eszuBSoZLfn1uZ1hnrVPe-sIPYSwq6DsDHy_JZqUdVL4Dmnr82oeOITJaQ&amp;source=9607060d97aac19f42cc5c59b0ec4a1d"
                                                            >link</a>.
                                                            </span>
                                                        </p>
                                                        <hr
                                                          style="
                                                            margin-top: 24px;
                                                            margin-bottom: 24px;
                                                            border: 0;
                                                            border-bottom: 1px solid #c1c7d0;
                                                          "
                                                        />
                                                        <div
                                                          style="
                                                            color: #707070;
                                                            font-size: 13px;
                                                            line-height: 19px;
                                                            text-align: center;
                                                            margin-top: 10px;
                                                          "
                                                        >
                                                          <table
                                                            width="100%"
                                                            cellpadding="0"
                                                            cellspacing="0"
                                                            border="0"
                                                            bgcolor="#ffffff"
                                                            align="center"
                                                            style="border-collapse: collapse"
                                                          >
                                                            <tbody>
                                                              <tr>
                                                                <td
                                                                  valign="top"
                                                                  align="center"
                                                                  style="
                                                                    padding-top: 10px;
                                                                    line-height: 18px;
                                                                    text-align: center;
                                                                    font-weight: none;
                                                                    font-size: 12px;
                                                                    color: #505f79;
                                                                  "
                                                                >
                                                                  <span
                                                                    >Has recibido este mensaje de
                                                                    parte de Atlassian Cloud</span
                                                                  ><br />
                                                                </td>
                                                              </tr>
                                                              <tr valign="top">
                                                                <td
                                                                  align="center"
                                                                  style="
                                                                    padding-top: 15px;
                                                                    padding-bottom: 30px;
                                                                  "
                                                                >
                                                                  <a
                                                                    href="https://www.atlassian.com"
                                                                    target="_blank"
                                                                    data-saferedirecturl="https://www.google.com/url?hl=es&amp;q=https://www.atlassian.com&amp;source=gmail&amp;ust=1715064449755000&amp;usg=AOvVaw3MYrMzUEv1vSlhVRzDJe88"
                                                                    ><img
                                                                      src="https://ci3.googleusercontent.com/meips/ADKq_NbKiDnhFfOAVr_X7wxGJlyVxY1JjjFSBZ7V-Xz7QqnmEG9ofVIyrlHH02gtNgxfvU3cqQkShDp5EpgfacA37f-M4L2sMthYT8nt91EYU9sRlb_09nvaNZqmrnMMZ92Y_XOP-pAsFjTZojSQ=s0-d-e1-ft#https://id-mail-assets.atlassian.com/shared/id-summit/id-summit-logo-email-footer.png"
                                                                      width="114"
                                                                      border="0"
                                                                      alt="Atlassian"
                                                                      style="
                                                                        border: 0px;
                                                                        line-height: 100%;
                                                                        outline: none;
                                                                        text-decoration: none;
                                                                        display: block;
                                                                        color: rgb(76, 154, 201);
                                                                        filter: invert(0);
                                                                      "
                                                                  /></a>
                                                                </td>
                                                              </tr>
                                                            </tbody>
                                                          </table>
                                                        </div>
                                                      </div>
                                                    </div>
                                                  </td>
                                                </tr>
                                              </tbody>
                                            </table></div
                                        ></font>
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
                   """.format(currentDate,userEmail,userName,userEmail))
    fileNameHtml=userName+"Atalasian.html"
    htmlFile=open(fileNameHtml,"w")
    htmlFile.write("./reportFolder/"+atalasianHtml)
    htmlFile.close()
    print("HTML creado y preparado para enviar")
    getPath()
    
    