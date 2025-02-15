CREATE DATABASE popvote;
CREATE USER access WITH PASSWORD 'passwords';

\connect popvote

CREATE TABLE IF NOT EXISTS cur_table (
    v_id SERIAL PRIMARY KEY,
    v_date DATE NOT NULL,
    v_long FLOAT,
    v_lat FLOAT,
    v_vote INT NOT NULL,
    v_table VARCHAR(40)
);

CREATE TABLE IF NOT EXISTS old_tables (
    c_id SERIAL PRIMARY KEY,
    v_id INT,
    v_date DATE NOT NULL,
    v_long FLOAT,
    v_lat FLOAT,
    v_vote INT NOT NULL,
    v_table VARCHAR(40)
);

CREATE TABLE IF NOT EXISTS history (
    h_id SERIAL PRIMARY KEY,
    h_date DATE NOT NULL,
    hv_table VARCHAR(40) NOT NULL
);

