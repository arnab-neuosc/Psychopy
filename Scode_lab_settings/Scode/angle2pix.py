import math

# def angle2pix(cfgScreen, angle):

#     pixSize = (cfgScreen['dispSize']['width'] / 10) / cfgScreen['resolution']['width']  # mm/pix
    
#     sz = float(2 * cfgScreen['distance'] * math.tan(math.pi * angle / (2 * 180)))  # distance in cm
    
#     pixel = round(sz / pixSize)  # pixel

#     return pixel


# def angle2pix(cfgScreen, angle):
#     # Ensure that the values are numeric
#     distance = float(cfgScreen['distance'])
#     pixSize = (cfgScreen['dispSize']['width'] / 10) / float(cfgScreen['resolution']['width'])  # mm/pix
    
#     sz = 2 * distance * math.tan(math.pi * angle / (2 * 180))  # distance in cm
    
#     pixel = round(sz / pixSize)  # pixel

#     return pixel
def angle2pix(cfgScreen, angle):
    pixSize = (cfgScreen['dispSize']['width'] / 10) / cfgScreen['resolution']['width']  # mm/pix
    
    if isinstance(angle, (int, float)):  # Check if angle is a scalar
        sz = float(2 * cfgScreen['distance'] * math.tan(math.pi * angle / (2 * 180)))  # distance in cm
        pixel = round(sz / pixSize)  # pixel
        return pixel
    elif isinstance(angle, (list, tuple)):  # Check if angle is a list or tuple
        pixels = []
        for ang in angle:
            sz = float(2 * cfgScreen['distance'] * math.tan(math.pi * ang / (2 * 180)))  # distance in cm
            pixel = round(sz / pixSize)  # pixel
            pixels.append(pixel)
        return pixels