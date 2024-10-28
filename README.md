# About
CLI interface to interact with Netskope's API in container format

#Usage
Clone the repository locally:
```
git clone https://github.com/hutama44/netskopeapicontainer
```
Access the created folder:
```
cd netskopeapicontainer
```
Build the docker image:
```
sudo docker image build -t netskope/apicont .
```
Opción 1: Sin requerimientos de creación de aplicaciones desde un archivo de texto separado por comas: 
```
sudo docker container run --rm -ti netskope/apicont
```
Opción 2: Para automatizar la creación de aplicaciones privadas se debe ubicar un archivo de texto separado por comas en el siguiente formato en la ruta referenciada: nombre de la app,url,,protocolo TCP/UDP,Puerto,Publisher ID,Publisher Name
```
sudo docker container run -v /ruta/del/archivo:/mnt --rm -ti netskope/apicont
```
