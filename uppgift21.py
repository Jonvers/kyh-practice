from pathlib import Path
import json


def main():
    content = Path("massadata.json").read_text(encoding="utf8")
    data = json.loads(content)
    print(data['entries'])
    total_total = 0
    for i in data['entries']:
        total_total += i['total']
    print(total_total)


if __name__ == '__main__':
    main()
