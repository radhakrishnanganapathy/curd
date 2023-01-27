FROM python:3.9

RUN mkdir /my_project
WORKDIR /my_project
# COPY ./requirements.txt /my_project/requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8006" ]




