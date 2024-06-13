
# x= [1,2,3,4,5]
# y= [1,2,3,4,5]
# y2= [1,1,1,1,1]

# pyplot.plot(x, y, 'b')
# pyplot.plot(x, y2, 'g')
# pyplot.show()

from matplotlib import pyplot as plt
from bs4 import BeautifulSoup
import requests

# Fetch and parse the HTML
response = requests.get("https://cs111.byu.edu/Projects/project04/assets/data.html")
soup = BeautifulSoup(response.content, "html.parser")

# Find the correct table
correct_table = soup.find('table', attrs={'id': 'CS111-Project4b'})

# Initialize a list to store column data
first_row = correct_table.find("tr")
num_columns = len(first_row.find_all("td"))
total_info = [[] for _ in range(num_columns)]

# Extract data
for row in correct_table.find_all("tr"):
    cols = row.find_all("td")
    if len(cols) == num_columns:
        for i in range(num_columns):
            total_info[i].append(float(cols[i].text))

# Plot the data
x = range(len(total_info[0]))

for i in range(num_columns):
    plt.plot(x, total_info[i])

plt.show()
