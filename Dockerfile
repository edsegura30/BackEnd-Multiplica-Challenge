FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
COPY devutils/wait-for-postgres.sh /devutils/wait-for-postgres.sh
RUN chmod +x devutils/wait-for-postgres.sh
