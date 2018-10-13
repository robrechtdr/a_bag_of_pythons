#!/usr/bin/env python

import json
import sys
import urlparse

import requests

from bs4 import BeautifulSoup


def extract_single(url):
    """
    Extracts hyperlink and img urls.
    """

    print "\nGet requesting {} ...".format(url)
    req = requests.get(url)
    print "Got page!"
    soup = BeautifulSoup(req.content, 'html.parser')


    def get_absolute_url(base_url, url):
        # External links
        if url.startswith("http"):
            return url
        # Internal links
        else:
            return urlparse.urljoin(base_url, url)

    print "Parsing links and images ..."
    links = []
    for link_el in soup.find_all("a"):
        if link_el.has_attr("href"):
            links.append(get_absolute_url(url, link_el["href"]))

    images = []
    for img_el in soup.find_all("img") :
        if img_el.has_attr("src"):
            images.append(get_absolute_url(url, img_el["src"]))

    print "Parsing finished!"
    return {"links": links, "images": images}  


def extract(urls):
    result = {}
    for url in urls:
        result[url] = extract_single(url)
    return json.dumps(result)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print ("Please provide at least one url as argument, e.g.: \n"
                "./{0} http://bbc.co.uk https://www.python.org\n".format(sys.argv[0]))
        sys.exit()
    else:
        script = sys.argv[0]
        urls = sys.argv[1:]

    print extract(urls)
