PROYECTO: ESTRUCTURAS DE DATOS Y MACHINE LEARNING
Basado en el libro: "50 algoritmos que todo programador debe conocer"

Autor: Luis José Sánchez Carreño
Repositorio de estudio, implementación y experimentación

======================================================================

1. INTRODUCCIÓN

Este repositorio tiene como objetivo central documentar, implementar y
comprender en profundidad los algoritmos fundamentales que todo programador
debe dominar, tomando como eje principal el libro:

"50 algoritmos que todo programador debe conocer"
Autor: Imran Ahmad

El proyecto no se limita a la simple implementación de código, sino que busca
desarrollar una comprensión estructural, matemática y computacional de cada
algoritmo, conectando los conceptos con aplicaciones reales en:

- Estructuras de datos
- Optimización
- Machine Learning
- Análisis de algoritmos
- Pensamiento computacional avanzado

======================================================================

2. OBJETIVO GENERAL

Construir una base sólida y progresiva en algoritmos clásicos, estructuras de
datos y fundamentos algorítmicos, que sirva como soporte técnico para el
desarrollo posterior de sistemas complejos, incluyendo modelos de Machine
Learning y sistemas inteligentes.

======================================================================

3. OBJETIVOS ESPECÍFICOS

- Implementar cada algoritmo desde cero, evitando dependencias innecesarias.
- Analizar la complejidad temporal y espacial (Big-O).
- Comprender el razonamiento matemático detrás de cada solución.
- Comparar enfoques ingenuos vs optimizados.
- Relacionar los algoritmos clásicos con aplicaciones modernas en ML.
- Documentar aprendizajes, errores comunes y mejoras.

======================================================================

4. ALCANCE DEL PROYECTO

Este repositorio cubre:

- Algoritmos clásicos descritos en el libro.
- Estructuras de datos necesarias para su implementación.
- Variaciones y optimizaciones relevantes.
- Ejercicios prácticos y casos de prueba.
- Notas teóricas y reflexiones técnicas.

NO es un curso introductorio.
Se asume conocimiento básico de programación y matemáticas discretas.

======================================================================

5. METODOLOGÍA DE TRABAJO

Para cada algoritmo se sigue el mismo protocolo:

1. Estudio teórico del algoritmo
2. Comprensión del problema que resuelve
3. Implementación desde cero
4. Análisis de complejidad
5. Pruebas con distintos casos
6. Reflexión y conexión con ML o sistemas reales

No se avanza a un nuevo algoritmo sin comprender completamente el anterior.

======================================================================

6. ESTRUCTURA DEL REPOSITORIO

El proyecto se organiza siguiendo una arquitectura modular, clara y escalable,
donde el núcleo del conocimiento reside en la carpeta `src/`.

La estructura actual es la siguiente:

src/
├── __init__.py
│
├── data_structures/
│   ├── arrays/
│   ├── linked_lists/
│   ├── stacks/
│   ├── queues/
│   ├── trees/
│   ├── heaps/
│   └── graphs/
│
├── algorithms/
│   ├── sorting/
│   ├── searching/
│   ├── recursion/
│   ├── greedy/
│   ├── dynamic_programming/
│   └── graph_algorithms/
│
├── machine_learning/
│   ├── optimization/
│   ├── feature_selection/
│   ├── clustering_basics/
│   └── search_spaces/
│
└── notes/
    ├── theory.txt
    ├── reflections.txt
    └── mistakes_and_lessons.txt


La carpeta `src/` contiene toda la lógica principal del proyecto:

- `data_structures/`: Implementaciones fundamentales de estructuras de datos.
- `algorithms/`: Algoritmos clásicos organizados por paradigma.
- `machine_learning/`: Conexiones conceptuales y algorítmicas con ML.
- `notes/`: Documentación teórica, reflexiones y lecciones aprendidas.

Todas las carpetas Python contienen su respectivo `__init__.py`,
permitiendo una correcta modularización e importación.

------------------------------------------------------------

La carpeta de pruebas se encuentra separada:

test/
├── test_data_structures.py
├── test_algorithms.py
└── test_machine_learning.py

Aquí se validan las implementaciones mediante casos de prueba,
garantizando corrección y consistencia.

------------------------------------------------------------

Esta estructura permite:
- Crecimiento ordenado
- Separación clara de responsabilidades
- Escalabilidad académica y técnica
- Reutilización futura en proyectos más complejos


======================================================================

7. LENGUAJE Y HERRAMIENTAS

- Lenguaje principal: Python
- Paradigma: Imperativo / Algorítmico
- Enfoque: Claridad > Micro-optimización
- Dependencias: mínimas o nulas

======================================================================

8. RELACIÓN CON MACHINE LEARNING

Muchos algoritmos clásicos son la base directa de técnicas modernas de ML.

Ejemplos:
- Búsqueda y optimización → entrenamiento de modelos
- Grafos → redes neuronales, embeddings
- Programación dinámica → optimización y RL
- Árboles → árboles de decisión y ensembles

Este repositorio establece esas conexiones explícitamente.

======================================================================

9. ESTADO DEL PROYECTO

Estado: EN DESARROLLO ACTIVO

El proyecto crece de forma incremental y disciplinada.
Cada algoritmo agregado implica comprensión completa y documentación.

======================================================================

10. FILOSOFÍA DEL PROYECTO

- No copiar código sin entenderlo
- No usar librerías como sustituto del razonamiento
- Priorizar comprensión profunda sobre velocidad
- Construir conocimiento reutilizable

======================================================================

11. NOTA FINAL

Este repositorio es tanto un registro de aprendizaje como una base técnica
para proyectos futuros en ingeniería de software y machine learning.

Su valor no está en la cantidad de código, sino en la calidad del
razonamiento detrás de cada línea.

======================================================================
