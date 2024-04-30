import requests
from bs4 import BeautifulSoup

url = "https://engine.com.pk/collections/men-tshirts"

response = requests.get(url)
# print(response)

soup = BeautifulSoup(response.text, 'html.parser')
prefix = "https://engine.com.pk"

images = soup.select('img.images-one')
image_list = []
for image in images:
    image_list.append(image.get('data-src'))

suit_disc = []
description = soup.select('div.product-bottom a.product-title span')
for desc in description:
    suit_disc.append(desc.text)

Money = []
money_elements = soup.select('div.product-details span.special-price')
for element in money_elements:
    Money.append(element.text)



hreftag = []
href = soup.select('a.product-grid-image')
for data in href:
    hreftag.append(data.get('href'))

complete = []
for item in hreftag:
    complete.append(prefix + item)

with open('data.js', 'r') as original_file:
    original_content = original_file.read()
    
with open('temp.js', 'w') as f:
    f.write('var javascript_array = [\n')
    for item in image_list:
        f.write(f'\'{item}\',\n')
    f.write('];\n')

    f.write('var imageLinks = [\n')
    for item in complete:
        f.write(f'\'{item}\',\n')
    f.write('];\n')

    f.write('var desc = [\n')
    for item in suit_disc:
        f.write(f'\'{item.strip()}\',\n') 
    f.write('];\n')
    
    f.write('var money = [\n')
    for item in Money:
        f.write(f'\'{item}\',\n')
    f.write('];\n')    
    
    f.write(original_content)

print("Total image links:", len(image_list))
print("Total decs links:", len(suit_disc))
print("Total price links:", len(Money))
print("Total images links:",len(hreftag))

print(hreftag[0:5])


