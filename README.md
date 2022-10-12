<h2> Parsers </h2>
This repository contains some parsers for next sites:<br>

1) <a href="https://health-diet.ru">health-diet.ru</a>
2) <a href="http://memorialroyal.by">memorialroyal.by</a>
3) <a href="https://zaka-zaka.com">zaka-zaka.com</a>

And CLI for usage with single python file.
Additional info of parser you can find in parser's code.

<h3> Used technologies </h3>

1) Python ≥ 3.10
2) BeautifulSoup4
3) lxml
4) requests

<h3> Installation guide for Linux/GNU OS </h3>

<b>Note</b>: if you are using Windows OS, do same steps but in 1st
paragraph skip two first command and replace all "python3"
with "python". In 2nd paragraph replace second command with
<path_to_venv>\Scripts\activate.bat

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
4) Use CLI to call specify parser.<br>
   a) to parse <a href="https://health-diet.ru">health-diet.ru</a>
   ```commandline
   python3 manage.py health_diet
   ```
   b) to parse <a href="http://memorialroyal.by">memorialroyal.by</a>
   ```commandline
   python3 manage.py memorial_royal
   ```
   c) to parse <a href="https://zaka-zaka.com">zaka-zaka.com</a>
   ```commandline
   python3 manage.py zaka_zaka
   ```
   
