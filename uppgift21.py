from pathlib import Path
import json

def main():
    content = Path("massadata.json").read_text(encoding="utf8")
    data = json.loads(content)
    print(data['entries'])
    b = data['entries']
    totaltotal = 0
    for i in data['entries']:
       totaltotal += i['total']
    print(totaltotal)


if __name__ == '__main__':
    main()