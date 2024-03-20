# Port 8501 is default hpsting for Streamlit
FROM python:3.10-slim

WORKDIR /streamlit_frontend

COPY ./requirements.txt /streamlit_frontend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /streamlit_frontend/requirements.txt

COPY . /streamlit_frontend

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]