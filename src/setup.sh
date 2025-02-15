#! /bin/bash
sudo apt-get install postgresql -y
sudo service postgresql start

#Setting up Postgres
sudo -u postgres psql < src/createDB.sql;

#Setting up
rm -r venv
python -m venv venv
source venv/bin/activate

