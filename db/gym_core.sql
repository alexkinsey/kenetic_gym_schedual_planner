DROP TABLE IF EXISTS attendance;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS trainers;
DROP TABLE IF EXISTS locations;
DROP TYPE IF EXISTS membership_types;

CREATE TYPE membership_types AS ENUM('standard', 'premium');

CREATE TABLE locations(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE trainers(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

-- NOTE the prefed date formate is YYYY/MM/DD
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    membership membership_types,
    join_date DATE, 
    post_code VARCHAR(10),
    phone_number VARCHAR(11),
    email VARCHAR(255)
);

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    trainer_id INT REFERENCES trainers ON DELETE CASCADE,
    location_id INT REFERENCES locations ON DELETE CASCADE,
    date DATE,
    time TIME,
    capacity INT
);

CREATE TABLE attendance (
    id SERIAL PRIMARY KEY,
    class_id INT REFERENCES classes ON DELETE CASCADE,
    customer_id INT REFERENCES customers ON DELETE CASCADE
);