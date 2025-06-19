# src/preprocesado.py

import numpy as np
from skimage import filters, morphology
from skimage.segmentation import clear_border
from src import config

def preprocess_image(image):
    gray_image = np.array(image.convert("L"))
    smoothed = filters.gaussian(gray_image, sigma=config.GAUSSIAN_SIGMA)
    binary = smoothed < config.THRESHOLD_VALUE
    cleaned = morphology.remove_small_objects(binary, min_size=config.MIN_REGION_SIZE)
    cleaned = morphology.remove_small_holes(cleaned, area_threshold=config.HOLE_AREA_THRESHOLD)
    cleaned = clear_border(cleaned)
    return cleaned
