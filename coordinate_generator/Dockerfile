FROM python:3.5.2


RUN mkdir /opt/app && chown www-data:www-data /opt/app
RUN mkdir /opt/app/static && chown www-data:www-data /opt/app/static


WORKDIR /opt/app

# Install python requirements
ADD requirements/* /opt/app/requirements/
RUN pip install -r requirements/dev.txt

# Copy other src
ADD . /opt/app/

#EXPOSE 8085

CMD ["python", "run.py"]
