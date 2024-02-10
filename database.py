import pymysql

connection = {
    "host": "nanowack.shop",
    "database": "nanowac1_app",
    "user": "nanowac1_appuser",
    "password": "]_dEeEEDKr;8"
}

# Veritabanına bağlanma
connection = pymysql.connect(**connection)

# Cursor oluşturma
cursor = connection.cursor()