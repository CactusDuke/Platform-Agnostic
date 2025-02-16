#! /bin/bash
sudo apt-get install postgresql -y
sudo service postgresql start

#Setting up Python
rm -r venv
python -m venv venv
source venv/bin/activate

#Libraries
pip install psycopg2-binary
pip install flask

#Setting up Postgres
sudo -u postgres psql < src/createDB.sql;


