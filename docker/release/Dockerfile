FROM idreeskun/todobackend-base:latest

# copy applicaiton artifact
COPY target /wheelhouse

# install application 
RUN . /appenv/bin/activate && \
    pip3 install --no-index -f /wheelhouse todobackend && \
    pip3 install django-nose && \
    rm -rf /wheelhouse