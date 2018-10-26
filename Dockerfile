FROM ubuntu:18.10

RUN apt update
RUN apt install -y python3.6
RUN apt install python3-pip -y

COPY ./ ./app
WORKDIR ./app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3.6"]

CMD ["app.py"]
