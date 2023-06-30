import requests
import json
from etext import send_sms_via_email
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()


def get_tao_data():

    res = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bittensor&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true').text
    price_object = json.loads(res)
    price = format(float(price_object["bittensor"]["usd"]), '.2f')
    volume = '{:,.2f}'.format(float(price_object["bittensor"]["usd_24h_vol"]))
    delta = format(float(price_object["bittensor"]["usd_24h_change"]), '.2f')

    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S")

    print(dt_string, price, volume, delta)

    return [dt_string, price, volume, delta]


results_array = get_tao_data()

phone_number = "970-644-7506"
message = f"Bittensor is currently trading at ${results_array[1]}, with a volume of ${results_array[2]}, and a 24-hour change of ${results_array[3]}"
provider = "T-Mobile"

# Get Credentials
email = os.environ.get("SENDER_EMAIL")
password = os.environ.get("SENDER_PASSWORD")
sender_credentials = (email, password)

send_sms_via_email(
    phone_number, message, provider, sender_credentials, subject=f"Bittensor Daily Update {results_array[0]}"
)








