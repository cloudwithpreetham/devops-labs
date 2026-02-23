FROM ubuntu:latest

RUN apt-get update && apt-get install -y curl

WORKDIR /app

COPY app.txt /app/app.txt

EXPOSE 8080

CMD ["cat", "/app/app.txt"]
