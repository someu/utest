FROM python:3.8-alpine

WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
ENV PYTHONIOENCODING=UTF-8

ENTRYPOINT ["python3", "-u" ,"manage.py", "runserver"]

