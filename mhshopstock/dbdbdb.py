import pandas as pd
import MySQLdb

file_path = r'C:\Users\nazmu\Downloads\lojaMH.xlsx'
df = pd.read_excel(file_path)

# Step 2: Connect to MySQL database
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="root",
    db="mhstock",
    charset='utf8mb4'
)

cursor = db.cursor()

# Step 3: Create table if not exists
create_table_query = """
CREATE TABLE IF NOT EXISTS products_product (
    code VARCHAR(10) PRIMARY KEY,
    type VARCHAR(50),
    category VARCHAR(50),
    gender VARCHAR(10),
    stock INT,
    price_sell DECIMAL(5,2),
    location VARCHAR(50),
    price_bought DECIMAL(5,2) DEFAULT NULL,
    brand VARCHAR(100),
    season VARCHAR(20)
);
"""

cursor.execute(create_table_query)
db.commit()

# Step 4: Insert data into MySQL
insert_query = """
INSERT INTO products_product (code, type, category, gender, stock, price_sell, location, price_bought, brand, season)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE 
    type=VALUES(type),
    category=VALUES(category),
    gender=VALUES(gender),
    stock=VALUES(stock),
    price_sell=VALUES(price_sell),
    location=VALUES(location),
    price_bought=VALUES(price_bought),
    brand=VALUES(brand),
    season=VALUES(season);
"""

for index, row in df.iterrows():
    values = [
        row['Código'] if not pd.isnull(row['Código']) else '0',
        row['Tipo'] if not pd.isnull(row['Tipo']) else '0',
        row['Classe'] if not pd.isnull(row['Classe']) else '0',
        row['Sexo'] if not pd.isnull(row['Sexo']) else '0',
        row['Stock'] if not pd.isnull(row['Stock']) else 0,
        row['preço-vender'] if not pd.isnull(row['preço-vender']) else 0.0,
        row['onde'] if not pd.isnull(row['onde']) else '0',
        row['preço-comprado'] if not pd.isnull(row['preço-comprado']) else 0.0,
        row['marca'] if not pd.isnull(row['marca']) else '0',
        row['Season'] if not pd.isnull(row['Season']) else '0'
    ]
    cursor.execute(insert_query, tuple(values))

db.commit()

# Step 5: Close the database connection
cursor.close()
db.close()