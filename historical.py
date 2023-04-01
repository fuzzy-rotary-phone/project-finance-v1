from kiteconnect import KiteConnect
import logging
import utils

API_KEY = "cdvy8c1vojniuz8c"
API_SECRET = "hc63ujjkpvyl6c16sey1qknsggr188hh"
ACCESS_TOKEN = "rtYzHqS2uZYdWxESNUArn753oJkf5Qsg"

logging.basicConfig(level=logging.DEBUG)

kite = KiteConnect(api_key=API_KEY)
kite.set_access_token(ACCESS_TOKEN)

NIFTY_50_TOKEN = 256265
FROM_DATE = '2023-01-01'
TO_DATE = '2023-03-28'

for single_date in utils.daterange(FROM_DATE, TO_DATE):
	n50 = kite.historical_data(NIFTY_50_TOKEN, single_date, single_date, 'day')
	nifty_price = n50[0]['open']
	opt_price = int(round(nifty_price, -2))
	opt_expiry = single_date + datetime.timedelta((3 - today.weekday()) % 7)
	tradingsymbol = 'NIFTY23' + str(d.month) + f'{d.day:02d}' + str(opt_price) + 'CE'
	

	
kite.historical_data(NIFTY_50_TOKEN, '2023-03-28', '2023-03-28', 'day', True, True)
