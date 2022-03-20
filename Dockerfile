FROM python:latest
WORKDIR /app/src
COPY . ./
RUN pip install -r requirements.txt
CMD ["python", "./main.py"]