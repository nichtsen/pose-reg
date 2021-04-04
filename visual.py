import math

import numpy as np
from scipy.misc import imresize, imsave, imread
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from PIL import ImageDraw, Image

def _npcircle(draw, cx, cy, radius):
    """Draw a circle on an image using only numpy methods."""
    radius = int(radius)
    cx = int(cx)
    cy = int(cy)
    draw.ellipse((cx-radius,cy-radius,cx+radius,cy+radius), outline = 128, fill = "orange")
	
#    y, x = np.ogrid[-radius: radius, -radius: radius]
#    index = x**2 + y**2 <= radius**2
##    index = x - y <= 4 
##    index1 = x - y <= 0
  
#    image1 = image[cy-radius:cy+radius, cx-radius:cx+radius][index] 

#    image1 = (
#    image1.astype('float32') * transparency +
#    np.array(color).astype('float32') * (1.0 - transparency)).astype('uint8')
##    tmpim = image.copy()   
        
 #   image[cy-radius:cy+radius, cx-radius:cx+radius][index] = (
 #   image[cy-radius:cy+radius, cx-radius:cx+radius][index].astype('float32') * transparency +
 #   np.array(color).astype('float32') * (1.0 - transparency)).astype('uint8')
   
##    image[cy-radius:cy+radius, cx-radius:cx+radius][index1] = tmpim[cy-radius:cy+radius, cx-radius:cx+radius][index1]
         
#    image[cy-radius:cy+radius, cx-radius:cx+radius][index1] = [158, 222, 235]
#    tmpim[cy-radius:cy+radius, cx-radius:cx+radius][index1].astype('float32'))
    
#    image[cy-radius:cy+radius, cx-radius:cx+radius][index1] = tmpim[cy-radius:cy+radius, cx-radius:cx+radius][index1]
    

#    tmpim[cy-radius:cy+radius, cx-radius:cx+radius][index1].astype('float32') * (1.0 - transparency)).astype('uint8')
    
 #   image[cy-radius:cy+radius, cx-radius:cx+radius][index1] = (
#    image[cy-radius:cy+radius, cx-radius:cx+radius][index1].astype('float32') * (1.0 - transparency) +
#    tmpim[cy-radius:cy+radius, cx-radius:cx+radius][index1].astype('float32')*(1.0 - transparency)) 
    
    
    


def check_point(cur_x, cur_y, minx, miny, maxx, maxy):
    return minx < cur_x < maxx and miny < cur_y < maxy


def visualize_joints(image, pose, key, di):
    imtmp = Image.open(di+key)
    draw = ImageDraw.Draw(imtmp)	
    marker_size = 4
    minx = 2 * marker_size
    miny = 2 * marker_size
    maxx = image.shape[1] - 2 * marker_size
    maxy = image.shape[0] - 2 * marker_size
    num_joints = pose.shape[0]
    x = np.arange(0, 100, 0.02)
    y1 = np.sin(x)
    plt.plot([x, y1], linestyle='solid', linewidth=2.0)

    imtrix = [[0] * 2 for row in range(num_joints)]		  
    for p_idx in range(num_joints):
        imtrix[p_idx] = (int(pose[p_idx, 0]),int(pose[p_idx, 1]))
        cur_x = pose[p_idx, 0]
        cur_y = pose[p_idx, 1]
        if check_point(cur_x, cur_y, minx, miny, maxx, maxy):
            _npcircle(draw,
                      cur_x, cur_y,
                      marker_size)
    print(imtrix)
    draw = ImageDraw.Draw(imtmp)
    for i in range(5):
        draw.line([imtrix[i],imtrix[i+1]], 'orangered', width = 3)
    for i in range(6,11):
        draw.line([imtrix[i],imtrix[i+1]], 'orangered', width = 3)
    draw.line([imtrix[12],imtrix[13]], 'orangered', width = 3)
    for i in range(8,10):
      draw.line([imtrix[i],imtrix[12]], 'orangered', width = 3)
     

   
    for i in range(2,4):
     for j in range(8,10):
      draw.line([imtrix[i],imtrix[j]], 'orangered', width = 3)
    
    imtmp.save(di+key)