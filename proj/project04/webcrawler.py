import sys
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from RequestGuard import RequestGuard
from urllib.parse import urljoin, urldefrag, urlparse
import csv
import image_processing
import requests


def check_args():
    #check length, check valid prefixes, if -i is prefix, make sure filter is valid
    if (
        len(sys.argv) < 5 or 
        sys.argv[1] not in ['-c','-p','-i'] or 
        (sys.argv[1] == '-i' and sys.argv[4] not in ['-s','-g','-f','-m'])
    ):
        print("invalid arguments")
        quit()

    # check valid url...
    # check valid file names...

def process_link(current_url, link):
    #print(f"Link at start: {link}")

    if link.startswith('http') or link.startswith('https'):
        absolute_link, _ = urldefrag(link) # urldefrag also returns what the fragment was, but we don't need it
    elif link.startswith('/'):
        absolute_link = urljoin(current_url, link)
    elif link.startswith('#'):
        absolute_link, _ = urldefrag(current_url)
    else:
        absolute_link = urljoin(current_url, link)
    
    #print(f"Link at end: {absolute_link}")

    return absolute_link

def count_links(url, output1, output2):
    """
    Link counting - starting at an initial page created for the class, 
    you'll find all the links on the page and load only the pages that 
    are on the same domain as the original page.
    On each page you load you will repeat the same process of finding and loading 
    links until you've found every link on every allowed page. 
    During that time your program will record how many times it sees each webpage. 
    At the end, you'll produce a histogram showing 
    the number of pages that have been seen once, twice, etc. This information will be saved to output files.
    >>> python3 webcrawler.py -c http://cs111.byu.edu/Projects/project04/assets/page1.html count_links.png count_links.csv """
    #i'm allowed to use pandas...?

    # dictionary to keep track of the number of times a link appeared on the pages of the website
    visited_links = {}
    # store initial URL, make sure robot protects it
    robot_protector = RequestGuard(url)
    # add url to list of links to visit
    links_to_visit = [url] 

    while links_to_visit:
        # Use the lst.pop() function to pop the next link off of the list each time, getting the next link
        current_url = links_to_visit.pop(0) 
        
        if current_url in visited_links: # if already visited:
            visited_links[current_url] += 1

        else: # if not already visited:
            visited_links[current_url] = 1
            # if we are allowed to load the page, add all links on the page to our links_to_visit
        
            response = robot_protector.make_get_request(current_url)

            if response: # if the robot says we can go here:
                soup = BeautifulSoup(response.text, 'html.parser')
                for tag in soup.find_all('a', href=True): # removes need to also save href as a variable
                    absolute_link = process_link(current_url, tag['href'])

                    # parsed = urlparse(absolute_link)
                    # domain = parsed.scheme + "://" + parsed.netloc

                    #print(f"debug the domain of the absolute link: {domain}")
                    #print(f"domain of robot:{robot_protector.domain}")

                    # if absolute_link not in visited_links:
                    #     print(f"This {absolute_link} was not previously in visited_links. Adding Now.")
                    #     links_to_visit.append(absolute_link)

                    links_to_visit.append(absolute_link)

                    # if the domain of the absolute link is the same as the domain of the robot
                    # if domain == robot_protector.domain and absolute_link not in visited_links:
                    #     links_to_visit.append(absolute_link)

    # Create a plot from the table of visited link counts
    # list of links and the number of times they were referenced
    counts = list(visited_links.values())
    bins = range(min(counts), max(counts) + 2) 

    # print(counts)
    # print(bins)

    hist_values, bin_edges, _ = plt.hist(counts, bins) # hist returns 3 items but we only need the first twox
    plt.savefig(output1)
    plt.clf()

    # Write the histogram data to the CSV file
    with open(output2,'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(hist_values)):
            writer.writerow([bin_edges[i], hist_values[i]])

def plot_data(url, output1, output2):
    """In this part of the project, you'll implement the functionality for the -p command line argument. 
    For this you'll find a specific table on a specified web page and read the data from the table, 
    plot it, and save the data to a CSV file."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content,"html.parser")

            """You need to find a table with the the "CS111-Project4b" id on the specified page. 
            Once you've found that you need to read the data from the table. 
            The first column of the table will contain the x-values for the data, 
            every subsequent column will contain a set of y-values for the x-value for the row. 
            Each column should be read into a list of data.
            Hint: Once you've found the table, you can extract a list of table row (<tr>) elements that 
            will contain as its table data (<td>) values, the x-value in the first <td> element, 
            and the y-values in all the others. Loop over the table rows, extracting the values 
            (assume they are all floats) and store them in the data lists as numbers."""

            correct_table = soup.find('table', attrs={'id': 'CS111-Project4b'})

            rows = correct_table.find_all("tr")
            if not rows:
                print("No rows found in the table")
                return

            # Initialize a list to store column data
            first_row = rows[0].find_all("td")
            num_columns = len(first_row)
            total_info = [[] for _ in range(num_columns)]


            # Extract data
            for row in rows:
                cols = row.find_all("td")
                if len(cols) == num_columns:
                    for i in range(num_columns):
                        total_info[i].append(float(cols[i].text))

            # Each set of y-values should be plotted against the x-values and all the lines should be on a single plot. 
            # Each set of y-values should have a different color. The first y-value set should be blue, 
            # the second, green, then red, then black. We will never have more than four data sets on a page for you to plot.
            # Once you've created the plot save it to the file specified as <output file 1> in the command line arguments.
            # After you've saved the plot, you should create the CSV file containing the data. 
            # This will be saved in the file specified by <output file 2> in the command line arguments. 
            # Each line should have the x-value, followed by each of the y-values for that x-value, separated by commas. 

            colors = ['b','g','r','k']

            x = total_info[0]

            for i in range(1, num_columns):
                plt.plot(x, total_info[i], colors[i-1])
            plt.savefig(output1)
            plt.close()

            # create csv and save it to output2
            with open(output2,'w', newline='') as file:
                writer = csv.writer(file)
                for i in range(len(total_info[0])):
                    row = [total_info[j][i] for j in range(num_columns)]
                    writer.writerow(row)

    except Exception as e:
        print(f"error accessing page, invalid URL: {e}")

def modify_imgs(url, output_file_prefix, filter_to_run):
    """Images on a web page are specified by the <img> tag. 
    The URL to the image is in the src attribute in that tag. 
    Just like the links in Part 2, the URLs in the src attribute may be complete, 
    absolute, or relative URLs that you will need to construct the complete URL for to be able to download the image.
    Load the web page specified by the <url> command line argument and create a 
    list of all the URLs to the images on that page. We'll use that list in the next task."""

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    all_imgs = soup.find_all('img')

    for img in all_imgs:
        if 'src' in img.attrs:
            img_url = urljoin(url, img['src'])
            img_response = requests.get(img_url)

            # Extract filename from img_url
            parsed_url = urlparse(img_url)
            img_filename = parsed_url.path.split('/')[-1]

            print(f"Downloading image: {img_filename}") # debug

            with open(img_filename, 'wb') as file: # saves OG image locally in order to modify it
                file.write(img_response.content)

            output_filename = f"{output_file_prefix}{img_filename}" # create new filename for new modified image

            if filter_to_run == "-s":
                image_processing.sepia([None, None, img_filename, output_filename])
            if filter_to_run == "-g":
                image_processing.grayscale([None, None, img_filename, output_filename])
            if filter_to_run == "-f":
                image_processing.flipped([None, None, img_filename, output_filename])
            if filter_to_run == "-m":
                image_processing.mirror([None, None, img_filename, output_filename])
            # The modified image is saved inside of a function in image_processing to the output filename
            
if __name__ == "__main__":
    """ Possible commands in the terminal: 
    -c http://cs111.byu.edu/Projects/project04/assets/page1.html project4plot.png project4data.csv
    -p http://cs111.byu.edu/Projects/project04/assets/data.html data.png data.csv
    -i http://cs111.byu.edu/Projects/project04/assets/images.html grey_ -g
    -i http://cs111.byu.edu/Projects/project04/assets/images.html sepia_ -s 
    
    The -c command is for counting the links. The URL is the starting page of the search. Output file 1 will contain the histogram image and output file 2 will contain the raw data in CSV format.
    The -p command is to extract and plot data. The URL is the page that contains the data to extract. Output file 1 will contain the data plot and output file 2 will contain the data in CSV format.
    The -i option is for finding and manipulating an image. The URL is the page where we want to extract images. The output file prefix is a sting that will be prepended to the name of every image manipulated to produce the name of the output image file. The filter to run will be a flag specifying which filter from your image manipulation program to run. Specifically, your program should handle the following filter flags:
    -s - sepia filter
    -g - grayscale filter
    -f - vertical flip
    -m - horizontal flip (mirror) """
    
    check_args()

    command = sys.argv[1]
    url = sys.argv[2]

    if command != "-i" :
        output_filename_1 = sys.argv[3]
        output_filename_2 = sys.argv[4]
    else:
        output_file_prefix = sys.argv[3]
        filter_to_run = sys.argv[4]

    if command == "-c":
        count_links(url, output_filename_1, output_filename_2)

    if command == "-p":
        plot_data(url, output_filename_1, output_filename_2)

    if command == "-i":
        modify_imgs(url, output_file_prefix, filter_to_run)