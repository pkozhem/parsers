<h2> Parsers </h2>
This repository contains some parsers for next sites:<br>

1) <a href="https://health-diet.ru">health-diet.ru</a>
2) <a href="http://memorialroyal.by">memorialroyal.by</a>
3) <a href="https://zaka-zaka.com">zaka-zaka.com</a>

Additional info of parser you can find in parser's code.

<h3> Used technologies </h3>

1) BeautifulSoup4
2) lxml
3) requests

<h3> Installation guide for Linux/GNU OS </h3>

1) Install all required solutions. Replace 'apt' with
   your distribution package manager.
   ```commandline
   sudo apt update && sudo apt upgrade
   sudo apt install -y git python3-venv python3-pip
   git clone https://github.com/pkozhem/parsers.git
   cd parsers
   ```
2) Create and activate virtual environment.
   ```commandline
   python3 -m venv venv
   source venv/bin/activate
   ```
3) Install all dependencies.
   ```commandline
   pip install -r requirements.txt
   ```
4) To use parser input following commands (in " " input parser name, for example zaka_zaka_com_parser).
   ```commandline
   cd "parser name"
   python3 parser.py
   ```
5) To exit parser.
   ```commandline
   cd ..
   ```