import matplotlib.pyplot as plt
import csv
from functools import lru_cache

@lru_cache(maxsize=None)
def get_gpas_get_sats():
    gpas = []
    sats = []

    # open and read
    with open("admission_algorithms_dataset.csv", 'r') as file:
        csv_reader = csv.reader(file)
        next(file) # skip header
        for row in csv_reader:
            # store info
            gpas.append(float(row[2]))
            sats.append(float(row[1]))

    return gpas, sats

def plot_histogram():
    """Open and read admission-algorithms-dataset.csv and store each of the students' GPA and SAT into their own respective lists. 
    Using those two lists, generate two histograms with one histogram displaying data of all the students' GPA and 
    the other displaying all the students' SAT data. The GPA histogram should be saved in a file called gpa.png, and 
    the SAT histogram should be saved in a file called sat_score.png.
    Recall that the file is organized like the following
        Student,SAT,GPA,Interest,High School Quality,Sem1,Sem2,Sem3,Sem4
    Recall the .split(<delimiter>) method of a string and remember to convert the strings that are representing numbers into floats."""

    gpas, sats = get_gpas_get_sats()

    # make histogram (GPA) save in file, clear
    plt.hist(gpas) # getting rid of range=[] worked
    plt.savefig("gpa.png")
    #plt.show()
    plt.clf()

    # make histogram (SAT) save in file, clear
    plt.hist(sats) # , bins=10, range=[900,1600]
    plt.savefig("sat_score.png")
    #plt.show()
    plt.clf()


def plot_scatter():
    """Using the same GPA and SAT lists from the previous problem, 
    create a scatter plot between those two lists with the GPA as the x-axis and SAT as the y-axis. 
    Save the graph to a file called correlation.png."""
    gpas, sats = get_gpas_get_sats()
    plt.scatter(gpas, sats)
    plt.savefig("correlation.png")
    plt.clf()

@lru_cache(maxsize=None)
def plot_spectra():
    """Open and read spectrum1.txt and spectrum2.txt. 
    These files will contain two columns representing the wavelength and flux respectively 
    (which detail the intensity of light of an astronomical object). On a single graph, 
    plot both datasets as a line plot with different colors. Data from spectrum1.txt will be blue, and data from spectrum2.txt will be green. Wavelength should be on the x-axis, and Flux should be on the y-axis. Save the final graph as spectra.png.
    Note: The data in the files are separated by four spaces. To separate a line into its separate 
    number components, use line.split() to get a list with the two numbers represented as strings"""
    
    spec1_flux = []
    spec1_wavelength = []
    spec2_flux = []
    spec2_wavelength = []

    # open and read
    with open("spectrum1.txt", 'r') as file:
        for line in file:
            # Split the line by 4 spaces
            parts = line.split('    ')
            spec1_wavelength.append(float(parts[0]))
            spec1_flux.append(float(parts[1]))
            
    with open("spectrum2.txt", 'r') as file:
        for line in file:
            # Split the line by 4 spaces
            parts = line.split('    ')
            spec2_wavelength.append(float(parts[0]))
            spec2_flux.append(float(parts[1]))

    plt.plot(spec1_wavelength, spec1_flux, color='blue')
    plt.plot(spec2_wavelength, spec2_flux, color='green')
    plt.savefig("spectra.png")

    # print(spec1_flux)
    # print(spec1_wavelength)
    # print(spec2_flux)
    # print(spec2_wavelength)

def main():
    plot_histogram()
    plot_scatter()
    plot_spectra()


def testing1():
    frequencies = [1,1,1,1,1,1, 2,2,2, 3, 4,4, 5]
    plt.hist(frequencies, [1, 2, 3, 4, 5, 6])
    plt.show()

def testing2():
    x_points = [1,5]
    y_points = [1,5]

    plt.plot(x_points, y_points)
    plt.show()


if __name__ == "__main__":
    main()
    



