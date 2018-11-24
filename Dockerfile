FROM debian:latest
MAINTAINER Juan F Paulini "jpaulini@gmail.com"
RUN apt-get -yqq update ;
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 
ENV PATH /opt/conda/bin:$PATH
ENV APP_NAME cv_app
ENV APP_HOME /opt/${APP_NAME}
ENV ENVIRONMENT dev
ENV FLASK_APP ${APP_HOME}/app.py 
ENV FLASK_ENV ${ENVIRONMENT}

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
 libglib2.0-0 libxext6 libsm6 libxrender1 \
  git mercurial subversion 

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-4.5.4-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

RUN mkdir ${APP_HOME}
ADD cv_app ${APP_HOME}
WORKDIR ${APP_HOME}
ADD requirements.txt ${APP_HOME}
RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "/opt/conda/bin/flask", "run" ,"--host=0.0.0.0" ]