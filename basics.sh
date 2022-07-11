#1. Instalacion del ambiente virtual
python -m pip install virtualenv
#en distro  ubuntu y similares:
apt install python3.8-venv

#2. ubicarse dentro del proyecto(directorio)
cd proyectonuevo

#3. creacion del ambiente virtual
python -m venv env

#4. ingresar al ambiente virtual
cd env/Scripts
activate
#en Linux ubicar env/env1/bin
source activate

#para salir del entorno virutal:
deactivate

#para instalar las dependencias desde un archivo
pip install -r requisitos.txt
