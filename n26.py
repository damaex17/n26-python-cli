#!/usr/bin/env python
import requests
import getpass
import pprint


def login(username,password):
  h = {"Authorization":"Basic  YW5kcm9pZDpzZWNyZXQ=", "Content-Type":"application/x-www-form-urlencoded"}
  payload = 'grant_type=password&username=%s&password=%s' % (username,password)
  r = requests.post('https://api.tech26.de/oauth/token', data=payload, headers=h)
  return r.json()['access_token']

def get_n26(token,url):
  h = {'Authorization': 'Bearer %s' % token, 'Content-type': 'application/json'}
  r = requests.get('%s' % url, headers=h)
  return r.json()

def get_credentials():
  username = raw_input("Enter your N26 email address: ")
  password = getpass.getpass('Enter your password:')
  return username,password

def main():
  username,password = get_credentials()
  token = login(username, password)
  pprint.pprint(get_n26(token,'https://api.tech26.de/api/me'))
  pprint.pprint(get_n26(token,'https://api.tech26.de/api/accounts'))
  pprint.pprint(get_n26(token,'https://api.tech26.de/api/smrt/transactions'))


if __name__ == "__main__":
    main()
