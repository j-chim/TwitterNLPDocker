FROM python:2


RUN apt-get update && \
    apt-get install -y default-jre && \
    apt-get clean;

RUN pip install flask

RUN git clone https://github.com/j-chim/twitter_nlp
ENV TWITTER_NLP=./
WORKDIR /twitter_nlp

ADD api.py /twitter_nlp

ENTRYPOINT ["python", "api.py"]