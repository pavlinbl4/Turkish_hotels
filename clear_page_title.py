import re

pattern = r'\w+\s.+\)'

def clear_title(name: str):
    return re.findall(pattern, name)[0].strip()


if __name__ == '__main__':
    clear_title('SERENIS HOTEL (Сиде) - отзывы, фото и сравнение цен - Tripadvisor')