# This Dockerfile is for making html, ebook, pdf of progit2-ko.
#
# Build Locally:
#   docker build -t progit2-ko .
#
# Run Locally Built Image:
#   docker run -it --rm -v `pwd`:/progit2-ko progit2-ko bash -c 'cd /progit2-ko; bundle exec rake book:build'
#
# Pull Image:
#   docker pull lethee/progit2-ko:latest
#
# Run pulled Image:
#   docker run -it --rm -v `pwd`:/progit2-ko lethee/progit2-ko:latest bash -c 'cd /progit2-ko; bundle exec rake book:build'

FROM ubuntu:focal

ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8

RUN sed -i 's/archive.ubuntu.com/mirror.kakao.com/g' /etc/apt/sources.list
RUN sed -i 's/security.ubuntu.com/mirror.kakao.com/g' /etc/apt/sources.list
RUN sed -i 's/extras.ubuntu.com/mirror.kakao.com/g' /etc/apt/sources.list

RUN apt update
RUN apt install -y --no-install-recommends build-essential
RUN apt install -y --no-install-recommends git libffi-dev libcurl4 bsdmainutils
RUN apt install -y --no-install-recommends ruby ruby-dev racc
RUN gem install bundler

COPY Gemfile Gemfile
RUN bundle install
RUN asciidoctor-pdf-cjk-kai_gen_gothic-install

CMD ["/bin/bash"]