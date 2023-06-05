FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /futbolistas
WORKDIR /futbolistas
COPY requirements.txt /futbolistas/
RUN pip install -r requirements.txt
COPY . /futbolistas/
CMD python manage.py runserver 0.0.0.0:8080
