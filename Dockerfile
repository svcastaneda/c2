FROM python:3
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true

RUN pip install --disable-pip-version-check pipenv

WORKDIR /src
ADD ./Pipfile* /src/
RUN pipenv install --system

ADD ./src /src/
