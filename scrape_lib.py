import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from scrapy.selector import Selector
import re
import time
import csv
from itertools import islice


'''Connects to the specified page using Selenium with the Headless Optionself.

page : Starting Webpage desired to connect to.
headless : True will no cause the Chrome drive to general physical webpages locallyself. False will cause the Chrome drive to render physical webpages.
True will be quicker, False allows transparency to make sure things are running as planned.
'''

def connect_to_page(page,  headless=True):
    if headless:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome('./driver/chromedriver', chrome_options=options)
    else:
        driver = webdriver.Chrome('./driver/chromedriver')
    driver.get(page)

    return driver

'''Function utilizing the connect_to_page function that connects to https://totalwine.com and uses selenium to automatically click the
popup buttons such as "are you over 21", after that it will extract all the URLs from the number of pages desired to go through.
I use the max number of options I can browse and divide by 180 to get the number of pages to go through.  '''


def get_liquor_list(url, num_pages = 1, head_less = True):
    # get the driver going
    driver = connect_to_page(url, headless=head_less)
    time.sleep(1)
    load = False
    # Total wine appears to have two different options that ask for age
    while load == False:
        try:
            # Option 1 : Red Button
            red_age = '//*[@id="btnYes"]'
            driver.find_element_by_xpath(red_age).click()
            load = True
        except:
            pass

        try:
            # Option 2 : Blue Button
            blue_age = '/html/body/div[2]/div/div[2]/div[3]/div/button[2]'
            driver.find_element_by_xpath(blue_age).click()
            load = True
        except:
            pass

        time.sleep(0.5)

        # if it prompts for online or instore via popup.
    try:
        shop_button = '/html/body/header/div[3]/div/div[1]'
        driver.find_element_by_xpath(shop_button).click()

    except:
        pass

    # Now that all the page buttons have been solved, we can extract the URLs for each of the pages.
    # extract page to disect
    page = BeautifulSoup(driver.page_source, 'lxml')

    liquor_urls = []
    bottles = page.find('ul',{'class':'plp-list'})

    for bottle in bottles.find_all('li'):
        liquor_urls.append('https://www.totalwine.com'+bottle.find('a')['href'])


    # if we need to go to additional pages.
    if num_pages > 1:
        for page in range(2,num_pages+1):
            page_add = url+'&page='+str(page)
            driver.get(page_add)
            page = BeautifulSoup(driver.page_source, 'lxml')
            bottles = page.find('ul',{'class':'plp-list'})

            for bottle in bottles.find_all('li'):
                liquor_urls.append('https://www.totalwine.com'+bottle.find('a')['href'])
            time.sleep(2)

    # End driver and return URLs list.
    driver.quit()
    return liquor_urls
