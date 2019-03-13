FROM python:2.7-alpine

COPY run.sh ./run.sh
COPY connect.py /usr/local/bin/py/connect.py

RUN apk add curl && pip install elasticsearch==2.3.0 && chmod +x ./run.sh /usr/local/bin/py/connect.py

ENTRYPOINT [ "./run.sh" ]