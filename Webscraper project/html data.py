import requests 
import csv
from bs4 import BeautifulSoup

DRIVER_PATH = "C:\\Users\\staya\\chromedriver"
BASE_URL = 'https://raleigh.craigslist.org'

soup = BeautifulSoup(driver.page_source, 'html.parser')

csv_file = 'craigslist_data.csv'

csv_writer = csv.writer(open(csv_file, 'w'))

heading = soup.find('h2')

print(heading.text)


