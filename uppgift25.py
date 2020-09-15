import json
import requests
import datetime


def main():
    r = requests.get("https://proagile.se/api/publicEvents")
    file = json.loads(r.text)

    real_number = False
    month = 0
    year = 0

    while not real_number:
        try:
            year = int(input('år:'))
            month = int(input('månad:'))
            real_number = True
        except ValueError:
            print('Skriv bara siffror')
            real_number = False

    for i in file:
        current_date = datetime.datetime.strptime(i['startDate'], '%Y-%m-%d')
        if current_date.month == month and current_date.year == year:
            print(f"Kursnamn:  {i['name']}\nStartdatum:  {i['startDate']}\n"
                  f"Slutdatum:  {i['endDate']}\n")


if __name__ == '__main__':
    main()
