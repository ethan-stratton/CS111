# IMPORTANT - Remember to import Image from the byuimage library: `from byuimage import Image`
from byuimage import Image

cougar_image = Image("test_files/cougar.png")
#                      ^ path to `cougar.png` file
for pixel in cougar_image:
    pixel.red = 0
    pixel.green = 0
    #pixel.blue = 0
    #pixel.color = (0, 0, pixel.blue) alternative way to write above statement

    #able to access images .height. .width, and .get_pixel(x,y) to iterate over pixels
    #for y in range(cougar_image.height): 
    #   for x in range(cougar_image.width): 
        #   pixel = cougar_image.get_pixel(x,y)

cougar_image.show()

def iron_puzzle(filename):
    """
    This picture contains an image of something famous; however, the image has been distorted. 
    The famous object is all in blue values, but the blue values have all been divided by 10, 
    so they are too small by a factor of 10. The red and green values are all just meaningless random values (“noise”)
    added to obscure the real image. You must undo these distortions to reveal the real image.
    All your code will be in a function called iron_puzzle(filename). 
    It takes one parameter, the filename of the image with the puzzle in it. It should return the edited iron.png image with the distortions undone. Your code should be able to show the modified image with code like this:
    """
    #go through image pixel by pixel, multiply blue by ten
    img = Image(filename)
    for y in range(img.height): 
        for x in range(img.width): 
           pixel = img.get_pixel(x,y)
           pixel.red = 0
           pixel.green = 0
           pixel.blue *= 10
           #img.putpixel((x,y),(r,g,b))

    return img


# solution_image = iron_puzzle("test_files/iron.png")
# solution_image.show()


def west_puzzle(filename):
    """
    The hidden image is exclusively in the blue values, so set all pixels' red and green values to 0. 
    The hidden image is encoded using only the blue values that are less than 16 (that is, 0 through 15). 
    If a blue value is less than 16, multiply it by 16 to scale it up to its proper value. 
    Alternately if a blue value for any pixel is 16 or more, it is random garbage and should be ignored (interpreted as 0). 
    Try using two for loops when traversing over each of the pixels.
    """
    img = Image(filename)
    for pixel in img:
        pixel.red = 0
        pixel.green = 0
        if pixel.blue < 16:
            pixel.blue *= 16
        else:
            pixel.blue = 0
    return img

#runs fine
# solution = west_puzzle("test_files/west.png")
# solution.show()


def darken(filename, percent):
    """
    The filename parameter contains the image's filename to darken, and the percent parameter tells you 
    how much to darken the image by. percent must and will be a number between 0 and 1. 
    The closer percent is to 1, the darker the image should be. darken should return the modified image.
    Notice that we can darken a pixel 80% by leaving it 20% as bright. 
    We can do this by multiplying each pixels' RGB values by 0.2:


    """
    img = Image(filename)

    darkened = 1 - percent
    for pixel in img:
        #pixel.color(pixel.red * percent, pixel.green * percent, pixel.blue * percent)
        pixel.red = pixel.red * darkened
        pixel.green = pixel.green * darkened
        pixel.blue = pixel.blue * darkened
    return img

#passes
# solution = darken("test_files/cougar.png", 0.3)
# solution.show()

# darken("test_files/iron.png", 0.6).show() 


def grayscale(filename):
    """
    Loop through all of the pixels.
    For each pixel, calculate the average color:
    average = (pixel.red + pixel.green + pixel.blue) / 3
    Set the pixel's red, green, and blue values equal to the average.
    """
    img = Image(filename)
    for pixel in img:
        average = (pixel.red + pixel.green + pixel.blue) / 3
        pixel.red = average
        pixel.blue = average
        pixel.green = average
        #pixel.color = average
    return img
    
# gray = grayscale("test_files/cougar.png")
# gray.show()

