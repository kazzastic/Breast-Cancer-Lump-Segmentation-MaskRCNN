import os 
import numpy as np
from PIL import Image
path = '/home/kazzastic/Downloads/send/'
out_path = '/home/kazzastic/Downloads/send/'
my_dir = os.listdir(path)

for i in range(len(my_dir)):
    img = np.load(path+my_dir[i], allow_pickle=True)
    out = out_path + str(my_dir[i])
    out = out.strip('.npy')
    out = out + '.png'
    img = Image.fromarray(img)
    img.save(out)