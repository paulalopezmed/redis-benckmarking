FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY redis-client.py .

CMD [ "python", "./redis-client.py" ]
