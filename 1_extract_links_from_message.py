"""
this script create cvs file with links to tripe advisor  from manager letter
"""

from bs4 import BeautifulSoup
from pathlib import Path
import csv
from browser.check_selenium import open_page_with_selenium
from browser.get_html import get_html_via_requests
from clear_page_title import clear_title

csv_file_path: str = f'{Path.home()}/Desktop'


def write_csv_file(hotels_list, column_header=None):
    if column_header is None:
        column_header = ['HOTELS', 'links']
    with open(f'{csv_file_path}/Turkish_hotels.csv', 'w', newline='') as cvs_file:
        cvs_writer = csv.writer(cvs_file)
        # add header to column
        cvs_writer.writerow(column_header)
        # write date from list
        for hotel in hotels_list:
            cvs_writer.writerow(hotel)


# get on links for tripadvisor from  letter
def get_links_on_hotels(html):  #
    soup = BeautifulSoup(html, 'lxml')
    tours = soup.find_all(class_="ta-rating")
    hotels_list = []
    for tour in tours:
        q_link = tour.find('a').get('href')
        result = open_page_with_selenium(q_link)
        page_name = clear_title(result.title)
        tp_link = result.current_url
        hotels_list.append([page_name, tp_link])
    return hotels_list


if __name__ == '__main__':
    # put here link from manager

    hotel_links = "https://qui-quo.ru/FP00-FW86"

    hotels_list_ = get_html_via_requests(hotel_links)

    # write  links in csv file
    write_csv_file(get_links_on_hotels(hotels_list_))
