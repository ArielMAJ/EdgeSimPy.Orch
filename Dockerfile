FROM python:3.12.10-slim

WORKDIR /

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

EXPOSE 3000

CMD ["python", "-m", "src.main"]
