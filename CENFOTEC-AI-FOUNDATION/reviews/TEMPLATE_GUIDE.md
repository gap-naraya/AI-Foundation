# Guía de Uso: Plantilla de Retroalimentación

Esta guía explica cómo usar la plantilla de retroalimentación (`REVIEW_TEMPLATE.md`) para mantener consistencia en todas las evaluaciones.

---

## Estructura del Archivo

### 1. Título
```markdown
# [Nombre del Entregable] — [Nombre del Grupo/Estudiante]
```
**Ejemplo:** `# Plan General de Proyecto — Grupo FocusKids`

---

## 2. Desglose de Calificación

### Estructura de la tabla:
- **Criterio**: Nombre del criterio de la rúbrica
- **Máx**: Puntos máximos posibles para ese criterio
- **Perdido**: Puntos deducidos (usar número negativo, ej: -5)
- **Ganado**: Puntos obtenidos (Máx + Perdido = Ganado)
- **Notas**: Explicación breve y específica de qué se evaluó y por qué se dedujo

### Reglas importantes:
- Cada deducción debe tener una razón clara
- Las notas deben ser específicas, no genéricas
- Referenciar secciones o elementos concretos del entregable
-Asegurate de revisar con profundidad el contenido de cada seccion de acuerdo a lo que se espera en la misma.
- La fila final muestra totales: **Máx**, **Total Deducido**, **Total Ganado**

**Ejemplo:**
```
| Plan de Calidad | 20 | -5 | 15 | Excelente cobertura: listas de verificación, casos de prueba, pruebas unitarias y DoD incluida. Pero hay deficiencias en la definición de las pruebas de rendimiento |
```

---

## 3. Calificación Final

Formato: `## Calificación Final: **[Puntos] / [Máximo]**`

**Ejemplo:** `## Calificación Final: **87 / 100**`

---

## 4. Retroalimentación

Esta sección tiene dos subsecciones: **Fortalezas** y **Áreas de mejora**.

### Fortalezas

**Reglas:**
- Mínimo 3 fortalezas (o según corresponda)
- Cada una debe ser numerada y tener un **título en negrita**
- Incluir descripción específica con ejemplos concretos
- Referenciar secciones del trabajo
- Ser genuino y reconocer el esfuerzo

**Formato:**
```markdown
**Fortalezas:**

1. **[Fortaleza Principal]** — [Descripción con ejemplos específicos.]

2. **[Fortaleza Principal]** — [Descripción con ejemplos específicos.]

3. **[Fortaleza Principal]** — [Descripción con ejemplos específicos.]
```

**Ejemplo:**
```markdown
**Fortalezas:**

1. **Estándares técnicos muy detallados** — La sección de estándares es sobresaliente: especifican colores en formato HEX (#B8A7F0, #7ECEC4, etc.), tamaños de fuente exactos (28-32px para títulos, 16px para cuerpo), espaciado específico, y criterios de accesibilidad WCAG 2.1.

2. **Análisis de riesgos comprehensivo** — 15 riesgos identificados cubriendo múltiples dimensiones (desarrollo, producto, configuración, calidad). Las matrices de probabilidad-impacto con mitigaciones para cada riesgo muestran madurez en gestión de riesgos.
```

### Áreas de Mejora

**Reglas:**
- Agrega todas las deficiencias encontradas en el documento.
- Cada una debe ser numerada
- **Ser constructivo y específico** — explicar dónde está el problema y cómo mejorarlo
- Referenciar indicaciones previas, estándares del curso, o rubrica si aplica
- No ser punitivista — enfocarse en aprendizaje
- Si hay incumplimiento grave, aclararlo

**Formato:**
```markdown
**Áreas de mejora:**

1. [Área]: [Descripción del problema. Dónde está, por qué es un problema, cómo corregirlo.]

2. [Área]: [Descripción del problema. Ser constructivo y ofrecer alternativas.]

3. [Área]: [Descripción del problema. Si aplica, referenciar indicaciones previas.]
```

**Ejemplo:**
```markdown
**Áreas de mejora:**

1. La EDT debe reflejar estrictamente el trabajo que el equipo va a realizar. Ustedes incluyeron el hito **1.3** que no deben trabajar en proyecto 3, por lo que no debería estar ahí. Pasa igual con el **1.2.3** y el paquete **1.1.5.4**. Esto denota una falta de atención a las indicaciones brindadas.

2. No agregaron los landing pages a la EDT. Estos son necesarios para cumplir el alcance del proyecto.

3. Se define POstman como herramienta para realizar pruebas de rendimiento, pero esta no es una herramienta apropiada para eso. Deben clarificar esto con el profesor Gino para no perder esta parte del alcance.
```

### Cierre

Terminar con una frase positiva y alentadora que reconozca el esfuerzo.

**Ejemplo:** `¡Excelente trabajo del equipo CAAG!`

---

## Consejos Generales

### ✅ Sí hacer:
- Ser específico con números, porcentajes, referencias
- Incluir ejemplos concretos del trabajo
- Explicar **por qué** algo es una fortaleza o un área de mejora
- Ofrecer sugerencias constructivas
- Reconocer el esfuerzo genuinamente
- Mantener tono profesional pero accesible

### ❌ No hacer:
- Ser genérico ("buen trabajo", "necesita mejorar")
- Omitir razones para deducir puntos
- Usar lenguaje punitivista o descalificador
- Hacer suposiciones sobre intenciones del equipo
- Mezclar idiomas (todo en español)

---

## Flujo de Uso

1. **Copiar la plantilla** a: `reviews/[CURSO]/[ASIGNACION]/feedback/[GRUPO].md`
2. **Reemplazar placeholders** con información real
3. **Llenar la tabla de calificaciones** usando la rúbrica del entregable
4. **Escribir fortalezas** basadas en lo que observó en el trabajo
5. **Escribir áreas de mejora** siendo constructivo y específico
6. **Cierre positivo** que reconozca el esfuerzo
7. **Revisar** que todo esté en español y sea consistente

---

## Ejemplo Completo

Ver archivo: `reviews/proyecto-3/plan-general-de-proyecto/feedback/Grupo-FocusKids.md`
