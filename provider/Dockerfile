FROM python:3.8
WORKDIR /pact/provider
COPY requirements.txt ./
RUN pip install -r requirements.txt
ENV FLASK_APP=provider.provider
ENV FLASK_ENV=development
EXPOSE 3000
COPY . .
CMD flask run --host=0.0.0.0 --port=3000