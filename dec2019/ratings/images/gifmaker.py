import imageio
import os

path = 'C:/Users/marku/Desktop/medium/dec2019/ratings/images/' # on Mac: right click on a folder, hold down option, and click "copy as pathname"

image_folder = os.fsencode(path)

filenames = []

for file in os.listdir(image_folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.jpeg', '.png', '.gif') ):
        filenames.append(path+filename)

filenames.sort() # this iteration technique has no built in order, so sort the frames
print(filenames)
images = list(map(lambda filename: imageio.imread(filename), filenames))

imageio.mimsave(os.path.join('movie6.gif'), images, duration = 0.5)