FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
