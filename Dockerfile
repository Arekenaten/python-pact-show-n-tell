FROM python:3.8
WORKDIR /pact
COPY requirements.txt ./
RUN pip install -r requirements.txt
ENV FLASK_APP=.
ENV FLASK_ENV=development
EXPOSE 3000
COPY . .
CMD flask run --host=0.0.0.0 --port=3000