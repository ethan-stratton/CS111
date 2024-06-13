from urllib.parse import urlparse, urljoin

import requests
from typing import List

def get_domain(url):
    """given a full URL, returns the full domain of the url, or an empty string if there is no full domain in the url. 
    It should also return an empty string if the scheme of the url is not valid (we'll consider http and https valid)
    >>> get_domain('https://cs111.byu.edu/lab/lab20/')
    'https://cs111.byu.edu'
    >>> get_domain('http://en.wikipedia.org/w/index.php')
    'http://en.wikipedia.org'
    >>> get_domain('proj/proj4/')
    '' # an empty string
    """

    parsed = urlparse(url)
    valid_schemes = ['https', 'http']
    
    if parsed.scheme in valid_schemes and parsed.netloc:
        return f"{parsed.scheme}://{parsed.netloc}"
    else:
        return ""
    
def combine_paths(url, path):
    """Given a url and a path to another page on the same website, 
    it should return the full url to the other page. You can expect that your function will only be given valid URLs and paths.

    >>> combine_paths('https://cs111.byu.edu/lab/lab15/', '/lab/lab20/')
    'https://cs111.byu.edu/lab/lab20/'
    >>> combine_paths('https://cs111.byu.edu/hw/hw03/#part-2', '/articles/about/')
    'https://cs111.byu.edu/articles/about/
    
    """
    # get the url, scrape off anything past netloc, append path to it
    parsed_url = urlparse(url)
    return (f"{parsed_url.scheme}://{parsed_url.netloc}{path}")

def combine_urls(base_url, join_url):
    """Given two urls (a base url and a url to join), it should return the full URL of the webpage pointed to by the url to join. 
    Try using a built in urllib function help with this task.

    >>> combine_urls('https://cs111.byu.edu/lab/lab15/', '/lab/lab20/')
    'https://cs111.byu.edu/lab/lab20/'
    >>> combine_urls('https://cs111.byu.edu/lab/lab08', 'lab20/')
    'https://cs111.byu.edu/lab/lab20/'
    >>> combine_urls('https://cs111.byu.edu/hw/hw05/', 'https://www.wikipedia.org')
    'https://www.wikipedia.org'
    >>> combine_urls('https://cs111.byu.edu/lab/lab20/assets/page1.html', 'page2.html')
    'https://cs111.byu.edu/lab/lab20/assets/page2.html'
    """

    return urljoin(base_url, join_url) # built in method


def print_pages(url, paths: List[str], output_file) -> None:
    """
    Given a url, a list of paths and pages, and an output file name, 
    it should visit each of those paths and pages and write the contents of ALL of the pages to the same output file. 
    The start of each page should be written on its own line. 
    Each new page/path should be combined with the full url of the previous page visited 
    (eg. the first path/page will need to be combined with the url that is passed into the function, 
    and the second path/page will need to be combined with the full url of the first page, etc.)

    Paths vs Pages: If the item in the list that you are processing starts with a forward slash (/lab/lab20/assets/page1.html), 
    it is a path, and should be appended to the domain directly and visited. 
    If the item does not begin with a forward slash (page2.html), 
    it is a page in the same "folder" as the previous file processed (https://cs111.byu.edu/lab/lab20/assets/page2.html).

    >>> print_pages('https://cs111.byu.edu', ['/lab/lab20/assets/page1.html', 'page2.html'], 'pages.output.txt') # no print output because you are just writing to the output file
    >>> print_pages('https://cs111.byu.edu/proj/proj4/', ['/lab/lab20/assets/page1.html', 'page2.html'], 'pages.output.txt')

    Both of the above function calls should write the same thing to the output file:

    you found page1! good job.
    this line is from page2.html
    """

    def get_content(full_url):
        response = requests.get(full_url)
        return response.text
    
    with open(output_file, 'w') as file:
        base_url = get_domain(url)
        current_url = base_url # chop off unnecessary stuff after netloc
    
        for path in paths:
            if path.startswith('/'):
                # It's a path, join with the base URL
                current_url = urljoin(base_url, path)
                #print(f"Debugging from path:{current_url}")

            else: # it is a page in the same folder as the previous file processed
                current_url = urljoin(current_url, path)
                #print(f"Debugging from page:{current_url}")

            content = get_content(current_url)
            file.write(content+'\n')



#print_pages('https://cs111.byu.edu', ['/lab/lab20/assets/page1.html', 'page2.html'], 'pages.output.txt') # no print output because you are just writing to the output file
#print_pages('https://cs111.byu.edu/proj/proj4/', ['/lab/lab20/assets/page1.html', 'page2.html'], 'pages.output.txt')

print_pages('https://cs111.byu.edu/pages/about/',
                ['/lab/lab20/assets/page1.html', 'page2.html', '/lab/lab20/assets/more_pages/page3.html', '/lab/lab20/assets/page4.html'],
                'paths.output.txt')