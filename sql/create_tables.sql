CREATE TABLE repinfo(
    id INT(10) NOT NULL,
    rep VARCHAR(50) NOT NULL,
    region VARCHAR(50),
    PRIMARY KEY (id)
)

CREATE TABLE product(
    pid INT(10) NOT NULL,
    item  VARCHAR(50) NOT NULL,
    unitCost DECIMAL(12,2),
    PRIMARY KEY (pid)
)

CREATE TABLE salesOrders(
    id INT(10) NOT NULL,
    pid INT(10) NOT NULL,
    orderData  DATE NOT NULL,
    units INT(10),
    totalCost DECIMAL(12,2),
    PRIMARY KEY (id)
)