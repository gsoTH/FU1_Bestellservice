DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS pizza;
DROP TABLE IF EXISTS orders;

CREATE TABLE pizza (
	id			INTEGER
,	name		TEXT
,	toppings	TEXT
,	price		REAL
,	PRIMARY KEY(id)
);	

CREATE TABLE orders (
	id			INTEGER
,	name		TEXT
,	phone		TEXT
,	PRIMARY KEY(id)
);

CREATE TABLE items (
	order_id	INTEGER
,	pizza_id	INTEGER
,	amount		INTEGER
,	PRIMARY KEY(order_id, pizza_id)
,	FOREIGN KEY (order_id) REFERENCES orders(id)
,	FOREIGN KEY (pizza_id) REFERENCES pizza(id)
);

INSERT INTO pizza VALUES
	(1, 'Mario', 'Käse, Tomatensauce', 9.5)
,	(2,	'Luigi', 'Käse, Spinat', 12.5)
;
