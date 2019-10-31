## Bulk image resizer

# This script simply resizes all the images in a folder to the input percentage from their
# original size. It's useful for shrinking large cell phone pictures down
# to a size that's more manageable for model training.

# Usage: python resizer.py --I=PathToInputImageFiles --O=PathToOutputImageFiles --SP=%Shrinking
import warnings
warnings.filterwarnings('ignore',category=FutureWarning)
import cv2
import numpy as np
import os
import tensorflow as tf

flags = tf.app.flags

flags.DEFINE_string('I', '', 'Path to the image directory')
flags.DEFINE_string('O', '', 'Path to output TFRecord')
flags.DEFINE_string('SP', '', 'Scale percent')
FLAGS = flags.FLAGS

dir_path = os.path.join(os.getcwd(), FLAGS.I)
out_dir = os.path.join(os.getcwd(), FLAGS.O)
s_per = float(int(FLAGS.SP)/100)
if (os.path.exists(out_dir) == False):
    os.mkdir(out_dir)

for filename in os.listdir(dir_path):
    # If the images are not .JPG images, change the line below to match the image type.
    #print(filename)
    if filename.endswith(".jpg"):
        try:
            image = cv2.imread(os.path.join(dir_path,filename) , cv2.IMREAD_UNCHANGED)
            width = int(image.shape[1] * s_per)
            height = int(image.shape[0] * s_per)
            dim = (width, height)
            resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
            cv2.imwrite(os.path.join(out_dir,filename),resized)
        except AttributeError:
            print("shape not found")
        except:
            print("error happened")