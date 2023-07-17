FROM ubuntu:18.04

ENV CUCKOO_CWD /cuckoo
ENV CUCKOO_UID 1000

# Update package list
RUN apt-get update

# Install persistent packages
RUN apt-get install -y nocache  \
  python2.7-dev \
  python-pip \
  bash \
  openssl \
  libxslt1.1 \
  libjpeg9 \
  libmagic1 \
  libpq5 \
  && pip install --upgrade pip wheel setuptools


# Install Build deps
RUN apt-get install build-essential --no-install-recommends --yes nocache \
  gcc \
  g++ \
  make \
  libssl-dev \
  libxml2-dev \
  libxslt1-dev \
  libtool \
  libjpeg-dev \
  automake \
  autoconf \
  musl-dev \
  libffi-dev \
  libfuzzy-dev \
  libpq-dev \
  curl \
  git \
  mitmproxy \
  && pip install psycopg2

# Install Cuckoo Sandbox Required Dependencies
ENV LIBRARY_PATH=/lib:/usr/lib
COPY services/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN pip install cryptography==3.3 ssdeep pydeep

# Prepare for Cuckoo installation
RUN mkdir /cuckoo \
  && mkdir /cuckoo_build \
  && useradd -ms /bin/bash cuckoo \
  && export PIP_NO_CACHE_DIR=off \
  && export PIP_DISABLE_PIP_VERSION_CHECK=on \
  && export CUCKOO_CWD=/cuckoo

# Install Cuckoo
ADD sandbox /cuckoo_build
WORKDIR /cuckoo_build
RUN pip install pexpect==4.0.1
RUN sed -i 's/from pexpect.replwrap import basestring/from six import string_types as basestring/g' setup.py
RUN python setup.py sdist && pip install -e .

WORKDIR /cuckoo
RUN cuckoo init

# Cleanup
RUN rm -rf /tmp/* \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get purge -y lib*-dev \
  && apt autoremove --yes \
  && apt clean

# Update configs
COPY conf /cuckoo/conf
RUN chown -R cuckoo /cuckoo/conf
COPY update_conf.py /update_conf.py
COPY docker-entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

EXPOSE 1337 31337
USER cuckoo

ENTRYPOINT ["/entrypoint.sh"]
