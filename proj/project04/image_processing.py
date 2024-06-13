import sys
import os
from byuimage import Image

"""
TODO: TO go FURTHER and BEYOND!!

If invalid command line arguments are provided, print out a message listing the possible commands and valid arguments
Add a help command (-h) that takes no arguments and lists all the available commands
Extend the collage functionality to allow the user to specify the color of the border
Extend the collage functionality to handle images of different sizes
Extend the collage functionality to allow the user to provide a different number of images and specify their positions
Extend the green screen functionality to allow the user to specify the position of the copied foreground image relative to the background image.
Handle any errors that might arise when the images passed to the green screen function aren't the same size
Add functionality to just print the red, green, or blue channel of the image.
Add some other functionality that you want to apply to your images

"""

def image_processing(args):
    """
    take input from the user on the command line and manipulate one or more images based on the provided input.
    """
    filename = args[2]
    img = Image(filename)
    img.show()

def load_image(args):
    return Image(args[2])

def darken(args):
    """
    darkens image by certain percent
    -k <input file> <output file> <percent in decimal form> 
    make sure save file is png
    """
    output_file = args[3]
    darkened = 1 - float(args[4])
    img = load_image(args)

    for pixel in img:
        pixel.red = pixel.red * darkened
        pixel.green = pixel.green * darkened
        pixel.blue = pixel.blue * darkened

    img.save(output_file)

def sepia(args):
    """
    true_red = 0.393*pixel.red + 0.769*pixel.green + 0.189*pixel.blue
    true_green = 0.349*pixel.red + 0.686*pixel.green + 0.168*pixel.blue
    true_blue = 0.272*pixel.red + 0.534*pixel.green + 0.131*pixel.blue

    pixel.red = true_red
    Finally, it may be the case that the color value is greater than 255. 
    If that happens, set that pixel's color value to the maximum value of 255. 
    For example:
    if pixel.red > 255:
    pixel.red = 255
    """

    output_file = args[3]
    img = load_image(args)

    for pixel in img:
        true_red = 0.393*pixel.red + 0.769*pixel.green + 0.189*pixel.blue
        true_green = 0.349*pixel.red + 0.686*pixel.green + 0.168*pixel.blue
        true_blue = 0.272*pixel.red + 0.534*pixel.green + 0.131*pixel.blue

        pixel.red = true_red
        pixel.green = true_green
        pixel.blue = true_blue

        if pixel.red > 255:
           pixel.red = 255

        if pixel.green > 255:
            pixel.green = 255

        if pixel.blue > 255:
            pixel.blue = 255

    img.save(output_file)

def grayscale(args):
    output_file = args[3]
    img = load_image(args)

    for pixel in img:
        average = (pixel.red + pixel.green + pixel.blue) / 3
        pixel.red = average
        pixel.blue = average
        pixel.green = average
        #pixel.color = average

    img.save(output_file)

def make_border(args):
    """
     that will put a border of equal thickness all the way around an image. 
     This function will take as input a filename containing an image to modify, 
     the thickness of the border, and color values for the red, green, and blue channels in the border region.
    """
    output_file = args[3]
    thickness = int(args[4])
    red = int(args[5])
    green = int(args[6])
    blue = int(args[7])
    img = load_image(args)
    

    new_width = img.width + (thickness * 2)
    new_height = img.height + (thickness * 2)
    new_img = Image.blank(new_width, new_height)

    for y in range(new_img.height):
        for x in range(new_img.width):
            if x < thickness or x >= new_width - thickness or y < thickness or y >= new_height - thickness:
                pixel = new_img.get_pixel(x, y)
                pixel.red = red
                pixel.green = green
                pixel.blue = blue

    for y in range(img.height):
        for x in range(img.width):
            transferred_pixel = img.get_pixel(x, y)
            new_x = x + thickness
            new_y = y + thickness

            original_pixel = img.get_pixel(x, y)
            new_pixel = new_img.get_pixel(new_x, new_y)

            new_pixel.red = original_pixel.red
            new_pixel.green = original_pixel.green
            new_pixel.blue = original_pixel.blue
            
    new_img.save(output_file)

# totally possible to reuse the code here and modify it slightly for the mirror function
def flipped(args):
    output_file = args[3]
    img = load_image(args)
    
    new_img = Image.blank(img.width, img.height)
    for y in range(0, img.height):
        for x in range(0, img.width):
            old_pixel = img.get_pixel(x,y)
            new_pixel = new_img.get_pixel(x, img.height - y - 1)

            new_pixel.red = old_pixel.red
            new_pixel.green = old_pixel.green
            new_pixel.blue = old_pixel.blue

    new_img.save(output_file)

