FROM python:3.9.7

# RUN apt-get update && apt-get upgrade -y && \
#     apt-get install -y nodejs \
#     npm  

WORKDIR /app

COPY requirements.txt .

# COPY package.json .
# COPY package-lock.json .

# RUN npm install

RUN pip install -r requirements.txt

EXPOSE 8000

