#! /bin/bash
sudo apt-get install postgresql -y
sudo service postgresql start

#Setting up
sudo -u postgres psql < src/createDB.sql;

