from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import time
from places import places





def scrape_with_location(place_array):

    for i in range(1,pages+1):
        pages_str=str(i)
        print(placess[place_array])
        link="https://internshala.com/internships/internship-in-"+placess[place_array]+"/page-"+pages_str
        print(link)
        response=requests.get(link)
        company_names=[]
        profiles=[]
        locations=[]
        startdates=[]
        stipends=[]
        
        soup=BeautifulSoup(response.text,'html.parser')
        no_of_pages=soup.find('span',id='total_pages')
        for company_name in soup.find_all('a',class_="link_display_like_text"):
            #print(company_name.text)
            company_names.append(company_name.text.replace(" ",""))


        for profile in soup.find_all('div',class_="profile"):
            #print(company_name.text)
            profiles.append(profile.text.replace(" ",""))

        for location in soup.find_all('a',class_="location_link"):
            #print(company_name.text)
            locations.append(location.text.replace(" ",""))

        for start_date in soup.find_all('span',class_="start_immediately_desktop"):
            #print(company_name.text)
            startdates.append(start_date.text.replace(" ",""))

        for stipend in soup.find_all('span',class_="stipend"):
            #print(company_name.text)
            stipends.append(stipend.text.replace(" ",""))

        

        for name,profile,location,startdate,stipend in zip(company_names,profiles,locations,startdates,stipends):
            print("Name",name)
            print("Profile",profile)
            print("Location:",location)
            print("StartDate:",startdate)
            print("Stipends:",stipend)
            print("\n")
        


def scrape_normal_pages():
    for i in range(1,pages+1):
        pages_str=str(i)
        link="https://internshala.com/internships/page-"+pages_str
        response=requests.get(link)
        company_names=[]
        profiles=[]
        locations=[]
        startdates=[]
        stipends=[]
        
        soup=BeautifulSoup(response.text,'html.parser')
        no_of_pages=soup.find('span',id='total_pages')
        for company_name in soup.find_all('a',class_="link_display_like_text"):
            #print(company_name.text)
            company_names.append(company_name.text.replace(" ",""))


        for profile in soup.find_all('div',class_="profile"):
            #print(company_name.text)
            profiles.append(profile.text.replace(" ",""))

        for location in soup.find_all('a',class_="location_link"):
            #print(company_name.text)
            locations.append(location.text.replace(" ",""))

        for start_date in soup.find_all('span',class_="start_immediately_desktop"):
            #print(company_name.text)
            startdates.append(start_date.text.replace(" ",""))

        for stipend in soup.find_all('span',class_="stipend"):
            #print(company_name.text)
            stipends.append(stipend.text.replace(" ",""))

        

        for name,profile,location,startdate,stipend in zip(company_names,profiles,locations,startdates,stipends):
            print("Name",name)
            print("Profile",profile)
            print("Location:",location)
            print("StartDate:",startdate)
            print("Stipends:",stipend)
            print("\n")
        






choice=int(input("Enter 1)For specific place internship \n 2)For all places"))
placess=[]
if(choice==1):
    places_available=BeautifulSoup(places,'html.parser')
    print("Please choose from the given places")
    for place in places_available.findAll('li',class_="active-result"):
        placess.append(place.text.replace(" ",""))
    for i in range(0,len(placess)):
        print(i,placess[i])
    array_pos=int(input("Enter the number:"))
    
    pages=int(input("Enter the page number till which you want to view the internships[More than 1]:"))
    scrape_with_location(array_pos)
else:
    pages=int(input("Enter the page number till which you want to view the internships[More than 1]:"))
    places_available=BeautifulSoup(places,'html.parser')    
    scrape_normal_pages()






