###########
# BUILDER #
###########

# pull official base image
# ЗАМЕНИТЬ СТРОКУ НИЖЕ ПЕРЕД ЗАЛИВОМ НА ПРОД!!! FROM python:3.11.3-slim-buster as builder
FROM python:3.11.3 as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

# lint
RUN pip install --upgrade pip
RUN pip install flake8==6.0.0
COPY . /usr/src/app/

# install python dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
# ЗАМЕНИТЬ СТРОКУ НИЖЕ ПЕРЕД ЗАЛИВОМ НА ПРОД!!! FROM python:3.11.3-slim-buster as builder
FROM python:3.11.3

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
#RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/backend
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
ENV PYTHONPATH=/home/app/backend/

# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends netcat
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy entrypoint-prod.sh
COPY ./entrypoint.sh $APP_HOME

# copy project
COPY . $APP_HOME

# RUN alembic revision --autogenerate -m "Initianal migration"
# RUN alembic upgrade head

CMD uvicorn main:app --reload --host=0.0.0.0 --port=8000

# chown all the files to the app user
#RUN chown -R app:app $APP_HOME
#USER app
# change to the app user

# run entrypoint.prod.s
# change to the web use
#CMD ["/home/app/backend/entrypoint.sh"]

# run entrypoint.prod.s
