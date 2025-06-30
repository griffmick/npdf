#!/usr/bin/env python3
'''
Copyright 2025, Michael Griffiths

This file is part of npdf aka "Natural PDF".
npdf is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
npdf is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with npdf. If not, see <https://www.gnu.org/licenses/>.
'''

from wand.image import Image
import os
import magic
import natsort

if __name__=="__main__":
  images = list()

  for file in os.listdir('.'):
    if os.path.isfile(file) and magic.Magic(mime=True).from_file(file).startswith('image/'):
      images.append(file)

  images = natsort.natsorted(images)

  with Image() as pdf:
    for image in images:
      with Image(filename=image) as img:
        pdf.sequence.append(img)
    pdf.auto_orient()
    pdf.save(filename=(os.path.basename(os.getcwd())+'.pdf'))

