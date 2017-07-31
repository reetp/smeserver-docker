# smeserver-docker
Koozali SME Server Docker support 

This sets up some of the basics for Docker on Koozali SME

It should have a subdomain to run for the web proxy soethign like this:

db domains show

docker.somedomain.com=domain
    Content=Primary
    Description=Docker Server
    Nameservers=localhost
    TemplatePath=ProxyPassVirtualDocker
    letsencryptSSLcert=enabled



This is normally set in domains but really needs created from the the docker db

ProxyPassTarget=http://127.0.0.1:3000/


ToDo

Set docker directory for images
eg /home/e-smith/files/docker

DOCKER_CERT_PATH

Startup scripts for images - configs can be pulled form a docker DB

so you could do kind of


start docker-myimage

Which would run a script, pull the image settings and then start the container (may need httpd regenerated for the proxy)

So this:

docker run -d -p 127.0.0.1:80:5000 training/webapp python app.py

gets reduced to

start docker-training app

DB something like this:

db docker show

training=docker
  host=127.0.0.1
  hostMachinePort=80
  dockerContainerPort=5000
  
  