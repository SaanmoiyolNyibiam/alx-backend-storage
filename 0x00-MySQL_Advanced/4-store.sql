-- This is an SQL script that creates a trigger that decreases
-- the quantity of an item after adding a new order

DROP TRIGGER IF EXISTS decrease_qty;
DELIMITER $$
CREATE TRIGGER decrease_qty
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- SQL statements to reduce entries
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE items.name = NEW.item_name;
END$$
DELIMITER ;

