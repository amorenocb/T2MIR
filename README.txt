Juan Andrés Moreno Cortez
18.641.636-8
amorenocb@gmail.com

Tarea desarrollada en Mac Book Pro (mid 2012):
2.5Ghz Intel core i5
4GB 1600 MHz DDR3
SSD 500GB

Desarrollado en ambiente virtual de Anaconda (https://www.anaconda.com/download/) con :
- Python 3.5.2
- pyflann 1.9.1
- bumpy 1.11.3
- pandas 0.18.1

Gráficos desarrollados en Jupyter notebook 1.0.0 con matplotlib.

El correr la tarea tiene los siguientes pasos:
1. Crear los indices para cada archivo y luego consultar este con otro archivo.
2. Crear resultados de búsqueda lineal para el mismo par de archivos.
3. Computar estadísticas con el resultado del paso 1 y del paso 2 (básicamente calcular eficiencia y efectividad)
4. Agrupar todos los resultados en dos archivos: aquellos resultados obtenidos de inputs con PCA aplicado y sin PCA aplicado.
5. Agrupar estos por columna “Features” (que indica el archivo de entrada), luego por “Algoritmo” que indica que método de indexación se utilizo y luego por “Parametro” (el valor de branching en caso de kmeans y trees en el caso de kdtree). 
6. Graficar.
(Para ver ejemplo revisar jupyter notebook entregado)

Se explicara el proceso para los archivos sin PCA aplicado ya que el otro caso es análogo:
Poner el par de archivos Q y R en el mismo directorio que el archivo “indexEvaluator.py” y ejecutar:
python indexEvaluator.py [Nombre de archivo R] [Nombre de archivo Q] [Indice a ocupar kdtree|kmeans|linear] [parametro del indice, si se escoge linear dejar en blanco]
Notar que el código requiere que el nombre de los archivos sea el mismo que los que están en el drive, pues del nombre se extrae información haciendo splits. 
Una vez que se hace este proceso para todos los tipos de features (sin PCA aplicado) se deben colocar todos los resultados en una misma carpeta. 
Así mismo en esta carpeta se debe colocar el resultado de correr indexEvaluator con la opción linear, para disponibilizar los resultados del linear scan para ser comparados con los otros resultados.
Dentro de esta carpeta donde se encuentran todos los resultados se debe colocar el archivo stats.py y ejecutarlo. Este generara un archivo con la siguiente estructura:

Features, Algoritmo, Parametro, Checks, Eficiencia, Efectividad

La primera columna indica que tipo de descriptor se utilizo, la segunda el tipo de indice. El tercero el parámetro asociado al a construcción del indice, el cuarto el parámetro checks utilizado en las consultas y las ultimas dos columnas las estadísticas de esa instancia contra el resultado de linear scan.

Se puede nombrar este archivo “non-pca-stats.csv”, colocarlo en el mismo directorio que el archivo de jupyter notebook y generar los gráficos con este. 

Completar los mismos pasos para los archivos con PCA aplicado y renombrar el archivo de resultados a “pca-stats.csv”.


