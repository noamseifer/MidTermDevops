FROM python:3.10.12
WORKDIR /MidtermDevOps
# These envs are not in use
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# These installation are not needed if you use a requirements.txt file, also not needed for flask
RUN apt-get update && apt-get install -y gcc build-essential && rm -rf /var/lib/apt/lists/*
# Could be done in one copy line
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
# you copy more files than you need to because you repo not organized enough
COPY . . 
CMD ["flask","run","--debug"]