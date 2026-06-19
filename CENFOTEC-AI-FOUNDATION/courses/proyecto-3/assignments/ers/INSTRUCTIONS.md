# Especificación de Requerimientos de Software — Instrucciones

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

Las personas hacia las que va dirigido el documento, tanto a lo interno del equipo, como al grupo de facilitadores y al cliente (cuando aplique). La audiencia va en una página aparte.

---

## Tabla de Contenidos

Debe mostrar los títulos (hasta 3 niveles) con la misma prioridad que tienen los apartados del documento. Va en una página aparte.

---

## I. Introducción

Esta sección debe incluir:
- El propósito u objetivo del documento
- Referencia corta del sistema o producto a desarrollar
- La composición del documento, con una breve descripción de cada apartado

---

## II. Participantes del Proyecto

Esta sección debe contener una lista con todos los participantes en el proyecto, tanto desarrolladores como clientes y usuarios. Para cada participante se deberá indicar:
- Nombre
- Papel que desempeña en el proyecto
- Organización a la que pertenece
- Cualquier otra información adicional que se considere oportuna

---

## III. Justificación de la Propuesta

Esta sección debe contener:
- Una descripción del problema y la necesidad que se desea satisfacer
- Estadísticas
- Descripción de situaciones reales
- Explicación detallada de la necesidad existente
- Cómo fue identificada la necesidad

---

## IV. Descripción de la Propuesta

Esta sección debe contener:
- Una descripción de la propuesta que el grupo va a plantear para resolver el problema
- Los productos finales a presentar
- Los módulos identificados

---

## V. Objetivos del Sistema

Esta sección debe contener una lista con los objetivos que se esperan alcanzar cuando el sistema a desarrollar esté en explotación, especificados mediante la metodología SMART (https://asana.com/es/resources/smart-goals).

**Importante:** Un objetivo es algo que se espera lograr con la implementación del sistema, **NO UN REQUERIMIENTO**.

Se requiere mínimo:
- 1 objetivo general
- 3 objetivos específicos

---

## VI. Catálogo de Requerimientos

Esta sección se divide en los perfiles de usuario, los requerimientos funcionales y los no funcionales.

### i. Perfiles de Usuario

Este apartado debe contener una lista con los perfiles o actores que se hayan identificado, especificados mediante la siguiente plantilla:

```
ACT-<id> ✔ <nombre descriptivo>

Descripción: <Descripción del rol que representa este actor>

Comentarios: <Comentarios adicionales>
```

### ii. Requerimientos

Esta sesión debe dividirse por módulos.

#### Requerimientos Funcionales

**Opción A — En el documento:**

Los requerimientos funcionales deben contener la siguiente información:

1. **Identificador único**
2. **Título**
3. **Descripción** (debe generarse en formato de historia de usuario)
4. **Prioridad**
5. **Datos de entrada**
6. **Datos de salida**
7. **Dependencias**
8. **Criterios de aceptación:**
   - TODA la funcionalidad que debe de cumplir el requerimiento
   - Incluir validaciones de campos
   - Incluir manejo de excepciones

**Opción B — En un proyecto JIRA:**

Si prefieres documentar los requerimientos funcionales en un proyecto JIRA, esta sección debe contener **únicamente un enlace al proyecto JIRA**. El proyecto debe incluir:

- **Epics** que representen los módulos del sistema
- **User Stories** con toda la información requerida (descritos arriba), distribuida en los campos de JIRA (descripción, criterios de aceptación, prioridad, linked issues para dependencias, etc.)
- Todos los requerimientos deben cumplir con los mismos estándares de calidad: claro, conciso, completo, consistente, verificable, rastreable, factible y necesario.

**Nota:** Elige una opción (A o B). No se requiere JIRA; es una alternativa para documentar los requerimientos funcionales si lo prefieres.

#### Requerimientos No Funcionales

Esta subsección debe contener la lista de requisitos no funcionales del sistema que se hayan identificado, especificados mediante la siguiente plantilla:

1. **Identificador único**
2. **Título**
3. **Descripción**
4. **Prioridad**
5. **Criterio de aceptación**
6. **Dependencias**

#### Matriz de Requerimientos

La matriz de requerimientos es un artefacto que debe mostrar la relación de cada uno de los requerimientos de la aplicación con los objetivos definidos al inicio de este documento.

- Las **filas** de la matriz son cada uno de los requerimientos
- Las **columnas** de la matriz son los objetivos

Cuando un requerimiento una vez completado contribuya con la obtención de un objetivo, se realiza la asociación de este con el objetivo.

---

## VII. Modelo Conceptual

Muestra gráficamente los conceptos identificados como parte del problema y las relaciones entre estos. Se debe seguir el estándar de UML para realizar el modelo conceptual.

Deberá presentarse, además, una descripción en prosa del contenido del modelo, su finalidad y cuál es la importancia de este. En caso de ponerlo en un Anexo, hacer referencia al mismo.

---

## VIII. Apéndices

Los apéndices se usarán para proporcionar información adicional a la documentación obligatoria del documento. Sólo deben aparecer si se consideran oportunos y se identificarán con letras ordenadas alfabéticamente: A, B, C, etc.

---

## Estándares de Calidad para Requerimientos

Todos los requerimientos (funcionales y no funcionales) deben cumplir con las siguientes características:

- **Claro:** Redactado de manera comprensible sin ambigüedades
- **Conciso:** Breve y directo, sin información innecesaria
- **Completo:** Contiene toda la información necesaria para su evaluación e implementación
- **Consistente:** No entra en conflicto con otros requerimientos
- **Verificable:** Puede ser probado y validado de manera objetiva
- **Rastreable:** Vinculado a objetivos del sistema y documentado en la matriz
- **Factible:** Realizable con los recursos y tecnología disponibles
- **Necesario:** Justificado y vinculado a la solución del problema
