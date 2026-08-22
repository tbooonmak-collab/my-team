SQL
-- ตารางเมนูอาหาร
CREATE TABLE IF NOT EXISTS menu_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL, -- 'Ramen', 'Izakaya', 'Drink'
    price REAL NOT NULL
);

-- ตารางโต๊ะอาหาร
CREATE TABLE IF NOT EXISTS tables (
    table_id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_number INT UNIQUE NOT NULL,
    status TEXT DEFAULT 'AVAILABLE' -- 'AVAILABLE', 'OCCUPIED'
);

-- ตารางออเดอร์หลัก
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    table_id INT NOT NULL,
    order_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'PENDING', -- 'PENDING', 'COOKING', 'SERVED', 'COMPLETED'
    FOREIGN KEY (table_id) REFERENCES tables(table_id)
);

-- ตารางรายละเอียดรายการอาหารในออเดอร์
CREATE TABLE IF NOT EXISTS order_details (
    detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INT NOT NULL,
    item_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (item_id) REFERENCES menu_items(item_id)
);
