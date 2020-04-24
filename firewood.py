# Xavier Collantes
# firewood.py

import logging
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

logging.basicConfig(
  format='%(levelname)s %(asctime)s:%(message)s',
  datefmt='%Y-%m-%d %H:%M:%S %Z',
  level=logging.DEBUG
)


URL = 'https://tinder.com/'
WEBDRIVER_PATH = '/Users/xcollantes/Documents/firewood/chromedriver81'

def main():
  driver = webdriver.Chrome(WEBDRIVER_PATH)
  logging.info(f'Using URL: {URL}')
  driver.get(URL)

  time.sleep(5)

  

  driver.close()

if __name__=='__main__':
  main()
