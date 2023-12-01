FROM python:3.10
RUN mkdir mailing
WORKDIR /mailing
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod a+x docker/*.sh