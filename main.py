from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import time


pages=int(input("Enter the page number till which you want to view the internships[More than 1]:"))

for i in range(1,pages):
    


    pages_str=str(pages)

    
    link="https://internshala.com/internships/page-"+pages_str

    response=requests.get(link)
    #print(response)

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
    
    print(no_of_pages.text) 