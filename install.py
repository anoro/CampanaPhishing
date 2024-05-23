import subprocess

# Instalación de Click
subprocess.call(['pip', 'install', 'click==7.1.2'])

# Lista de paquetes de Flask
paquetes_flask = [
    'flask',
    'flask-login',
    'flask-wtf',
    'click'
    'smtplib',
    'email',
<<<<<<< HEAD
    'segno'
=======
    'qrcode'
>>>>>>> b2021e40f97dea3d7e5a6bbfcdf39eb655617850
]

# Instalación de paquetes
for paquete in paquetes_flask:
    subprocess.call(['pip', 'install', paquete])