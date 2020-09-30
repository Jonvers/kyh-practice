import json
from pathlib import Path


def main():
    content = Path("data.json").read_text(encoding="utf8")
    data = json.loads(content)
    pass


# int, float, bool, string, dictionary

if __name__ == '__main__':
    main()
