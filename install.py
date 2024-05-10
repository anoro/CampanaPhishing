import subprocess

# Lista de paquetes de Flask
paquetes_flask = [
    'flask',
    'flask-login',
    'flask-wtf',
    'smtplib',
    'email'
]

# Instalación de paquetes
for paquete in paquetes_flask:
    subprocess.call(['pip', 'install', paquete])