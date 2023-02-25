FROM python:3.11.2-alpine3.17
WORKDIR /gita
COPY db.json db.py main.py requirements.txt /gita/
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]

