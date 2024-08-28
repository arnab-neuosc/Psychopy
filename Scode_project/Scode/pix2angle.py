import math

def pix2angle(display, pix):

    # Calculate pixel size in cm
    pix_size = display['width'] / display['resolution']  # cm per pixel
    
    # Convert pixels to cm
    sz = pix * pix_size  # cm

    # Calculate visual angle in degrees
    ang = 2 * 180 * math.atan(sz / (2 * display['dist'])) / math.pi

    return ang

# Example usage:
display = {
    'dist': 65,          # Distance from screen in cm
    'width': 28.65,      # Width of screen in cm
    'resolution': 1680   # Number of pixels in horizontal direction
}



