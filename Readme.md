# Documentation

## Get_Quran
- The **Get_Quran** program will access the api and check if there is an English edition of Quran for each of the requested types:
    - tafsir
    - translation
    - quran
    - transliteration
    - versebyverse

- If any type does not have an English edition, the program will select the first edition shown.
At the end, a file called resultado.json will be saved, with the following structure:

        - Edition
            - Juz
                - Surah

- Each item on the Surah list will contain an Ayah.

## Conect_Server
- The **Conect_Server** file will connect to the server and check for the existence of a database called Quran. If this database doesn't exist, it will be created.
- Within this database, a table called Tabela will be created, where the data in the resultado.json file will be saved.

# Challenges
- Not all the types requested had an English edition. We therefore chose to select the first edition of the type.
- It was not possible to create materialized views using mariadb, as there is no syntax for creating materialized views in MySQL. We therefore chose to create tables with the queries presented in the **Queries.md** file.
- Tables were chosen because, like a materialized view, they actually store the data and can be used to improve query performance.