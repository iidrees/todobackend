FROM idreeskun/todobackend-base:latest

# Dev/build dependencies
RUN apt-get update && \
    apt-get install -qy python-dev
RUN apt-get update -y && \
  apt-get install -y python3-pip python3-dev python3 zlib1g-dev libbz2-dev && \
  apt-get install build-essential -y && \
  apt-get install libssl-dev libmysqlclient-dev -y 
  # pip3 install django


  # curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash && \
  # export PATH="/root/.pyenv/bin:$PATH" && \
  # eval "$(pyenv init -)" && \
  # eval "$(pyenv virtualenv-init -)"  && \
  # pyenv install 3.6.5 -s && \
  # export PATH="/root/.pyenv/versions/3.6.5:$PATH" && \
  # export LC_ALL=C.UTF-8 && \
  # export LANG=C.UTF-8 && \
  # export PATH="/root/activo-api/start_api.sh:$PATH" && \
  # pip3 install --user pipenv==2018.5.18 && \
  # python3 -m pip install pipenv==2018.5.18 && \

RUN . /appenv/bin/activate && \
    pip3 install wheel --upgrade

# pip env var after installing wheel
ENV WHEELHOUSE=/wheelhouse PIP_WHEEL_DIR=/wheelhouse PIP_FIND_LINKS=/wheelhouse XDG_CACHE_HOME=/cache

# OUTPUT: Build cache
VOLUME /build

#  OUTPUT: build artefacts (wheels) are output here
VOLUME /wheelhouse

# OUTPUT: Test reports are output here
VOLUME /reports


COPY scripts/test.sh /usr/local/bin/test.sh
# RUN chmod +x /usr/local/bin/test.sh

#  Set defaults fore entrypount and command string
ENTRYPOINT [ "test.sh" ]

CMD ["python3", "manage.py", "test", "--noinput"]

# Add application source 
COPY src /application
WORKDIR /application
