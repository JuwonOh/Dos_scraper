import re
import time
from .utils import get_soup

def get_latest_allnews(last_date, sleep=1.0):
    """
    Artuments
    ---------
    last_date : Date
    sleep : float
        Sleep time. Default 1.0 sec
    """

    raise NotImplemented

patterns_transcript = [
    re.compile('https://www.state.gov/[\w]+')]
base_url = 'https://www.state.gov/r/pa/prs/ps/{}/index.htm'

def get_allnews_urls(begin_year=2018, end_year=2019, verbose=True):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """

    links_all = []
    for year in range(begin_year, end_year):
        url = base_url.format(year)
        soup = get_soup(url)
        sub_links = soup.find('div', class_= 'l-wrap')
        for link in sub_links.find_all("a"):
            if 'href' in link.attrs:
                 links_all += [link.attrs['href']]
        if verbose:
            print('get briefing statement urls {} / {}'.format(begin_year, end_year))

    links_all = ['https://www.state.gov' + i for i in links_all]

    return links_all

def get_last_page_num():
    """
    Returns
    -------
    page : int
        Last page number.
        eg: 503 in 'https://dod.defense.gov/News/Transcripts/?Page=62'
    """
    raise NotImplemented
