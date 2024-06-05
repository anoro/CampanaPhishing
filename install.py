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
    'segno',
    'requests'
]

# Instalación de paquetes
for paquete in paquetes_flask:
    subprocess.call(['pip', 'install', paquete])