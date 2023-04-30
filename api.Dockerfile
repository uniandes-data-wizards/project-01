FROM python:3.9

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN python -m nltk.downloader stopwords

COPY . .

EXPOSE 8000

CMD cd model_deployment && python3 -m uvicorn main:app --reload
