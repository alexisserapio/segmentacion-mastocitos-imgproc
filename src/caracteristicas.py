# src/caracteristicas.py

import numpy as np
from skimage.feature import graycomatrix, graycoprops
from skimage.measure import regionprops, label

def extract_features(image, mask):
    gray_image = np.array(image.convert("L"))
    masked_image = np.where(mask, gray_image, 0)
    region_area = mask.sum()

    glcm = graycomatrix(masked_image, distances=[1, 2, 3, 4], 
                        angles=[0, np.pi / 4, np.pi / 6, np.pi / 3, np.pi / 2,
                                2 * np.pi / 3, 5 * np.pi / 6, 3 * np.pi / 4],
                        levels=256, symmetric=True, normed=True)

    contrast = graycoprops(glcm, 'contrast').mean()
    energy = graycoprops(glcm, 'energy').mean()
    correlation = graycoprops(glcm, 'correlation').mean()
    dissimilarity = graycoprops(glcm, 'dissimilarity').mean()
    asm = graycoprops(glcm, 'ASM').mean()

    mean_intensity = masked_image[mask].mean()
    std_intensity = masked_image[mask].std()

    labeled_mask = label(mask)
    props = regionprops(labeled_mask)
    eccentricity = props[0].eccentricity if props else 0
    solidity = props[0].solidity if props else 0

    return [region_area, contrast, energy, correlation, mean_intensity,
            std_intensity, eccentricity, solidity, dissimilarity, asm]
