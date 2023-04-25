from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scraped_data = []

def scrape():
    bright_star_table = soup.find("table",attrs = {"class","wikitable"})
    for row in table_rows:
        table_clos = row.find_all('td')
        print(table_cols)

        for col_data in table_cols:
            print(col_data.text)

            data = col_data.text.strip()
            print(data)

            temp_list.append(data)

        scraped_data.apped(temp_list)

    stars_data = []

    for i in range(0,len(scraped_data)):
        Stars_names = scraped_data[i][1]
        Distance = scraped_data[i][3]
        Mass = scraped_data[i][5]
        Radius = scraped_data[i][6]
        Lum = scraped_data[i][7]

        required_data = [ Stars_names,Distance,Mass,Radius,Lum]
        stars_data.append(required_data)

        

def scrape_more_data(hyperlink):
    try:
        new_stars_data = []
        page = requests.get(hyperlink)
        soup = BeautifulSoup(page.content,"html.parser")

        temp_list = []

        for tr_tag in soup.find_all("tr",attrs = {"class":"fact_row"}):
            td_tags = tr_tag.find_all("td")

            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div",attrs={"class":"value"})[0].contents[0])

                except:
                    temp_list.append("")
    
        new_stars_data.append(temp_list)

    except:
        time.sleep(1)
        scrape_more_data(hyperlink)

    for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            td_tags = ul_tag.find_all("td")
            temp_list = []
            for index, td_tag in enumerate(td_tags):
                if index == 0:
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("") 



headers = ['Star_name','distance','Mass','Radius','Luminosity']
        
star_df_1 =pd.DataFrame(stars_data,columns = headers)

star_df_1.to_csv('scraped_data.csv', index=True, index_label = 'id' )
