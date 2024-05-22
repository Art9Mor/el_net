FROM python:3.11

WORKDIR /running

COPY ./requirements.txt /running/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /running/requirements.txt

COPY . .

ENV PYTHONUNBUFFERED 1

CMD ["python3","manage.py", "runserver", "127.0.0.1:8000"]