FROM python:3.5

RUN mkdir /opt/app && chown www-data:www-data /opt/app
RUN mkdir /opt/app/static && chown www-data:www-data /opt/app/static

WORKDIR /opt/app

# Install python requirements
ADD requirements/* /opt/app/requirements/
RUN pip install -r requirements/dev.txt

# Copy other src
ADD . /opt/app/

RUN chown www-data:www-data run_web.sh run_celery.sh &&  chmod +x run_web.sh run_celery.sh
