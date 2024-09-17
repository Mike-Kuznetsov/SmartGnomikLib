#!/bin/sh

apt install libffi-dev libportaudio2 python3-dev python3-pip idle -y
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
apt-add-repository 'deb https://download.mono-project.com/repo/ubuntu stable-focal main'
pip3 install pythonnet vosk sounddevice OrangePi.GPIO paramiko wakeonlan
apt install mono-complete dirmngr gnupg apt-transport-https ca-certificates software-properties-common -y