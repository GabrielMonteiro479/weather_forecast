FROM python-base:latest

COPY requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir -r /app/requirements.txt

COPY app /app
COPY run.py /run.py

RUN python run.py
