import requests
from bs4 import BeautifulSoup
import csv
import os

def scrape_table_to_csv(url, packet_name = "", output_file='portuguese_french_deck.csv'):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table')
        if table:
            file_exists = os.path.isfile(output_file)
            with open(output_file, mode='a', newline='', encoding="utf-8") as file:
                writer = csv.writer(file)

                if not file_exists:
                    writer.writerow(["#deck column:1"])
                    writer.writerow(["#separator:Comma"])
                    writer.writerow(["#html:false"])


                rows = table.find_all('tr')[1:]  # Ignorer la première ligne qui contient les en-têtes
                for row in rows:
                    cells = row.find_all('td')
                    if cells and 'bgcolor' not in cells[0].attrs:
                        cell_data = ["Vocabulaire Portugais::"+packet_name] + [cell.text for cell in cells] # Ignorer les lignes colorées qui indiquent un séparation logique du tableau
                        writer.writerow(cell_data)

        else:
            print(f'Aucun tableau trouvé sur la page {packet_name}')
    else:
        print(f'Échec de la requête : {response.status_code}')


if __name__ == "__main__":
    main_url = 'https://fichesvocabulaire.com/vocabulaire-portugais-pdf'

    response = requests.get(main_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        ol = soup.find('ol')
        if ol:
            links = ol.find_all('a')
            for link in links:
                href = link.get('href')
                if href:
                    full_url = requests.compat.urljoin(main_url, href)
                    packet_name = link.text.strip()
                    print(packet_name, full_url)
                    scrape_table_to_csv(full_url, packet_name)
        else :
            print("Aucune liste trouvée.")
    else:
        print(f'Échec de la requête : {response.status_code}')