FROM mcr.microsoft.com/playwright/python:v1.61.0-noble

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
CMD ["pytest"]