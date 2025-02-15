CREATE DATABASE popvote;
CREATE USER python WITH PASSWORD 'Password';
GRANT ALL PRIVILEGES ON DATABASE popvote TO python;

\connect popvote

CREATE TABLE IF NOT EXISTS cur_table (
    v_id SERIAL PRIMARY KEY,
    v_date TIMESTAMP NOT NULL,
    v_long FLOAT,
    v_lat FLOAT,
    v_vote INT NOT NULL,
    v_table VARCHAR(40)
);

CREATE TABLE IF NOT EXISTS old_tables (
    c_id SERIAL PRIMARY KEY,
    v_id INT,
    v_date TIMESTAMP NOT NULL,
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

GRANT ALL PRIVILEGES ON cur_table TO python;
GRANT SELECT, UPDATE, INSERT, DELETE ON cur_table to python;
GRANT USAGE, SELECT, UPDATE ON SEQUENCE cur_table_v_id_seq TO python;

GRANT ALL PRIVILEGES ON old_tables TO python;
GRANT SELECT, UPDATE, INSERT, DELETE ON old_tables to python;
GRANT USAGE, SELECT, UPDATE ON SEQUENCE old_tables_c_id_seq TO python;

GRANT ALL PRIVILEGES ON history TO python;
GRANT SELECT, UPDATE, INSERT, DELETE ON history to python;
GRANT USAGE, SELECT, UPDATE ON SEQUENCE history_h_id_seq TO python;

