# Plan General del Proyecto

**Nota:** Todas las referencias, bibliografía y citas deben usar la norma APA.

---

## Portada

Debe incluir, como mínimo:
- Logo de la Universidad Cenfotec
- Nombre y/o logo del equipo
- Nombre y/o logo del producto (si aplica)
- Nombre del documento
- Nombre del curso
- Nombre de los profesores del curso
- Fecha de entrega
- Período lectivo

---

## Audiencia

Las personas hacia las que va dirigido el documento, tanto a lo interno del equipo, como al grupo de facilitadores y al cliente (cuando aplique).

---

## Tabla de Contenidos

Debe mostrar los títulos (hasta 3 niveles) con la misma prioridad que tienen los apartados del documento.

---

## Introducción

Esta sección debe incluir:
- El propósito u objetivo del documento
- Referencia corta del sistema o producto a desarrollar
- La composición del documento, con una breve descripción de cada apartado

---

## Definiciones, Acrónimos y Abreviaturas

Definiciones, acrónimos y abreviaturas utilizados en el documento.

---

## Plan de Administración de la Calidad

La administración de la calidad que se llevará a cabo en el proyecto constará básicamente del:
- Control de calidad de los documentos mediante listas de verificación
- Control de calidad del producto de software mediante pruebas (tanto para los prototipos como para los productos finales)
- Diseño y realización de pruebas unitarias y pruebas de rendimiento y estrés

### Formato y Detalle de las Listas de Verificación

Las listas de verificación consisten en listas que se usan para verificar la calidad de los elementos básicos de los distintos entregables. Una lista de verificación consta de una tabla, en la que se deben incluir los siguientes encabezados:
- Descripción del elemento a revisar
- Si el documento cumple o no
- Fecha de la revisión

Debe haber una lista para cada documento entregable, y dicha lista deberá de ser entregada como adjunto a cada entregable del documento.

**⚠️ Penalidad:** Si la lista de verificación no se incluye en el artefacto que se entrega, el mismo tendrá una penalidad inmediata de 15 puntos sobre la nota.

Para ejemplos de las listas de verificación, referirse a los ejemplos en la plataforma.

### Diseño y Especificación de los Casos de Prueba (Test Cases)

Cada requerimiento que luego se convertirá en un elemento del backlog debe de pasar por el proceso de aseguramiento de calidad como parte de la verificación de que el requerimiento fue completado a cabalidad.

Para esto deben definir una serie de casos de prueba que deben de ser ejecutados para poder garantizar que la funcionalidad requerida está debidamente implementada.

En esta sección deben de definir:
- Qué datos van a recopilar en cada caso de prueba
- Cómo van a recopilar la evidencia de su ejecución

Fuera de la plantilla que va a seguir cada caso de prueba, deben definir:
- La herramienta que van a utilizar para la gestión de estos
- La jerarquía que se debe utilizar dentro de los mismos

**Ejemplo de jerarquía:**
- **Test Case:** Es una prueba simple y puntual que ayuda a validar los criterios de aceptación
- **Test Cycle:** Es el conjunto de test cases asociados a una iteración (sprint)
- **Test Plan:** Es el grupo de test cycles asociados a un proyecto con un propósito (ej: smoke test, regression, functional, etc.)

### Diseño y Especificación de las Pruebas Unitarias (Unit Tests)

En esta sección deberá de incluirse:
- La herramienta o herramientas que se van a utilizar en el proceso de las pruebas unitarias
- En qué momento las mismas deberán de ser incluidas
- En qué momento se va a verificar que el desarrollador realice las pruebas unitarias

### Diseño y Especificación de las Pruebas de Rendimiento (Performance Tests)

Deberá de detallarse:
- El diseño, alcance y especificación de la herramienta de pruebas de rendimiento que se van a utilizar
- El momento en el que se deberá de realizar
- Una explicación detallada de la herramienta y la justificación de la elección de dicha herramienta
- Pantallas y explicación de qué partes de la herramienta se deberá de usar

### Definition of Done (DoD)

En esta sección los encargados de calidad deben gestionar con el equipo de trabajo los lineamientos que deben de cumplir como equipo para considerar que un requerimiento está completado.

Pueden generarlo como un tipo de checklist con todos los aspectos que como EQUIPO definieron.

