import logging
import json
from kiteconnect import KiteConnect
from datetime import datetime
from datetime import date
from datetime import timedelta
import calendar
from pymongo import MongoClient

API_KEY = "cdvy8c1vojniuz8c"
API_SECRET = "hc63ujjkpvyl6c16sey1qknsggr188hh"
ACCESS_TOKEN = "NomlVMX7H5NpeYJO5XVN7aU1UmTGFb99"

logging.basicConfig(level=logging.DEBUG)

kite = KiteConnect(api_key=API_KEY)

# Redirect the user to the login url obtained
# from kite.login_url(), and receive the request_token
# from the registered redirect url after the login flow.
# Once you have the request_token, obtain the access_token
# as follows.

# data = kite.generate_session("request_token_here", api_secret=API_SECRET)
# kite.set_access_token(data["access_token"])
kite.set_access_token(ACCESS_TOKEN)

NIFTY_50_TOKEN = 256265
today = date.today()
DAY_FORMAT = 'YYYY-MM-DD'
TODAY_DAY_FORMAT = utils.convert_datetime_to_string(today, DAY_FORMAT)

n50 = kite.historical_data(NIFTY_50_TOKEN, TODAY_DAY_FORMAT, TODAY_DAY_FORMAT, 'day')
nifty_price = n50[0]['open']
opt_price = int(round(nifty_price, -2))
opt_expiry = today + datetime.timedelta((3 - today.weekday()) % 7)
month = calendar.monthcalendar(today.year, today.month)
last_thursday = max(month[-1][calendar.THURSDAY], month[-2][calendar.THURSDAY])

if opt_expiry.day == last_thursday:
    tradingsymbolcall = 'NIFTY23' + opt_expiry.strftime('%b').upper() + str(opt_price) + 'CE'
    tradingsymbolput = 'NIFTY23' + opt_expiry.strftime('%b').upper() + str(opt_price) + 'PE'
else:
    tradingsymbolcall = 'NIFTY23' + str(today.month) + f'{today.day:02d}' + str(opt_price) + 'CE'
    tradingsymbolput = 'NIFTY23' + str(today.month) + f'{today.day:02d}' + str(opt_price) + 'PE'

l = kite.instruments()
calltoken = [i['instrument_token'] for i in fl if i['tradingsymbol'] == tradingsymbolcall][0]
puttoken = [i['instrument_token'] for i in fl if i['tradingsymbol'] == tradingsymbolput][0]

calltokendata = kite.historical_data(calltoken, TODAY_DAY_FORMAT, TODAY_DAY_FORMAT, 'min', True, True)
puttokendata = kite.historical_data(puttoken, TODAY_DAY_FORMAT, TODAY_DAY_FORMAT, 'min', True, True)

data = []
for d in calltokendata:
    d['symbol'] = tradingsymbolcall
    data.append(d)
for d in puttokendata:
    d['symbol'] = tradingsymbolput
    data.append(d)    

client = MongoClient()
db = client.kite
options = db.options

options.insert_many(data)

client.close()

# Place an order
# try:
#     order_id = kite.place_order(tradingsymbol="INFY",
#                                 exchange=kite.EXCHANGE_NSE,
#                                 transaction_type=kite.TRANSACTION_TYPE_BUY,
#                                 quantity=1,
#                                 variety=kite.VARIETY_AMO,
#                                 order_type=kite.ORDER_TYPE_MARKET,
#                                 product=kite.PRODUCT_CNC,
#                                 validity=kite.VALIDITY_DAY)

#     logging.info("Order placed. ID is: {}".format(order_id))
# except Exception as e:
#     logging.info("Order placement failed: {}".format(e.message))

# # Fetch all orders
# kite.orders()

# # Get instruments
# kite.instruments()

# print(json.dumps(data_MOM_desc_on_exchange[:MOM_LIMIT], default=str, indent=0))