import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"
data = requests.get(url)
html = data.content
soup = BeautifulSoup(html,'html.parser')
# print(soup.prettify())

# print(soup.title) #Get Title 
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name) 

# print(soup.p)
# print("Classes \t",soup.p['class'])
 
# print(soup.a)
# print(soup.find_all('a'),"\n\n") 

# print(soup.find(id ="__NEXT_DATA__"))
# for link in soup.find_all('a'):
#     print(link.get('href'))

# print(soup.get_text())
tag = soup.b
print(tag.name)