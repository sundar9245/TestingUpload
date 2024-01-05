# Get the database using the method we defined in pymongo_test_insert file
from python_get_db import get_database
dbname = get_database()
collection_name = dbname["web_gallery_list"].web_items


def insert(**kwargs):
    collection_name.insert_one(kwargs)
    

web_details_3 = {
  "_id" : "E_web1",
  "web_name" : "World Bank Open Data",
  "hyper_link" : "https://data.worldbank.org/",
  "rating" : 5,
  "category" : "Economic",
  "web_description": "Datasets covering population demographics and a huge number of economic and development indicators from across the world.",
  "image": "1.jpg"
  }

web_details_4 = {

  "_id" : "E_web2",
  "web_name" : "IMF Data",
  "category" : "Economic",
  "rating" : 5,
  "hyper_link" : "https://www.imf.org/en/Data",
  "web_description" : "The International Monetary Fund publishes data on international finances, debt rates, foreign exchange reserves, commodity prices and investments.",
  "image": "2.jpg"
    }

web_details_5 = {
  "_id" : "E_web3",
  "web_name" : "Financial Times Market Data",
  "category" : "Economic",
  "rating" : 5,
  "hyper_link" : "https://markets.ft.com/data/",
  "web_description" : "Up to date information on financial markets from around the world, including stock price indexes, commodities and foreign exchange.", 
  "image": "3.jpg"
  } 

web_details_6 = {
  "_id": "E_web4",
  "web_name": "Moneycontrol",
  "hyper_link": "https://www.moneycontrol.com",
  "rating": 5,
  "category": "Economic",
  "web_description": "moneycontrol.com today gets over 17 million visitors every month across all its platforms-web, mobile and tablets that makes it the largest online financial platform in India",
  "image": "4.jpg"
}

web_details_7 = {
  "_id": "E_web5",
  "web_name": "NSE India",
  "category": "Economic",
  "rating": 5,
  "hyper_link": "https://www.nseindia.com",
  "web_description": "National Stock Exchange of India Limited is the leading stock exchange under the ownership of various group of domestic and global financial institutions, public and privately owned entities and individuals. It is located in Mumbai, Maharashtra",
  "image": "5.jpg"
}



collection_name.insert_many([web_details_3, web_details_4, web_details_5, web_details_6, web_details_7])
