# Xavier Collantes
# firewood.py

import logging

from selenium import webdriver
from selenium.webdriver.common.by import By

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
