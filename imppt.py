import os
import sys
import glob
from PIL import ImageDraw, Image, ImageSequence 
import numpy as np
import imageio


gif_name='gif.gif'
	
def find_all_png():

    pngs = glob.glob(r"D:/time/*.png") 
    print(pngs)
    buf=[]
    for png in pngs:
        buf.append(png)
    return buf
	
def create_gif(image_list, gif_name):  

    frames = []  
    for image_name in image_list:  
        frames.append(imageio.imread(image_name))  
    # Save them as frames into a gif   
    imageio.mimsave(gif_name, frames, 'GIF', duration = 0.4)  

    return 
	
if __name__ == '__main__':

    buff = find_all_png()
    create_gif(buff, gif_name )

	
#	iter = ImageSequence.Iterator(iml)
	#~ size = (600,350)  
#	ima = iml[1]
#	ima.show()
	#~ for im in iml:  
		#~ im.thumbnail(size, Image.ANTIALIAS)  
#	gifd='d:/time/'  
#	writeGif(gifd+"fff.gif", iml, duration=0.05,nq=0.1)  