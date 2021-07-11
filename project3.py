#Project3: Web Scraper using BeautifulSoup4, request, SQL and Databases
#Web Scrapper code:
import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect

oyo_url="https://www.oyorooms.com/hotels-in-bangalore/?page="
parser=argparse.ArgumentParser()

parser.add_argument("--page_num_max",help="Enter the number of pages to parse",type=int)
parser.add_argument("--dbname",help="Enter the number of pages to parse",type=str)

args=parser.parse_args()
page_num_max=args.page_num_max

scrapped_info_List=[]
connect.connect(args.dbname)

for page_num in range(1,page_num_max):
    url=oyo_url+str(page_num)
    print("GET Request for: " + url)
    req=requests.get(url)
    content=req.content

    print(content)

    soup=BeautifulSoup(content,"html.parser")

    all_hotels=soup.find_all("div",{"class":"hotelCardListing"})

    for hotel in all_hotels:
        hotel_dict={}
        hotel_dict["name"]=hotel.find("h3",{"class":"listingHotelDescription__hotelName"}).text
        hotel_dict["address"]=hotel.find("span",{"itemprop":"streetAddress"}).text
        hotel_dict["price"]=hotel.find("span",{"class":"listingPrice__finalPrice"}).text
    #try....except
        try:
            hotel_dict["rating"]=hotel.find("span",{"class":"hotelRating__ratingSummary"}).text
        except AttributeError:
            hotel_dict["rating"]=None

        parent_amenity_elements=hotel.find("div",{"class":"amenityWrapper"})
        amenities_list=[]
        for amenity in parent_amenity_elements.find_all("div",{"class":"amenityWrapper__amenity"}):
            amenities_list.append(amenity.find("span",{"class":"d-body-smd"}).text.strip())

        hotel_dict["amenities"]=", ".join(amenities_list[:-1])

        scrapped_info_List.append(hotel_dict)
        connect.insert_into_table(args.dbname,tup(hotel_dict.values()))

        #print(hotel_name,hotel_address,hotel_price,hotel_rating)

dataFrame = pandas.DataFrame(scrapped_info_List)
print("Creating csv file...")
dataFrame.to_csv("Oyo.csv")
connect.get_hotel_info(args.dbname)



#Code for creating Database using SQL:
#using databases to create a table and adding info into db
#using sql (Structured Query Language)
#pip install db-sqlite3
import sqlite3

def connect(dbname):
    conn=sqlite3.connect(dbname)

    conn.execute("CREATE TABLE IF NOT EXISTS OYO_HOTELS (NAME TEXT, ADDRESS TEXT, PRICE INT, AMENITIES TEXT, RATING TEXT)")

    print("Table created successfully")

    conn.close()

def insert_into_table(dbname, values):
    conn=sqlite3.connect(dbname)
    print("Inserted into table"+ str(values))
    insert_sql="INSERT INTO OYO_HOTELS (NAME, ADDRESS, PRICE, AMENITIES, RATING) VALUES (?, ?, ?, ?, ?)"

    conn.execute(insert_sql,values)

    conn.commit()
    conn.close()

def get_hotel_info(dbname):
    conn=sqlite3.connect(dbname)

    cur=conn.cursor()

    cur.execute("SELECT * FROM OYO_HOTELS")

    table_data=cur.fetchall()

    for record in table_data:
        print(record)

    conn.close()
