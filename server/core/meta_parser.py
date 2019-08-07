import requests
from bs4 import BeautifulSoup


def parse_meta_data(url):
    html_doc = requests.get(url)

    if html_doc.status_code != 200:
        headers = {'User-Agent': '*', 'Disallow': ''}
        html_doc = requests.get(url, headers=headers)

    soup = BeautifulSoup(html_doc.text, 'html.parser')

    title = soup.find_all("meta", {"property": "og:title"})

    if not title:
        title = soup.find_all("meta", {"name": "twitter:title"})

    description = soup.find_all("meta", {"property": "og:description"})

    if not description:
        description = soup.find_all("meta", {"name": "twitter:description"})

    image = soup.find_all("meta", {"property": "og:image"})

    if not image:
        image = soup.find_all("meta", {"name": "twitter:image"})

    try:
        title = title[0].get('content', None)
        description = description[0].get('content', None)
        image = image[0].get('content', None)
    except (KeyError, TypeError, IndexError):
        title = ''
        description = ''
        image = ''

    if not title or not description:
        title = soup.find("title")
        description = soup("meta", {"name": "description"})
        image = soup("meta", {"name": "image"})

        try:
            title = title.text
        except (KeyError, TypeError, IndexError):
            title = ''

        try:
            description = description[0].get('content', None)
        except (KeyError, TypeError, IndexError):
            description = ''

        try:
            image = image[0].get('context', None)
        except (KeyError, TypeError, IndexError):
            image = ''

    return title, description, image
