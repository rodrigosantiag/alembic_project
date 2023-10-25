FROM python:3.11

WORKDIR /app

COPY requirements.txt .
COPY src .
COPY Makefile .

RUN make install

EXPOSE 8000

CMD ["ipython"]
