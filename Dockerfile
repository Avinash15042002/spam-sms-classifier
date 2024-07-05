FROM ubuntu:latest
RUN apt-get update
RUN apt-get -y install nginx

COPY vectorizer.pkl /var/www/html/vectorizer.pkl
COPY procfile /var/www/html/procfile
COPY app.py /var/www/html/app.py
COPY spam_sms_detection.py /var/www/html/spam_sms_detection.py
COPY gitignore /var/www/html/gitignore
COPY model.pkl /var/www/html/model.pkl
COPY nltk.txt /var/www/html/nltk.txt
COPY setup.sh /var/www/html/setup.sh
COPY spam.csv /var/www/html/spam.csv
COPY requirements.txt /var/www/html/requirements.txt

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
