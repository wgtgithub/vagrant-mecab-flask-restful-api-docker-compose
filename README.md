Usage: 
- Using Vagrant
    - start app: vagrant up
    - finish app: vagrant halt

- Docker-compose
    - cd ./web/
    - docker-compose --build -d

- setup flask into your PC after installed python and pip
    - pip install -upgrade pip
    - if on MacOS append --user: pip upgrade pip --user
    - export FLASK_APP=./web/app/app.py

- run flask: start app
    - flask run
    - if stop press ctrl+c

About Docker Image
- Dockerfile uses wgtdocker/mecab-python-docker:latest as docker pull image
- You can check the resource the following url
- https://github.com/wgtgithub/vagrant-mecab-python-docker

Note:
- I am not modified this resorces forever
- If you clone it and then something happened but I won't follow you
