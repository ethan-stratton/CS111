import requests
from urllib.parse import urlparse
import re

class RequestGuard:
    def __init__(self, url):
        # its also possible to use urljoin instead of manually doing it: robotsUrl = parse.urljoin(url, "/robots.txt")...
        self.url = url
        parsed_url = urlparse(url)
        self.domain = f"{parsed_url.scheme}://{parsed_url.netloc}" # store the domain of the url
        self.forbidden = self.parse_robots() # store the parse_robots call in this variable
        
    def can_follow_link(self, url):
        """
        Does the link start with the stored domain? - If it doesn't, return False. Otherwise proceed to the next check.
        Does the link contain any of the paths specified in the list generated from the path list provided? - 
        If it does, return False, otherwise return True."""

        parsed = urlparse(url)
        checking_url_domain = f"{parsed.scheme}://{parsed.netloc}"

        if checking_url_domain != self.domain:
            return False
        
        for forbidden_path in self.forbidden: # previous error: used if x in y to check, when needed for loop for each line
            if parsed.path.startswith(forbidden_path): # previous error, compared whole path to illegal path, now only compares subsectional path
                return False
        
        return True
    
    def make_get_request(self, url, use_stream= False):
        """checks if the url it gets can be followed"""
        if self.can_follow_link(url):
            return requests.get(url, stream= use_stream)
        else: 
            return None

    def parse_robots(self):
        """get the robots.txt file from a site. Ignore all lines in the file except for Disallow, store those lines in a list"""
        robots_txt = f"{self.domain}/robots.txt"
        robots = requests.get(robots_txt)
        disallowed = re.findall(r'^Disallow: (.+)', robots.text, re.MULTILINE)
        return disallowed


    