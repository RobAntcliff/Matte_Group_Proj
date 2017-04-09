#!/bin/bash

sudo apt-get update
sudo apt-get -y install tcl
sudo apt-get -y install tcl-dev
sudo apt-get -y install check
sudo apt-get -y install expect
sudo apt-get -y install libxml2
sudo apt-get -y install libxml2-dev
sudo apt-get -y install byacc
sudo apt-get -y install flex
sudo apt-get -y install libreadlinr-dev
sudo apt-get -y install libreadline-gplv2-dev
sudo apt-get -y build-dep build-essential
sudo apt-get -y install gcc
sudo apt-get -y install g++
sudo apt-get -y install python3-lxml

sudo apt-get -y install libncurses5-dev
sudo apt-get -y install python-pip
sudo pip install --upgrade pip
sudo pip install ontospy
