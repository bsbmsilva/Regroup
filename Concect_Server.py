import mysql.connector
import json

# Settings for the connection to the MariaDB database
config = {
    "user": "root",
    "password": "26051984",
    "host": "localhost",
    "database": "Quran"
}

# Function to insert data into the table
def inserir_dados(edition, juz, surah, text):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # Insert data into the table
        query = "INSERT INTO Tabela (edition, juz, surah, text) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (edition, juz, surah, text))

        connection.commit()
        print("Successful data entry")
    except mysql.connector.Error as err:
        print(f"Erro: {err}")

    finally:
        cursor.close()
        connection.close()

# Open Json File
with open("resultado.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

# Iterate through the JSON data and insert into the table
for edition, juz_data in data.items():
    for juz, surah_data in juz_data.items():
        for surah, text in surah_data.items():
            inserir_dados(edition, juz, surah, text[0])