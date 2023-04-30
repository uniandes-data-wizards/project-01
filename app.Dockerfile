FROM python:3.9

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8050

CMD cd model_deployment && python app.py

