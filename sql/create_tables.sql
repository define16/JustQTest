CREATE DATABASE IF NOT EXISTS justq_subject_db;
USE justq_subject_db;

CREATE TABLE repinfo(
    rid INT(10) NOT NULL,
    rep VARCHAR(50) NOT NULL,
    region VARCHAR(50),
    PRIMARY KEY (rid)
);

CREATE TABLE productinfo(
    pid INT(10) NOT NULL,
    item  VARCHAR(50) NOT NULL,
    unitCost DECIMAL(12,2),
    PRIMARY KEY (pid)
);

CREATE TABLE salesOrders(
    rid INT(10) NOT NULL,
    pid INT(10) NOT NULL,
    orderDate  VARCHAR(12) NOT NULL,
    units INT(10),
    totalCost DECIMAL(12,2)
);