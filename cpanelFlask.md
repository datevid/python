# Introducción:
Si te da pereza puedes ver el video de la configuración de un proyecto en Flask y Cpanel
https://www.youtube.com/watch?v=260eDcsUheE

# Pasos:
1. Crear la aplicación Setup Python App 
  - Configuracion: Aplication root: es el path de tu directorio creao
  - Application URL: Ruta
  - Application startup file: siempre será app.py
  - Aplication Entry point: siempre será app
  
2.  asdf

# Codigo de testeo
Test de configuración de un proyecto en Flask y Cpanel
´´´python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hola mundo"
    
if __name__ == '__main__':
    app.run()
´´´
