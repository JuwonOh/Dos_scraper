import re
from .utils import get_soup
from .utils import now

def parse_page(url):
    """
    Argument
    --------
    url : str
        Web page url

    Returns
    -------
    json_object : dict
        JSON format web page contents
        It consists with
            title : article title
            time : article written time
            content : text with line separator \\n
            url : web page url
            scrap_time : scrapped time
    """

    try:
        soup = get_soup(url)
        title = soup.find('h2', class_= 'title left').text
        time = soup.find('div', id= 'date_long').text
        content = soup.find('div', id = 'centerblock').text

        json_object = {
            'title' : title,
            'time' : time,
            'content' : content,
            'url' : url,
            'scrap_time' : now()
        }
        return json_object
    except Exception as e:
        print(e)
        print('Parsing error from {}'.format(url))
        return None
