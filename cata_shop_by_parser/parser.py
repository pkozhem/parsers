import os
import json
import requests
from bs4 import BeautifulSoup


def get_http_context():
    url = "http://cata-market.by/"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"
    }
    return url, headers


def get_main_page():
    request = requests.get(url=get_http_context()[0], headers=get_http_context()[1])
    src = request.text
    return src


def get_internal_hrefs():
    soup = BeautifulSoup(get_main_page(), "lxml")
    item_context = soup.find_all("a", class_="item__link item__bg-dark")
    categories = {}
    to_replace = (",", " ", "-", "'", ":")
    for item in item_context:
        title = item.find("span", class_="item__title").text

        for char in to_replace:
            if char in title:
                title = title.replace(char, "_")

        href = item.get("href")
        categories[title] = '{}{}'.format(get_http_context()[0], href)

        with open("cata_shop_by_parser/categories.json", "w", encoding="utf-8") as file:
            json.dump(categories, file, indent=4, ensure_ascii=False)


def main():
    if not os.path.exists("cata_shop_by_parser/data"):
        os.mkdir("cata_shop_by_parser/data")

    get_internal_hrefs()

    with open("cata_shop_by_parser/categories.json", encoding="utf-8") as file:
        categories = json.load(file)

    count = 0
    to_replace = (",", " ", "-", "'", ":")

    for title, href in categories.items():
        for char in to_replace:
            if char in title:
                title = title.replace(char, "_")

        request = requests.get(url=href, headers=get_http_context()[1])
        src = request.text
        soup = BeautifulSoup(src, "lxml")
        product = soup.find_all("div", class_="product-item")
        context = []

        for item in product:
            name = item.find("span", class_="product-item__title").text.strip()
            price = item.find("span", class_="product-item__price").text.strip()

            context.append(
                {
                    "Name": name,
                    "Price": price
                }
            )

            with open(f"cata_shop_by_parser/data/{count}_{title}.json", "w", encoding="utf-8") as file:
                json.dump(context, file, indent=4, ensure_ascii=False)

        count += 1


if __name__ == "__main__":
    main()
