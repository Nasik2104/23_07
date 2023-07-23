from bs4 import BeautifulSoup

path_to_my_file = "E:\\python_work\\homework\\22_07\\example.html"

with open(path_to_my_file) as file:
    soup = BeautifulSoup(file, "html.parser")

for data in soup.find_all("h1"):
    print(data.text)

services_section = soup.find('section', id='services-section')

services_list = services_section.find('ul', class_='services-list')

services = []

for service in services_list.find_all('li'):
    services.append(service.text)

print(services)

for footer in soup.find_all("footer"):
    for i in footer.find("p"):
        print(i)
