# Queries used to create views

--This sequence will access an existing database called Quran. It will then delete previous views and create 5 new views, one for each type of edition.

USE Quran;
DROP VIEW IF EXISTS tafsir_View;
CREATE VIEW tafsir_View AS
SELECT
       CONCAT('Juz ', Juz) AS Juz, 
       CONCAT('Surah ', Surah, ': ', Text) AS Surah_Text
FROM Tabela
WHERE Edition = 'King Fahad Quran Complex'
ORDER BY CAST(Juz AS SIGNED), Surah;

DROP VIEW IF EXISTS translation_View;
CREATE VIEW translation_View AS
SELECT
       CONCAT('Juz ', Juz) AS Juz, 
       CONCAT('Surah ', Surah, ': ', Text) AS Surah_Text
FROM Tabela
WHERE Edition = 'Wahiduddin Khan'
ORDER BY CAST(Juz AS SIGNED), Surah;

DROP VIEW IF EXISTS quran_View;
CREATE VIEW quran_View AS
SELECT 
       CONCAT('Juz ', Juz) AS Juz, 
       CONCAT('Surah ', Surah, ': ', Text) AS Surah_Text
FROM Tabela
WHERE Edition = 'Simple'
ORDER BY CAST(Juz AS SIGNED), Surah;

DROP VIEW IF EXISTS transliteration_View;
CREATE VIEW transliteration_View AS
SELECT
       CONCAT('Juz ', Juz) AS Juz, 
       CONCAT('Surah ', Surah, ': ', Text) AS Surah_Text
FROM Tabela
WHERE Edition = 'English Transliteration'
ORDER BY CAST(Juz AS SIGNED), Surah;

DROP VIEW IF EXISTS versebyverse_View;
CREATE VIEW versebyverse_View AS
SELECT
       CONCAT('Juz ', Juz) AS Juz, 
       CONCAT('Surah ', Surah, ': ', Text) AS Surah_Text
FROM Tabela
WHERE Edition = 'Ibrahim Walk'
ORDER BY CAST(Juz AS SIGNED), Surah;