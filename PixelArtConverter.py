import os
import math
from PIL import Image, ImageDraw

print("Welcome to Pixel art converter 1.1 by @Jingyu \"Cetacean\" Zhuang. All rights reserved\n")


    
exit = False

while exit != True:
    path = input("Please enter the path of the picture.(Example: D:/pictures/picture.jpg)\n")
        
    x_pixels = int(input("Please enter the # of pixels you want horizontally.\n"))
    y_pixels = int(input("Please enter the # of pixels you want vertically.\n"))
    
    im = Image.open(path)
    width,height = im.size
    l_rgb = []
    i = 0
    
    for x in range(0, width, width//x_pixels+1):
        l_rgb.append([])
        for y in range(0, height, height//y_pixels+1):
            rgb_im = im.convert('RGB')
            r, g, b = rgb_im.getpixel((x, y))
            l_rgb[i].append((r,g,b))
        i += 1
    
    pixel = int(math.sqrt((width**2 + height**2)/(x_pixels**2 + y_pixels**2)))
    out = Image.new('RGB', (len(l_rgb)*pixel, len(l_rgb[1])*pixel))
    draw = ImageDraw.Draw(out)
    w_temp = 0
    h_temp = 0
    for i in l_rgb:
        for j in i:
            draw.rectangle(((w_temp, h_temp), (w_temp+pixel, h_temp+pixel)), fill = j)
            h_temp += pixel
        w_temp += pixel
        h_temp = 0
    
    out.show()
    save = ""
    while save != "Y" and save != "N":
        save = input("Nice picture! You want to save it? (Enter Y or N)\n")
    
    if save == "Y":
        path_out = input("Please enter the path you want to save.(Example: D:/pictures/picture2.jpg)\n")
        out.save(path_out)
    
    again = ""
    while again != "Y" and again != "N":
        again = input("Want to convert another one? (Enter Y or N)\n")
    
    if again == "N":
        exit = True
    
quit = input("\nThank you for using Pixel Converter 1.1! Press ENTER to leave.\n")
    
    


