# Analisis y segmentación automática de mastocitos
#### Programa de aprendizaje automático y procesamiento de imagenes donde se realiza el analisis y la segmentación automática de los mastocitos (célula cancerígena) presentes en muestras tumorales caninas y clasificarlas tanto en sanas como en enfermas a través de una máquina de soporte vectorial.

## Introducción
Este programa desarrollado en lenguaje python fue desarrollado para realizar la detección de celulas cancerígenas (mastocitos) a través del procesamiento de imagenes para poder funcionar un modelo de aprendizaje automático que sea capaz de clasificar automáticamente las celulas sanas y las celulas tumorales.

Dentro de la veterinaria canina, los mastocitomas son un tipo común de tumor cutáneo en perros, destacando debido a su potencial agresividad y alta incidencia. Estos mastocitomas se dan dentro de los mastocitos, por lo que con una imagen muestra de lo que se considera podria ser o no un tumor se puede determinar si el perro sufre de esta enfermedad o no, con la ayuda de un modelo entrenado, es posible detectar a partir de una imagen si el paciente sufre de la condición o no.

<img src="https://github.com/alexisserapio/segmentacion-mastocitos-imgproc/blob/main/data/mastocito_mastocitoma.png" alt="Captura de Pantalla que contiene las caracteristicas de las imagenes procesadas para entrenamiento" width="500" height="350">


Para esto, se eligió utilizar una Máquina de Soporte Vectorial (SVM) como modelo de aprendizaje debido a la robustez que presenta frente a valores atípicos al suavizar el margen utilizando un parámetro de coste, de igual manera se realizó una clasificación y entrenamiento previo al programa para poder medir a través de las caracteristicas de las imagenes un resultado medible obteniendo un margen del 94% de precisión en este modelo.

## 💻 Tech Stack
- Para desarrollar el proyecto se utilizó el lenguaje **Python** dentro de **Visual Studio Code** y **Google Collab**.
- Se hizo uso de **Labelme** para realizar una clasificación de entrenamiento manual de las células tumorales y las células sanas.
- Se utilizan las librerías **numpy** para el análisis de datos, **PIL** y **scikit-image** para realizar el procesado de las imagenes y finalmente **scikit-learn** para el machine learning.
- Se hizo uso de la máquina de soporte vectorial (SVM) como modelo de aprendizaje.
- Se realiza la extracción de caracteristicas de la imagen tales como propiedades geométricas (área, excentricidad, solidez), Estadísticas de textura basadas en la matriz GLCM (como contraste, energía, correlación, ASM) e Intensidad media y desviación estándar de los píxeles.
- En el proceso de desarrollo se implemento control de versionamiento utilizando **Git** y manejo de repositorios en **Github**.

## 📲 Como trabaja el programa:
- Al ejecutar la aplicación, el programa toma imagenes de la carpeta "src" donde previamente se etiquetaron con labelme las células sanas de las células tumorales para dar inicio con el entrenamiento del modelo:
<img src="https://github.com/alexisserapio/segmentacion-mastocitos-imgproc/blob/main/output/clusters-en-la-imagen-de-entrenamiento.jpg" alt="Captura de Pantalla que contiene las caracteristicas de las imagenes procesadas para entrenamiento" width="500" height="350">

- Durante este proceso, se miden las caracteristicas dentro de cada imagen de prueba obteniendo como resultado la siguiente salida:
<img src="https://github.com/alexisserapio/segmentacion-mastocitos-imgproc/blob/main/output/caracteristicas.png" alt="Captura de Pantalla que contiene las caracteristicas de las imagenes procesadas para entrenamiento" width="500" height="350">

Como podemos apreciar, se llegó a obtener una precisión global del 0.94 que fue la medición más alta que pudimos calcular teniendo en cuenta las caracteristicas que eligimos para clasificar ambos tipos de célula.

---
- Una vez entrenado el modelo aplicando la SVM, se procesa la imagen que se quiere analizar ejecutando el reconocimiento de acuerdo a lo aprendido en el entrenamiento.
- El programa entrenado fue capaz de realizar la siguiente detección de mastocitos sanos y tumorales como se aprecia en la siguiente imagen:
<img src="https://github.com/alexisserapio/segmentacion-mastocitos-imgproc/blob/main/output/salida-con-celulas-detectadas.jpg" alt="Captura de Pantalla que contiene las caracteristicas de las imagenes procesadas para entrenamiento" width="500" height="350">

## 📣 To-do
- Aumentar las imagenes de entrenamiento del modelo para poder aumentar la precisión de las predicciones.
- Realizar optimización de los códigos.
