#Project2: Web Scraper using BeautifulSoup4 and requests
#Simple Web Scrapper without using SQL and Databases
import requests
from bs4 import BeautifulSoup
import pandas
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("--page_num_max",help="Enter the number of pages to parse",type=int)
args=parser.parse_args()

oyo_url="https://www.oyorooms.com/hotels-in-bangalore/?page="
page_num_max=args.page_num_max

scrapped_info_List=[]

for page_num in range(1,page_num_max):

    req=requests.get(oyo_url+str(page_num))
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
            pass

        parent_amenity_elements=hotel.find("div",{"class":"amenityWrapper"})
        amenities_list=[]
        for amenity in parent_amenity_elements.find_all("div",{"class":"amenityWrapper__amenity"}):
            amenities_list.append(amenity.find("span",{"class":"d-body-smd"}).text.strip())

        hotel_dict["amenities"]=", ".join(amenities_list[:-1])

        scrapped_info_List.append(hotel_dict)

        #print(hotel_name,hotel_address,hotel_price,hotel_rating)

dataFrame = pandas.DataFrame(scrapped_info_List)
dataFrame.to_csv("Oyo.csv")
