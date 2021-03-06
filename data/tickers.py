import requests
import csv
import json
import secrets
import os
import time
from datetime import date


polygon_api_key = os.environ['polygon_api_key']
symbols_list = []
symbols = 'data/symbols.csv'
with open(symbols, 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        ticker_symbol = row['Ticker'].strip()
        symbols_list.append(ticker_symbol)


# =========================== HELPER FUNCTIONS FOR CALCULATIONS ===================================== #

def calculate_payout_schedule(results):
  """Return count of payouts for a given year"""
  # str.startswith(str, beg=0,end=len(string));
  count = 0
  for result in results:
   if result['paymentDate'].startswith('2020'):
        count += 1
  return count

# =========================== HELPER FUNCTIONS FOR API REQUESTS ===================================== #

def get_dividends(symbol, key):
  # print('symbol line 95',symbol)
  """Takes in a ticker symbol and api key and requests info on dividends then
      parses the data"""

  data = requests.get(f'https://api.polygon.io/v2/reference/dividends/{symbol}?&apiKey={key}')
  dividends = data.json()
  payload = {'payment_interval': None, 'amount': None}
  if 'results' in dividends:
    if len(dividends['results']) > 0:
      index = dividends['results'][0]
      payload['payment_interval'] = calculate_payout_schedule(dividends['results'])
      if 'amount' in index:
        payload['amount'] = index['amount']
  return payload

def get_financials(symbol, key):
  """Takes in a ticker symbol and api key and requests info on financials then
      parses the data"""
  data = requests.get(f'https://api.polygon.io/v2/reference/financials/{symbol}?limit=5&apiKey={key}')
  financials = data.json()
  payload = {'dividend_yield': None, 'payout_ratio': None}
  if 'results' in financials:
    if len(financials['results']) > 0:
      index = financials['results'][0]
      if 'dividendYield' in index:
        payload['dividend_yield'] = index['dividendYield']
      if 'payout_ratio' in index:
        payload['payout_ratio'] = index['payoutRatio']
  return payload


def get_open(symbol, key):
  """Takes in a ticker symbol and api key and requests info on opens then parses the data"""
  data = requests.get(f'https://api.polygon.io/v1/open-close/{symbol}/2020-10-14?unadjusted=true&apiKey={key}')
  open_data = data.json()
  payload = {'ticker_open': None}
  if 'open' in open_data:
    payload['ticker_open'] = open_data['open']
  return payload


# =========================== Function To Get Ticker Data And Seed CSV ===================================== #

def get_fucking_data(listslice, apikey=polygon_api_key):
    rows = []
    for symbol in listslice:
        dividends = get_dividends(symbol,apikey)
        financials = get_financials(symbol,apikey)
        stock_price = get_open(symbol,apikey)
        rows.append([symbol, dividends['amount'], financials['dividend_yield'],financials['payout_ratio'],dividends['payment_interval'], stock_price['ticker_open']])


    fields = ['Ticker Symbol','Dividend Amount','Dividend Yield','Payout Ratio','Payout Schedule','Stock Price']
    with open('Acclivity', 'a') as f:

      write = csv.writer(f)
      # write.writerow(fields)
      write.writerows(rows)


option1 = symbols_list[:5]


def slice_tickers(symbols):
  """Return a list of ticker slices in increments of 5"""

  beg = 0
  end = 5
  slices = []
  for i in range(200):
    slices.append(symbols[beg:end])
    beg += 5
    end += 5
  #print('Ticker slices from slice_tickers function: ', slices) #uncomment to test
  return slices

ticker_slices = slice_tickers(symbols_list)

api_keys = ['BKbRifpJKOqo7sbgdiS4dpNgJJbhgA2b', '64Pq2r00bGiIMp1p2v5OlW1HyKPqf2Lc',
'qFu3Rz73EdWbzqYWGoW6s2LxMOEdl9pv', 'EJmtRBPyXNWTUdWJ7ufLp2QApbbZLQJO', 'dbQowNI4tspD24g23hPz7XcpzFwGqE6p',
'fYQG1lXt9u2BgCAsdp7i_5ELabU8lY_9', '9ASTRoiT24JqQBzyPx7QSJhSzVEzcpgQ', 'ReaesOJdPhkSbqVAKZHhmCEhrODblLXw',
'SpZFySFjaK30dFGJ32o2TnvlVwR6ZPnu']

def call_data_function_with_tickers(tickers, keys):
  """Invoking our get_fucking_data function with sliced list of tickers and API keys"""

  index = 0
  for ticker in tickers:
    get_fucking_data(ticker, keys[index])
    if index >= 8:
      time.sleep(60)
      index = 0
    else:
      index += 1

call_data_function_with_tickers(ticker_slices, api_keys)
# ! NEED 
# get_fucking_data(option1, 'BKbRifpJKOqo7sbgdiS4dpNgJJbhgA2b')
# def get_fucking_data(64Pq2r00bGiIMp1p2v5OlW1HyKPqf2Lc, listslice)
# get_fucking_data(option1, 'qFu3Rz73EdWbzqYWGoW6s2LxMOEdl9pv')
# get_fucking_data(option1,'EJmtRBPyXNWTUdWJ7ufLp2QApbbZLQJO')
# def get_fucking_data(dbQowNI4tspD24g23hPz7XcpzFwGqE6p, listslice)
# def get_fucking_data(fYQG1lXt9u2BgCAsdp7i_5ELabU8lY_9, listslice)
# def get_fucking_data(9ASTRoiT24JqQBzyPx7QSJhSzVEzcpgQ, listslice)
# def get_fucking_data(ReaesOJdPhkSbqVAKZHhmCEhrODblLXw, listslice)
# def get_fucking_data(SpZFySFjaK30dFGJ32o2TnvlVwR6ZPnu, listslice)
# ! NEED
