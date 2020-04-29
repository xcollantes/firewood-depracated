# Xavier Collantes

import requests
import logging


logging.basicConfig(level=logging.DEBUG)

url = 'https://api.gotinder.com/auth'

def main():
  payload = {
    'facebook_token': '82b3f39197af7c54860267685b83d6e',
    'facebook_id': '2579217559062726'
  }

  response = requests.post(url, params=payload)

  logging.debug(response.text)

if __name__=='__main__':
  main()

# AMDG
