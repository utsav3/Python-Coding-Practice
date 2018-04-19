""" This module defines functions for searching for information
about countries listed in the CIA World Factbook. """
import requests
import re
import sys

keywords = {"Area": "Area", "Population": "Population", "Capital": "Capital", "Languages": "Languages", "Currency": "Exchange rates"}
url = "https://www.cia.gov/library/publications/the-world-factbook/"

def get_info(search_term):
    """ The initial function called to start a searching process. Takes a 
    search term as an argument and checks to see whether the term is an
    attribute (e.g. Population) or a country. If it is an attribute,
    a dictionary mapping every country to its data for that attribute is 
    returned. If the search term is a country, a dictionary mapping
    a pre-selected set of attributes to the data for that country is 
    returned. 
    :param search_term: country or keyword request.  
    :type search_term: str.
    :returns: Dict. or None.
    :raises: None.
    """
    main_page = requests.get(url)
    if search_term in keywords:
        return dict(get_keyword(search_term, main_page))
    else:
        link = re.search(r'<option value="([^>]+)"> ' + search_term.capitalize() + ' </option>', main_page.text)
        if link:
            country_page = requests.get(url+link.group(1))
            return dict(get_country(country_page))
        else:
            return None
            
def get_keyword(search_term, main_page):
    """ Returns the data associated to the keyword 
    for each country as a list of tuple pairs. 
    :param search_term: keyword request.  
    :type search_term: str.
    :param main_page: the main Factbook page.
    :type main_page: Response obj.
    :returns: List of tuple pairs.
    :raises: None.
    """
    results = []
    keyword = keywords[search_term]
    link_pairs = re.findall(r'<option value="([^>]+)"> (.*?) </option>', main_page.text)
    for link, country in link_pairs:
        country_page = requests.get(url+link)
        data = get_country_by_keyword(country_page, keyword)
        results.append((country, data))
    return results

def get_country(country_page):
    """ Returns the data for the country as a list of tuple pairs. 
    :param country_page: The country's page on the Factbook.  
    :type country_page: Response obj.
    :returns: List of tuple pairs.
    :raises: None.
    """
    results = []    
    for keyword in keywords.values():
        data = get_country_by_keyword(country_page, keyword)     
        if data:
            results.append((keyword,data))
    return results

def get_country_by_keyword(country_page, keyword):
    """ Returns the data associated to the keyword 
    for the specific country. 
    :param country_page: The country's page on the Factbook.  
    :type country_page: Response obj.
    :param search_term: keyword request.  
    :type search_term: str.
    :returns: str.
    :raises: None.
    """
    if keyword == "Area" or keyword == "Capital":
        data = re.search(keyword + r":.*?<span class=category_data>(.+?)</span>", country_page.text, re.S)
        if data:
            return data.group(1)   
    elif keyword == "Exchange rates":
        data = re.search(keyword + r":.*?<div class=category_data>(.+?)</div>\n<div class=category_data>(.+?)</div>", country_page.text, re.S)
        if data:
            return data.group(1).rstrip(" -") + ": " + data.group(2)
    else:
        data = re.search(keyword + r":.*?<div class=category_data>(.+?)</div>", country_page.text, re.S)
        if data:
            return data.group(1)
    return None

   
if __name__ == "__main__":
    search_term = raw_input("Please enter a country or keyword: ")
    results = get_info(search_term)
    for key, value in results.items():
        print(key, ": ", value, sep="")
