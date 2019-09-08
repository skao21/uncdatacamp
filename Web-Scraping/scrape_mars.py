#  import
from bs4 import BeautifulSoup
from splinter import Browser
from pprint import pprint
import pymongo
import numpy as np
import pandas as pd
import requests
from flask import Flask, render_template
import time
import json
from selenium import webdriver

def scrape_all_sites():
    colloctions = {}

    exec_path = {"executable_path": "Resources/chromedriver.exe"}
    browser = Browser("chrome", **exec_path, headless=False)
    browser.visit('https://mars.nasa.gov/news/')
    news_html = browser.html
    news_soup = BeautifulSoup(news_html, 'html.parser')

    # pull titles from website
    title = news_soup.find('div', class_="content_title").text
    colloctions["news_title"] = title

    # pull body from website
    body = news_soup.find('div', class_="rollover_description").text
    colloctions["news_snip"] = body

    ### JPL Mars Space Images - Featured Image
    browser.visit("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars")
    browser.click_link_by_partial_text('FULL IMAGE')
    jpl_html = browser.html
    jpl_soup = BeautifulSoup(jpl_html, 'html.parser')
    img_path = jpl_soup.find('img', class_='thumb')['src']
    featured_image_url = f'https://www.jpl.nasa.gov{img_path}'
    colloctions["featured_image_url"] = featured_image_url


    ### Mars Weather
    browser.visit('https://twitter.com/marswxreport?lang=en')
    weather_soup = BeautifulSoup(browser.html, 'html.parser')
    mars_weather = weather_soup.find('p', class_="tweet-text").text
    colloctions["mars_weather"] = mars_weather


    ### Mars Facts
    table = pd.read_html("https://space-facts.com/mars/")
    table[0].columns = ["Facts", "ValueM", 'ValueE']
    df = table[0].set_index("Facts")
    # Convert DataFrame to HTML and save the file
    facts_html = df.to_html().replace("\n","")
    colloctions["fact_table"] = facts_html

    ## Mars Hemispheres
    # collect urls
    urls_dict = { 'Cerberus Hemispheres'    : 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced',
                'Schiaparelli Hemisphere' : 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced',
                'Syrtis Hemisphere'       : 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced',
                'Valles Marineris Hemisphere' : 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'}
    # get beautiful soup from url
    soups_dict = {}
    for key, url in urls_dict.items():
        browser.visit(url)
        soups_dict[key] = BeautifulSoup(browser.html, 'html.parser')
    # scrapping image
    imgs_dict = { key: soup.find_all('div', class_="wide-image-wrapper")   for key, soup in soups_dict.items()}
    hemisphere_image_urls = []
    for key, imgs in imgs_dict.items():
        hemisphere_image_url = {}
        title = soups_dict[key].find('h2', class_='title').text
        hemisphere_image_url['title'] = title
        full_img_url = ''
        for img in imgs:
            pic = img.find('li')
            full_img_url = pic.find('a')['href']
        hemisphere_image_url['img_url'] = full_img_url
        hemisphere_image_urls.append(hemisphere_image_url)

    colloctions["hemisphere_image"] = hemisphere_image_urls
    return colloctions

if __name__ == "__main__":
    
    # If run from shell
    print (scrape_all_sites())