import time
import os
import sys
import smtplib
from helper.helper import get_input_en,saveTemplateGenerated,urlShorter

def aws_en():
    #Data of the victim
    userName,url,userEmail,currentDate=get_input_en()
    ##HTML spoof aws
    print("\nGenerating spoof of bitdefender...")
    print("\nVictim data used for this attack:\n[User]:"+userName+"\n[Email]:"+userEmail)
    urlShort=urlShorter(url+userName)
    print("\n[Malicious Url]:"+url+userName+"\n[Short Url]:"+urlShort)
    ##HTML that will be send to the victim
    awsHtml=("""
                   <div>
                      <table
                        class="x_MsoNormalTable"
                        border="1"
                        cellpadding="0"
                        style="
                          background-image: initial;
                          background-position: initial;
                          background-size: initial;
                          background-repeat: initial;
                          background-attachment: initial;
                          background-origin: initial;
                          background-clip: initial;
                          background-color: rgb(42, 44, 20) !important;
                          border: 1pt solid black;
                        "
                        data-ogsb="lightyellow"
                      >
                      </table>
                      <div>
                        <center
                          style="
                            width: 100%;
                            background-image: initial;
                            background-position: initial;
                            background-size: initial;
                            background-repeat: initial;
                            background-attachment: initial;
                            background-origin: initial;
                            background-clip: initial;
                            background-color: rgb(44, 44, 44) !important;
                            text-align: left;
                          "
                          data-ogsb="rgb(249, 249, 249)"
                        >
                          <div
                            id="x_preheaderText"
                            style="
                              display: none;
                              font-family: sans-serif;
                              font-size: 1px;
                              line-height: 1px;
                              max-height: 0px;
                              max-width: 0px;
                              opacity: 0;
                              overflow: hidden;
                            "
                          >
                            Your invitation to access your applications.
                          </div>
                          <div
                            id="x_preheaderSpacingHack"
                            style="
                              display: none;
                              font-family: sans-serif;
                              font-size: 1px;
                              line-height: 1px;
                              max-height: 0px;
                              max-width: 0px;
                              opacity: 0;
                              overflow: hidden;
                            "
                          >
                            ‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;‌&nbsp;
                          </div>
                          <div class="x_email-container" style="max-width: 600px; margin: auto">
                            <table
                              role="presentation"
                              cellspacing="0"
                              cellpadding="0"
                              border="0"
                              align="center"
                              width="100%"
                              id="x_logoContainer"
                              style="max-width: 600px"
                            >
                              <tbody>
                                <tr>
                                  <td style="padding: 20px 0 10px 0; text-align: left">
                                    <img
                                      data-imagetype="External"
                                      src="https://m.media-amazon.com/images/G/01/amazonwebservices/AWS_logo_RGB_REV.png"
                                      width="67"
                                      height="40"
                                      alt="AWS logo"
                                      border="0"
                                      style="
                                        font-family: sans-serif;
                                        font-size: 15px;
                                        line-height: 140%;
                                        color: rgb(187, 187, 187) !important;
                                      "
                                      data-ogsc="rgb(85, 85, 85)"
                                    />
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                            <table
                              role="presentation"
                              cellspacing="0"
                              cellpadding="0"
                              border="0"
                              align="center"
                              width="100%"
                              id="x_emailBodyContainer"
                              style="
                                border: 1px solid #e5e5e5;
                                border-bottom-color: #ccc;
                                border-top-color: #f0f0f0;
                                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                                max-width: 600px;
                              "
                            >
                              <tbody>
                                <tr>
                                  <td
                                    class="x_module"
                                    style="
                                      background-color: rgb(41, 41, 41) !important;
                                      color: rgb(200, 200, 200) !important;
                                      font-family: sans-serif;
                                      font-size: 14px;
                                      line-height: 140%;
                                      padding: 25px 35px;
                                    "
                                    data-ogsc="rgb(68, 68, 68)"
                                    data-ogsb="rgb(255, 255, 255)"
                                  >
                                    <p style="margin: 0 0 15px 0; padding: 0 0 0 0">
                                      Hello Movicoders - {},
                                    </p>
                                    <p style="margin: 0 0 15px 0; padding: 0 0 0 0">
                                      Your AWS Organization (AWS Account #438954726445) uses AWS IAM
                                      Identity Center (successor to AWS Single Sign-On) to provide
                                      access to AWS accounts and business applications.
                                    </p>
                                    <p style="margin: 0; padding: 0">
                                      Your administrator has invited you to access the AWS access
                                      portal. Accepting this invitation activates your user account
                                      in IAM Identity Center so that you can access assigned AWS
                                      accounts and applications. Choose the link below to accept
                                      this invitation.
                                    </p>
                                  </td>
                                </tr>
                                <tr>
                                  <td
                                    class="x_module x_module-button"
                                    style="
                                      background-color: rgb(41, 41, 41) !important;
                                      color: rgb(200, 200, 200) !important;
                                      font-family: sans-serif;
                                      font-size: 14px;
                                      line-height: 140%;
                                      padding: 0px 35px;
                                    "
                                    data-ogsc="rgb(68, 68, 68)"
                                    data-ogsb="rgb(255, 255, 255)"
                                  >
                                    <table
                                      role="presentation"
                                      cellspacing="0"
                                      cellpadding="0"
                                      border="0"
                                      align="left"
                                      style="margin: auto"
                                    >
                                      <tbody>
                                        <tr>
                                          <td
                                            class="x_button-td"
                                            style="
                                              background-image: initial;
                                              background-position: initial;
                                              background-size: initial;
                                              background-repeat: initial;
                                              background-attachment: initial;
                                              background-origin: initial;
                                              background-clip: initial;
                                              background-color: rgb(0, 111, 169) !important;
                                              border-radius: 3px;
                                              text-align: center;
                                            "
                                            data-ogsb="rgb(43, 152, 214)"
                                          >
                                            <a
                                              href="{}"
                                              target="_blank"
                                              rel="noopener noreferrer"
                                              data-auth="NotApplicable"
                                              class="x_button-a"
                                              style="
                                                background-image: initial;
                                                background-position: initial;
                                                background-size: initial;
                                                background-repeat: initial;
                                                background-attachment: initial;
                                                background-origin: initial;
                                                background-clip: initial;
                                                background-color: rgb(0, 111, 169) !important;
                                                border: 15px solid rgb(43, 152, 214);
                                                border-radius: 3px;
                                                color: rgb(123, 174, 255) !important;
                                                display: block;
                                                font-family: sans-serif;
                                                font-size: 14px;
                                                line-height: 110%;
                                                text-align: center;
                                                text-decoration: none;
                                              "
                                              data-linkindex="1"
                                              data-ogsc="rgb(17, 102, 187)"
                                              data-ogsb="rgb(43, 152, 214)"
                                              ><span class="x_button-link" style="color: #fff"
                                                >&nbsp;&nbsp;Accept invitation&nbsp;&nbsp;</span
                                              >
                                            </a>
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>
                                  </td>
                                </tr>
                                <tr>
                                  <td
                                    class="x_module"
                                    style="
                                      background-color: rgb(41, 41, 41) !important;
                                      color: rgb(168, 168, 168) !important;
                                      font-family: sans-serif;
                                      font-size: 14px;
                                      line-height: 140%;
                                      padding: 10px 35px 0px;
                                    "
                                    data-ogsc="gray"
                                    data-ogsb="rgb(255, 255, 255)"
                                  >
                                    This invitation will expire in 7 days.
                                  </td>
                                </tr>
                                <tr>
                                  <td
                                    class="x_module"
                                    style="
                                      background-color: rgb(41, 41, 41) !important;
                                      color: rgb(200, 200, 200) !important;
                                      font-family: sans-serif;
                                      font-size: 14px;
                                      line-height: 140%;
                                      padding: 25px 35px;
                                    "
                                    data-ogsc="rgb(68, 68, 68)"
                                    data-ogsb="rgb(255, 255, 255)"
                                  >
                                    <p style="margin: 0 0 15px 0; padding: 0 0 0 0">
                                      <strong>Accessing the AWS access portal</strong><br />After
                                      you've accepted the invitation, you can sign in to the AWS
                                      access portal by using the information below.
                                    </p>
                                    <p style="margin: 0 0 15px 0; padding: 0 0 0 0">
                                      <strong>Your AWS access portal URL:</strong><br /><a
                                        href="https://appser.awsapps.com/start/"
                                        target="_blank"
                                        rel="noopener noreferrer"
                                        data-auth="NotApplicable"
                                        style="
                                          color: rgb(123, 174, 255) !important;
                                          text-decoration: none;
                                        "
                                        data-linkindex="2"
                                        data-ogsc="rgb(17, 102, 187)"
                                        >https://<span
                                          data-markjs="true"
                                          class="markx8v2v2thn"
                                          data-ogac=""
                                          data-ogab=""
                                          data-ogsc=""
                                          data-ogsb=""
                                          style="background-color: rgb(255, 241, 0); color: black"
                                          >appser</span
                                        >.awsapps.com/start/</a
                                      >
                                    </p>
                                    <p style="margin: 0; padding: 0">
                                      <strong>Your Username:</strong
                                      ><br />{}
                                    </p>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                            <table
                              role="presentation"
                              cellspacing="0"
                              cellpadding="0"
                              border="0"
                              align="center"
                              width="100%"
                              id="x_footer"
                              style="max-width: 600px"
                            >
                              <tbody>
                                <tr>
                                  <td
                                    style="
                                      color: rgb(162, 162, 162) !important;
                                      font-family: sans-serif;
                                      font-size: 12px;
                                      line-height: 18px;
                                      padding: 20px 10px;
                                      text-align: center;
                                    "
                                    data-ogsc="rgb(119, 119, 119)"
                                  >
                                    Amazon Web Services, Inc. is a subsidiary of Amazon.com, Inc.
                                    <a
                                      href="https://amazon.com/"
                                      target="_blank"
                                      rel="noopener noreferrer"
                                      data-auth="NotApplicable"
                                      style="
                                        color: rgb(162, 162, 162) !important;
                                        text-decoration: none;
                                      "
                                      data-linkindex="3"
                                      data-ogsc="rgb(119, 119, 119)"
                                      >Amazon.com</a
                                    >
                                    is a registered trademark of Amazon.com, Inc. This message was
                                    produced and distributed by Amazon Web Services, Inc., 410 Terry
                                    Ave. North, Seattle, WA 98109-5210.
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                          </div>
                        </center>
                      </div>
                      <table
                        class="x_MsoNormalTable"
                        border="1"
                        cellpadding="0"
                        style="
                          background-image: initial;
                          background-position: initial;
                          background-size: initial;
                          background-repeat: initial;
                          background-attachment: initial;
                          background-origin: initial;
                          background-clip: initial;
                          background-color: rgb(102, 53, 42) !important;
                          border: 1pt solid black;
                        "
                        data-ogsb="rgb(255, 191, 176)"
                      >
                      </table>
                    </div>
                    
                   """.format(userName,urlShort,userEmail))
    saveTemplateGenerated(userName,"AWS",awsHtml,"IMPORTANT notification of your AWS account","notify@movicoders.link",userEmail)
    