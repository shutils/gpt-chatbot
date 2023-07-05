FROM python:3.10.12

WORKDIR /opt/app

COPY Pipfile* ./

RUN pip install pipenv
RUN pipenv sync --system

COPY src ./
