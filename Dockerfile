FROM python:3.10

RUN mkdir -p /opt/services/bot/geektech-bot
WORKDIR /opt/services/bot/

COPY . /opt/services/bot/

RUN pip install -r requirements.txt

CMD ["python", "/opt/services/bot/main.py"]