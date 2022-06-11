import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('--year', type=int, required=True)
parser.add_argument('--month', type=int, required=True)
args = parser.parse_args()

year = args.year
month = args.month

url = 'http://0.0.0.0:8080'

body = {'year': year, 'month': month}

r = requests.post(url, json=body)

if r.status_code == 200:
    body = r.json()
    prediction = float(body['prediction'])
    print(prediction)
else:
    print('Error:', r.status_code)