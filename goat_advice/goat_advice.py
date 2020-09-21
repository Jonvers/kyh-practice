from pathlib import Path
import json
import webbrowser
import requests

def main():
    old_browser = Path("test.html")
    new_browser = Path("goat_quote.html")
    html_template = old_browser.read_text(encoding="utf8")
    advice_r = requests.get("https://api.adviceslip.com/advice")
    advice_j = json.loads(advice_r.text)
    new_html = html_template.replace("QUOTE_TEXT", advice_j['slip'].get('advice'))
    new_browser.write_text(new_html)
    webbrowser.open(str(new_browser))

if __name__ == '__main__':
    main()