Referencia: [Ejemplos Prácticos para Crear una Definición de Terminado](https://www.scrum.org/resources/blog/ejemplos-practicos-para-crear-una-definicion-de-terminado-genial)

---

## Plan de Gestión de Riesgos

Esta sección debe incluir los riesgos identificados en cada una de las áreas y definir cuáles serán las acciones de mitigación y de contingencia a realizar en el caso de que alguno de los riesgos se presente.

### Tabla de Riesgos

Esta tabla deberá tener, por cada área (Desarrollo, producto, configuración y calidad), los riesgos identificados y la descripción de cada uno.

### Tabla de Impactos

El análisis de impactos requiere de dos tablas:
1. **Tabla de impactos:** Tendrá los rangos de impacto y los valores numéricos que dicho rango va a tener
2. **Lista de impactos:** Tendrá para cada riesgo, el nivel del impacto que tiene asociado

### Tabla de Probabilidades

El análisis de probabilidad requiere de dos tablas:
1. **Tabla de probabilidades:** Tendrá los rangos de probabilidad y los valores numéricos que dicho rango va a tener
2. **Lista de probabilidades:** Tendrá para cada riesgo, el nivel de probabilidad que tiene asociado

### Tabla de Probabilidad e Impacto

Esta es una tabla en la que se cuantifican tanto el impacto como la probabilidad para poder ubicar la prioridad que tendrá el riesgo. Nos sirve de referencia para poder clasificar y priorizar la lista de riesgos.

### Mitigaciones y Contingencias

Para cada riesgo que no sea de baja prioridad, debemos crear los planes de contingencia y mitigación.

---

## Plan de Administración de la Configuración

En esta sección deberán de definirse el proceso de control de configuración que se va a utilizar en el curso. Esto debe incluir:
- La herramienta que se va a utilizar
- Quién se va a encargar de su control
- Cómo se van a manejar las versiones de los documentos y el software
- Cuántos ambientes se van a manejar
- El proceso de respaldo de la información

### Descripción de las Herramientas

En esta sección deberán de explicarse e incluirse cada una de las herramientas que se van a usar para la gestión de la configuración. Incluye tanto la herramienta como el proveedor del servicio.

### Administración del Repositorio

En esta sección se deberá de explicar:
- La estructura del repositorio
- El encargado
- El flujo que se va a utilizar (estrategia que va a utilizar el equipo para manejar las diferentes ramas)

### Reglas del Repositorio

En esta sección se deberá de explicar las reglas que cada desarrollador debe seguir para el uso del repositorio, incluyendo:
- La frecuencia de commits
- La especificación de lo que debe subir

---

## Plan de Estándares

En esta sección se deben definir los estándares de desarrollo que se van a seguir a lo largo del proyecto. Esta sección deberá incluir:
- Estándares de color y controles de interfaz gráfica
- Estándares de nomenclatura de código
- Estándares de nomenclatura de base de datos
- Estándares de documentación (Java Doc obligatorio, tanto de código como de los objetos de la base de datos)

### Estándares de Interfaz Gráfica

En esta sección se debe incluir el detalle de los estándares de interfaz gráfica:
- Paleta de colores
- Nomenclatura de controles
- Definición de cada uno de los componentes que se van a utilizar a lo largo de todo el producto

Ejemplos de componentes: botones, textboxes, dropdowns, tablas, listboxes, radiobuttons, etc.

Referencia: [16 Sistemas de Diseño de Grandes Empresas](https://medium.com/magnt/16-sistemas-de-dise%C3%B1o-de-grandes-empresas-46efe431a289)

### Estándares de Codificación

Esta sección debe incluir el detalle de los estándares de codificación:
- Estándares de bases de datos
- Código en Angular
- Código en JavaScript
- Código en Java (Java Doc obligatorio)

---

## Plan de Administración del Tiempo

En esta sección se debe incluirse:
- WBS (Estructura de Desglose de Trabajo)
- Diagrama de red
- Especificación de las herramientas que se van a utilizar para las minutas, control de tareas y administración del proyecto

### Estructura de Desglose de Trabajo (WBS)

Debe incluirse y explicarse la estructura que presenta el desglose de cada uno de los elementos de cada entregable. Incluye:
- Los documentos
- Los informes a nivel de documentación
- A nivel de código: los módulos y las historias de usuario que lo conforman

### Diagrama de Red

Debe de incluir el diagrama de precedencia de cada una de las historias de usuario identificadas de forma parcial en el proyecto.

### Herramienta de Gestión de Proyectos

En esta sección se debe estipular cuál herramienta de manejo de proyectos va a utilizar el equipo de trabajo.

Adicionalmente deben de definir cuál es el flujo de trabajo que van a utilizar para cada historia de usuario.

Referencia: [Crear un nuevo Workflow en Jira](https://www.atlassian.com/es/software/jira/guides/workflows/tutorials#create-new-workflow)
