#!/bin/sh

apt install libffi-dev=3.3-4 libportaudio2=19.6.0-1build1 python3-dev python3-pip idle -y
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
apt-add-repository 'deb https://download.mono-project.com/repo/ubuntu stable-focal main'
pip3 install pythonnet==3.0.3 vosk==0.3.45 sounddevice==0.5.0 OrangePi.GPIO==0.6.3 paramiko==3.5.0 wakeonlan==3.1.0
apt install mono-complete dirmngr gnupg apt-transport-https ca-certificates software-properties-common -y