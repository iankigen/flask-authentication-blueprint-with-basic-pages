FROM python:3
MAINTAINER Ian Kigen <ian.kigen@andela.com>

ENV INSTALL_PATH /snakeeyes
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install --editable .

CMD gunicorn -c "python:config.gunicorn" "snakeeyes.app:create_app()"
