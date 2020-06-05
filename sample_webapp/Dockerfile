FROM rackspacedot/python37

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD flask run

EXPOSE 5000
