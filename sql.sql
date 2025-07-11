CREATE DATABASE testdb;
\c testdb
CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    feature1 INT,
    feature2 INT,
    prediction INT
);
