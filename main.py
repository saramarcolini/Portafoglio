import requests # importa la libreria requests per effettuare richieste HTTP
import csv # importa la libreria csv per gestire file CSV
import json # importa la libreria json per convertire dati in formato JSON
import yaml # importa la libreria yaml per convertire dati in formato YAML

def getFile(url): # definisce una funzione per ottenere il contenuto di un file dalla URL
    header = {'Connection': 'keep-alive',
            'Expires': '-1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
            }
    # definisce l'intestazione della richiesta HTTP
    website = requests.get(url, headers=header) # effettua una richiesta HTTP con la URL e l'intestazione
    return website.text # restituisce il contenuto del file come stringa

def parseCsv(content): # definisce una funzione per analizzare il contenuto CSV
    csvReader = csv.DictReader(content.splitlines()) # legge il contenuto CSV come dizionario
    data = [row for row in csvReader] # converte ogni riga del file CSV in una riga di dati
    return data # restituisce i dati come lista di dizionari

def convert_to_json(data): # definisce una funzione per convertire i dati in formato JSON
    json_data = [] # inizializza una lista vuota per i dati JSON
    for i, row in enumerate(data): # itera su ogni riga di dati
        json_data.append({"chiave": i+1, "valore": row}) # aggiunge la riga di dati alla lista come dizionario
    json_data = json.dumps(json_data, indent=4) # converte la lista di dati in formato JSON
    with open("PIRC.MI.json", "w") as f: # apre un file per scrivere i dati JSON
        f.write(json_data) # scrive i dati JSON nel file
    print("\nConversion to JSON done") # stampa un messaggio di conferma della conversione

def convert_to_yaml(data): # definisce una funzione per convertire i dati in formato YAML
    yaml_data = [] # inizializza una lista vuota per i dati YAML
    for i, row in enumerate(data): # itera su ogni riga di dati
        yaml_data.append({"chiave": i+1, "valore": row}) # aggiunge la riga di dati alla lista come dizionario
    yaml_data = yaml.dump(yaml_data) # converte la lista di dati in formato YAML
    with open("PIRC.MI.yaml", "w") as f: # apre un file per scrivere i dati YAML
        f.write(yaml_data) # scrive i dati YAML nel file
    print("\nConversion to YAML done") # stampa un messaggio di conferma della conversione


def main():
    csvContent = getFile("https://query1.finance.yahoo.com/v7/finance/download/PIRC.MI?period1=1642923403&period2=1674459403&interval=1d&events=history&includeAdjustedClose=true")
    data = parseCsv(csvContent)
    convert_to_json(data)
    convert_to_yaml(data)


if __name__ == "__main__":
    main()
