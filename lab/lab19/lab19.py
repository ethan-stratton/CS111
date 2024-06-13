import requests
from bs4 import BeautifulSoup

def download(url, output_filename):
    """Write a function called download that has the parameters url and output_filename. 
    The function should get the HTML text from the url, open the file, and write it to the provided output_filename.
    When getting the text, use .text rather than .content.
    To test, get the HTML contents from the CS111's pair programming article and write them to a file called lab19_test.txt. 
    Compare your file to the HTML content on the webpage.
    
    url = 'https://cs111.byu.edu'
    output_filename = 'lab19_test.txt'
    download(url, output_filename)
    """
    response_object = requests.get(url)
    with open(output_filename, 'w') as f:
            f.write(response_object.text)


def make_pretty(url, output_filename):
    """Write a function called make_pretty which takes in a url and an output_filename. 
    The function should save the results of calling .prettify() on the web page given by the url to the output_filename.

    >>> retty_output_filename = 'lab19_pretty_test.txt'
    >>> make_pretty('https://cs111.byu.edu', pretty_output_filename)
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    pretty_html = soup.prettify()
    
    with open(output_filename, 'w') as f:
        f.write(pretty_html)


def find_paragraphs(url, output_filename):
    """
    >>> list_of_tags = soup_object.find_all('p')
    >>> print(list_of_tags)
    [<p>Computer Science is amazing!</p>, <p>I want to become a CS Major!</p>]"""

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    all_p = soup.find_all('p')

    with open(output_filename, 'w') as f:
        for p in all_p:
            f.write(str(p)+"\n")


def find_links(url, output_filename):
    """Same thing as find_paragraphs but with links (hrefs), find all a tags and extract the href"""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    all_links = soup.find_all('a') # its also possible to do this a['href']

    with open(output_filename, 'w') as f:
        for link in all_links:
            href = link.get('href')
            f.write(href + '\n')


# response_object = requests.get("https://cs111.byu.edu")
# print(response_object.url)
# print(response_object.status_code)
# print(response_object.headers)


# soup_object = bs4.BeautifulSoup(response_object.content, features="html.parser") # `features` prevent an unimportant warning for this class 