def mirror(args):
    output_file = args[3]
    img = load_image(args)
    
    new_img = Image.blank(img.width, img.height)
    for y in range(0, img.height):
        for x in range(0, img.width):
            old_pixel = img.get_pixel(x,y)
            new_pixel = new_img.get_pixel(img.width - x - 1, y)

            new_pixel.red = old_pixel.red
            new_pixel.green = old_pixel.green
            new_pixel.blue = old_pixel.blue

    new_img.save(output_file)

def composite(args):
    img1 = Image(args[2])
    img2 = Image(args[3])
    img3 = Image(args[4])
    img4 = Image(args[5])
    output_file = args[6]
    thickness = int(args[7])
    #get height and width
    height = img1.height
    width = img1.width
    new_width = 2 * width + 3 * thickness
    new_height = 2 * height + 3 * thickness
    composite_image = Image.blank(new_width,new_height)
    for pixel in composite_image:
        pixel.color = 0 # make it all black

    for y in range(height):
        for x in range(width):
            original_pixel = img1.get_pixel(x, y)
            new_pixel = composite_image.get_pixel(x + thickness, y + thickness)
            new_pixel.color = original_pixel.color
    
    for y in range(height):
        for x in range(width):
            original_pixel = img2.get_pixel(x, y)
            new_pixel = composite_image.get_pixel(x + width + 2 * thickness, y + thickness)
            new_pixel.color = original_pixel.color
    
    for y in range(height):
        for x in range(width):
            original_pixel = img3.get_pixel(x, y)
            new_pixel = composite_image.get_pixel(x + thickness, y + height + 2 * thickness)
            new_pixel.color = original_pixel.color

    
    for y in range(height):
        for x in range(width):
            original_pixel = img4.get_pixel(x, y)
            new_pixel = composite_image.get_pixel(x + width + 2 * thickness, y + height + 2 * thickness)
            new_pixel.color = original_pixel.color

    composite_image.save(output_file)

def is_green_enough(pixel, threshold, factor):
    average = (pixel.red + pixel.green + pixel.blue) / 3
    if pixel.green >= factor * average and pixel.green > threshold:
        return True
    else:
        return False

def greenscreen(args):
    """
    puts foreground image is the one with the greenscreen
    """
    foreground = Image(args[2]) # man
    background = Image(args[3]) # explosion
    output_file = args[4]
    threshold = int(args[5])
    factor = float(args[6])

    height = foreground.height
    width = foreground.width

    for y in range(height):
        for x in range(width):
            #if a foreground pixel is green enough, put the background pixel on top of the foreground
            #background_pixel = background.get_pixel(x,y)
            foreground_pixel = foreground.get_pixel(x,y)

            if is_green_enough(foreground_pixel, threshold, factor):
                background_pixel = background.get_pixel(x,y)
                foreground_pixel.color = background_pixel.color

    foreground.save(output_file)   

def validate_commands(args):
    """
    returns True or False depending on if that list contains a valid set of commands and arguments. 
    The list passed to this function should have the operation as the first element and the arguments as the rest of the elements in the list.
    For example:
    python image_processing.py <operation flag> [<argument 1> <argument 2> ...]
    """
    valid = ["-d", "-k", "-s", "-g", "-b", "-f", "-m", "-c", "-y"]

    if args[1] in valid and len(args) > 2:
        return True
    else:
        return False
    
def flags(args):
    img_command = args[1]
    if img_command == "-d":
        image_processing(args)
    elif img_command == "-k" and len(args) >= 3:
        darken(args)
    elif img_command == "-s" and len(args) >= 2:
        sepia(args)
    elif img_command == "-g" and len(args) >= 2:
        grayscale(args)
    elif img_command == "-b" and len(args) >= 6:
        make_border(args)
    elif img_command == "-f" and len(args) >= 2:
        flipped(args)
    elif img_command == "-m" and len(args) >= 2:
        mirror(args)
    elif img_command == "-c" and len(args) >= 6:
        composite(args)
    elif img_command == "-y" and len(args) >= 5:
        greenscreen(args)
    else:
        print("some other error")

def main():
    """python image_processing.py <operation flag> [<argument 1> <argument 2> ...]
    Operation flag: -d <image file> """
    # arg0 is image_processing, arg1 is operation flag, arg2 is image file

    args = sys.argv
    if validate_commands(args):
        print("Command line is valid!")
        flags(args)
    else:
        print("There is a problem with the command line")

if __name__ == "__main__":
    main()