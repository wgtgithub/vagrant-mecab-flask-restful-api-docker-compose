#FROM python:3.8.5-alpine3.12
FROM python:3.7-alpine

COPY . /

RUN apk add --update --no-cache build-base
ENV build_deps 'curl git bash file sudo openssh'
ENV dependencies 'openssl'

RUN apk add --update --no-cache ${build_deps} \
  # Install dependencies
  && apk add --update --no-cache ${dependencies}


RUN pip install --upgrade pip
RUN pip install -r requirements.txt \
&& pip install gunicorn

RUN ["chmod", "+x", "/runserver.sh"]

ENTRYPOINT ["/runserver.sh"]



