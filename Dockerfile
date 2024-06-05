FROM kalilinux/kali-rolling

# do APT update
RUN apt-get -y update && apt-get -y dist-upgrade && apt-get -y autoremove && apt-get clean
RUN apt update

RUN apt-get -y install python3 python3-pip --fix-missing

# install project
COPY app.py /root
COPY install.py /root
ADD helper /root/helper/

#Set work directory
WORKDIR /root

#Install dependencies python
RUN python3 ./install.py

RUN mkdir reportsCampana

#Run flask proyect
EXPOSE 5000
CMD ["/bin/sh"]