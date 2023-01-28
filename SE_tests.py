# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 12:02:58 2023

@author: Kaitlin

Runs test cases for the 
"""


import requests
from bs4 import BeautifulSoup
import Storygraph_Extraction_v3 as SE

def check_book_details(book):
    print("input: ",book)
    link = SE.get_SGLink(book)
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(link)

    book_type, genre = SE.get_genre(soup)
    print(book_type,genre)
    mood = SE.get_mood(soup)
    print(mood)
    pacing = SE.get_pacing(soup)
    print(pacing)
    book_len = SE.get_book_len(soup)
    print(book_len)

    book_date = SE.get_book_date(soup)
    print(book_date)

    author = SE.get_author(soup)
    print(author)
    series = SE.get_series(soup)
    print(series)
    return



# This block is a test case for the functions in the imported file

book1 = "book" # random novel essentially it happens to pull Book Lovers as of Jan 2023
book2 = "The Calculating Stars" # Specific novel in a series
book3 = "Artemis (Andy Weir)"
book4 = "Impostors (Scott Westerfeld)"
book5 = "The Hobbit, or There and Back Again" # Have to put the full book name unless there's a subtitle with a colon
book6 = "Impostors 1" # Proves it doesn't break with some of the details missing
book7 = "Bad Advice"


check_book_details(book1)
check_book_details(book2)
check_book_details(book3)
check_book_details(book4)
check_book_details(book5)
check_book_details(book6)
check_book_details(book7)
