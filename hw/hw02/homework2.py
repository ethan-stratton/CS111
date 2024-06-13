from byuimage import Image

def flipped(filename):
    """
    Takes any image and flips it vertically
    """
    #print(f"debug: {filename}")
    img = Image(filename)
    
    #create new image the same size as the original image
    new_img = Image.blank(img.width, img.height)
    #loop over all pixels and copy them to the right position in the new img
    for y in range(0, img.height):
        for x in range(0, img.width):
            #save pixel in og image
            old_pixel = img.get_pixel(x,y)
            #put that pixel in the new image in the right place
            new_pixel = new_img.get_pixel(x, img.height - y - 1)

            new_pixel.red = old_pixel.red
            new_pixel.green = old_pixel.green
            new_pixel.blue = old_pixel.blue
    return new_img

def make_borders(filename, thickness, red, green, blue):
    """
     that will put a border of equal thickness all the way around an image. 
     This function will take as input a filename containing an image to modify, 
     the thickness of the border, and color values for the red, green, and blue channels in the border region.
    """
    img = Image(filename)

    new_width = img.width + (thickness * 2)
    new_height = img.height + (thickness * 2)
    new_img = Image.blank(new_width, new_height)

    #this loop sets the border colors in the new image
    for y in range(new_img.height):
        for x in range(new_img.width):
            if x < thickness or x >= new_width - thickness or y < thickness or y >= new_height - thickness:
                #set border colors
                pixel = new_img.get_pixel(x, y)
                pixel.red = red
                pixel.green = green
                pixel.blue = blue

    for y in range(img.height):
        for x in range(img.width):
            #get colors from OG image
            transferred_pixel = img.get_pixel(x, y)
            new_x = x + thickness
            new_y = y + thickness
            #transfer them to the correct position in the new image
            #starting at new_x and new_y, pixels at x, y are equal to old pixels

            original_pixel = img.get_pixel(x, y)
            new_pixel = new_img.get_pixel(new_x, new_y)

            new_pixel.red = original_pixel.red
            new_pixel.green = original_pixel.green
            new_pixel.blue = original_pixel.blue
            

    
    return new_img

def main():
    """
    Runs programs functions
    """
    image_filename = "test_files/landscape.png"
    #print(f"Debug: {image_filename}")

    #flipped(image_filename).show()

    make_borders(image_filename, 50, 0, 0, 0).show()



if __name__ == "__main__":
    main()