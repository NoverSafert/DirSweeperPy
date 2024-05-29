FROM python:3.10.11

ADD src/ src/
COPY src src
ADD testing/ testing/
COPY testing testing

RUN pip install click 
