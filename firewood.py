# Xavier Collantes
# firewood.py

import logging
import platform
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

logging.basicConfig(
  format='[%(levelname)s] [%(asctime)s]: %(message)s',
  datefmt='%Y-%m-%d %H:%M:%S %Z',
  level=logging.DEBUG
)

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')

os_driver = ''
if platform.system() == 'Linux':
  os_driver = 'chromedriver81_linux'
elif platform.system() == 'Darwin':  # Mac OS
  os_driver = 'chromedriver81'
else:
  logging.error('''Could not determine which version of Chrome driver 
          to use due to could not determine OS.''')

logging.info('Found OS as {}'.format(platform.system()))
logging.info('Found Chrome driver called {os_driver}'.format(os_driver=os_driver))

current_path = os.path.abspath(os.path.curdir)

URL = 'https://tinder.com/'
WEBDRIVER_PATH = '{current_path}/{driver_type}'.format(
                                                 current_path=current_path,
                                                 driver_type=os_driver,
                                                )
logging.debug('{}'.format(WEBDRIVER_PATH))

def main():
  driver = webdriver.Chrome(WEBDRIVER_PATH, options=chrome_options)
  logging.info("Using URL: {inURL}".format(inURL=URL))
  driver.get(URL)

  for x in range(5):
    time.sleep(1)
    logging.debug("SLEEP " + x)

  

  driver.close()

if __name__=='__main__':
  main()
