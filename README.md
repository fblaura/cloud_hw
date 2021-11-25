# Despliege de modelos de aprendizaje supervisado en la plataforma Azure 

Una de las formas para mostrar el desarrollo de un modelo de Machine Learning puede darse a través del despliegue en platformas basadas en la nube. En términos generales, el despliegue de modelos es el método para integrar un modelo de aprendizaje automático en un entorno de producción existente que no presente muchas limitaciones relacionadas a los recursos físicos de una máquina en especifico. La plataforma Microsoft Azure en particular, es unos de los servicios en la nube que más se utiliza para entrenar, desplegar, automatizar y gestionar modelos de aprendizaje automático. 

Para el desarrollo de este trabajo se realizará el despliegue de un modelo de aprendizaje supervisado a través de la plataforma Azure. Con el fin de desarrollar el taller final de la asignatura de Data Streaming, se realizará el ciclo MLOps, que consiste en los siguientes pasos: 

1. **Proyectos**
2. **Entrenamientos** 
3. **Registros** 
4. **Despliegue**

## Elección de proyecto/modelo para desplegar y Entrenamiento

Como elección de trabajo se tomó en cuenta un dataset proveniente de la plataforma Kaggle, cuyo objetivo es el trabajo de predicción con modelos de aprendizaje automático para predecir la estabilidad de la red eléctrica de un productor de electricidad indeterminado, el cual hace uso redes eléctricas descentralizadas inteligentes (Smart Grids).
Una red inteligente es una red eléctrica que incluye una serie de medidas de funcionamiento y energía, como contadores inteligentes, dispositivos inteligentes, recursos de energía renovable y recursos de eficiencia energética. El aspecto importante de una red inteligente recae en el control de la producción y distribución de electricidad. 
Dentro del dataset tenemos 11 atributos predictivos (tau1,tau2,tau3,tau4,p1,p2,p3,p4,g1,g2,g3,g4) y 2 objetivos (stab, stabf), los cuales se describen a continuación: 

- tau[x]: tiempo de reacción del participante (real del rango [0,5,10]s); por ejemplo Tau1, es el valor del productor de electricidad.
- p[x]: potencia nominal consumida(negativa)/producida(positiva)(real). Para los consumidores del rango [-0,5,-2]s^-2; p1 = abs(p2 + p3 + p4)
- g[x]: coeficiente (gamma) proporcional a la elasticidad del precio (real del rango [0,05,1]s^-1). g1: el valor para el productor de electricidad.
- stab: la parte real máxima de la raíz de la ecuación característica (si es positiva - el sistema es linealmente inestable sino es linealmente estable)(real)
- stabf: la etiqueta de estabilidad del sistema (categórica: estable/inestable). 
En este caso, la categórica no se usará para predecir, el modelo sólo se enfocará en la ecuación caracteristica del sistema. 

El dataset que se trabajará posee 10000 muestras, 12 columnas predictoras y 2 objetivos de predicción. El dataset está compuesto por valores numéricos representados en la tasa que detalla su descripción anterior como se ve en la siguiente figura. 

![alt text](https://github.com/fblaura/cloud_hw/blob/main/images/dataset.PNG)

Antes de iniciar con la creacción y entrenamiento de los modelos para que sean subidos a Azure, es necesario hacer la creación del grupo de recursos, espacio de Machine Learning y clusters para que pueda haber una correcta conexión con Azure.

### Creación de grupo de recursos y demás elementos en Azure

Un grupo de recursos es un contenedor que contiene recursos relacionados para una solución Azure. En este caso el grupo de recursos creado, contiene un registro de contenedor, almacén de claves, espacio de aprendizaje automático, application insights y una cuenta de almacenamiento. La imagen que refleja la creación de este grupo se puede ver a continuación: 
![alt text](https://github.com/fblaura/cloud_hw/blob/main/images/Recurso%20creado.PNG)

Los elementos del grupo de recursos nombrados de acuerdo a buenas prácticas y convenciones quedó así: 
![alt text](https://github.com/fblaura/cloud_hw/blob/main/images/Recurso.PNG)

### Creación de cluster de trabajo 

Una vez obtenido un grupo de recursos, es posible iniciar el estudio de aprendizaje automático que provee Azure, este espacio permite, crear clusters (que describen el tipo de máquina que se requiere para el procesamiento del modelo), registrar los modelos y hacer despliegue hasta obtener un endpoint que puede ser usado luego. La creación de cluster se puede ver a continuación: 
![alt text](https://github.com/fblaura/cloud_hw/blob/main/images/Compute%20cluster.PNG)

### Creación de ambientes conda/azure, workspace y modelo haciendo uso de Visual Studio Code

Para poder hacer la conexión de forma local de un modelo y la plataforma Azure es necesario crear ambiente con paquetes/librerías que permitan la conexión entre ambos. Para ello se utiliza por defecto, el entorno Anaconda para crear dichos ambientes. Con base en lo anterior, se generaron dos ambientes: uno local y uno con las librerías de Azure, como se ve en la figura a continuación: 
![alt text](https://github.com/fblaura/cloud_hw/blob/main/images/ambientes.png)
Una vez generados dichos ambientes, es posible entrenar de forma local el modelo y después de comprobar su funcionamiento en local (sobretodo cuando no sea un modelo que demande demasiados recursos) usar el otro ambiente para subir el modelo a Azure. Para generar la conexión entre el local y la plataforma se crea un workspace, el cual inicia una ventana de autenticación que relaciona tu cuenta y la subscripción donde quedará la factura por el desarrollo del modelo en la nube. 

Una vez conectado con Azure es posible entrenar un modelo en local (en caso de que lo requiera) y luego hacer el entrenamiento del modelo para que sea subido a Azure. En este caso el modelo que se desarrolló es un modelo de regresión lineal (Kernel Ridge) con ayuda de la librería Scikit-Learn; dicho modelo entrega como métricas una varianza explicada de 1.0 y un Mean Absolute Error - MAE de 0.077. 

## Registro y despliegue de modelo 

Al haber entrenado efectivamente el modelo con Azure, es posible hacer un registro del modelo (el archivo .py queda registrado en la carpeta de este repositorio), que queda guardado con un nombre determinados y unas etiquetas que hacen referencia a las métricas obtenidas durante la ejecución del modelo. La ruta del modelo que se utiliza para el registro hace relación a las salidas obtenida del entrenamiento del modelo, pues una vez termina de hacer entrenamiento con la partición de entrenamiento (X_train y Y_train) es posible salvar el modelo como un archivo pickle que será usado más adelante. El registro del modelo se puede ver a continuación: 
