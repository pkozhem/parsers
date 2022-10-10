"""
    This script parses data from https://zaka-zaka.com/game/new - novelties of Games World.

    Parses all games names in: games_list.json.
    Parses all single game data in: data/<game_number>_<game_name>.json
"""

import os
import shutil
import json
import requests
from bs4 import BeautifulSoup


def get_page(i):
    url = f"https://zaka-zaka.com/game/new/page{i}"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"
    }

    request = requests.get(url=url, headers=headers)
    src = request.text

    return src


def get_games_list_json(pages_amount):
    games_list = {}

    if os.path.exists("games_list.json"):
        os.remove("games_list.json")

    for i in range(1, pages_amount + 1):
        soup = BeautifulSoup(get_page(i), "lxml")
        games = soup.find_all(class_="game-block")

        for item in games:
            game_name = item.find(class_="game-block-name").text
            game_href = item.get("href")
            games_list[game_name] = game_href

            with open("games_list.json", "w") as file:
                json.dump(games_list, file, indent=4, ensure_ascii=False)


def main():
    pages_amount = int(input("Input amount of pages to parser in range [1..15]: "))
    get_games_list_json(pages_amount)

    if os.path.exists("data"):
        shutil.rmtree("data")

    os.mkdir("data")

    with open("games_list.json") as file:
        all_games = json.load(file)

    count = 0
    to_replace = (",", " ", "-", "'", ":")
    for name, href in all_games.items():
        for item in to_replace:
            if item in name:
                name = name.replace(item, "_")

        request = requests.get(url=href, headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"
        })
        src = request.text

        soup = BeautifulSoup(src, "lxml")
        description = soup.find(class_="description")
        details = {}

        genre = description.find_all("p")[3].text.strip("Жанр:")
        publisher = description.find_all("p")[4].text.strip("Издатель: ")
        language = description.find_all("p")[5].text.strip("Язык: ")
        date = description.find_all("p")[6].text.strip("Дата выхода: ")
        amount = description.find_all("p")[7].text.strip("Наличие: ")

        details["Name"] = name
        details["Genre"] = genre
        details["Publisher"] = publisher
        details["Language"] = language
        details["Date"] = date
        details["Amount"] = amount

        with open(f"data/{count}_{name}.json", "a") as file:
            json.dump(details, file, indent=4, ensure_ascii=False)

        count += 1


if __name__ == "__main__":
    main()
