FROM python:3.8-slim

WORKDIR /mnt/etl

ENV PYTHONPATH ${PYTHONPATH}:/mnt/etl/src

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

CMD [ "tail", "-f", "/dev/null" ]
