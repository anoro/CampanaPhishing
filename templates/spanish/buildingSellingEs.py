import time
import os
import sys
import smtplib
from helper.helper import saveTemplateGenerated,get_input_es, urlShorter

def building_selling_es():
    
    userName,url,userEmail,currentDate=get_input_es()
    print("\nGenerando suplantanción idealista...")
    print("\nLos datos de la victima usados para este ataque:\n[Usuario]:"+userName+"\n[Email]:"+userEmail)
    urlShort=urlShorter(url+userName)
    print("\n[Url Maliciosa]:"+url+userName+"\n[Url Acortada]:"+urlShort)

    idealista_html=("""
<html>
  <div>
    <div>
      <div
        style="background-color: rgb(49, 49, 47) !important"
        data-ogsb="rgb(240, 240, 238)"
      >
        <span
          style="
            display: none;
            visibility: hidden;
            opacity: 0;
            color: rgba(255, 255, 255, 0) !important;
            height: 0px;
            width: 0px;
          "
          data-ogsc="transparent"
          >Te enviamos una novedad de tu búsqueda guardada.
        </span>
        <div
          style="
            background-image: initial;
            background-position: initial;
            background-size: initial;
            background-repeat: initial;
            background-attachment: initial;
            background-origin: initial;
            background-clip: initial;
            background-color: rgb(36, 59, 0) !important;
            margin: 0px auto;
            max-width: 600px;
          "
          data-ogsb="rgb(223, 250, 69)"
        >
          <table
            align="center"
            border="0"
            cellpadding="0"
            cellspacing="0"
            role="presentation"
            style="
              background-image: initial;
              background-position: initial;
              background-size: initial;
              background-repeat: initial;
              background-attachment: initial;
              background-origin: initial;
              background-clip: initial;
              background-color: rgb(36, 59, 0) !important;
              width: 100%;
            "
            data-ogsb="rgb(223, 250, 69)"
          >
            <tbody>
              <tr>
                <td
                  style="
                    direction: ltr;
                    font-size: 0px;
                    padding: 18px 24px;
                    text-align: center;
                    vertical-align: top;
                  "
                >
                  <div
                    class="x_mj-column-per-100 x_outlook-group-fix"
                    style="
                      font-size: 13px;
                      text-align: left;
                      direction: ltr;
                      display: inline-block;
                      vertical-align: top;
                      width: 100%;
                    "
                  >
                    <table
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      width="100%"
                      style="vertical-align: top"
                    >
                      <tbody>
                        <tr>
                          <td
                            align="left"
                            style="
                              font-size: 0px;
                              padding: 0;
                              word-break: break-word;
                            "
                          >
                            <table
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              style="
                                border-collapse: collapse;
                                border-spacing: 0px;
                              "
                            >
                              <tbody>
                                <tr>
                                  <td style="width: 111px">
                                    <a
                                      href="{}"
                                      target="_blank"
                                      rel="noopener noreferrer"
                                      data-auth="NotApplicable"
                                      data-linkindex="1"
                                      data-ogsc=""
                                      style="
                                        color: rgb(219, 151, 255) !important;
                                      "
                                      ><img
                                        data-imagetype="External"
                                        src="https://s3testbucketganoro.s3.eu-west-1.amazonaws.com/image/idealista.png"
                                        height="auto"
                                        width="111"
                                        style="
                                          border: 0;
                                          display: block;
                                          outline: none;
                                          text-decoration: none;
                                          height: auto;
                                          width: 100%;
                                        "
                                    /></a>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div
          style="
            background-image: initial;
            background-position: initial;
            background-size: initial;
            background-repeat: initial;
            background-attachment: initial;
            background-origin: initial;
            background-clip: initial;
            background-color: rgb(41, 41, 41) !important;
            margin: 0px auto;
            max-width: 600px;
          "
          data-ogsb="rgb(255, 255, 255)"
        >
          <table
            align="center"
            border="0"
            cellpadding="0"
            cellspacing="0"
            role="presentation"
            style="
              background-image: initial;
              background-position: initial;
              background-size: initial;
              background-repeat: initial;
              background-attachment: initial;
              background-origin: initial;
              background-clip: initial;
              background-color: rgb(41, 41, 41) !important;
              width: 100%;
            "
            data-ogsb="rgb(255, 255, 255)"
          >
            <tbody>
              <tr>
                <td
                  style="
                    direction: ltr;
                    font-size: 0px;
                    padding: 24px 24px 0;
                    text-align: center;
                    vertical-align: top;
                  "
                >
                  <div style="margin: 0px auto; max-width: 552px">
                    <table
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="width: 100%"
                    >
                      <tbody>
                        <tr>
                          <td
                            style="
                              direction: ltr;
                              font-size: 0px;
                              padding: 0 0 8px;
                              text-align: center;
                              vertical-align: top;
                            "
                          >
                            <div
                              class="x_mj-column-per-100 x_outlook-group-fix"
                              style="
                                font-size: 13px;
                                text-align: left;
                                direction: ltr;
                                display: inline-block;
                                vertical-align: top;
                                width: 100%;
                              "
                            >
                              <table
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                width="100%"
                              >
                                <tbody>
                                  <tr>
                                    <td style="vertical-align: top; padding: 0">
                                      <table
                                        border="0"
                                        cellpadding="0"
                                        cellspacing="0"
                                        role="presentation"
                                        width="100%"
                                      >
                                        <tbody>
                                          <tr>
                                            <td
                                              align="left"
                                              style="
                                                font-size: 0px;
                                                padding: 0;
                                                word-break: break-word;
                                              "
                                            >
                                              <div
                                                style="
                                                  font-family: Arial, serif,
                                                    EmojiFont;
                                                  font-size: 20px;
                                                  font-weight: 700;
                                                  line-height: 24px;
                                                  text-align: left;
                                                  color: rgb(
                                                    243,
                                                    243,
                                                    243
                                                  ) !important;
                                                "
                                                data-ogsc="rgb(20, 20, 20)"
                                              >
                                                Hola {},
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
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                  <div style="margin: 0px auto; max-width: 552px">
                    <table
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="width: 100%"
                    >
                      <tbody>
                        <tr>
                          <td
                            style="
                              direction: ltr;
                              font-size: 0px;
                              padding: 0;
                              text-align: center;
                              vertical-align: top;
                            "
                          >
                            <div
                              class="x_mj-column-per-100 x_outlook-group-fix"
                              style="
                                font-size: 13px;
                                text-align: left;
                                direction: ltr;
                                display: inline-block;
                                vertical-align: top;
                                width: 100%;
                              "
                            >
                              <table
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                width="100%"
                              >
                                <tbody>
                                  <tr>
                                    <td style="vertical-align: top; padding: 0">
                                      <table
                                        border="0"
                                        cellpadding="0"
                                        cellspacing="0"
                                        role="presentation"
                                        width="100%"
                                      >
                                        <tbody>
                                          <tr>
                                            <td
                                              align="left"
                                              style="
                                                font-size: 0px;
                                                padding: 0;
                                                word-break: break-word;
                                              "
                                            >
                                              <div
                                                style="
                                                  font-family: Arial, serif,
                                                    EmojiFont;
                                                  font-size: 16px;
                                                  line-height: 24px;
                                                  text-align: left;
                                                  color: rgb(
                                                    243,
                                                    243,
                                                    243
                                                  ) !important;
                                                "
                                                data-ogsc="rgb(20, 20, 20)"
                                              >
                                                Te enviamos una novedad de tu
                                                búsqueda guardada.
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
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div
          style="
            background-image: initial;
            background-position: initial;
            background-size: initial;
            background-repeat: initial;
            background-attachment: initial;
            background-origin: initial;
            background-clip: initial;
            background-color: rgb(41, 41, 41) !important;
            margin: 0px auto;
            max-width: 600px;
          "
          data-ogsb="rgb(255, 255, 255)"
        >
          <table
            align="center"
            border="0"
            cellpadding="0"
            cellspacing="0"
            role="presentation"
            style="
              background-image: initial;
              background-position: initial;
              background-size: initial;
              background-repeat: initial;
              background-attachment: initial;
              background-origin: initial;
              background-clip: initial;
              background-color: rgb(41, 41, 41) !important;
              width: 100%;
            "
            data-ogsb="rgb(255, 255, 255)"
          >
            <tbody>
              <tr>
                <td
                  style="
                    direction: ltr;
                    font-size: 0px;
                    padding: 0 24px;
                    text-align: center;
                    vertical-align: top;
                  "
                >
                  <div style="margin: 0px auto; max-width: 552px">
                    <table
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="width: 100%"
                    >
                      <tbody>
                        <tr>
                          <td
                            style="
                              direction: ltr;
                              font-size: 0px;
                              padding: 0;
                              text-align: center;
                              vertical-align: top;
                            "
                          >
                            <div
                              class="x_mj-column-per-100 x_outlook-group-fix"
                              style="
                                font-size: 13px;
                                text-align: left;
                                direction: ltr;
                                display: inline-block;
                                vertical-align: top;
                                width: 100%;
                              "
                            >
                              <table
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                width="100%"
                              >
                                <tbody>
                                  <tr>
                                    <td
                                      style="
                                        vertical-align: top;
                                        padding: 24px 0 4px;
                                      "
                                    >
                                      <table
                                        border="0"
                                        cellpadding="0"
                                        cellspacing="0"
                                        role="presentation"
                                        width="100%"
                                      >
                                        <tbody>
                                          <tr>
                                            <td
                                              align="left"
                                              style="
                                                font-size: 0px;
                                                padding: 0;
                                                word-break: break-word;
                                              "
                                            >
                                              <div
                                                style="
                                                  font-family: Arial, serif,
                                                    EmojiFont;
                                                  font-size: 20px;
                                                  line-height: 24px;
                                                  text-align: left;
                                                  color: rgb(
                                                    243,
                                                    243,
                                                    243
                                                  ) !important;
                                                "
                                                data-ogsc="rgb(20, 20, 20)"
                                              >
                                                <b
                                                  >Oficinas en Área de
                                                  Zaragoza</b
                                                >
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
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                  <div style="margin: 0px auto; max-width: 552px">
                    <table
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="width: 100%"
                    >
                      <tbody>
                        <tr>
                          <td
                            style="
                              direction: ltr;
                              font-size: 0px;
                              padding: 0 0 10px;
                              text-align: center;
                              vertical-align: top;
                            "
                          >
                            <div
                              class="x_mj-column-per-100 x_outlook-group-fix"
                              style="
                                font-size: 13px;
                                text-align: left;
                                direction: ltr;
                                display: inline-block;
                                vertical-align: top;
                                width: 100%;
                              "
                            >
                              <table
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                width="100%"
                                style="vertical-align: top"
                              >
                                <tbody>
                                  <tr>
                                    <td
                                      align="left"
                                      style="
                                        font-size: 0px;
                                        padding: 0;
                                        word-break: break-word;
                                      "
                                    >
                                      <table
                                        cellpadding="0"
                                        cellspacing="0"
                                        width="100%"
                                        border="0"
                                        style="
                                          color: rgb(255, 255, 255) !important;
                                          font-family: Arial;
                                          font-size: 13px;
                                          line-height: 22px;
                                          table-layout: auto;
                                          width: 100%;
                                        "
                                        data-ogsc="rgb(0, 0, 0)"
                                      >
                                        <tbody>
                                          <tr>
                                            <td
                                              width="100"
                                              valign="top"
                                              style="
                                                padding-top: 8px;
                                                line-height: 0;
                                              "
                                            >
                                              <img
                                                data-imagetype="External"
                                                src="https://maps3.idealista.com/maps/api/staticmap?path=weight%3A2%7Ccolor%3A0x666664ff%7Cfillcolor%3A0x8e8f8c44%7Cenc%3Aeqy%7CFtqiEcn%40cYuzAj%5De%5Ex%5BoInd%40lLzhAqd%40rdB%7BcBnvCuIdl%40%7D%5Cng%40c%40fdB%7ETzvA%7BT%7CpBxNfMyFla%40c_%40jXqnAs%7BAo%7CAp%40cvBofAeVtFcsCzsBmf%40yh%40eS%7DpAk%7C%40%7BjB%7DRhIka%40oq%40xCiXjb%40o%5Czg%40dHbbAqWtV%7BQ%7E%5D_y%40j%60%40qgBsNonA%7E%40gn%40_e%40e%7BAkOiCoY%60MkVjd%40wyA%60%7BDQsq%40%7Cm%40waA%7Ck%40mfCf%5Cgr%40gQ_E%7BAun%40oj%40o%5BrAiSfRoLeDgItNwZkJiLrDoj%40kEiG%7DVmLwXbCkT_Ze%5E%60q%40oP%7CFqeBfrE%7Dr%40doAwsAhmAss%40%7C%60DsKxvDuVnM%7BgAkk%40o%7B%40su%40woBlF_PwYc%5E%7DFqOcd%40sdA_%60AeNy%5B_l%40w%5Due%40kB_e%40%60Km_Ac%60BsRqx%40%60Bkt%40yNek%40cEgaAmJgSwt%40kVyg%40giAvBu%5Bk%5Bkv%40sc%40aiC%60Kke%40%7BXsp%40jAaa%40qL%7DOrCew%40y%60%40uw%40im%40bG_dApa%40iqBeMug%40fSkoB%60B%7Bv%40rQuYmFgKyb%40pV%7BzAzCmrBbVc%7E%40dXu%5CwDq%60%40nX_lAqA%7Da%40hJsWjk%40ig%40%60BcSvg%40%7D%7B%40zPibAvf%40cqAjD%7Bd%40hNwDnv%40afBj_%40apBhXg_Goi%40ar%40gCa%5BtY%7BkDgLiq%40jF%7D%60E%60vAoi%40nvCkuB%60j%40mL%60i%40uvA%7EVyjBzRqV%7C%7D%40jUns%40nd%40tp%40mS%7CkA%7E%7D%40p%5C%7C%40xoBttBnDhXxYve%40gn%40pmCwa%40vp%40mt%40hQsyBj%7CAplA%7E%7EAbn%40daCdM%7CGxTa%7BAdD%7BlA%60cD%7ENjyBuN%60v%40cd%40p%7D%40k%40%7ELv%5CvU%7Dc%40pa%40%7DUdd%40hJfVrUzYd%7C%40yDtSzG%60i%40t_%40_Wzu%40vLk%40sCbu%40md%40r%60%40oEdJfH%60%5D%7D%5CjLav%40zTsf%40ff%40iOjK_%60AzRaHxc%40qi%40Ecu%40ob%40x%40t%40e%7CEmHypAjOkx%40ng%40pFvcD_%5EfiAkp%40hpA%7Ba%40xj%40ce%40fz%40yAnb%40uMlbAqoAE%7DUki%40%7Di%40vYodCiAoYzPsu%40hf%40%7Df%40vzE%7ClA%60Heo%40r_%40rFfZ%7BJrI%7CLz%7C%40xF%7C%60AfyAp%7C%40r%5EhfAhw%40xD%7Ec%40jUsa%40vnAtjAbY%7DNlk%40%7CdAr%5CyH%60a%40%7D%60%40xh%40xf%40xbF%7CrAdvBv%7BAfvAlFjrAmt%40%7EDvnB_%7BAf%7BCjB%7ETdgBj%7EBs%7B%40ptCaIfwBke%40%7E%7EAnAhTiWfkAil%40blAgb%40dvAm%5D%60xDir%40px%40cVbt%40mOr%40uIxh%40%7DOhKtGxNcCv%5DeHxCsIzd%40q_%40%7CGkLf%60%40gh%40zTwT%7Ee%40av%40%7C_%40yYdz%40on%40fr%40chCi%60BoGtiAvuBfoCvQfIeJlfBtDfcBn%5E%7BGnGpKli%40bMvsAab%40%7EcA%7CQpq%40r%5C%60tA%7COd%5Cu%5B%7Ec%40xJbj%40qNlLiWrWjJje%40lmBbA%7CjAnc%40hlAifAzqCcE%7EdAuIh%40k%5Bn%60Aye%40pm%40yFnd%40cXnd%40%7DjB%7EIwmAxW_HzTkf%40h%5Du%40fF%7CJ%40kWxh%40hA%60SeZ%7EGyy%40%60uA%7D%60%40z%5DeFhv%40mOHem%40eb%40qrA%7B%7BBuc%40b%60%40kiAox%40mf%40cr%40ce%40ni%40iZvo%40%7CTxw%40b%40jVgITNxHbYdF%7BDtNtK%60EmOrNY%7EMsSkHbA%60QmU%7DM%7ERrz%40mNzB%7DLoVwBdRoKb%40a%40dTzKnHuHnJ_Ada%40mV%7BYwLzt%40mM%7BOG%7B%7BAwRhd%40sAgk%40%7BIkCbQyf%40um%40th%40aTwA%40en%40%60NwNqF%60DgYoYfNm%5BkSlBgF%7Bd%40aGpHoNcBv%40a%5EuTz%5EqUh%40%7DKu_%40dDgFac%40gXwGg%7B%40fLaDBe%5D&amp;size=100x100&amp;format=png&amp;maptype=roadmap&amp;language=es&amp;key=AIzaSyBvWPgYmrRwIkojymtF7I60mxoB8n56onQ&amp;signature=mEETYdTMX0c5_cI-n3E6abmieAc="
                                              />
                                            </td>
                                            <td
                                              valign="top"
                                              align="left"
                                              style="
                                                padding-left: 16px;
                                                padding-top: 6px;
                                              "
                                            >
                                              <div>
                                                <span
                                                  style="
                                                    font-size: 16px;
                                                    display: inline-block;
                                                    line-height: 24px;
                                                  "
                                                  >Todos los precios</span
                                                >
                                              </div>
                                              <div>
                                                <span
                                                  style="
                                                    font-size: 16px;
                                                    display: block;
                                                    line-height: 24px;
                                                  "
                                                  >Sin otros filtros</span
                                                >
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
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                  <div style="margin: 0px auto; max-width: 552px">
                    <table
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="width: 100%"
                    >
                      <tbody>
                        <tr>
                          <td
                            style="
                              direction: ltr;
                              font-size: 0px;
                              padding: 0;
                              text-align: center;
                              vertical-align: top;
                            "
                          >
                            <div
                              class="x_mj-column-per-100 x_outlook-group-fix"
                              style="
                                font-size: 13px;
                                text-align: left;
                                direction: ltr;
                                display: inline-block;
                                vertical-align: top;
                                width: 100%;
                              "
                            >
                              <table
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                width="100%"
                                style="vertical-align: top"
                              >
                                <tbody>
                                  <tr>
                                    <td
                                      style="
                                        font-size: 0px;
                                        word-break: break-word;
                                      "
                                    >
                                      <div
                                        style="height: 12px"
                                        aria-hidden="true"
                                      >
                                        &nbsp;
                                      </div>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                  <div
                    class="x_cards-margin"
                    style="
                      background-image: initial;
                      background-position: initial;
                      background-size: initial;
                      background-repeat: initial;
                      background-attachment: initial;
                      background-origin: initial;
                      background-clip: initial;
                      background-color: rgb(41, 41, 41) !important;
                      margin: 0px auto;
                      max-width: 552px;
                    "
                    data-ogsb="rgb(255, 255, 255)"
                  >
                    <table
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="
                        background-image: initial;
                        background-position: initial;
                        background-size: initial;
                        background-repeat: initial;
                        background-attachment: initial;
                        background-origin: initial;
                        background-clip: initial;
                        background-color: rgb(41, 41, 41) !important;
                        width: 100%;
                      "
                      data-ogsb="rgb(255, 255, 255)"
                    >
                      <tbody>
                        <tr>
                          <td
                            style="
                              border-bottom: 1px solid #e5e6e1;
                              border-left: 1px solid #e5e6e1;
                              border-right: 1px solid #e5e6e1;
                              border-top: 1px solid #e5e6e1;
                              direction: ltr;
                              font-size: 0px;
                              padding: 0;
                              text-align: center;
                              vertical-align: top;
                            "
                          >
                            <div
                              class="x_mj-column-per-55 x_outlook-group-fix"
                              style="
                                font-size: 13px;
                                text-align: left;
                                direction: ltr;
                                display: inline-block;
                                vertical-align: top;
                                width: 100%;
                              "
                            >
                              <a
                                href="{}"
                                target="_blank"
                                rel="noopener noreferrer"
                                data-auth="NotApplicable"
                                title="Oficina en plaza de San Miguel, Paseo Independencia, Zaragoza"
                                data-linkindex="2"
                                data-ogsc=""
                                style="color: rgb(219, 151, 255) !important"
                                ><img
                                  data-imagetype="External"
                                  src="https://img3.idealista.com/blur/500_375_mq/0/id.pro.es.image.master/6c/96/00/944400992.jpg"
                                  alt="Oficina en plaza de San Miguel, Paseo Independencia, Zaragoza"
                                  class="x_imagen-inmueble"
                                  width="277"
                                  style="width: 277px; display: block"
                              /></a>
                              <table
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                width="100%"
                                style="vertical-align: top"
                              ></table>
                            </div>
                            <div
                              class="x_mj-column-per-44 x_outlook-group-fix"
                              style="
                                font-size: 13px;
                                text-align: left;
                                direction: ltr;
                                display: inline-block;
                                vertical-align: top;
                                width: 100%;
                              "
                            >
                              <table
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                width="100%"
                              >
                                <tbody>
                                  <tr>
                                    <td
                                      style="
                                        vertical-align: top;
                                        padding: 16px 14px;
                                      "
                                    >
                                      <table
                                        border="0"
                                        cellpadding="0"
                                        cellspacing="0"
                                        role="presentation"
                                        width="100%"
                                      >
                                        <tbody>
                                          <tr>
                                            <td
                                              align="left"
                                              style="
                                                font-size: 0px;
                                                padding: 0 0 8px;
                                                word-break: break-word;
                                              "
                                            >
                                              <div
                                                style="
                                                  font-family: Arial, serif,
                                                    EmojiFont;
                                                  font-size: 14px;
                                                  font-weight: 700;
                                                  line-height: 18px;
                                                  text-align: left;
                                                  color: rgb(
                                                    255,
                                                    124,
                                                    207
                                                  ) !important;
                                                "
                                                data-ogsc="rgb(182, 38, 130)"
                                              >
                                                Novedad
                                              </div>
                                            </td>
                                          </tr>
                                          <tr>
                                            <td
                                              align="left"
                                              style="
                                                font-size: 0px;
                                                padding: 0;
                                                word-break: break-word;
                                              "
                                            >
                                              <div
                                                style="
                                                  font-family: Arial, serif,
                                                    EmojiFont;
                                                  font-size: 14px;
                                                  line-height: 16px;
                                                  text-align: left;
                                                  color: rgb(
                                                    255,
                                                    255,
                                                    255
                                                  ) !important;
                                                "
                                                data-ogsc="rgb(0, 0, 0)"
                                              >
                                                <a
                                                  href="{}"
                                                  target="_blank"
                                                  rel="noopener noreferrer"
                                                  data-auth="NotApplicable"
                                                  title="Oficina en plaza de San Miguel, Paseo Independencia, Zaragoza"
                                                  style="
                                                    color: rgb(
                                                      110,
                                                      172,
                                                      242
                                                    ) !important;
                                                    text-decoration: none;
                                                  "
                                                  data-linkindex="3"
                                                  data-ogsc="rgb(33, 114, 178)"
                                                  >Oficina en plaza de San
                                                  Miguel, Paseo Independencia,
                                                  Zaragoza</a
                                                >
                                              </div>
                                            </td>
                                          </tr>
                                          <tr>
                                            <td
                                              align="left"
                                              class="x_price-table"
                                              style="
                                                font-size: 0px;
                                                padding: 0;
                                                word-break: break-word;
                                              "
                                            >
                                              <table
                                                cellpadding="0"
                                                cellspacing="0"
                                                width="100%"
                                                border="0"
                                                style="
                                                  color: rgb(
                                                    255,
                                                    255,
                                                    255
                                                  ) !important;
                                                  font-family: Arial;
                                                  font-size: 13px;
                                                  line-height: 22px;
                                                  table-layout: auto;
                                                  width: 100%;
                                                "
                                                data-ogsc="rgb(0, 0, 0)"
                                              >
                                                <tbody>
                                                  <tr>
                                                    <td
                                                      valign="middle"
                                                      align="left"
                                                      height="42"
                                                    >
                                                      <span
                                                        ><span
                                                          style="
                                                            color: rgb(
                                                              215,
                                                              215,
                                                              215
                                                            ) !important;
                                                            font-weight: bold;
                                                            font-size: 22px;
                                                            line-height: 16px;
                                                          "
                                                          data-ogsc="rgb(51, 51, 51)"
                                                          >1400 €/mes
                                                        </span></span
                                                      >
                                                    </td>
                                                  </tr>
                                                </tbody>
                                              </table>
                                            </td>
                                          </tr>
                                          <tr>
                                            <td
                                              align="left"
                                              style="
                                                font-size: 0px;
                                                padding: 0 0 4px;
                                                word-break: break-word;
                                              "
                                            >
                                              <div
                                                style="
                                                  font-family: Arial, serif,
                                                    EmojiFont;
                                                  font-size: 14px;
                                                  line-height: 16px;
                                                  text-align: left;
                                                  color: rgb(
                                                    243,
                                                    243,
                                                    243
                                                  ) !important;
                                                "
                                                data-ogsc="rgb(20, 20, 20)"
                                              >
                                                170 m²  9.74€/m²
                                              </div>
                                            </td>
                                          </tr>
                                          <tr>
                                            <td
                                              align="left"
                                              style="
                                                font-size: 0px;
                                                padding: 0 0 11px;
                                                word-break: break-word;
                                              "
                                            >
                                              <div
                                                style="
                                                  font-family: Arial, serif,
                                                    EmojiFont;
                                                  font-size: 14px;
                                                  line-height: 16px;
                                                  text-align: left;
                                                  color: rgb(
                                                    178,
                                                    179,
                                                    176
                                                  ) !important;
                                                "
                                                data-ogsc="rgb(142, 143, 140)"
                                              >
                                                <p
                                                  style="
                                                    height: 30px;
                                                    overflow: hidden;
                                                    margin-top: 0;
                                                    margin-bottom: 0;
                                                  "
                                                >
                                                  ¡SE ALQUILA! PRECIOSA OFICINA
                                                  CÉNTRICA, Acondicionada en
                                                  Plaza San Miguel muy Luminosa,
                                                  Cé...
                                                </p>
                                              </div>
                                            </td>
                                          </tr>
                                          <tr>
                                            <td
                                              align="center"
                                              style="
                                                font-size: 0px;
                                                padding: 0;
                                                word-break: break-word;
                                              "
                                            >
                                              <table
                                                border="0"
                                                cellpadding="0"
                                                cellspacing="0"
                                                role="presentation"
                                                style="
                                                  border-collapse: separate;
                                                  width: 100%;
                                                  line-height: 100%;
                                                "
                                              >
                                                <tbody>
                                                  <tr>
                                                    <td
                                                      align="center"
                                                      bgcolor="rgb(54, 54, 50)"
                                                      role="presentation"
                                                      valign="middle"
                                                      style="
                                                        border: 1px solid
                                                          rgb(203, 204, 199);
                                                        border-radius: 2px;
                                                        padding: 4px 16px;
                                                        background-image: initial;
                                                        background-position: initial;
                                                        background-size: initial;
                                                        background-repeat: initial;
                                                        background-attachment: initial;
                                                        background-origin: initial;
                                                        background-clip: initial;
                                                        background-color: rgb(
                                                          54,
                                                          54,
                                                          50
                                                        ) !important;
                                                      "
                                                      data-ogsb="rgb(229, 230, 225)"
                                                      data-ogab="#e5e6e1"
                                                    >
                                                      <a
                                                        href="{}"
                                                        target="_blank"
                                                        rel="noopener noreferrer"
                                                        data-auth="NotApplicable"
                                                        style="
                                                          background-image: initial;
                                                          background-position: initial;
                                                          background-size: initial;
                                                          background-repeat: initial;
                                                          background-attachment: initial;
                                                          background-origin: initial;
                                                          background-clip: initial;
                                                          background-color: rgb(
                                                            54,
                                                            54,
                                                            50
                                                          ) !important;
                                                          color: rgb(
                                                            243,
                                                            243,
                                                            243
                                                          ) !important;
                                                          font-family: Arial;
                                                          font-size: 16px;
                                                          font-weight: 700;
                                                          line-height: 24px;
                                                          margin: 0px;
                                                          text-decoration: none;
                                                          text-transform: none;
                                                        "
                                                        data-linkindex="4"
                                                        data-ogsc="rgb(20, 20, 20)"
                                                        data-ogsb="rgb(229, 230, 225)"
                                                        ><span
                                                          style="display: block"
                                                          >Ver 30 fotos</span
                                                        ></a
                                                      >
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
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                  <div style="margin: 0px auto; max-width: 552px">
                    <table
                      align="center"
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      style="width: 100%"
                    >
                      <tbody>
                        <tr>
                          <td
                            style="
                              direction: ltr;
                              font-size: 0px;
                              padding: 0;
                              text-align: center;
                              vertical-align: top;
                            "
                          >
                            <div
                              class="x_mj-column-per-100 x_outlook-group-fix"
                              style="
                                font-size: 13px;
                                text-align: left;
                                direction: ltr;
                                display: inline-block;
                                vertical-align: top;
                                width: 100%;
                              "
                            >
                              <table
                                border="0"
                                cellpadding="0"
                                cellspacing="0"
                                role="presentation"
                                width="100%"
                                style="vertical-align: top"
                              >
                                <tbody>
                                  <tr>
                                    <td
                                      style="
                                        font-size: 0px;
                                        word-break: break-word;
                                      "
                                    >
                                      <div
                                        style="height: 12px"
                                        aria-hidden="true"
                                      >
                                        &nbsp;
                                      </div>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div style="margin: 0px auto; max-width: 600px">
          <table
            align="center"
            border="0"
            cellpadding="0"
            cellspacing="0"
            role="presentation"
            style="width: 100%"
          >
            <tbody>
              <tr>
                <td
                  style="
                    direction: ltr;
                    font-size: 0px;
                    padding: 0;
                    text-align: center;
                    vertical-align: top;
                  "
                >
                  <div
                    class="x_mj-column-per-100 x_outlook-group-fix"
                    style="
                      font-size: 13px;
                      text-align: left;
                      direction: ltr;
                      display: inline-block;
                      vertical-align: top;
                      width: 100%;
                    "
                  >
                    <table
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      role="presentation"
                      width="100%"
                    >
                      <tbody>
                        <tr>
                          <td style="vertical-align: top; padding: 0">
                            <table
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              role="presentation"
                              width="100%"
                            >
                              <tbody>
                                <tr>
                                  <td
                                    style="
                                      font-size: 0px;
                                      padding: 0;
                                      word-break: break-word;
                                    "
                                  >
                                    <p
                                      style="
                                        border-top: solid 6px #f0f0ee;
                                        font-size: 1;
                                        margin: 0px auto;
                                        width: 100%;
                                      "
                                    ></p>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <div
          style="
            background-image: initial;
            background-position: initial;
            background-size: initial;
            background-repeat: initial;
            background-attachment: initial;
            background-origin: initial;
            background-clip: initial;
            background-color: rgb(41, 41, 41) !important;
            margin: 0px auto;
            max-width: 600px;
          "
          data-ogsb="rgb(255, 255, 255)"
        >
          <div class="R1UVb" style="height: 424px; width: 100%">
            <div class="qF8_5">
              <button
                type="button"
                class="ms-Button ms-Button--icon wD8TJ root-508"
                title="Mostrar tamaño original"
                aria-label="Mostrar tamaño original"
                data-is-focusable="true"
              >
                <span
                  class="ms-Button-flexContainer flexContainer-158"
                  data-automationid="splitbuttonprimary"
                  ><i
                    data-icon-name="FullScreen"
                    aria-hidden="true"
                    class="ms-Icon root-90 css-293 ms-Button-icon icon-160"
                    style="font-family: controlIcons"
                    ></i
                  ></span
                >
              </button>
            </div>
            <table
              align="center"
              border="0"
              cellpadding="0"
              cellspacing="0"
              role="presentation"
              style="
                background-image: initial;
                background-position: initial;
                background-size: initial;
                background-repeat: initial;
                background-attachment: initial;
                background-origin: initial;
                background-clip: initial;
                background-color: rgb(41, 41, 41) !important;
                width: 100%;
                transform: scale(0.791383, 0.791383);
                transform-origin: left top;
              "
              data-ogsb="rgb(255, 255, 255)"
              min-scale="0.7913832199546486"
            >
              <tbody>
                <tr>
                  <td
                    style="
                      direction: ltr;
                      font-size: 0px;
                      padding: 0;
                      text-align: center;
                      vertical-align: top;
                    "
                  >
                    <div style="margin: 0px auto; max-width: 600px">
                      <table
                        align="center"
                        border="0"
                        cellpadding="0"
                        cellspacing="0"
                        role="presentation"
                        style="width: 100%"
                      >
                        <tbody>
                          <tr>
                            <td
                              style="
                                direction: ltr;
                                font-size: 0px;
                                padding: 24px 24px 0;
                                text-align: center;
                                vertical-align: top;
                              "
                            >
                              <div
                                class="x_mj-column-per-100 x_outlook-group-fix"
                                style="
                                  font-size: 13px;
                                  text-align: left;
                                  direction: ltr;
                                  display: inline-block;
                                  vertical-align: top;
                                  width: 100%;
                                "
                              >
                                <table
                                  border="0"
                                  cellpadding="0"
                                  cellspacing="0"
                                  role="presentation"
                                  width="100%"
                                  style="vertical-align: top"
                                >
                                  <tbody>
                                    <tr>
                                      <td
                                        align="left"
                                        style="
                                          font-size: 0px;
                                          padding: 0;
                                          word-break: break-word;
                                        "
                                      >
                                        <div
                                          style="
                                            font-family: Arial, serif, EmojiFont;
                                            font-size: 16px;
                                            font-weight: 700;
                                            line-height: 24px;
                                            text-align: left;
                                            color: rgb(
                                              174,
                                              174,
                                              172
                                            ) !important;
                                          "
                                          data-ogsc="rgb(102, 102, 100)"
                                        >
                                          Sobre los anuncios en este correo
                                        </div>
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                              </div>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                    <div style="margin: 0px auto; max-width: 600px">
                      <table
                        align="center"
                        border="0"
                        cellpadding="0"
                        cellspacing="0"
                        role="presentation"
                        style="width: 100%"
                      >
                        <tbody>
                          <tr>
                            <td
                              style="
                                direction: ltr;
                                font-size: 0px;
                                padding: 0 24px 24px;
                                text-align: center;
                                vertical-align: top;
                              "
                            >
                              <div
                                class="x_mj-column-per-100 x_outlook-group-fix"
                                style="
                                  font-size: 13px;
                                  text-align: left;
                                  direction: ltr;
                                  display: inline-block;
                                  vertical-align: top;
                                  width: 100%;
                                "
                              >
                                <table
                                  border="0"
                                  cellpadding="0"
                                  cellspacing="0"
                                  role="presentation"
                                  width="100%"
                                  style="vertical-align: top"
                                >
                                  <tbody>
                                    <tr>
                                      <td
                                        align="left"
                                        style="
                                          font-size: 0px;
                                          padding: 0;
                                          word-break: break-word;
                                        "
                                      >
                                        <div
                                          style="
                                            font-family: Arial, serif, EmojiFont;
                                            font-size: 16px;
                                            line-height: 24px;
                                            text-align: left;
                                            color: rgb(
                                              174,
                                              174,
                                              172
                                            ) !important;
                                          "
                                          data-ogsc="rgb(102, 102, 100)"
                                        >
                                          Desde
                                          <a
                                            href="{}"
                                            target="_blank"
                                            rel="noopener noreferrer"
                                            data-auth="NotApplicable"
                                            style="
                                              color: rgb(
                                                110,
                                                172,
                                                242
                                              ) !important;
                                              text-decoration: none;
                                            "
                                            data-linkindex="5"
                                            data-ogsc="rgb(33, 114, 178)"
                                            >Tus búsquedas</a
                                          >
                                          puedes revisar tus criterios, elegir
                                          recibir avisos inmediatos o seguir
                                          recibiendo este resumen diario.
                                          <br />Si ya no te interesan, puedes
                                          <a
                                            href="{}"
                                            target="_blank"
                                            rel="noopener noreferrer"
                                            data-auth="NotApplicable"
                                            style="
                                              color: rgb(
                                                110,
                                                172,
                                                242
                                              ) !important;
                                              text-decoration: none;
                                            "
                                            data-linkindex="6"
                                            data-ogsc="rgb(33, 114, 178)"
                                            >dejar de recibir el resumen diario
                                            de novedades y recomendaciones</a
                                          >.
                                        </div>
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                              </div>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                    <div
                      style="
                        background-image: initial;
                        background-position: initial;
                        background-size: initial;
                        background-repeat: initial;
                        background-attachment: initial;
                        background-origin: initial;
                        background-clip: initial;
                        background-color: rgb(38, 59, 0) !important;
                        margin: 0px auto;
                        max-width: 600px;
                      "
                      data-ogsb="rgb(225, 245, 110)"
                    >
                      <table
                        align="center"
                        border="0"
                        cellpadding="0"
                        cellspacing="0"
                        role="presentation"
                        style="
                          background-image: initial;
                          background-position: initial;
                          background-size: initial;
                          background-repeat: initial;
                          background-attachment: initial;
                          background-origin: initial;
                          background-clip: initial;
                          background-color: rgb(38, 59, 0) !important;
                          width: 100%;
                        "
                        data-ogsb="rgb(225, 245, 110)"
                      >
                        <tbody>
                          <tr>
                            <td
                              style="
                                direction: ltr;
                                font-size: 0px;
                                padding: 24px 24px 16px;
                                text-align: center;
                                vertical-align: top;
                              "
                            >
                              <div
                                class="x_mj-column-per-100 x_outlook-group-fix"
                                style="
                                  font-size: 13px;
                                  text-align: left;
                                  direction: ltr;
                                  display: inline-block;
                                  vertical-align: top;
                                  width: 100%;
                                "
                              >
                                <table
                                  border="0"
                                  cellpadding="0"
                                  cellspacing="0"
                                  role="presentation"
                                  width="100%"
                                  style="vertical-align: top"
                                >
                                  <tbody>
                                    <tr>
                                      <td
                                        align="left"
                                        style="
                                          font-size: 0px;
                                          padding: 0;
                                          word-break: break-word;
                                        "
                                      >
                                        <div
                                          style="
                                            font-family: Arial, serif, EmojiFont;
                                            font-size: 16px;
                                            line-height: 24px;
                                            text-align: left;
                                            color: rgb(
                                              174,
                                              174,
                                              172
                                            ) !important;
                                          "
                                          data-ogsc="rgb(102, 102, 100)"
                                        >
                                          Con la app de idealista podrás recibir
                                          de inmediato nuevos anuncios o la
                                          respuesta de los anunciantes que
                                          contactes.
                                        </div>
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                              </div>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                    <div
                      style="
                        background-image: initial;
                        background-position: initial;
                        background-size: initial;
                        background-repeat: initial;
                        background-attachment: initial;
                        background-origin: initial;
                        background-clip: initial;
                        background-color: rgb(38, 59, 0) !important;
                        margin: 0px auto;
                        max-width: 600px;
                      "
                      data-ogsb="rgb(225, 245, 110)"
                    >
                      <table
                        align="center"
                        border="0"
                        cellpadding="0"
                        cellspacing="0"
                        role="presentation"
                        style="
                          background-image: initial;
                          background-position: initial;
                          background-size: initial;
                          background-repeat: initial;
                          background-attachment: initial;
                          background-origin: initial;
                          background-clip: initial;
                          background-color: rgb(38, 59, 0) !important;
                          width: 100%;
                        "
                        data-ogsb="rgb(225, 245, 110)"
                      >
                        <tbody>
                          <tr>
                            <td
                              style="
                                direction: ltr;
                                font-size: 0px;
                                padding: 0 24px 24px;
                                text-align: center;
                                vertical-align: top;
                              "
                            >
                              <div
                                class="x_mj-column-per-100 x_outlook-group-fix"
                                style="
                                  font-size: 13px;
                                  text-align: left;
                                  direction: ltr;
                                  display: inline-block;
                                  vertical-align: top;
                                  width: 100%;
                                "
                              >
                                <table
                                  border="0"
                                  cellpadding="0"
                                  cellspacing="0"
                                  role="presentation"
                                  width="100%"
                                  style="vertical-align: top"
                                >
                                  <tbody>
                                    <tr>
                                      <td
                                        align="left"
                                        style="
                                          font-size: 0px;
                                          padding: 0;
                                          word-break: break-word;
                                        "
                                      >
                                        <div
                                          style="
                                            font-family: Arial, serif, EmojiFont;
                                            font-size: 16px;
                                            font-weight: 700;
                                            line-height: 1;
                                            text-align: left;
                                            color: rgb(
                                              255,
                                              255,
                                              255
                                            ) !important;
                                          "
                                          data-ogsc="rgb(0, 0, 0)"
                                        >
                                          <a
                                            href="{}"
                                            target="_blank"
                                            rel="noopener noreferrer"
                                            data-auth="NotApplicable"
                                            style="
                                              color: rgb(
                                                110,
                                                172,
                                                242
                                              ) !important;
                                              text-decoration: none;
                                            "
                                            data-linkindex="7"
                                            data-ogsc="rgb(33, 114, 178)"
                                            >Descárgate la app de idealista</a
                                          >
                                        </div>
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                              </div>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                    <div
                      style="
                        background-image: initial;
                        background-position: initial;
                        background-size: initial;
                        background-repeat: initial;
                        background-attachment: initial;
                        background-origin: initial;
                        background-clip: initial;
                        background-color: rgb(53, 53, 51) !important;
                        margin: 0px auto;
                        max-width: 600px;
                      "
                      data-ogsb="rgb(231, 231, 228)"
                    >
                      <table
                        align="center"
                        border="0"
                        cellpadding="0"
                        cellspacing="0"
                        role="presentation"
                        style="
                          background-image: initial;
                          background-position: initial;
                          background-size: initial;
                          background-repeat: initial;
                          background-attachment: initial;
                          background-origin: initial;
                          background-clip: initial;
                          background-color: rgb(53, 53, 51) !important;
                          width: 100%;
                        "
                        data-ogsb="rgb(231, 231, 228)"
                      >
                        <tbody>
                          <tr>
                            <td
                              style="
                                direction: ltr;
                                font-size: 0px;
                                padding: 24px 24px 16px;
                                text-align: center;
                                vertical-align: top;
                              "
                            >
                              <div
                                class="x_mj-column-per-100 x_outlook-group-fix"
                                style="
                                  font-size: 13px;
                                  text-align: left;
                                  direction: ltr;
                                  display: inline-block;
                                  vertical-align: top;
                                  width: 100%;
                                "
                              >
                                <table
                                  border="0"
                                  cellpadding="0"
                                  cellspacing="0"
                                  role="presentation"
                                  width="100%"
                                  style="vertical-align: top"
                                >
                                  <tbody>
                                    <tr>
                                      <td
                                        align="left"
                                        style="
                                          font-size: 0px;
                                          padding: 0;
                                          word-break: break-word;
                                        "
                                      >
                                        <div
                                          style="
                                            font-family: Arial, serif, EmojiFont;
                                            font-size: 12px;
                                            line-height: 20px;
                                            text-align: left;
                                            color: rgb(
                                              174,
                                              174,
                                              172
                                            ) !important;
                                          "
                                          data-ogsc="rgb(102, 102, 100)"
                                        >
                                          ¿Problemas? Contacta con idealista
                                          <a
                                            href="{}"
                                            target="_blank"
                                            rel="noopener noreferrer"
                                            data-auth="NotApplicable"
                                            style="
                                              margin: 0px;
                                              padding: 0px;
                                              color: rgb(
                                                174,
                                                174,
                                                174
                                              ) !important;
                                              font-size: 12px;
                                              font-family: Arial, sans-serif !important;
                                            "
                                            data-linkindex="8"
                                            data-ogsc="rgb(102, 102, 102)"
                                            >a través de la web</a
                                          >
                                        </div>
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                              </div>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                    <div
                      style="
                        background-image: initial;
                        background-position: initial;
                        background-size: initial;
                        background-repeat: initial;
                        background-attachment: initial;
                        background-origin: initial;
                        background-clip: initial;
                        background-color: rgb(53, 53, 51) !important;
                        margin: 0px auto;
                        max-width: 600px;
                      "
                      data-ogsb="rgb(231, 231, 228)"
                    >
                      <table
                        align="center"
                        border="0"
                        cellpadding="0"
                        cellspacing="0"
                        role="presentation"
                        style="
                          background-image: initial;
                          background-position: initial;
                          background-size: initial;
                          background-repeat: initial;
                          background-attachment: initial;
                          background-origin: initial;
                          background-clip: initial;
                          background-color: rgb(53, 53, 51) !important;
                          width: 100%;
                        "
                        data-ogsb="rgb(231, 231, 228)"
                      >
                        <tbody>
                          <tr>
                            <td
                              style="
                                direction: ltr;
                                font-size: 0px;
                                padding: 0 24px;
                                text-align: center;
                                vertical-align: top;
                              "
                            >
                              <div
                                class="x_mj-column-per-100 x_outlook-group-fix"
                                style="
                                  font-size: 13px;
                                  text-align: left;
                                  direction: ltr;
                                  display: inline-block;
                                  vertical-align: top;
                                  width: 100%;
                                "
                              >
                                <table
                                  border="0"
                                  cellpadding="0"
                                  cellspacing="0"
                                  role="presentation"
                                  width="100%"
                                  style="vertical-align: top"
                                >
                                  <tbody>
                                    <tr>
                                      <td
                                        align="left"
                                        style="
                                          font-size: 0px;
                                          padding: 0;
                                          word-break: break-word;
                                        "
                                      >
                                        <div
                                          style="
                                            font-family: Arial, serif, EmojiFont;
                                            font-size: 12px;
                                            line-height: 20px;
                                            text-align: left;
                                            color: rgb(
                                              174,
                                              174,
                                              172
                                            ) !important;
                                          "
                                          data-ogsc="rgb(102, 102, 100)"
                                        >
                                          La utilización de esta página supone
                                          que has leído la
                                          <a
                                            href="{}"
                                            target="_blank"
                                            rel="noopener noreferrer"
                                            data-auth="NotApplicable"
                                            style="
                                              margin: 0px;
                                              padding: 0px;
                                              color: rgb(
                                                174,
                                                174,
                                                174
                                              ) !important;
                                              font-size: 12px;
                                              font-family: Arial, sans-serif !important;
                                            "
                                            data-linkindex="9"
                                            data-ogsc="rgb(102, 102, 102)"
                                            >política de privacidad</a
                                          >
                                          y has aceptado los
                                          <a
                                            href="{}"
                                            target="_blank"
                                            rel="noopener noreferrer"
                                            data-auth="NotApplicable"
                                            style="
                                              margin: 0px;
                                              padding: 0px;
                                              color: rgb(
                                                174,
                                                174,
                                                174
                                              ) !important;
                                              font-size: 12px;
                                              font-family: Arial, sans-serif !important;
                                            "
                                            data-linkindex="10"
                                            data-ogsc="rgb(102, 102, 102)"
                                            >términos y condiciones</a
                                          >
                                          del servicio
                                        </div>
                                      </td>
                                    </tr>
                                  </tbody>
                                </table>
                              </div>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                    <div
                      style="
                        background-image: initial;
                        background-position: initial;
                        background-size: initial;
                        background-repeat: initial;
                        background-attachment: initial;
                        background-origin: initial;
                        background-clip: initial;
                        background-color: rgb(53, 53, 51) !important;
                        margin: 0px auto;
                        max-width: 600px;
                      "
                      data-ogsb="rgb(231, 231, 228)"
                    >
                      <table
                        align="center"
                        border="0"
                        cellpadding="0"
                        cellspacing="0"
                        role="presentation"
                        style="
                          background-image: initial;
                          background-position: initial;
                          background-size: initial;
                          background-repeat: initial;
                          background-attachment: initial;
                          background-origin: initial;
                          background-clip: initial;
                          background-color: rgb(53, 53, 51) !important;
                          width: 100%;
                        "
                        data-ogsb="rgb(231, 231, 228)"
                      >
                        <tbody>
                          <tr>
                            <td
                              style="
                                direction: ltr;
                                font-size: 0px;
                                padding: 24px 24px 0;
                                text-align: left;
                                vertical-align: top;
                              "
                            >
                              <div
                                class="x_mj-column-px-121 x_outlook-group-fix"
                                style="
                                  font-size: 13px;
                                  text-align: left;
                                  direction: ltr;
                                  display: inline-block;
                                  vertical-align: top;
                                  width: 100%;
                                "
                              >
                                <table
                                  border="0"
                                  cellpadding="0"
                                  cellspacing="0"
                                  role="presentation"
                                  width="100%"
                                >
                                  <tbody>
                                    <tr>
                                      <td
                                        style="
                                          vertical-align: top;
                                          padding-bottom: 16px;
                                        "
                                      >
                                        <table
                                          border="0"
                                          cellpadding="0"
                                          cellspacing="0"
                                          role="presentation"
                                          width="100%"
                                        >
                                          <tbody>
                                            <tr>
                                              <td
                                                align="left"
                                                style="
                                                  font-size: 0px;
                                                  padding: 0 10px 0 0;
                                                  word-break: break-word;
                                                "
                                              >
                                                <table
                                                  border="0"
                                                  cellpadding="0"
                                                  cellspacing="0"
                                                  role="presentation"
                                                  style="
                                                    border-collapse: collapse;
                                                    border-spacing: 0px;
                                                  "
                                                >
                                                  <tbody>
                                                    <tr>
                                                      <td style="width: 111px">
                                                        <img
                                                          data-imagetype="External"
                                                          src="image/idealista.png"
                                                          height="auto"
                                                          width="111"
                                                          style="
                                                            border: 0;
                                                            display: block;
                                                            outline: none;
                                                            text-decoration: none;
                                                            height: auto;
                                                            width: 100%;
                                                          "
                                                        />
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
                              </div>
                              <div
                                class="x_mj-column-px-393 x_outlook-group-fix"
                                style="
                                  font-size: 13px;
                                  text-align: left;
                                  direction: ltr;
                                  display: inline-block;
                                  vertical-align: bottom;
                                  width: 100%;
                                "
                              >
                                <table
                                  border="0"
                                  cellpadding="0"
                                  cellspacing="0"
                                  role="presentation"
                                  width="100%"
                                >
                                  <tbody>
                                    <tr>
                                      <td
                                        style="
                                          vertical-align: bottom;
                                          padding-bottom: 16px;
                                        "
                                      >
                                        <table
                                          border="0"
                                          cellpadding="0"
                                          cellspacing="0"
                                          role="presentation"
                                          width="100%"
                                        >
                                          <tbody>
                                            <tr>
                                              <td
                                                align="left"
                                                style="
                                                  font-size: 0px;
                                                  padding: 0;
                                                  word-break: break-word;
                                                "
                                              >
                                                <div
                                                  style="
                                                    font-family: Arial, serif,
                                                      EmojiFont;
                                                    font-size: 14px;
                                                    line-height: 1;
                                                    text-align: left;
                                                    color: rgb(
                                                      168,
                                                      168,
                                                      154
                                                    ) !important;
                                                  "
                                                  data-ogsc="rgb(113, 113, 100)"
                                                >
                                                  © 2000 - 2024
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
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <img
          data-imagetype="External"
          src="https://col.idealista.com/toto?s=582065&amp;xto=EPR-1168-[daily_total_alerts_20240508|]-20240508-[]-72493771780@1-20240508075412&amp;type=email&amp;"
          border="0"
          width="1"
          height="1"
        />
      </div>
    </div>
  </div>
</html>

                    """).format(urlShort,userName,urlShort,urlShort,urlShort,urlShort,urlShort,urlShort,urlShort,urlShort,urlShort)
    saveTemplateGenerated(userName,'Idealistas',idealista_html,"Nuevos anuncios hoy "+currentDate,"notificaciones-idea@movicoders.link",userEmail)
