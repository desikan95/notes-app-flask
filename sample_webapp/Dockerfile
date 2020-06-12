FROM rackspacedot/python37

WORKDIR /app

ADD . /app

RUN pip --default-timeout=100 install -r requirements.txt

#CMD flask run --host=0.0.0.0

EXPOSE 5000
