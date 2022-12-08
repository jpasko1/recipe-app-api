FROM python:3.9-alpine3.13
LABEL maintainer="pasko.net"
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

# Moving lower as our code will change frequently and it's silly to keep pip installing after from
# a Docker layer perspective

#COPY ./app /app
#WORKDIR /app 
#EXPOSE 8000

ARG DEV=false # This will be overridden by docker-compose when we are doing ttesting

RUN adduser \
   --disabled-password \
   --no-create-home \
   django-user

RUN python -m venv /py && \
/py/bin/pip install --upgrade pip && \
apk add --update --no-cache postgresql-client && \
apk add --update --no-cache --virtual .tmp-build-deps \
build-base postgresql-dev musl-dev && \
/py/bin/pip install -r /tmp/requirements.txt && \
if [ $DEV = "true" ]; \
    then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
fi && \
rm -rf /tmp \
apk del .tmp-build-deps


COPY ./app /app
WORKDIR /app 
EXPOSE 8000

ENV PATH="/py/bin:$PATH"
USER django-user