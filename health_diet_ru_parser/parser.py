"""
    This script parses all data about calories, proteins, fats and carbohydrates of all products from
    https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie.

    Parses all categories in: categories.json.
    Parses all products by categories in: data/<category_number>_<category_name>.json
"""

import os
import json
import requests
from bs4 import BeautifulSoup


def create_or_check_index_html(url, headers):
    if os.path.exists("index.html"):
        return

    request = requests.get(url=url, headers=headers)
    src = request.text

    with open("health_diet_ru_parser/index.html", "w") as file:
        file.write(src)

    print("Creating index.html ...")


def create_or_check_categories_json(categories):
    if os.path.exists("categories.json"):
        return

    with open("health_diet_ru_parser/categories.json", "w") as file:
        json.dump(categories, file, indent=4, ensure_ascii=False)

    print("Creating categories.json ...")


def main():
    url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"
    }
    create_or_check_index_html(url, headers)

    with open("health_diet_ru_parser/index.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    print("Removing index.html ...")
    os.remove("health_diet_ru_parser/index.html")
    products_hrefs = soup.find_all("a", class_="mzr-tc-group-item-href")

    categories = {}
    for item in products_hrefs:
        categories[item.text] = "https://health-diet.ru" + item.get("href")

    create_or_check_categories_json(categories)

    with open("health_diet_ru_parser/categories.json") as file:
        all_categories = json.load(file)

    count = 0
    to_replace = (",", " ", "-", "'")

    if not os.path.exists("health_diet_ru_parser/data"):
        os.mkdir("health_diet_ru_parser/data")

    for category_name, category_href in all_categories.items():
        print(f"Iteration #{count}. Initializing {category_name} category ...\nPending {53 - count} categories.")

        for item in to_replace:
            if item in category_name:
                category_name = category_name.replace(item, "_")

        request = requests.get(url=category_href, headers=headers)
        src = request.text

        with open(f"health_diet_ru_parser/data/{count}_{category_name}.html", "w") as file:
            file.write(src)

        with open(f"health_diet_ru_parser/data/{count}_{category_name}.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")

        alert = soup.find(class_="uk-alert-danger")
        if alert is not None:
            os.remove(f"health_diet_ru_parser/data/{count}_{category_name}.html")
            continue

        products_data = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")

        products_json = []
        for item in products_data:
            products_tds = item.find_all("td")

            title = products_tds[0].find("a").text
            calories = products_tds[1].text
            proteins = products_tds[2].text
            fats = products_tds[3].text
            carbohydrates = products_tds[4].text

            products_json.append(
                {
                    "Title": title,
                    "Calories": calories,
                    "Proteins": proteins,
                    "Fats": fats,
                    "Carbohydrates": carbohydrates
                }
            )

        with open(f"health_diet_ru_parser/data/{count}_{category_name}.json", "a") as file:
            json.dump(products_json, file, indent=4, ensure_ascii=False)

        os.remove(f"health_diet_ru_parser/data/{count}_{category_name}.html")
        count += 1

    print("All data collected. Ending program ...")


if __name__ == '__main__':
    main()
