"""
function receive link to hotel in tripadvisor and return dict with info about hotel
at first with function '1_extract_links_from_message' make csv file with links to
trip advisor in 2 column and then run 2_read_csv script. It will read csv file and
run this script
"""

from bs4 import BeautifulSoup

from icecream import ic

from browser.get_html import get_html_via_requests
from write_data_from_dict_in_xlsx import write_dict_to_xlsx


def get_information_from_tripadvisor_about_hotel(tp_link):
    html = get_html_via_requests(tp_link)
    if html is None:
        print("Bad response")
    else:
        soup = BeautifulSoup(html, 'lxml')
        hotels_dict = {
            'hotel_name': soup.find("h1", attrs={'id': 'HEADING'}).text,
            'hotel_address': soup.find_all('span', attrs={'class': 'biGQs _P pZUbB KxBGd'})[1].text,
            'hotel_rating': soup.find("span", attrs={'class': 'kJyXc P'}).text,
            'feedback_number': soup.find_all('span', attrs={'class': 'biGQs _P pZUbB KxBGd'})[2].text,
            'hotel_link': tp_link,
            'hotel_stars': 'no information',
        }
        try:
            hotels_dict['hotel_stars'] = soup.find('title', attrs = {'id': ':lithium-R4ml6l4lsnsla:'}).text
        except AttributeError as e:
            print(e)
        write_dict_to_xlsx(hotels_dict)
        return hotels_dict


if __name__ == '__main__':
    hotels_dict_ = get_information_from_tripadvisor_about_hotel(
        'https://www.tripadvisor.ru/Hotel_Review-g678226-d2677793-Reviews-Club_Hotel_Belpinar-Beldibi_Kemer_Turkish_Mediterranean_Coast.html'
    )
    ic(hotels_dict_)
