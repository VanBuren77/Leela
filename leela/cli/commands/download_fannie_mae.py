from http.client import HTTPSConnection
from base64 import b64encode
from leela.config import config
import requests




def download_fannie_mae(year, quarter):
    import requests
    import json

    headers = {
        'accept': 'application/json',
        'Authorization': f'{config.FANNIE_MAE_AUTH_TOKEN}'
    }
    URL = fr"https://api.theexchange.fanniemae.com/v1/sf-loan-performance-data/years/{year}/quarters/{quarter}"
    print("Querying...", URL)
    response = requests.get(URL, headers=headers)
    print(response.content)
    s3uri_path = json.loads(response.content)["lphResponse"][0]["s3Uri"]
    print()
    print(s3uri_path)
    print()
    temp = json.loads(s3uri_path)["lphResponse"][0]["s3Uri"]
    import urllib.request
    zip_file_name = f"{year}{quarter}.zip"
    print("Downloading...", zip_file_name)
    urllib.request.urlretrieve(temp, f"C:\Projects\GitHub\Leela\data\Fannie\zips\\" + zip_file_name)
    