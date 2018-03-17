# -*- coding: utf-8 -*-

"""Main module."""
import requests
import re
from concert import Concert
import pprint
from bs4 import BeautifulSoup


class RedScare(object):
    def getToursPage(self):
        url = "http://www.redscare.net/site/tours/"

        response = requests.get(url)
        return response


    def parseTourPage(self):
        res = self.getToursPage()
        soup = BeautifulSoup(res.text, "html.parser")
        content = soup.find('div', id="content")
        relevantDetails = content.contents
        relevantDetails = list(filter(('\n').__ne__, relevantDetails))
        results = []
        for i in range(1, len(relevantDetails) - 4, 2):
            artistDetails = self.getConcertsByArtist(relevantDetails[i], relevantDetails[i + 1])
            results = results + artistDetails
        return results


    def getConcertsByArtist(self, artistEl, detailsEl):
        results = []
        artist = artistEl.text.strip()
        caliShows = detailsEl.find_all("td", string=re.compile('CA$'))
        for show in caliShows:
            venue = show.next_sibling.next_sibling.string.strip()
            date = show.previous_sibling.previous_sibling.string.strip()
            results.append(Concert(artist, venue, date))

        return results
