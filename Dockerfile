FROM python:3.10

WORKDIR /app

ENV FLASK_APP main.py

RUN mkdir -p /var/log/miapi

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt numpy -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com

COPY . /app

EXPOSE 5000

ENTRYPOINT ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]