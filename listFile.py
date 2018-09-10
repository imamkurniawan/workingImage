# Read nc file as list
import os
import sys
import datetime
import imageio

path = "PNG"
files = os.listdir(path)
for name in files:
    print (path+"/"+name)

def create_gif(files, duration):
    images = []
    for filename in files:
        images.append(imageio.imread(path+"/"+filename))
    output_file = 'Gif-%s.gif' % datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    imageio.mimsave(output_file, images, duration=duration)

if __name__ == "__main__":
	duration = 1
	create_gif(files, duration)