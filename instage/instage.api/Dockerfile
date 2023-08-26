FROM python:3.9

WORKDIR /app


COPY app.py /app/
COPY templates /app/templates/

RUN pip install Flask redis

EXPOSE 5000

CMD ["python", "app.py"]
