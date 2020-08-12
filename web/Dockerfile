FROM wgtdocker/mecab-python-docker:latest

COPY . /

RUN pip install --upgrade pip
RUN pip install -r requirements.txt && pip install gunicorn

RUN ["chmod", "+x", "/runserver.sh"]

ENTRYPOINT ["/runserver.sh"]



