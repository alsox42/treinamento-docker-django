Vamos usar docker-compose para desenvolvimento
Dockerfile para produção
Excutar deploy-local com sudo
Se ao executar deploy-local der error, executar antes
docker-compose down


sudo docker build -t sendcrushes
sudo docker-compose run web django-admin startproject <nome-do-projeto> .