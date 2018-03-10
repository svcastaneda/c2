FROM python:3
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true

RUN mkdir /src
WORKDIR /src
ADD ./src /src/
RUN pip install -r requirements.txt
