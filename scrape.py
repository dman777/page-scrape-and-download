from bs4 import BeautifulSoup
import requests
import colorama
import re


success_files = 0

def get_link():
    try:
        link = raw_input('Give link to scrape page pelase: ')
        if not link:
            raise ValueError('Must enter link, jack!')
        return link
    except ValueError as e:
        print e
        sys.exit(1)

def get_page(link):
    try:
        html = requests.get(link).content
        return html
    except requests.exceptions.RequestException as e:
        print e
        sys.exit(1)

def download_file(file):
    global success_files
    with open(file[1], 'wb') as f:
        response = requests.get(file[0])

        if response.status_code == 200:
            success_files+=1
            print success_files

def get_keyword():
    try:
        keyword = raw_input('Enter url link keyword for '
                             'download link(besides https/http): ')
        if not link:
            raise ValueError('Must enter keyword, jack!')
        return keyword
    except ValueError as e:
        print e

def scrape_page(html, keyword):
    soup = BeautifulSoup(html)
    soup = soup.find_all('a', href=re.compile('^(http).*{0}|(https).*{0}'
        .format(keyword)))
    download_list = [
        [download['href'], re.sub(
            'MAME 0.149 ROMs/', '', download.get_text())]
        for download in soup]
    return download_list

if __name__ == "__main__":
    link = get_link()
    keyword = get_keyword()
    html = get_page(link)
    download_list = scrape_page(html, keyword)
    [download_file(file) for file in download_list]
    print "success with {} files".format(success_files)




