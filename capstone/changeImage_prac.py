#!/usr/bin/env python3

import os
from PIL import Image

path = os.path.expanduser('~') + '/supplier-data/images/'

for image in os.listdir(path):
    if '.tiff' in image and '.' not in image[0]:
        img = Image.open(path + image)
        img.resize((600, 400)).convert("RGB").save(path + image.split('.')[0] + '.jpeg', 'jpeg')
        img.close()

#!/usr/bin/env python3
import os
from PIL import Image
import re

inpath = os.path.expanduser('~') + '/images/'
outpath = os.path.expanduser('~') + '/opt/icons/'

def operate(infile,outfile):
  im=Image.open(infile)
  im.rotate(90).resize((128,128)).convert('RGB').save(outfile,"JPEG")

def main(inpath,outpath):
  for f in os.listdir(inpath):
    if f[0:2]=="ic":
      f_start, f_end=os.path.splitext(f)
      in_f=os.path.join(inpath,f)
      out_f=os.path.join(outpath,f_start)
      operate(in_f,out_f)

if __name__=="__main__":
  main(inpath,outpath)