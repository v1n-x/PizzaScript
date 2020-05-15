# -file- PARSEHTML.py
from bs4 import BeautifulSoup


def grabAccurateAddressHREF(raw_html) :
    # Find indexes to slice off useless information
    startingIndex = raw_html.find("<a class=\"store-result btn next\"")
    finalIndex = raw_html.find("onclick=\"addressSelectEvent\"")
    htmlstring = raw_html[startingIndex:finalIndex]

    return htmlstring

def parseAddressHREF(raw_html):
    address = BeautifulSoup(grabAccurateAddressHREF(raw_html), 'html.parser')
    link = address.find('a')

    return link.get('href')
