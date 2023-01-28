# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 23:44:30 2022

@author: Kaitlin

Objective: Building functions to find the storygraph for a given book title and 
scrape information about the book from the html
Compatible with the Storygraph ui update made January 2023
Will require further updates for every ui update until after Storygraph develops an API
"""

import requests
from bs4 import BeautifulSoup
import Levenshtein as leven 

def remove_author(book_name):
    search_pts = book_name.split(" (")
    book_name = search_pts[0]
    return book_name

def search_link(page, book_name): # Picks the most relevant result to return as the link
    #print(book_name)
    if book_name.find("(") > 0:
        book_name = remove_author(book_name)
    soup = BeautifulSoup(page.content, 'html.parser')
    link_containers = soup.find_all("h3", class_='font-bold text-base leading-5')
    if len(link_containers) == 0 :
        return "could not find the link :c"
    diff_rate = []
    for i in range(0,len(link_containers)): # Checks for the best title match on the first page
        a_tag = link_containers[i].find("a", href=True)
        title = a_tag.string.split(':') # To ignore subtitles, so it doesn't skip over the right book
        diff_rate.append(leven.distance(title[0], book_name))  
        #print(a_tag, leven.distance(title[0], book_name))  # For Debug               
    best_match = diff_rate.index(min(diff_rate))
    a_tag = link_containers[best_match].find("a", href=True)
    #print("Pick:", a_tag) # For Debug
    link = 'https://app.thestorygraph.com/' + a_tag['href']
    return link

def get_SGLink(book_name): # Brings you to the search page for the book
    book_name = str(book_name) # Converts to a string if all the inputs are numbers
    URL = 'https://app.thestorygraph.com/browse?search_term=' + book_name
    page = requests.get(URL)
    return search_link(page, book_name)

def get_genre(soup): # Grabs the book's listed genres and saves them in one string
    gclass = "inline-block text-xs sm:text-sm text-teal-700 dark:text-teal-200 mr-0.5 mt-1 border border-darkGrey dark:border-darkerGrey rounded-sm py-0.5 px-2"
    genre_containers = soup.find_all("span", class_=gclass)
    #print(genre_containers)
    genre = ""
    size_list = int(len(genre_containers)/2) # it's each genre and mood is listed twice, so it's half the length
    if size_list > 0:
        book_type = genre_containers[0].string
        for i in range(1,size_list):
            genre += genre_containers[i].string +", "
    else:
        book_type = ""
        genre = ""
    return book_type, genre

def get_mood(soup): # Grabs the book's listed moods and saves them in one string
    mclass = "inline-block text-xs sm:text-sm text-pink-500 dark:text-pink-200 mr-0.5 mt-1 border border-darkGrey dark:border-darkerGrey rounded-sm py-0.5 px-2"
    mood_containers = soup.find_all("span", class_=mclass)
    mood = ""
    size_list = int(len(mood_containers)/2) 
    for i in range(0,size_list):
        mood += mood_containers[i].string +", "   
    return mood

def get_pacing(soup): # Grabs the book's listed pacing and saves it in a string
    pclass = "inline-block text-xs sm:text-sm text-pink-500 dark:text-pink-200 border border-darkGrey dark:border-darkerGrey rounded-sm mt-1 py-0.5 px-2"
    pacing_container = soup.find("span", class_=pclass)
    if pacing_container is not None:
        pacing = pacing_container.string
    else:
        pacing = ""
    return pacing

def get_book_len(soup): # Grabs the book's listed page count if available
    lenclass = "text-xs min-[520px]:text-sm font-light text-darkestGrey dark:text-grey mt-1"
    book_len_container = soup.find("p", class_=lenclass)
    book_dets =[]
    for string in book_len_container.strings:
        dets = string
        dets = dets.split("\n")
        book_dets.append(dets)
    if book_dets != []:
        book_len = book_dets[0][1]
        book_len = book_len.replace("  ","")
        if book_len == "missing page info":
            book_len = ""
    else:
        book_len = ""
    return book_len

def get_book_date(soup): # Grabs the book's listed year published if available
    dclass = 'toggle-edition-info-link underline decoration-darkerGrey dark:decoration-lightGrey cursor-pointer hover:text-cyan-700 dark:hover:text-cyan-500 hover:decoration-cyan-700 dark:hover:decoration-cyan-500'
    book_date_container = soup.find("span", class_=dclass)
    book_dets = book_date_container.string
    book_dets = book_dets.split(" ")
    book_date = book_dets[2]
    if book_date == "info":
        book_date = ""
    return book_date

def get_author(soup): # Grabs the name of the author of the book
    aclass = "hover:text-cyan-700 dark:hover:text-cyan-500"
    author_container = soup.find("a", class_=aclass)
    author = author_container.string
    return author

def get_series(soup): # Checks if there's series information and returns the name as a string if available
    sclass = "font-semibold hover:text-cyan-700 dark:hover:text-cyan-500 text-lg"
    book_series_container = soup.find("p", class_=sclass)
    book_dets =[]
    if book_series_container is None:
        return ''
    for string in book_series_container.strings:
        dets = str(repr(string))
        dets = dets.replace("'","")
        book_dets.append(dets)
    return book_dets[0]