def sepia(filename):
    """
    To apply the sepia filter, you will need to loop over all pixels, and then for each pixel, compute these values:

true_red = 0.393*pixel.red + 0.769*pixel.green + 0.189*pixel.blue
true_green = 0.349*pixel.red + 0.686*pixel.green + 0.168*pixel.blue
true_blue = 0.272*pixel.red + 0.534*pixel.green + 0.131*pixel.blue
Then, set each pixel color. For example:

pixel.red = true_red
Finally, it may be the case that the color value is greater than 255. If that happens, set that pixel's color value to the maximum value of 255. For example:

if pixel.red > 255:
    pixel.red = 255
    """

    img = Image(filename)
    for pixel in img:
        true_red = 0.393*pixel.red + 0.769*pixel.green + 0.189*pixel.blue
        true_green = 0.349*pixel.red + 0.686*pixel.green + 0.168*pixel.blue
        true_blue = 0.272*pixel.red + 0.534*pixel.green + 0.131*pixel.blue

        if pixel.red < 255:
            pixel.red = true_red
        else:
            pixel.red = 255

        if pixel.green < 255:
            pixel.green = true_green
        else:
            pixel.green = 255

        pixel.blue = true_blue
        if pixel.blue > 255:
            pixel.blue = 255


    return img

# solution = sepia("test_files/cougar.png")
# solution.show()

def create_left_border(filename, weight):
    """
    Step 1: Create a new larger image.
    Step 2: Make the new area for the border blue.
    Do this by setting the pixel's green and red values to 0 while setting the blue value to 255.
    You can either color the entire new image blue, then copy the old image onto the new image OR 
    color only the new area blue. (The first approach is easier, but the second approach is significantly more efficient.)
    Step 3:
    Iterate over each pixel in the old image and find the correct pixel in the new image. 
    Then copy the contents of one pixel to another.
    """
    img = Image(filename)
    #get width and height, make new image with more width to account for border
    new_img = Image.blank(img.width + weight, img.height)

    #new area should be blue, (only color new area blue)
    for y in range(img.height):
        for x in range(weight):
            new_pixel = new_img.get_pixel(x, y)
            new_pixel.red = 0
            new_pixel.green = 0
            new_pixel.blue = 255

    #loop through each pixel in the old image (borderless) to find the correct pixel in the new one
    for y in range(img.height):
        for x in range(img.width):
            if x + weight < new_img.width and y < new_img.height:

                original_pixel = img.get_pixel(x, y)
                new_pixel = new_img.get_pixel(x + weight, y)

                new_pixel.red = original_pixel.red
                new_pixel.green = original_pixel.green
                new_pixel.blue = original_pixel.blue

    return new_img
        
# result_image = create_left_border("test_files/cougar.png", 50)
# result_image.show()  

###################################################
# Code below here is for extra practice and doesn't count for or against
# your grade on this lab.
def create_stripes(filename):
    """
    Create a new blank image with the same dimensions as the image given in filename, 
    but the width is an extra 50 pixels and the height is an extra 25 pixels.
    
    1. Make the pixel green if it is on a even row
    2. Make the pixel blue if it on a odd column (or slot)
    3. Otherwise, make the pixel red
    Return the newly edited image
    """
    img = Image(filename)
    new_img = Image.blank(img.width + 50, img.height + 25)

    for y in range(new_img.height):
        for x in range(new_img.width):
            pixel = new_img.get_pixel(x,y)
            if y % 2 == 0:
                pixel.red = 0
                pixel.green = 255
                pixel.blue = 0
            elif x % 2 == 1:
                pixel.red = 0
                pixel.green = 0
                pixel.blue = 255
            else:
                pixel.red = 255
                pixel.green = 0
                pixel.blue = 0

    return new_img

# image = create_stripes("test_files/cougar.png")
# image.show()

def copper_puzzle(filename):
    """
    The hidden image is in the blue and green values; however, all the blue and green values have all been divided by 20, 
    so the values are very small. The red values are all just random numbers, noise added on top to obscure things. 
    Undo these distortions to reveal the true image.
    What happens if you fix only the green values or only the blue values?
    """
    img = Image(filename)
    for pixel in img:
        pixel.red = 0
        pixel.green *= 20
        pixel.blue *= 20
    return img


#solution = copper_puzzle("test_files/copper.png")
#solution.show()
