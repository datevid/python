### Instalacion del ambiente virtual
1.Instalacion de pip
```
sudo apt-get install python3-pip #command for Python 3
```
o
```
sudo apt install python3-pip	#command for Python 3
```
2. Instalacion del ambiente virtual
```
pip install virtualenv
```
or
```
python -m pip install virtualenv
```
Distro ubuntu and similar if previus show error:
```
apt install python3.8-venv
```

3. ubicarse dentro del proyecto(directorio)
```
cd proyectonuevo
```

4. creacion del ambiente virtual
```
python -m venv env
```
5. ingresar al ambiente virtual
```
cd env/Scripts
activate
```
en Linux ubicar env/env1/bin
```
source activate
```

para salir del entorno virutal:
```
deactivate
```
### Instalar django
```
python -m pip install Django
```

### Instalar las dependencias desde un archivo
```
pip install -r requisitos.txt
```

### how make python execute python3

```
sudo apt install python-is-python3
```
