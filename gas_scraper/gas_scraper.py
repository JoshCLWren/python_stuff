import requests
from bs4 import BeautifulSoup
import sqlite3
import datetime
import threading
from random import randrange



cities = ["oklahomacity", "tulsa", "dallas", "wichita", "albany", "miami", "denver"]
connection = sqlite3.connect("gas_prices.db")
c = connection.cursor()

def add_gas_price(city):
  current_time = str(datetime.datetime.now())

  url = f"http://www.{city}gasprices.com/"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  gas_price = float(soup.find("h2").get_text())
  data = (gas_price, current_time, city)
  print(f"Gas price for {city} is currently {gas_price}")
  add_to_db(data)
  print(f"Historic gas prices for {city}:")
  query = 'SELECT * FROM national_gas_prices WHERE CITY=?'
  c.execute(query, [city])


def add_to_db(data):
  c.execute("INSERT INTO national_gas_prices VALUES (?,?,?)", data)
  connection.commit()

def show_prices(city):
  print(f"Gas prices for {city}:")
  query = 'SELECT * FROM national_gas_prices WHERE CITY=?'
  c.execute(query, [city])

def gas_adder():
  for city in cities:
    connection = sqlite3.connect("gas_prices.db")
    # c = connection.cursor()
    # c.execute('''CREATE TABLE national_gas_prices (price REAL, dateAdded TEXT, city TEXT );''')
    add_gas_price(city)
    print(f"Adding gas price for {city}.")
    # show_prices(city)
    connection.close()

gas_adder()


