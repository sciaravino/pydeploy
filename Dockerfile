FROM python:3.7

WORKDIR /app

RUN pip install pandas scikit-learn flask gunicorn

ADD ./model ./model
ADD app.py app.py

EXPOSE 5000

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "app:app" ]