import mysql.connector
import json

# Settings for the connection to the MariaDB database
config = {
    "user": "root",
    "password": "26051984",
    "host": "localhost"
}

# Function to create the Quran database if it doesn't exist
def create_database():
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # Create the Quran database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS Quran")
        print("Database 'Quran' created or already exists")

        # Switch to the Quran database
        cursor.execute("USE Quran")

        # Create the table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Tabela (
                id INT AUTO_INCREMENT PRIMARY KEY,
                edition VARCHAR(255),
                juz INT,
                surah INT,
                text LONGTEXT
            )
        """)
        print("Table 'Tabela' created or already exists")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        connection.close()

# Function to insert data into the table
def inserir_dados(edition, juz, surah, text):
    try:
        connection = mysql.connector.connect(**config, database="Quran")
        cursor = connection.cursor()

        # Insert data into the table
        query = "INSERT INTO Tabela (edition, juz, surah, text) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (edition, juz, surah, text))

        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        connection.close()

# Open Json File
with open("resultado.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

# Create the database and table if necessary
create_database()

# Iterate through the JSON data and insert into the table
for edition, juz_data in data.items():
    for juz, surah_data in juz_data.items():
        for surah, text_list in surah_data.items():
            for text_item in text_list:
                inserir_dados(edition, juz, surah, text_item)