import requests
from bs4 import BeautifulSoup
import sys

def load_and_find(url, html_elmt, attr, output_file):
    """
    Write a program that will take command line arguments containing a URL, an HTML element, an attribute, and an output file name. 
    The program should load the page specified by the given URL and find the HTML element with the specified attribute. 
    This same attribute will contain the data for the next step in the scavenger hunt. 
    The information is stored as a comma-separated list (<URL>,< desired tag>,<attribute name>).

    >>> python3 lab21.py https://cs111.cs.byu.edu/ p checkpoint1 output.txt
    The program should look for the paragraph tag <p> in the CS111 home page with the attribute checkpoint1.
        <p checkpoint1="https://www.byu.edu/,a,checkpoint2">Do you know Joe?</p>
    
    Once the program does that, the program should then go to https://www.byu.edu/, 
    look for an anchor tag with the attribute checkpoint2, and read its contents to find the next location.
    
    Continue recursively searching until you find an attribute called final. 
    Once final is found, write the tag's attribute content to the output file.

    For example, if we have an HTML tag that looks like this:
        <img src="doge.jpg" final="Congratulations! You made it!">
    We would write Congratulations! You made it! to the output file specified from the command line."""

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the element with the specified tag and attribute
    element = soup.find(html_elmt, {attr: True})

    if not element:
        print("Error, specified attr not found")
        return
    
    # If element with the final attribute is found, write its content to the output file
    if 'final' in element.attrs:
        final_content = element['final']
        with open(output_file, 'w') as f:
            f.write(final_content)
        return
    
    # If final is not found, get the next URL, HTML element, and attribute name from the current element
    next_info = element[attr].split(',')
    next_url = next_info[0]
    next_html_elmt = next_info[1]
    next_attr = next_info[2]

    load_and_find(next_url, next_html_elmt, next_attr, output_file)

if __name__ == '__main__':
    url = sys.argv[1] 
    html_elmt = sys.argv[2]
    attr = sys.argv[3]
    output_file = sys.argv[4]

    load_and_find(url, html_elmt, attr, output_file)

    








"""
Going Further for Project 4

In reality, not all links contain the full URL to a webpage. For example, consider the following links:

<a href="/lab/lab21">Link 1</a>
<a href="#scavenger-hunt">Link 2</a>
<a href="sample2.html">Link 3</a>
In project 4, you will be building a web scraper that will count and store all the links on a webpage given a URL. After storing and counting all the links, the web scraper will visit all webpages given the valid links (the links that are on the CS 111 website) and count the links at those webpages. To help you visit valid webpages given the types of links provided above, we will write a function that will be able to properly process these types of links.

In order to do this correctly, you have to know how to correctly process hrefs like the one's given above. Down below is information to help you do this. If you want to view examples as your go through the bullet points below, visit https://cs111.byu.edu/proj/proj4/assets/page1.html and https://cs111.byu.edu/proj/proj4/assets/page2.html. Right click on the webpage and click View page source or Inspect to view the HTML and view the links.

If the link begins with http or https, it is a full URL. If the full URL contains a fragment # (ex. https://docs.python.org/3/library/functions.html#int), remove the fragment part and use just the base URL (https://docs.python.org/3/library/functions.html). If the URL doesn't have a fragment, you can just use it as is.
If the link begins with a forward slash (ex. /assets/page1.html) it is a relative link and should be added to the domain of the site you are currently visiting (<domain>/assets/page1.html) before being counted (make sure you don't end up with any // after the domain).
If the link begins with a pound sign (ex. #section) it is a link fragment which links to a different location on the page you are already visiting. Therefore, process the link as another copy of the URL you are currently visiting since the fragment links to the same page you are already on.
If the link doesn't fall into any of the categories above, it is likely a relative page in the same "folder". For example, if your current URL is https://cs111.byu.edu/proj/proj4/assets/page1.html and the link you are processing is page2.html, then you'll want to access the page2.html file which is in the same "folder" as page1.html. In this example the link you would append to your links to visit list would be https://cs111.byu.edu/proj/proj4/assets/page2.html.
Hint: In all cases, if the link contains a pound sign (or hashtag - the "#" symbol), the web crawler should strip off the pound sign and all following characters. With the stripped result, use that result to process considering the bullet points above. (As always, feel free to disregard this hint if you feel it will not help you.)

Write a function that will handle this logic given the necessary information and return the link to count and visit. It is up to you how you write it (as long as it follows the guidelines above). You should write the function in such a way where you only have to make a minor adjustment to your current code.

Test your code:

python3 lab21.py https://cs111.cs.byu.edu/lab/lab21/assets/webpage10.html footer link-checkpoint1 output.txt
It may be worth visiting https://cs111.cs.byu.edu/lab/lab21/assets/webpage10.html and following the link-checkpoints.

"""