FROM python:alpine
COPY . /api-bookstore
WORKDIR /api-bookstore
RUN pip install -r requirements.txt
EXPOSE 80
CMD python ./bookstore-api.py