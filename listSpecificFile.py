#listSpecificFile
import glob
import os
import sys
import datetime
import imageio

path = "G:\\IMAM97242\\HIMAWARI16_NTB\\2017\\06\\18"
x = glob.glob(path+"/"+"H08_EH*.png")
#print (x)
for nama in x:
	print (nama)
	
def create_gif(x, duration):
    images = []
	for filename in x:
		print(filename)
        #images.append(imageio.imread(filename))
    #output_file = 'Gif-%s.gif' % datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    #imageio.mimsave(output_file, images, duration=duration)

if __name__ == "__main__":
	duration = 0.15
	#create_gif(x, duration)