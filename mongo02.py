from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import DataFrame
import time
import pymongo as mongo
import json

client = mongo.MongoClient("mongodb://127.0.0.1:27017/")

# make db for bitcoin
bitcoin_db = client["Bitcoin"]
 
# make collection
col_highest = bitcoin_db["amounts"]

def Scrape():
    page = requests.get('https://www.blockchain.com/btc/unconfirmed-transactions')
    soup = BeautifulSoup(page.text, 'html.parser')

    df = pd.DataFrame()
    #df = pd.DataFrame(columns=['Hash','Time','Amount (BTC)','Amount (USD)'])   

    for transaction in soup.find_all('div', class_='sc-20ch6p-0 beTSoK'):
        for article in transaction.find_all('div', class_='sc-1g6z4xm-0 hXyplo'):
            hash = article.a.text
            for times in article.find_all('div', class_='sc-1au2w4e-0 emaUuf'):
                hour = times.find('span', class_='sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC').text
                amounts = article.find_all('div', class_='sc-1au2w4e-0 fTyXWG')
                amountBTC = amounts[0].text
                amountBTC = amountBTC.split(')')[1]
                amountUSD = amounts[1].text
                amountUSD = amountUSD.split(')')[1]


                df2 = pd.DataFrame([hash, hour, amountBTC, amountUSD])
                df2 = df2.transpose()

                df = df.append(df2)

    #print(df)

    for i in df[3]:
        df[3] = df[3].replace("$","").replace(",","")
    df[3] = [item.replace("$","").replace(",","") for item in df[3]]
    df[3] = df[3].astype(float)

    max_result = df[3].max()

    with open('result.json', 'w') as json_file:
        json.dump(max_result, json_file)

    with open('result.json', 'r') as result_file:
        file_result = json.load(result_file)
        x = col_highest.insert_one(file_result)

Scrape()

