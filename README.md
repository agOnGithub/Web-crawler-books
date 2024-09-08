
# Web crawler - books

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Scrapy)
![Static Badge](https://img.shields.io/badge/PR-Welcome-blue)

My first attempt at creating a web crawler in Python. It traverses an online book shop and grabs book titles and URLs.

I have followed the tutorial that can be found at: https://realpython.com/web-scraping-with-scrapy-and-mongodb/.




## Lessons Learned
While working on this project I have learned the following:

- Set up and configure a project using Scrapy
- Build a working web scraper using Scrapy
- Extract data from websites using CSS selectors
- Store scraped data in a MongoDB database

In addition, my code takes into account that sometimes duplicate data can be scraped so the duplicates are ignored.
## Installation
Python: 
Get it from here: https://www.python.org/downloads/ or via Microsoft Store

venv:
```bash
pip install virtualenv
```

Scrapy: 
```bash
python -m pip install scrapy
```

MongoDB: 
Download the relevant to you installer from https://www.mongodb.com/docs/manual/installation/#mongodb-community-edition-installation-tutorials. Additionally, you will need to run the below command in cmd:
```bash
python -m pip install pymongo
```

## Deployment

To deploy this project run the following commands in the cmd:

1. venv
```bash
venv\Scripts\activate.bat
```
or add it to your PATH

2. Scrapy

```bash
  scrapy startproject books
```

3. MongoDB
```bash
test> use books_db
switched to db books_db
books_db> db.createCollection("books")
{ ok: 1 }
books_db> show collections
books
books_db>

```
## Roadmap

- Scrape dynamically generated content
