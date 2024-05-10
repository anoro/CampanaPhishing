import time
import os
import sys
import smtplib
from helper.helper import getPath,get_input_es

def atlassian_es():
    
    get_input_es()
    
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
                                                        href="https://www.google.com"
                                                        target="_blank"
                                                        data-saferedirecturl="https://www.google.com"
                                                        ><img
                                                          src="https://s3testbucketganoro.s3.eu-west-1.amazonaws.com/image/atlassian.png?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIG1A0QK3vUhFcHvKc%2F0v0f%2BkaSXr3JVPEt7s72GSY89gAiB8dXaZJpCuKORDpIdXHIMWcNHOZ2ZuBwGagfPS6IR8BCroAggoEAEaDDIyMjU1Njg2MTQ1NiIMp7SeGioRacf6LNMbKsUCGD%2BA0%2BiyQwJtyqYvyoRR2ju9svRs%2F0DCLCAv3BjmopTTMDkxeF2hE9H1yYVcyW6FDi5Ho1cSsMOH7QjBXDUZXMPhQXuBQTVyu8AQro%2BiwzVTM%2F4QLlprHJjLTqOr%2FjkKL3n1kUw%2F%2FeM6X%2F7bamEQmdn%2FiAfVJN2U16pn72PMc%2B6Tyaftnqr98DzVxSMrN1cK5OmEanwHply8L7OCzhMvYZZ1rvYkJLqwAOBn6%2FlKVC4aJQnaFcCBO9gAv24ExABonqgUlPa1rzfqspLx2PJ1tu%2Fu10hTm4u1Ps12RKyXgqt7vYPTa66uPvNNPvGE6GJ%2FDX4xYScnHOllixuJK8sq1aVDFvnqEJKVYvR87fJJQUgNKwmlalbIgHaKVljStP4foZyUMuVOs7HNP2E1W50bn5xNZcUNBTp75s%2FbX2iJ8yMpbfrxsjC3gfexBjq0ArPuk%2F7gjPtlb9%2FZvtMIFv3tnE0jdyWqEBMnZMtFSrA2Dm85uwRmNUyCjpYsjhmzYtD7xQZdj%2FCydCMXLn4NLdD0B%2Bfqybgzb7L8BgQCv7SV30Kk4iZxI5t0fVSrch0DbOP%2Fzd%2BZQl4Maz7%2BBFgik1FtQc8b1joXx35Ah144X80%2Bg8Ce7RkDPFFJTQL%2FQ%2BHCb8rMwfvGiMI6Qf%2FTifEfTh76TZhr7vyM89T%2BlbGT01XWImyK8Wc%2FZnGh1cZtscV21w24FiWO446b9NMKrdOdBa7Zj8U2yMg5NmU%2B%2BrbGKBYOhgZrOHIumPGZ96ZSGq%2B3VRaIgO08yIbEnx14%2FKyb1SjWFQDzdwTFVxrKt7uE12ftAjwcn1fZ%2FcBss2x1IfBxIFtd5uYgch2i8iIkZy1MqeXSKMZR&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240510T104929Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIATHULMGQIH3CJNA7F%2F20240510%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Signature=c30c9c79ad7f7a13fa60690633936e73dfd541afe7b1e3390d67423fe8cdddce"
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
                                                      Hola:
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
                                                          >usuario@movicoders.com</a
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
                                                        href="https://www.google.es"
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
                                                        data-saferedirecturl="https://www.google.es"
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
                                                                href="https://www.google.es"
                                                                target="_blank"
                                                                data-saferedirecturl="https://www.google.com"
                                                                ><img
                                                                  src="https://s3testbucketganoro.s3.eu-west-1.amazonaws.com/image/atlassian.png?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJGMEQCIG1A0QK3vUhFcHvKc%2F0v0f%2BkaSXr3JVPEt7s72GSY89gAiB8dXaZJpCuKORDpIdXHIMWcNHOZ2ZuBwGagfPS6IR8BCroAggoEAEaDDIyMjU1Njg2MTQ1NiIMp7SeGioRacf6LNMbKsUCGD%2BA0%2BiyQwJtyqYvyoRR2ju9svRs%2F0DCLCAv3BjmopTTMDkxeF2hE9H1yYVcyW6FDi5Ho1cSsMOH7QjBXDUZXMPhQXuBQTVyu8AQro%2BiwzVTM%2F4QLlprHJjLTqOr%2FjkKL3n1kUw%2F%2FeM6X%2F7bamEQmdn%2FiAfVJN2U16pn72PMc%2B6Tyaftnqr98DzVxSMrN1cK5OmEanwHply8L7OCzhMvYZZ1rvYkJLqwAOBn6%2FlKVC4aJQnaFcCBO9gAv24ExABonqgUlPa1rzfqspLx2PJ1tu%2Fu10hTm4u1Ps12RKyXgqt7vYPTa66uPvNNPvGE6GJ%2FDX4xYScnHOllixuJK8sq1aVDFvnqEJKVYvR87fJJQUgNKwmlalbIgHaKVljStP4foZyUMuVOs7HNP2E1W50bn5xNZcUNBTp75s%2FbX2iJ8yMpbfrxsjC3gfexBjq0ArPuk%2F7gjPtlb9%2FZvtMIFv3tnE0jdyWqEBMnZMtFSrA2Dm85uwRmNUyCjpYsjhmzYtD7xQZdj%2FCydCMXLn4NLdD0B%2Bfqybgzb7L8BgQCv7SV30Kk4iZxI5t0fVSrch0DbOP%2Fzd%2BZQl4Maz7%2BBFgik1FtQc8b1joXx35Ah144X80%2Bg8Ce7RkDPFFJTQL%2FQ%2BHCb8rMwfvGiMI6Qf%2FTifEfTh76TZhr7vyM89T%2BlbGT01XWImyK8Wc%2FZnGh1cZtscV21w24FiWO446b9NMKrdOdBa7Zj8U2yMg5NmU%2B%2BrbGKBYOhgZrOHIumPGZ96ZSGq%2B3VRaIgO08yIbEnx14%2FKyb1SjWFQDzdwTFVxrKt7uE12ftAjwcn1fZ%2FcBss2x1IfBxIFtd5uYgch2i8iIkZy1MqeXSKMZR&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240510T104929Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIATHULMGQIH3CJNA7F%2F20240510%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Signature=c30c9c79ad7f7a13fa60690633936e73dfd541afe7b1e3390d67423fe8cdddce"
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
                   """.format(currentDate,userEmail,userName,userEmail,url,url))
    fileNameHtml=userName+"Atalassian.html"
    htmlFile=open("./reportFolder/"+fileNameHtml,"w")
    htmlFile.write(atalasianHtml)
    htmlFile.close()
    print("HTML creado y preparado para enviar")
    getPath()
    
    