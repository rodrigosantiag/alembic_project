FROM python:3.11

WORKDIR /app

COPY . .

RUN make install

EXPOSE 8000

CMD ["ipython"]
