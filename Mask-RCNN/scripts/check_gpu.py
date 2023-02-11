import sys
import random
import math
import numpy as np
import cv2
import matplotlib as plt
import json
import pydicom
from imgaug import augmenters as iaa
from tqdm import tqdm
import pandas as pd 
import glob
from sklearn.model_selection import KFold 
from tensorflow.python.client import device_lib

print(device_lib.list_local_devices())