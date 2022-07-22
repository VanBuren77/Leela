from http.client import HTTPSConnection
from base64 import b64encode
from leela.config import config
import requests




def download_fannie_mae(year, quarter):

    # This sets up the https connection
    # we need to base 64 encode it
    # and then decode it to acsii as python 3 stores it as a byte string
    # URL = fr"//api.theexchange.fanniemae.com/v1/sf-loan-performance-data/years/{year}/quarters/{quarter}"
    # URL = r"api.theexchange.fanniemae.com/v1/sf-loan-performance-data/primary-dataset"
    # userAndPass = b64encode(f"{login}:{pw}".encode('utf-8')).decode("ascii")
    
    # URL = fr"https://api.theexchange.fanniemae.com/v1/sf-loan-performance-data/years/{year}/quarters/{quarter}"
    # # payload = { 'Authorization' : config.FANNIE_MAE_AUTH_TOKEN}
    # headers = { 'Authorization' : config.FANNIE_MAE_AUTH_TOKEN,
    #              'accept' : 'application/json'
    #              }
    # # print(config.FANNIE_MAE_AUTH_TOKEN)
    # # headers = {}
    # # res = requests.post(URL, headers=headers)
    # res = requests.get(URL, headers=headers)
    # print(res)

    # import requests

    # headers = {
    #     'accept': 'application/json',
    #     'Authorization': 'Basic ' + b64encode(f"{config.FANNIE_MAE_LOGIN}:{config.FANNIE_MAE_PW}".encode('utf-8')).decode("ascii")
    # }

    # response = requests.get('https://api.theexchange.fanniemae.com/v1/sf-loan-performance-data/primary-dataset', headers=headers)
    # print(response)


    from http.client import HTTPSConnection
    from base64 import b64encode
    # This sets up the https connection
    # c = HTTPSConnection("www.thisisanexample.com")
    c = HTTPSConnection(r"www.api.theexchange.fanniemae.com/v1/sf-loan-performance-data/primary-dataset")
    # we need to base 64 encode it
    # and then decode it to acsii as python 3 stores it as a byte string
    userAndPass = b64encode((config.FANNIE_MAE_LOGIN + ":" + config.FANNIE_MAE_PW).encode('ascii')).decode("ascii")
    headers = { 'Authorization' : 'Basic %s' %  userAndPass }
    #then connect
    res = c.request('GET', '/', headers=headers)
    print(res)

    # print()
    # print("Connecting...")
    # print()
    # print(URL)
    # print()
    
