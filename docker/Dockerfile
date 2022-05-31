FROM ubuntu

LABEL name: malu "chikamaluj@gmail.com"

RUN apt-get update -y && apt-get install -y python3-pip

CMD ["ufw allow 5000"]

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./myapi.py /app

ENTRYPOINT ["python3"]

CMD ["myapi.py"]