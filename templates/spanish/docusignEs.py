import time
import os
import sys
import smtplib
from helper.helper import saveTemplateGenerated,get_input_en, urlShorter

def docusign_es():
    userName,url,userEmail,currentDate=get_input_en()
    ##HTML suplantacion bbva
    print("\nGenerando suplantación de docusign...")
    print("\nVictim data used for this attack:\n[User]:"+userName+"\n[Email]:"+userEmail)
    urlShort=urlShorter(url+userName)
    print("\n[Malicious Url]:"+url+userName+"\n[Short Url]:"+urlShort)
    
    docusignHtml=("""
<html lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="viewport" content="initial-scale=1.0" />
    <meta name="format-detection" content="telephone=no" />
    <title>EnvelopeActivation</title>
  </head>
  <body
    style="
      background-color: #eaeaea;
      padding: 2%;
      font-family: Helvetica, Arial, Sans Serif;
    "
  >
    <table
      role="presentation"
      border="0"
      cellspacing="0"
      cellpadding="0"
      align="center"
      width="100%"
      dir=""
    >
      <tbody>
        <tr>
          <td></td>
          <td width="640">
            <table
              style="
                mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                border-collapse: collapse;
                background-color: #ffffff;
                max-width: 640px;
              "
            >
              <tbody>
                <tr>
                  <td style="padding: 8px 16px">
                    <img
                      style="border: none; height: 50px"
                      width=""
                      src="https://s3testbucketganoro.s3.eu-west-1.amazonaws.com/image/Docusign.png"
                      alt=""
                    />
                  </td>
                </tr>
                <tr>
                  <td style="padding: 0px 24px 30px 24px">
                    <table
                      role="presentation"
                      border="0"
                      cellspacing="0"
                      cellpadding="0"
                      width="100%"
                      align="center"
                      style="background-color: #214e9f; color: #ffffff"
                    >
                      <tbody>
                        <tr>
                          <td
                            style="
                              padding: 28px 36px 36px 36px;
                              border-radius: 2px;
                              background-color: #214e9f;
                              color: #ffffff;
                              font-size: 16px;
                              font-family: Helvetica, Arial, Sans Serif;
                              width: 100%;
                              text-align: center;
                            "
                            align="center"
                          >
                            <img
                              width="75"
                              height="75"
                              src="https://d1yynrqd2fp86j.cloudfront.net/EmailTemplates/Common/images/docInvite-white.png"
                              style="width: 75px; height: 75px"
                              alt=""
                            />
                            <table
                              role="presentation"
                              border="0"
                              cellspacing="0"
                              cellpadding="0"
                              width="100%"
                            >
                              <tbody>
                                <tr>
                                  <td
                                    style="
                                      padding-top: 24px;
                                      font-size: 16px;
                                      font-family: Helvetica, Arial, Sans Serif;
                                      border: none;
                                      text-align: center;
                                      color: #ffffff;
                                    "
                                    align="center"
                                  >
                                    Payroll sent you a document to review and
                                    sign.
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                            <table
                              role="presentation"
                              border="0"
                              cellspacing="0"
                              cellpadding="0"
                              width="100%"
                            >
                              <tbody>
                                <tr>
                                  <td align="center" style="padding-top: 30px">
                                    <div>
                                      <table cellspacing="0" cellpadding="0">
                                        <tbody>
                                          <tr>
                                            <td
                                              align="center"
                                              height="44"
                                              style="
                                                font-size: 15px;
                                                color: #333333;
                                                background-color: #ffc820;
                                                font-family: Helvetica, Arial,
                                                  Sans Serif;
                                                font-weight: bold;
                                                text-align: center;
                                                text-decoration: none;
                                                border-radius: 2px;
                                                background-color: #ffc820;
                                                display: block;
                                              "
                                            >
                                              <a
                                                href="{}"
                                                style="
                                                  font-size: 15px;
                                                  color: #333333;
                                                  background-color: #ffc820;
                                                  font-family: Helvetica, Arial,
                                                    Sans Serif;
                                                  font-weight: bold;
                                                  text-align: center;
                                                  text-decoration: none;
                                                  border-radius: 2px;
                                                  background-color: #ffc820;
                                                  display: inline-block;
                                                "
                                                ><span
                                                  style="
                                                    padding: 0px 24px;
                                                    line-height: 44px;
                                                  "
                                                  ><!--[if mso
                                                    ]>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<!
                                                  [endif]-->
                                                  REVIEW DOCUMENT
                                                  <!--[if mso
                                                    ]>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<!
                                                  [endif]--></span
                                                ></a
                                              >
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                    </div>
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
                  <td
                    style="
                      padding: 0px 24px 24px 24px;
                      color: #000000;
                      font-size: 16px;
                      font-family: Helvetica, Arial, Sans Serif;
                      background-color: white;
                    "
                  >
                    <table
                      role="presentation"
                      border="0"
                      cellspacing="0"
                      cellpadding="0"
                    >
                      <tbody>
                        <tr>
                          <td style="padding-bottom: 20px">
                            <div
                              style="
                                font-family: Helvetica, Arial, Sans Serif;
                                font-weight: bold;
                                line-height: 18px;
                                font-size: 15px;
                                color: #333333;
                              "
                            >
                              Payroll
                            </div>
                            <div
                              style="
                                font-family: Helvetica, Arial, Sans Serif;
                                line-height: 18px;
                                font-size: 15px;
                                color: #666666;
                              "
                            >
                              Finance &amp; Vendor Management
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                    <span
                      style="
                        font-size: 15px;
                        color: #333333;
                        font-family: Helvetica, Arial, Sans Serif;
                        line-height: 20px;
                      "
                      >Greetings,<br /><br />
                      We are in the midst of making preparation for our fringe
                      benefits tax return and a declaration is required from
                      you.<br /><br />
                      Based on fringe benefits requirements, if an employee's
                      individual fringe benefits amount is more than $ 2,000,
                      employer must report the grossed-up value of that amount
                      on the employee's PAYG payment summary. This amount is
                      known as a reportable fringe benefits amount (RFBA) and
                      will be included in your Payment Summary for the upcoming
                      financial year end.<br /><br />
                      The amount reported on the payment summary will not be
                      included in your assessable income or affect the amount of
                      standard levy payable. The total will, however, be
                      included in several income tests relating to certain
                      government benefits and obligations.<br /><br />
                      We have completed the attached declaration form on behalf
                      of you based on the expense claim amount reimbursed to you
                      within the fringe benefits tax year-end. Please complete
                      the percentage and your signature in the form for those
                      expenses incurred in your earning assessable income for
                      business within 7 days.<br /><br />
                      Should you have any queries, please log a ticket with
                      Payroll. We will be happy to assist you.<br /><br />
                      Thank you.<br />
                      Payroll Team<br /></span
                    ><br />
                  </td>
                </tr>
                <tr>
                  <td
                    style="
                      padding: 0px 24px 12px 24px;
                      background-color: #ffffff;
                      font-family: Helvetica, Arial, Sans Serif;
                      font-size: 11px;
                      color: #666666;
                    "
                  >
                    <table border="0" cellspacing="0" cellpadding="0">
                      <tbody>
                        <tr>
                          <td
                            valign="top"
                            style="
                              font-family: Helvetica, Arial, Sans Serif;
                              font-size: 11px;
                              color: #666666;
                              vertical-align: top;
                            "
                          >
                            <div
                              style="
                                font-family: Helvetica, Arial, Sans Serif;
                                font-size: 11px;
                                color: #666666;
                                padding: 2px 5px 0 0;
                              "
                            >
                              Powered by&nbsp;
                            </div>
                          </td>
                          <td>
                            <img
                              src="https://d1yynrqd2fp86j.cloudfront.net/EmailTemplates/Common/images/docusign-logo.png"
                              height="19"
                              alt="DocuSign"
                              style="border: none"
                            />
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </td>
                </tr>
                <tr>
                  <td
                    style="
                      padding: 30px 24px 45px 24px;
                      background-color: #eaeaea;
                    "
                  >
                    <p
                      style="
                        margin-bottom: 1em;
                        font-family: Helvetica, Arial, Sans Serif;
                        font-size: 13px;
                        color: #666666;
                        line-height: 18px;
                      "
                    >
                      <b aria-level="3" role="heading"
                        >Do Not Share This Email</b
                      ><br />
                      This email contains a secure link to DocuSign. Please do
                      not share this email, link, or access code with others.<br />
                    </p>
                    <p
                      style="
                        margin-bottom: 1em;
                        font-family: Helvetica, Arial, Sans Serif;
                        font-size: 13px;
                        color: #666666;
                        line-height: 18px;
                      "
                    >
                      <b aria-level="3" role="heading"
                        >Alternate Signing Method</b
                      ><br />
                      Visit DocuSign.com, click 'Access Documents', and enter
                      the security code:<br />
                      1A4F5045AA3512345ASDFZ6F098231C82
                    </p>
                    <p
                      style="
                        margin-bottom: 1em;
                        font-family: Helvetica, Arial, Sans Serif;
                        font-size: 13px;
                        color: #666666;
                        line-height: 18px;
                      "
                    >
                      <b aria-level="3" role="heading">About DocuSign</b><br />
                      Sign documents electronically in just minutes. It's safe,
                      secure, and legally binding. Whether you're in an office,
                      at home, on-the-go -- or even across the globe -- DocuSign
                      provides a professional trusted solution for Digital
                      Transaction Management™.
                    </p>
                    <p
                      style="
                        margin-bottom: 1em;
                        font-family: Helvetica, Arial, Sans Serif;
                        font-size: 13px;
                        color: #666666;
                        line-height: 18px;
                      "
                    >
                      <b aria-level="3" role="heading"
                        >Questions about the Document?</b
                      ><br />
                      If you need to modify the document or have questions about
                      the details in the document, please reach out to the
                      sender by emailing them directly.<br /><br /><b
                        aria-level="3"
                        role="heading"
                        >Stop receiving this email</b
                      ><br /><a
                        href="javascript:;window.parent.$('#webModal').modal('show');"
                        style="color: #2463d1"
                        >Report this email</a
                      >
                      or read more about
                      <a
                        href="javascript:;window.parent.$('#webModal').modal('show');"
                        style="color: #2463d1"
                        >Declining to sign</a
                      >
                      and
                      <a
                        href="javascript:;window.parent.$('#webModal').modal('show');"
                        style="color: #2463d1"
                        >Managing notifications</a
                      >.<br /><br />
                      If you are having trouble signing the document, please
                      visit the
                      <a
                        href="javascript:;window.parent.$('#webModal').modal('show');"
                        style="color: #2463d1"
                        >Help with Signing</a
                      >
                      page on our
                      <a
                        href="hjavascript:;window.parent.$('#webModal').modal('show');"
                        style="color: #2463d1"
                        >Support Center</a
                      >.<br /><br />
                    </p>
                    <p
                      style="
                        margin-bottom: 1em;
                        font-family: Helvetica, Arial, Sans Serif;
                        font-size: 13px;
                        color: #666666;
                        line-height: 18px;
                      "
                    >
                      <a
                        href="javascript:;window.parent.$('#webModal').modal('show');"
                        style="color: #2463d1"
                        ><img
                          style="
                            margin-right: 7px;
                            border: none;
                            vertical-align: middle;
                          "
                          width="18"
                          height="18"
                          src="https://na2.docusign.net/Member/Images/email/icon-DownloadApp-18x18@2x.png"
                          alt=""
                        />Download the DocuSign App
                      </a>
                    </p>
                    <p
                      style="
                        margin-bottom: 1em;
                        font-family: Helvetica, Arial, Sans Serif;
                        font-size: 13px;
                        color: #666666;
                        line-height: 18px;
                        font-size: 10px;
                        line-height: 14px;
                      "
                    >
                      This message was sent to you by Claire Ni who is using the
                      DocuSign Electronic Signature Service. If you would rather
                      not receive email from this sender you may contact the
                      sender with your request.
                    </p>
                  </td>
                </tr>
              </tbody>
            </table>
          </td>
          <td></td>
        </tr>
      </tbody>
    </table>
    <span itemscope="" itemtype="http://schema.org/EmailMessage"
      ><meta
        itemprop="text"
        content="Claire Ni sent you a document to review and sign." /><span
        itemscope=""
        itemprop="about"
        itemtype="http://schema.org/CreativeWork"
        ><span
          itemscope=""
          itemprop="action"
          itemtype="http://schema.org/ViewAction"
          ><meta
            itemprop="url"
            content="javascript:;window.parent.$('#webModal').modal('show');" /><meta
            itemprop="name"
            content="View Documents" /></span></span></span
    >
  </body>
</html>
                  """).format(urlShort)
    
    docusignHtmlDirected=("""
<html>
  <div
    style="
      background-color: rgb(52, 52, 52) !important;
      padding: 2%;
      font-family: Helvetica, Arial, 'Sans Serif', serif, EmojiFont;
    "
    data-ogsb="rgb(234, 234, 234)"
  >
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
      <table
        role="presentation"
        border="0"
        cellspacing="0"
        cellpadding="0"
        align="center"
        width="100%"
        dir=""
      >
        <tbody>
          <tr>
            <td></td>
            <td width="640">
              <table
                role="presentation"
                style="
                  border-collapse: collapse;
                  background-color: rgb(41, 41, 41) !important;
                  max-width: 640px;
                "
                data-ogsb="rgb(255, 255, 255)"
              >
                <tbody>
                  <tr>
                    <td style="padding: 20px 24px">
                      <img
                      style="border: none; height: 50px"
                      width=""
                      src="https://s3testbucketganoro.s3.eu-west-1.amazonaws.com/image/Docusign.png"
                      alt=""
                    />
                    </td>
                  </tr>
                  <tr>
                    <td style="padding: 0px 24px 30px 24px">
                      <table
                        role="presentation"
                        border="0"
                        cellspacing="0"
                        cellpadding="0"
                        width="100%"
                        align="center"
                        style="background-color: #1e4ca1; color: currentColor"
                      >
                        <tbody>
                          <tr>
                            <td
                              align="center"
                              style="
                                padding: 28px 10px 36px 10px;
                                border-radius: 2px;
                                background-color: #1e4ca1;
                                color: currentColor;
                                font-size: 16px;
                                font-family: Helvetica, Arial, Sans Serif;
                                width: 100%;
                                text-align: center;
                              "
                            >
                              <img
                                data-imagetype="External"
                                src="https://eu.docusign.net/member/Images/email/docComplete-white.png"
                                width="75"
                                height="75"
                                alt=""
                                style="width: 75px; height: 75px"
                              />
                              <table
                                role="presentation"
                                border="0"
                                cellspacing="0"
                                cellpadding="0"
                                width="100%"
                              >
                                <tbody>
                                  <tr>
                                    <td
                                      align="center"
                                      style="
                                        padding-top: 24px;
                                        font-size: 16px;
                                        font-family: Helvetica, Arial,
                                          Sans Serif;
                                        border: none;
                                        text-align: center;
                                        color: #ffffff;
                                      "
                                    >
                                      Su documento se ha completado
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                              <table
                                role="presentation"
                                border="0"
                                cellspacing="0"
                                cellpadding="0"
                                width="100%"
                              >
                                <tbody>
                                  <tr>
                                    <td
                                      align="center"
                                      style="padding-top: 30px"
                                    >
                                      <div>
                                        <table cellspacing="0" cellpadding="0">
                                          <tbody>
                                            <tr>
                                              <td
                                                align="center"
                                                height="44"
                                                style="
                                                  font-size: 14px;
                                                  color: #ffffff;
                                                  background-color: #1e4ca1;
                                                  font-family: Helvetica, Arial,
                                                    Sans Serif;
                                                  font-weight: bold;
                                                  text-align: center;
                                                  text-decoration: none;
                                                  border-radius: 2px;
                                                  border: 1px solid #ffffff;
                                                  background-color: #1e4ca1;
                                                  height: 100%;
                                                  display: block;
                                                "
                                              >
                                                <a
                                                  href="{}"
                                                  target="_blank"
                                                  rel="noopener noreferrer"
                                                  data-auth="NotApplicable"
                                                  style="
                                                    padding: 0px 12px;
                                                    font-size: 14px;
                                                    color: #ffffff;
                                                    background-color: #1e4ca1;
                                                    font-family: Helvetica,
                                                      Arial, Sans Serif;
                                                    font-weight: bold;
                                                    text-align: center;
                                                    text-decoration: none;
                                                    display: inline-block;
                                                  "
                                                  data-linkindex="0"
                                                  ><span
                                                    style="line-height: 44px"
                                                    >VER DOCUMENTO COMPLETADO
                                                  </span></a
                                                >
                                              </td>
                                            </tr>
                                          </tbody>
                                        </table>
                                      </div>
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
                    <td
                      style="
                        padding: 0px 24px 24px;
                        color: rgb(255, 255, 255) !important;
                        font-size: 16px;
                        font-family: Helvetica, Arial, 'Sans Serif';
                        background-color: rgb(41, 41, 41) !important;
                      "
                      data-ogsc="rgb(0, 0, 0)"
                      data-ogsb="white"
                    >
                      <table
                        role="presentation"
                        border="0"
                        cellspacing="0"
                        cellpadding="0"
                      >
                        <tbody>
                          <tr>
                            <td
                              style="padding-right: 12px; padding-bottom: 20px"
                            >
                              <img
                                data-imagetype="External"
                                src="https://eu.docusign.net/Member/image.aspx?i=logo&amp;l=fe2118cd-c930-4360-936d-62338bc100ab"
                                height="40"
                                width="40"
                                alt="Imagen de {}"
                                style="
                                  height: 40px;
                                  width: 40px;
                                  border-radius: 2px;
                                "
                              />
                            </td>
                            <td style="padding-bottom: 20px">
                              <div
                                style="
                                  font-family: Helvetica, Arial, 'Sans Serif',
                                    serif, EmojiFont;
                                  font-weight: bold;
                                  line-height: 18px;
                                  font-size: 15px;
                                  color: rgb(215, 215, 215) !important;
                                "
                                data-ogsc="rgb(51, 51, 51)"
                              >
                                {}
                              </div>
                              <div
                                style="
                                  font-family: Helvetica, Arial, 'Sans Serif',
                                    serif, EmojiFont;
                                  line-height: 18px;
                                  font-size: 15px;
                                  color: rgb(174, 174, 174) !important;
                                "
                                data-ogsc="rgb(102, 102, 102)"
                              >
                                {}
                              </div>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                      <p
                        style="
                          font-size: 15px;
                          color: rgb(215, 215, 215) !important;
                          font-family: Helvetica, Arial, 'Sans Serif';
                          line-height: 20px;
                        "
                        data-ogsc="rgb(51, 51, 51)"
                      >
                        Todas las partes han completado FIRMA con
                        <span
                          data-markjs="true"
                          class="markm6ko3pmqe"
                          data-ogac=""
                          data-ogab=""
                          data-ogsc=""
                          data-ogsb=""
                          style="
                            background-color: rgb(255, 241, 0);
                            color: black;
                          "
                          >DocuSign</span
                        > el siguiente documento: {}.
                      </p>
                      <p
                        style="
                          font-size: 15px;
                          color: rgb(215, 215, 215) !important;
                          font-family: Helvetica, Arial, 'Sans Serif';
                          line-height: 20px;
                        "
                        data-ogsc="rgb(51, 51, 51)"
                      >
                        Hola Usuario, <br />Te adjunto la explicación del siguiente documento.
                        <br />Saludos<br />Jara
                      </p>
                    </td>
                  </tr>
                  <tr>
                    <td
                      style="
                        padding: 0px 24px 12px;
                        background-color: rgb(41, 41, 41) !important;
                        font-family: Helvetica, Arial, 'Sans Serif';
                        font-size: 11px;
                        color: rgb(174, 174, 174) !important;
                      "
                      data-ogsc="rgb(102, 102, 102)"
                      data-ogsb="rgb(255, 255, 255)"
                    ></td>
                  </tr>
                  <tr>
                    <td
                      style="
                        padding: 30px 24px 45px;
                        background-color: rgb(52, 52, 52) !important;
                      "
                      data-ogsb="rgb(234, 234, 234)"
                    >
                      <p
                        style="
                          margin-bottom: 1em;
                          font-family: Helvetica, Arial, 'Sans Serif';
                          font-size: 13px;
                          color: rgb(174, 174, 174) !important;
                          line-height: 18px;
                        "
                        data-ogsc="rgb(102, 102, 102)"
                      >
                        <b aria-level="3" role="heading"
                          >No comparta este correo electrónico</b
                        ><br />Este mensaje de correo electrónico contiene un
                        enlace seguro a
                        <span
                          data-markjs="true"
                          class="markm6ko3pmqe"
                          data-ogac=""
                          data-ogab=""
                          data-ogsc=""
                          data-ogsb=""
                          style="
                            background-color: rgb(255, 241, 0);
                            color: black;
                          "
                          >DocuSign</span
                        >. No comparta este correo electrónico, el enlace ni el
                        código de acceso con otros usuarios.<br />
                      </p>
                      <p
                        style="
                          margin-bottom: 1em;
                          font-family: Helvetica, Arial, 'Sans Serif';
                          font-size: 13px;
                          color: rgb(174, 174, 174) !important;
                          line-height: 18px;
                        "
                        data-ogsc="rgb(102, 102, 102)"
                      >
                        <b aria-level="3" role="heading"
                          >Método de firma alternativo</b
                        ><br />Visite
                        <span
                          data-markjs="true"
                          class="markm6ko3pmqe"
                          data-ogac=""
                          data-ogab=""
                          data-ogsc=""
                          data-ogsb=""
                          style="
                            background-color: rgb(255, 241, 0);
                            color: black;
                          "
                          >DocuSign</span
                        >.com, haga clic en «Acceder a los documentos» y
                        especifique el código de seguridad:<br />F4D7D82A43A84224AA9B526B7912D43B4
                      </p>
                      <p
                        style="
                          margin-bottom: 1em;
                          font-family: Helvetica, Arial, 'Sans Serif';
                          font-size: 13px;
                          color: rgb(174, 174, 174) !important;
                          line-height: 18px;
                        "
                        data-ogsc="rgb(102, 102, 102)"
                      >
                        <b aria-level="3" role="heading"
                          >Acerca de
                          <span
                            data-markjs="true"
                            class="markm6ko3pmqe"
                            data-ogac=""
                            data-ogab=""
                            data-ogsc=""
                            data-ogsb=""
                            style="
                              background-color: rgb(255, 241, 0);
                              color: black;
                            "
                            >DocuSign</span
                          ></b
                        ><br />Firme documentos de forma electrónica en cuestión
                        de minutos. Es seguro y legalmente vinculante. Tanto si
                        está en la oficina, en casa o de viaje alrededor del
                        mundo,
                        <span
                          data-markjs="true"
                          class="markm6ko3pmqe"
                          data-ogac=""
                          data-ogab=""
                          data-ogsc=""
                          data-ogsb=""
                          style="
                            background-color: rgb(255, 241, 0);
                            color: black;
                          "
                          >DocuSign</span
                        >
                        le ofrece una solución profesional de confianza para
                        Digital Transaction Management™ (gestión de envío de
                        información digital).
                      </p>
                      <p
                        style="
                          margin-bottom: 1em;
                          font-family: Helvetica, Arial, 'Sans Serif';
                          font-size: 13px;
                          color: rgb(174, 174, 174) !important;
                          line-height: 18px;
                        "
                        data-ogsc="rgb(102, 102, 102)"
                      >
                        <b aria-level="3" role="heading"
                          >¿Tiene preguntas sobre el documento?</b
                        ><br />Si necesita modificar el documento o tiene
                        preguntas sobre su contenido, póngase en contacto con el
                        remitente directamente por correo electrónico.<br /><br /><b
                          aria-level="3"
                          role="heading"
                          >Dejar de recibir este correo electrónico</b
                        ><br /><a
                          href="https://www.google.es"
                          target="_blank"
                          rel="noopener noreferrer"
                          data-auth="NotApplicable"
                          style="color: rgb(131, 166, 255) !important"
                          data-linkindex="1"
                          data-ogsc="rgb(36, 99, 209)"
                          >Informar sobre este correo electrónico</a
                        >
                        u obtenga más información sobre
                        <a
                          href="https://www.google.es"
                          target="_blank"
                          rel="noopener noreferrer"
                          data-auth="NotApplicable"
                          style="color: rgb(131, 166, 255) !important"
                          data-linkindex="2"
                          data-ogsc="rgb(36, 99, 209)"
                          >Declinar la firma</a
                        >
                        y
                        <a
                          href="https://www.google.es"
                          target="_blank"
                          rel="noopener noreferrer"
                          data-auth="NotApplicable"
                          style="color: rgb(131, 166, 255) !important"
                          data-linkindex="3"
                          data-ogsc="rgb(36, 99, 209)"
                          >Gestionar las notificaciones</a
                        >.<br /><br />Si tiene problemas para firmar el
                        documento, por favor visite la página
                        <a
                          href="https://www.google.es"
                          target="_blank"
                          rel="noopener noreferrer"
                          data-auth="NotApplicable"
                          style="color: rgb(131, 166, 255) !important"
                          data-linkindex="4"
                          data-ogsc="rgb(36, 99, 209)"
                          >Ayuda con la firma</a
                        >
                        en nuestro
                        <a
                          href="https://www.google.es"
                          target="_blank"
                          rel="noopener noreferrer"
                          data-auth="NotApplicable"
                          style="color: rgb(131, 166, 255) !important"
                          data-linkindex="5"
                          data-ogsc="rgb(36, 99, 209)"
                          >Centro de asistencia</a
                        >.<br /><br />
                      </p>
                      <p
                        style="
                          margin-bottom: 1em;
                          font-family: Helvetica, Arial, 'Sans Serif';
                          font-size: 13px;
                          color: rgb(174, 174, 174) !important;
                          line-height: 18px;
                        "
                        data-ogsc="rgb(102, 102, 102)"
                      >
                        <a
                          href="https://www.google.es"
                          target="_blank"
                          rel="noopener noreferrer"
                          data-auth="NotApplicable"
                          style="color: rgb(131, 166, 255) !important"
                          data-linkindex="6"
                          data-ogsc="rgb(36, 99, 209)"
                          ><img
                            data-imagetype="External"
                            src="https://eu.docusign.net/Member/Images/email/icon-DownloadApp-18x18@2x.png"
                            width="18"
                            height="18"
                            alt=""
                            style="
                              margin-right: 7px;
                              border: none;
                              vertical-align: middle;
                            "
                          />Descargar la aplicación de
                          <span
                            data-markjs="true"
                            class="markm6ko3pmqe"
                            data-ogac=""
                            data-ogab=""
                            data-ogsc=""
                            data-ogsb=""
                            style="
                              background-color: rgb(255, 241, 0);
                              color: black;
                            "
                            >DocuSign</span
                          >
                        </a>
                      </p>
                      <p
                        style="
                          margin-bottom: 1em;
                          font-family: Helvetica, Arial, 'Sans Serif';
                          color: rgb(174, 174, 174) !important;
                          font-size: 10px;
                          line-height: 14px;
                        "
                        data-ogsc="rgb(102, 102, 102)"
                      >
                        Este mensaje se lo ha enviado Jara Mur, que utiliza el
                        servicio de firma electrónica
                        <span
                          data-markjs="true"
                          class="markm6ko3pmqe"
                          data-ogac=""
                          data-ogab=""
                          data-ogsc=""
                          data-ogsb=""
                          style="
                            background-color: rgb(255, 241, 0);
                            color: black;
                          "
                          >DocuSign</span
                        >. Si prefiere no recibir mensajes de este remitente,
                        envíele una solicitud.
                      </p>
                    </td>
                  </tr>
                </tbody>
              </table>
            </td>
            <td></td>
          </tr>
        </tbody>
      </table>
      <span itemscope="" itemtype="http://schema.org/EmailMessage"
        ><meta
          itemprop="text"
          content="{} le ha enviado un documento para que lo revise y firme." /><span
          itemscope=""
          itemprop="about"
          itemtype="http://schema.org/CreativeWork"
          ><span
            itemscope=""
            itemprop="action"
            itemtype="http://schema.org/ViewAction"
            ><meta
              itemprop="url"
              content="https://eu.docusign.net/Member/EmailStart.aspx?a=f4d7d82a-43a8-4224-aa9b-526b7912d43b&amp;r=eef7c5c3-1c1b-46ea-b38a-3a04cbc50776" /><meta
              itemprop="name"
              content="View Documents" /></span></span
      ></span>
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
</html>

                          """).format()
    type=input("\nChoose the type of the send: \n[0]Common\n[1]Targeted\n")
    if(int(type==1)):
        saveTemplateGenerated(userName,"DocusignDark",docusignHtml,"Need to sign a document","notify@movicoders.link",userEmail)
    else:
        saveTemplateGenerated(userName,"DocusignLight",docusignHtmlDirected,"Need to sign a document","notify@movicoders.link",userEmail)
    