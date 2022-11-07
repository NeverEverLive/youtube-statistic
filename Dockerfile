FROM python:3.10-slim

RUN apt-get --yes update
RUN apt-get --yes install libopenblas-dev libomp-dev

COPY requirements.txt .
RUN pip install -U pip && pip install setuptools && pip install -r requirements.txt
RUN rm requirements.txt

COPY src /src
COPY server.py /

CMD ["python", "server.py"]
