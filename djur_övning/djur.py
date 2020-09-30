import webbrowser
from pathlib import Path

OUTPUT_PATH = Path("djur.html")
TEMPLATE_PATH = Path('djur_template')

class Djur:
    def __init__(self, name, carnivore, wiki_url):
        self.name = name
        self.carnivore = carnivore
        self.wiki_url = wiki_url


if __name__ == '__main__':
    djur = []
    zebra = Djur('Zebra', True, 'https://sv.wikipedia.org/wiki/Zebror')
    djur.append(zebra)
    html = '<html><table>'
    for d in djur:
        if d.carnivore:
            cell_2 = 'Köttätare'
        else:
            cell_2 = 'Vegetarian'
        html += f'<tr><td><a href="{d.wiki_url}"></td><td>{cell_2}</td></tr>\n'
    html += '</table></html>'
    OUTPUT_PATH.write_text(html, encoding='utf8')
    webbrowser.open(str(OUTPUT_PATH))