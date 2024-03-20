FROM tiangolo/uvicorn-gunicorn:python3.10

WORKDIR /backend

COPY ./requirements.txt /backend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

COPY . /backend

EXPOSE 8000

ENTRYPOINT ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]