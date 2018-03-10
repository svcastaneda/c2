FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /config
ADD ./config/requirements.txt /config/
RUN pip install -r /config/requirements.txt

RUN mkdir /code
WORKDIR /code
ADD ./code /code/
