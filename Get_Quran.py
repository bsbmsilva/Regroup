import requests
import json

types = ["tafsir", "translation", "quran", "transliteration", "versebyverse"]
editions = []
structure = {}
results = {}
# URL base for edition
base_url_edition = 'http://api.alquran.cloud/v1/edition/type/'
# URL base for text
base_url = 'http://api.alquran.cloud/v1/quran/'

try:
    # Find one edition for each type
    for type in types:
        # Create the URL
        url = f"{base_url_edition}{type}"
        edition = 'null'
        # Make a GET request to the API
        response = requests.get(url)

        # Checks if the request was successful
        if response.status_code == 200:
            # Gets the content of the response as a JSON dictionary
            data = response.json()
            
            # Search for an English edition
            for i in range(len(data['data'])):
                if data['data'][i]['language'] == "en":
                    edition = data['data'][i]['identifier']
            
            # If there is no English version, select the first edition of this type
            if edition == 'null':
                edition = data['data'][0]['identifier']

            # Adds the chosen edition to the list
            editions.append(edition)
        else:
            print(f'Failed to access API for type {type}. Status code: {response.status_code}')

    # Download the selected editions
    for edit in editions:
        # Builds the URL with the current edition
        url = f"{base_url}{edit}"
        
        # Make a GET request to the API
        response = requests.get(url)

        # Checks if the request was successful
        if response.status_code == 200:
            # Gets the content of the response as a JSON dictionary
            data = response.json()

            #Check the name of the current edition
            edition_name = data["data"]["edition"]["englishName"]

            for surah in data["data"]["surahs"]:
                surah_number = surah["number"]
                juz_number = surah["ayahs"][0]["juz"]

                if edition_name not in structure:
                    structure[edition_name] = {}

                if juz_number not in structure[edition_name]:
                    structure[edition_name][juz_number] = {}

                if surah_number not in structure[edition_name][juz_number]:
                    structure[edition_name][juz_number][surah_number] = []

                for ayah in surah["ayahs"]:
                    structure[edition_name][juz_number][surah_number].append(ayah["text"])
        else:
            print(f'Failed to access API for edition {edit}. Status code: {response.status_code}')

    # Grava os resultados em um arquivo JSON
    results = structure
    with open('resultado.json', 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)

    print('Results saved in resultado.json.')

except Exception as e:
    print(f'Error when running the program: {str(e)}')