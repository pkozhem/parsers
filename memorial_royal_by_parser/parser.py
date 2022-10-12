"""
    This script parses data of all memorials from http://memorialroyal.by/Memorials.
"""

import json
import re
import requests
from bs4 import BeautifulSoup


def get_page():
    url = "http://memorialroyal.by/Memorials"
    headers = {
        "Access": "*/*",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"
    }

    request = requests.get(url=url, headers=headers)
    src = request.text

    return src


def main():
    print("Collecting data ...")
    soup = BeautifulSoup(get_page(), "lxml")
    memorials = soup.find_all("div", class_="m-3 border-0")
    content = []

    for item in memorials:
        title = item.find("h4").text
        size = item.find(text=re.compile("Размер стеллы:")).next_element.text
        granit = item.find(text=re.compile("Гранит:")).next_element.text
        kit = item.find(text=re.compile("Комплект:")).next_element.text

        content.append(
            {
                "Title": title,
                "Size": size,
                "Granit": granit,
                "Kit": kit
            }
        )

        with open("memorial_royal_by_parser/memorials.json", "w") as file:
            json.dump(content, file, indent=4, ensure_ascii=False)

    print("All data collected. Ending program ...")


if __name__ == '__main__':
    main()
