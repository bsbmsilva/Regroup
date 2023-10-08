# Queries used to create views

-- This sequence will access an existing database called Quran. It will then delete previous tables and create 5 new tables, one for each type of edition.

USE Quran;
DROP TABLE IF EXISTS tafsir_View;
CREATE TABLE tafsir_View AS
SELECT
       CONCAT('Juz ', Juz) AS Juz, 
       CONCAT('Surah ', Surah, ': ', Text) AS Surah_Text
FROM Tabela
WHERE Edition = 'King Fahad Quran Complex'
ORDER BY CAST(Juz AS SIGNED), Surah;

DROP TABLE IF EXISTS translation_View;
CREATE TABLE translation_View AS
SELECT
       CONCAT('Juz ', Juz) AS Juz, 
       CONCAT('Surah ', Surah, ': ', Text) AS Surah_Text
FROM Tabela
WHERE Edition = 'Wahiduddin Khan'
ORDER BY CAST(Juz AS SIGNED), Surah;

DROP TABLE IF EXISTS quran_View;
CREATE TABLE quran_View AS
SELECT 
       CONCAT('Juz ', Juz) AS Juz, 
       CONCAT('Surah ', Surah, ': ', Text) AS Surah_Text
FROM Tabela
WHERE Edition = 'Simple'
ORDER BY CAST(Juz AS SIGNED), Surah;

DROP TABLE IF EXISTS transliteration_View;
CREATE TABLE transliteration_View AS
SELECT
       CONCAT('Juz ', Juz) AS Juz, 
       CONCAT('Surah ', Surah, ': ', Text) AS Surah_Text
FROM Tabela
WHERE Edition = 'English Transliteration'
ORDER BY CAST(Juz AS SIGNED), Surah;

DROP TABLE IF EXISTS versebyverse_View;
CREATE TABLE versebyverse_View AS
SELECT
       CONCAT('Juz ', Juz) AS Juz, 
       CONCAT('Surah ', Surah, ': ', Text) AS Surah_Text
FROM Tabela
WHERE Edition = 'Ibrahim Walk'
ORDER BY CAST(Juz AS SIGNED), Surah;