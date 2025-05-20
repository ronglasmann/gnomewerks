# python base image_name (Debian Linux v11)
FROM python:bullseye

RUN apt-get update

# get the latest pip
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade flit

# install the AWS cli
RUN pip3 --no-cache-dir install --upgrade awscli

# for CodeBuild?
ARG AWS_DEFAULT_REGION
ARG AWS_CONTAINER_CREDENTIALS_RELATIVE_URI

# for Dev containers
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY

# install beanstalkd
RUN apt-get install beanstalkd

# install from artifact repo
#RUN aws codeartifact login --tool pip --domain astreanalytics --repository common --region us-east-1
#RUN python -m pip install fwq

# install from local distribution (for Dev env)
COPY dist .
RUN python -m pip install --no-index --find-links dist fwq

#ENV PYTHONPATH "${PYTHONPATH}:/app"
#WORKDIR /app

#RUN mkdir -p fwq
#COPY pyproject.toml .
#RUN aws codeartifact login --tool pip --domain astreanalytics --repository common --region us-east-1
#RUN touch fwq/__init__.py && FLIT_ROOT_INSTALL=1 flit install --only-deps
#RUN rm -rf fwq
#
#COPY src .
#COPY pyproject.toml .
#RUN aws codeartifact login --tool pip --domain astreanalytics --repository common --region us-east-1
#RUN FLIT_ROOT_INSTALL=1 flit install --deps none

