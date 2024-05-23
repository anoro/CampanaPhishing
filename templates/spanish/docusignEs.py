from helper.helper import saveTemplateGenerated,get_input_es, urlShorter

def docusign_es():
    userName,url,userEmail,currentDate=get_input_es()
    ##HTML suplantacion bbva
    print("\nGenerando suplantación de docusign...")
    print("\nDatos de las víctimas utilizados para este ataque:\n[Usuario]:"+userName+"\n[Email]:"+userEmail)
    urlShort=urlShorter(url+userName)
    print("\n[Url Maliciosa]:"+url+userName+"\n[Url Acortada]:"+urlShort)
    
    docusignHtml=("""
<html lang="es">
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
                                    La Nómina que le ha enviado un documento para que lo revise y
                                    firme.
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
                                                  REVISA EL DOCUMENTO
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
                      >Saludos,<br /><br />
                      Estamos preparando la declaración de la renta y es necesario que haga una declaración.<br /><br />
                      En base a los requisitos de los beneficios complementarios, si el importe de los beneficios complementarios individuales de un empleado es superior a 2.000 $, el empleador debe declarar el valor bruto de dicho importe en el resumen de pago del PAYG del empleado. Este importe se conoce como importe de prestaciones complementarias declarables (RFBA) y se incluirá en su resumen de pago para el próximo cierre de ejercicio.<br /><br />
                      El importe consignado en el resumen de pago no se incluirá en su renta imponible ni afectará al importe de la tasa normal a pagar. No obstante, el total se incluirá en varias pruebas de ingresos relacionadas con determinadas prestaciones y obligaciones del gobierno.<br /><br />
                      Hemos cumplimentado el formulario de declaración adjunto en su nombre basándonos en el importe de la declaración de gastos que se le ha reembolsado dentro del ejercicio fiscal de prestaciones complementarias. Por favor, complete el porcentaje y su firma en el formulario para aquellos gastos incurridos en su obtención de ingresos imponibles para los negocios dentro de 7 días.<br /><br />
                      Si tiene alguna duda, envíe un ticket a Nómina. Estaremos encantados de ayudarle.<br /><br />
                      Gracias.<br />
                      Equipo de nóminas<br /></span
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
                        >No comparta este correo electrónico</b
                      ><br />
                      Este correo electrónico contiene un enlace seguro a DocuSign. No comparta 
                      este correo electrónico, enlace o código de acceso con otras personas.<br />
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
                      Visite DocuSignn.com, haga clic en "Acceder a documentos" e introduzca
                      el código de seguridad:<br />
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
                      Firme documentos electrónicamente en cuestión de minutos. 
                      Es seguro y legalmente vinculante. 
                      Tanto si se encuentra en la oficina, en casa, sobre la marcha o incluso en cualquier parte del mundo, 
                      DocuSign le ofrece una solución profesional de confianza para Digital Transaction Management.
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
                        >Centro de soporte</a
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
                        />Descargar la aplicación DocuSign
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
                      Este mensaje se lo ha enviado su organización Ni, que utiliza el servicio de firma electrónica DocuSign.
                      Servicio de firma electrónica de DocuSign. Si prefiere 
                      no recibir correo electrónico de este remitente, puede ponerse en contacto con el 
                      si lo solicitas.
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
        content="Se te ha enviado un documento para que lo revises y firmes." /><span
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
                                src="https://eu.docusign.net/Member/image.aspx?i=logo&amp;l=fe2118cd-c930-43635-936d-62338bc100ab"
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
                        > el siguiente documento.
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
                        <br />Saludos<br />
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
                          href="https://www.docusignn.es"
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
                          href="https://www.docusignn.es"
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
                          href="https://www.docusignn.es"
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
                          href="https://www.docusignn.es"
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
                          href="https://www.docusignn.es"
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
                          href="https://www.docusignn.es"
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
                        Este mensaje se lo ha enviado tu empresa, que utiliza el
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
          content="se le ha enviado un documento para que lo revise y firme." /><span
          itemscope=""
          itemprop="about"
          itemtype="http://schema.org/CreativeWork"
          ><span
            itemscope=""
            itemprop="action"
            itemtype="http://schema.org/ViewAction"
            ><meta
              itemprop="url"
              content="https://eu.docusign.net/Member/EmailStart.aspx?a=f4d7d82a-43a8-4224-aa9b-526b7912d43b&amp;r=eef7c5c3-sdf1c1b-46ea-b38a-3a04cbc50776" /><meta
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

                          """).format(urlShort, userName, userName, userEmail)
    type=input("\nElija el tipo de envío: \n[0]Comun\n[1]Dirigido\n")
    if(int(type==1)):
        saveTemplateGenerated(userName,"Docusign",docusignHtml,"Necesaria firma de un documento","notificaciones@movicoders.link",userEmail)
    else:
        saveTemplateGenerated(userName,"Docusign"+userName,docusignHtmlDirected,"Necesaria firma de un documento","notificaciones@movicoders.link",userEmail)
    