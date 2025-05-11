

# -*- coding: utf-8 -*-
"""
File importing S&P 500 index from scraping


"""
#%% Import requests
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import time
from selenium import webdriver

#%%
# Get the base url
path ="https://www.slickcharts.com/sp500"

#%%
    
# Set up Selenium WebDriver (Make sure to have the correct WebDriver installed)
driver = webdriver.Chrome()  # Or use another browser driver
driver.get(path)  # Replace with the actual URL

    # Wait for JavaScript to load (optional, based on the site's speed)

time.sleep(5)

    # Get the rendered HTML and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

ConstTable = soup.find("table", class_ = "table table-hover table-borderless table-sm")

#%%
print(ConstTable)

#%%     
# Loop through each row in the table body
rows = ConstTable.find_all('tr')

# Find the stat name and the associated value
data = []
for row in rows:
   cols = row.find_all('td')
   if len(cols) == 7:
            index = cols[0].text.strip()
            company_name = cols[1].text.strip()
            symbol = cols[2].text.strip()
            weight = cols[3].text.strip()
            price = cols[4].text.strip().split()[-1]  # last part after the image
            change = cols[5].text.strip()
            percent_change = cols[6].text.strip()
            # Append the data to the list
            data.append([index, company_name, symbol, weight, price, change, percent_change])
# Create a DataFrame
columns = ["Index", "Company", "Symbol", "Weight", "Price", "Change", "Percent Change"]
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv("D:/Financial_trading/Training/algorithmic_trading_python/data/S_P_500.csv", index=False)

print("Data has been written to S_P_500.csv")
