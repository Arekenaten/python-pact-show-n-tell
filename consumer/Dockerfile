FROM python:3.8
WORKDIR /pact/consumer
COPY requirements.txt ./
RUN pip install -r requirements.txt
ENV FLASK_APP=consumer.consumer
ENV FLASK_ENV=development
EXPOSE 3001
COPY . .
CMD flask run --host=0.0.0.0 --port=3001