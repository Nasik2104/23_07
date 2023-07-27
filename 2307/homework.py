from bs4 import BeautifulSoup
import requests

page = 1
while page < 22:
    site_to_parse = "http://yermilovcentre.org/medias/?page=" + str(page)
    my_answer = requests.get(site_to_parse)
    soup = BeautifulSoup(my_answer.content, "html.parser")

    div = soup.find_all('div', class_="block-container-small-card ml-0 px-0 margin-right-12px")#"block-container-small-card ml-0 px-0 margin-right-12px")


    for d in div:
        text = d.find('a', class_="row title-text mx-0 pt-3 pb-2")
    
        a = d.find('a', class_='title-text')

        href_value = a.get('href')
        result = 'http://yermilovcentre.org' + href_value
    
        print(f"Назва -- {text.text.strip()}, Посилання -- {result.strip()}")
    page += 1