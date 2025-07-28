# Analisis y segmentación automática de mastocitos
#### Programa de aprendizaje automático y procesamiento de imagenes donde se realiza el analisis y la segmentación automática de los mastocitos (célula cancerígena) presentes en muestras tumorales caninas a través de una máquina de soporte vectorial.

## Introducción
Este programa desarrollado en lenguaje python fue desarrollado para realizar la detección de celulas cancerígenas (mastocitos) a través del procesamiento de imagenes para poder funcionar un modelo de aprendizaje automático que sea capaz de clasificar automáticamente las celulas sanas y las celulas tumorales.

## 💻 Tech Stack
- Para desarrollar el proyecto se utilizó el lenguaje **Python** dentro de **Visual Studio Code** y **Google Collab**.
- Se realiza la extracción de caracteristicas de la imagen tales como propiedades geométricas (área, excentricidad, solidez), Estadísticas de textura basadas en la matriz GLCM (como contraste, energía, correlación, ASM) e Intensidad media y desviación estándar de los píxeles.
- Se hizo uso de la máquina de soporte vectorial (SVM) como modelo de aprendizaje.
- Se utilizó la biblioteca Labelme
- En el proceso de desarrollo se implemento control de versionamiento utilizando **Git** y manejo de repositorios en **Github**.

## 📲 Resultados del programa
- Al ejecutar la aplicación, el programa toma imagenes de la carpeta "src" para iniciar el entrenamiento del modelo, aplicando la SVM el programa entrenado fue capaz de realizar la siguiente detección de mastocitos sanos y tumorales como se aprecia en la siguiente imagen:
<img src="https://github.com/alexisserapio/segmentacion-mastocitos-imgproc/blob/main/output/clusters-en-la-imagen-de-entrenamiento.jpg" alt="Captura de Pantalla que contiene las caracteristicas de las imagenes procesadas para entrenamiento" width="500" height="350">

- Durante este proceso, se miden las caracteristicas dentro de cada imagen de prueba obteniendo como resultado la siguiente salida:
<img src="https://github.com/alexisserapio/segmentacion-mastocitos-imgproc/blob/main/output/caracteristicas.png" alt="Captura de Pantalla que contiene las caracteristicas de las imagenes procesadas para entrenamiento" width="500" height="350">

- Una vez entrenado el modelo, se procesa la imagen que se quiere analizar ejecutando el reconocimiento de acuerdo a lo aprendido en el entrenamiento, una vez se termina de procesar, se tienen los siguientes resultados:
<img src="https://github.com/alexisserapio/segmentacion-mastocitos-imgproc/blob/main/output/salida-con-celulas-detectadas.jpg" alt="Captura de Pantalla que contiene las caracteristicas de las imagenes procesadas para entrenamiento" width="500" height="350">
