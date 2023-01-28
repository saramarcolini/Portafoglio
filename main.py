import requests
import pandas
import json

def getFile(url):
    header = {'Connection': 'keep-alive',
            'Expires': '-1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
            }
    website = requests.get(url, headers=header)
    return website.text

def convert_to_json(csv):
    df = pandas.read_csv(csv)
    data_dict = df.to_dict()
    json_data = json.dumps(data_dict)
    with open("data.json", "w") as f:
        f.write(json_data)
    print("Conversion to JSON done.")

def main():
    csv = getFile("https://query1.finance.yahoo.com/v7/finance/download/PIRC.MI?period1=1642923403&period2=1674459403&interval=1d&events=history&includeAdjustedClose=true")
    with open("file.csv", "w") as f:
        f.write(csv)
    convert_to_json("file.csv")

if __name__ == "__main__":
    main()
