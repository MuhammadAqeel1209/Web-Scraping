# Webscraping --> Get Html page of website --> does not give to server --> Some content scrap in your python program
# Steps
"""
    1 Setting the Enviorment # --> Python Intsall, Request Module, html5lib module, bs4 Module
    2 Get The HTML
    3 Parse the HTML
    4 HTML tree traversal
    """
"""
Websracping the websites
    1 Using API
    2 HTML scraping using tools like bs4
    """
import requests #type:ignore
from bs4 import BeautifulSoup #type:ignore

url = "https://codewithharry.com"
mywebsiteUrl = "http://hotelcuisine-aqeel.surge.sh/"
mywebsite = ["http://hotelcuisine-aqeel.surge.sh/",
              "http://hotelcuisine-aqeel.surge.sh/menu.html",
              "http://hotelcuisine-aqeel.surge.sh/about.html",
              "http://hotelcuisine-aqeel.surge.sh/contactus.html",
            "http://hotelcuisine-aqeel.surge.sh/timming.html"]

data = requests.get(mywebsiteUrl)
htmlContent = data.content
soup = BeautifulSoup(htmlContent, 'html.parser')

# data = list()
# p = soup.find_all('p')
# for i in p:
#        data.append(i)
# print(data)

def TablesFind(mywebsite):
    data = requests.get(mywebsite)
    htmlContent = data.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    table = soup.find('table')

    if table:
        # Loop through the table rows and extract data
        for row in table.find_all('tr'):
            # Assuming the table has header cells in the first row
            header_cells = row.find_all('th')
            data_cells = row.find_all('td')

            if header_cells:
                # This is a header row; print column names
                column_names = [cell.text.strip() for cell in header_cells]
                print(column_names)
            elif data_cells:
                # This is a data row; print data values
                data_values = [cell.text.strip() for cell in data_cells]
                print(data_values)
    else:
            print("Table not found on the webpage   .")


def GetTitleAllPage(mywebsite):
    data = requests.get(mywebsite)
    htmlContent = data.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    title = soup.title.string
    print(f"Title of {mywebsite} is \t",title)

def GetParagraphofAllPage(soup,mywebsite):
        pargraph = soup.find_all('p')
        print(f"Paras of {mywebsite} is \t",pargraph)

def GetAbchorofAllPage(soup,mywebsite):
        anch = soup.find_all('a')
        print(f"Paras of {mywebsite} is \t",anch)        

# for i in mywebsite:
#     GetTitleAllPage(i)


# for i in mywebsite:
#      TablesFind(i)

#print(soup.prettify()) # --> show data in the form of HTML

#Commonly used of object
"""
1 Tag
2 Navigation String
3 Beautiful Soap
4 Comment
"""

title = soup.title# --> Title of HTML File

# markup = "<p><!-- This is a comment--><p>"
# commentSoup = BeautifulSoup(markup)
#print(title)
# print(type(title)) # --> Tag
#print((title.string)) # --> Navigation String
# print(type(soup)) # --> Beautiful Soap
# print(commentSoup.p)
#print(type(commentSoup.p.string)) # --> Comment



# for i in mywebsite:
#         GetParagraphofAllPage(soup,i)

paras = soup.find_all('p') # --> Get the Paragraph of HTML File
# print(paras)

anchor = soup.find_all('a') # --> Get the Anchor tag of HTML File
# for i in mywebsite:
#        GetAbchorofAllPage(soup,i)


# --> Get all link of HTML Page
all_links = list()
# # Get all the links on the page:
# for link in anchor:
#     if(link.get('href') != '#'):
#         linkText = "http://hotelcuisine-aqeel.surge.sh/" +link.get('href')
#         all_links.append(link)
#         print(linkText)

# print(soup.find('p').get_text()) # --> Get the text from the tags/soup
# print(soup.get_text()) # --> Get the full text from the tags/soup

#__next imgpreview2 --> id # --> That id of https://codewithharry.com
# idHTML = soup.find(id='__next ')

# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator
# for elem in idHTML.children:
#     print(elem)

# for item in idHTML.strings:
#     print(item)

# for item in idHTML.parents:
#     # print(item)
#     print(item.name)

# print(idHTML.next_sibling)
# print(idHTML.previous_sibling)

elem = soup.select('.allign ') 
#print(elem)

elem = soup.attrs # Find the Id of HTML Page
#print(elem)

elem = soup.select('.image ') 
#print(elem)

elem = soup.select('.row ') 
#print(elem)

# --> https://www.crummy.com/software/BeautifulSoup/bs4/doc/