# Projet de Scraping de Lexique Portugais-Français pour Anki

Ce projet consiste à récupérer du lexique portugais-français à partir d'une page web et à en faire un paquet de cartes mémoire Anki pour faciliter l'apprentissage du vocabulaire lusophone.

Le deck d'apprentissage obtenu est téléchargeable sur [ce lien](https://ankiweb.net/shared/info/1356231771).

## Utilisation

Ce script peut être utilisé pour télécharger les fiches de vocabulaire des autres langues proposées par ce site.

1. **Installer les dépendances** :

   ```sh
   pip install requests beautifulsoup4
   ```

2. Modifier la variable `main_url` pour correspondre à la page de la langue désirée.

3. **Exécuter le script** :

   ```sh
   python scraper.py
   ```

Ce script parcourt les fiches de vocabulaire du site internet [FichesVocabulaire.com](https://fichesvocabulaire.com/vocabulaire-portugais-pdf), scrape le lexique de chaque fiche, et enregistre les données dans un fichier CSV qui peut être importé dans le logiciel [Anki](https://apps.ankiweb.net/).

## Exemple de Sortie

Le fichier CSV généré aura la structure suivante :

```
#deck column:1
#separator:Comma
#html:false
NomDuPaquet,MotPortugais,MotFrançais
NomDuPaquet,MotPortugais,MotFrançais
```