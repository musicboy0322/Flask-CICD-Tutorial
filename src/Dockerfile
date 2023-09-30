FROM python:3.10-alpine
COPY . /app
WORKDIR /app
RUN pip install flask
RUN pip install requests
CMD [ "flask", "run", "-h", "0.0.0.0"]