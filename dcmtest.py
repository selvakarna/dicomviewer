from nilearn import image
import nilearn
import numpy as np
import cv2
from pydicom import dcmread
# import mayavi
from nilearn import plotting
from mayavi import mlab
import cv2
import os
import glob
import pydicom
##########
input_dir=r'/home/oem/Desktop/Project/DICOM/DCM/Shoulder'
data_path = os.path.join(input_dir, '*dcm')
files = glob.glob(data_path)
data=[]
def dcm2bndry(files):
        for f1 in sorted(files):
             RefDs=pydicom.dcmread(f1)
             print(RefDs)
             pxl=RefDs.pixel_array
             data.append(pxl)


            #  cv2.namedWindow('image',cv2.WINDOW_GUI_NORMAL)

            #  cv2.imshow('image',pxl)
            #  cv2.waitKey(1)
        return data


s=dcm2bndry(files)
print(np.shape(s))

ss=np.array(s)


# mlab.pipeline.volume(mlab.pipeline.scalar_field(ss))
                     

mlab.contour3d(ss)

# s = mlab.mesh(ss)
mlab.show()

