FROM python:3.11
WORKDIR /code
COPY . /code/

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t my-fastapi-app .
# docker run -p 8000:8000 my-fastapi-app