"""
write date from dict to xlsx file
dict keys - columns names
"""

import os
import pandas as pd


def write_dict_to_xlsx(hotels_dict: dict):
    columns = ['hotel_name','hotel_stars', 'hotel_rating', 'feedback_number', 'hotel_address', 'hotel_link']
    # Create a pandas DataFrame from the dictionary
    df = pd.DataFrame([hotels_dict], columns=columns)

    # Check if the output file exists
    if os.path.exists('Hotels.xlsx'):
        # If the file exists, append the new data to it
        with pd.ExcelWriter('Hotels.xlsx', mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
            # Get the last row number of the existing sheet
            last_row = writer.sheets['Sheet1'].max_row

            # Write the new data starting from the next row
            df.to_excel(writer, index=False, header=False, startrow=last_row)
    else:
        # If the file doesn't exist, create a new one
        df.to_excel('Hotels.xlsx', index=False)


if __name__ == '__main__':
    hotels_dict_ = {'feedback_number': '319 отзывов',
                   'hotel_address': 'Başkomutan, Atatürk Cd., Бельдиби, Кемер 7990 Турция',
                   'hotel_link': 'https://www.tripadvisor.ru/Hotel_Review-g678226-d2677793-Reviews-Club_Hotel_Belpinar-Beldibi_Kemer_Turkish_Mediterranean_Coast.html',
                   'hotel_name': 'Club Hotel Belpinar Клуб Отель Бельпинар',
                   'hotel_rating': '4,0'}
    write_dict_to_xlsx(hotels_dict_)
