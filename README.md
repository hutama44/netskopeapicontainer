# About/Acerca de
CLI interface to interact with Netskope's API in container format / Interface CLI para interactuar con el API de Netskope en formato de contenedor

# Required API Privileges/Permisos Requeridos en el API
/api/v2/steering/apps/private \
/api/v2/policy/npa/rules \
/api/v2/steering/apps/private/tags \
/api/v2/incidents/user/uciimpact \
/api/v2/scim/Groups	\
/api/v2/steering/apps/private/tags/getpolicyinuse \
/api/v2/incidents/users/uci/reset \
/api/v2/scim/Users	\
/api/v2/ubadatasvc/user/uci \
/api/v2/policy/npa/policygroups \

# Usage/Uso
Clone the repository locally: / Clonar el repositorio localmente:
```
git clone https://github.com/hutama44/netskopeapicontainer
```
Access the created folder: / Acceder a la carpeta creada:
```
cd netskopeapicontainer
```
Build the docker image: / Construir la imagen de docker:
```
sudo docker image build -t netskope/apicont .
```
Option 1: No requirements to create private apps from a csv file / Opción 1: Sin requerimientos de creación de aplicaciones desde un archivo de texto separado por comas: 
```
sudo docker container run --rm -ti netskope/apicont
```
Option 2: To automate the private apps creation you need to place a csv file in the following format in the path referenced: app_name,url,,TCP/UDP Protocol,port,Publisher_ID,Publisher_Name / Opción 2: Para automatizar la creación de aplicaciones privadas se debe ubicar un archivo de texto separado por comas en el siguiente formato en la ruta referenciada: nombre de la app,url,,protocolo TCP/UDP,Puerto,Publisher ID,Publisher Name
```
sudo docker container run -v /ruta/del/archivo:/mnt --rm -ti netskope/apicont
```
