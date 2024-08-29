FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

ENV TZ=ASIA/Dhaka
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app
RUN mkdir tecgen

RUN apt-get update && apt-get install build-essential binutils libproj-dev gdal-bin curl -y
RUN pip3 install -U pip
ADD requirements.txt /app
RUN pip3 install -r requirements.txt && apt-get --purge autoremove build-essential -y


COPY tecgen/ /app/tecgen/
COPY entrypoint.sh /usr/local/bin
RUN chmod +x /usr/local/bin/entrypoint.sh
CMD ["entrypoint.sh"]

EXPOSE 8000