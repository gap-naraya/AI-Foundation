# Plan General de Proyecto — PiedPiper

## Desglose de Calificación

| Criterio | Máx | Perdido | Ganado | Notas |
|---|---|---|---|---|
| Documento y Estructura | 10 | -1 | 9 | Portada completa, tabla de contenidos clara, secciones bien organizadas. Minor: sin etiqueta "Portada" explícita |
| Plan de Calidad | 20 | -2 | 18 | Listas de verificación (4 anexos), jerarquía Test Case→Test Cycle→Test Plan clara, unit tests (JUnit 5, Mockito, Jasmine, Karma), Definition of Done con 9 criterios. Falta: métricas específicas de rendimiento (ej: target response times, thresholds) |
| Plan de Riesgos | 20 | 0 | 20 | 20 riesgos identificados en 4 áreas, matriz probabilidad-impacto con color coding, planes de mitigación y contingencia exhaustivos para cada riesgo |
| Plan de Configuración | 10 | -3 | 7 | Git/GitHub bien documentado, flujo Git Flow claro, reglas de repositorio definidas. **Crítico: solo 2 ambientes (desarrollo, prod) en lugar de 3 requeridos (desarrollo, staging, producción)** |
| Plan de Estándares | 20 | -1 | 19 | Paleta de colores con 15 valores HEX, nomenclatura de controles (3 letras), estándares PostgreSQL/Angular/Java exhaustivos. Falta: convenciones CSS explícitas (BEM u otro) |
| Plan de Administración del Tiempo | 20 | -2 | 18 | WBS bien desglozado (2 niveles), diagrama de red con dependencias, Jira con flujo de 9 estados. Mejora: diagramas en archivos externos Draw.io, falta Gantt chart en documento |
| | **100** | **-9** | **91** | |

## Calificación Final: **91 / 100**

---

## Retroalimentación

**Fortalezas:**

1. **Plan de Riesgos excepcional** — PiedPiper identificó 20 riesgos distribuidos estratégicamente (5 en cada área: Desarrollo, Producto, Configuración, Calidad). La matriz probabilidad-impacto está completa con color coding. Cada riesgo tiene mitigation plan y contingency plan específicos (pp. 41-47), con descripción clara de prevención y respuesta. Este es el trabajo más exhaustivo de gestión de riesgos entre las entregas.

2. **Estructura organizacional clara** — El documento está profesionalmente estructurado con 4 páginas de tabla de contenidos, sección explícita de Audiencia (3 grupos de stakeholders definidos), y definiciones de 15 términos clave. Los números de sección (§01 a §10) facilitan la navegación. La estructura facilita seguimiento y referencia.

3. **Listas de verificación contextualizadas** — Cuatro verification lists (LV-GEN-01, LV-PGP-01, LV-ERS-01, LV-DAD-01) diseñadas como anexos con criterios específicos y columnas de seguimiento. Esto demuestra pensamiento práctico en calidad. El enfoque de anexos mantiene el documento limpio sin sacrificar detalle.

4. **Plan de Calidad con herramientas específicas** — La integración de QAlity Plus (herramienta de gestión de pruebas nativa en Jira), combinada con JUnit 5 + Mockito (backend) y Jasmine + Karma (frontend), demuestra selección de herramientas coherente. El Definition of Done tiene 9 criterios explícitos. Las pruebas de rendimiento con Apache JMeter están documentadas.

5. **Configuración y Estándares detallados** — Git Flow strategy claramente explicada. Estándares de GUI incluyen 15 colores HEX con nomenclatura de 3 letras para controles (btn, txt, ddl, etc.). Estándares de codificación para PostgreSQL, Angular y Java están bien documentados con convenciones de nomenclatura. 

**Áreas para mejorar:**

**Crítica — Plan de Configuración (-3 pts):** El rubric requiere especificar "3 ambientes de despliegue: desarrollo, staging, producción." PiedPiper menciona solo 2: desarrollo y prod. Se necesita agregar explícitamente el ambiente de staging/QA como tier intermedio. Esto es esencial para una arquitectura de deployment profesional: desarrollo (para testing local) → staging (para QA final) → producción (live).

**Importante — Plan de Calidad (-2 pts):** Las pruebas de rendimiento están mencionadas pero faltan **métricas específicas y thresholds**. Se debe definir: ¿Cuál es el target de response time (ej: <500ms para 90th percentile)? ¿Cuántos usuarios concurrentes debe soportar como mínimo? ¿Cuál es el error rate máximo aceptable? Sin thresholds, las pruebas de rendimiento no pueden considerarse completadas.

**Importante — Plan de Administración del Tiempo (-2 pts):** El WBS y diagrama de red están documentados pero vinculados a archivos externos (Draw.io). Aunque los enlaces funcionan, el documento sería más accesible si incluyera al menos una visualización simplificada del diagrama de red dentro del PDF. No hay Gantt chart visible.

**Mejora menor — Plan de Estándares (-1 pt):** Los estándares de CSS/SCSS no están explícitos. ¿Se usa BEM? ¿Scoped component styles? ¿SMACSS? Se debería especificar la convención de nombrado para hojas de estilos.

**Mejora menor — Documento y Estructura (-1 pt):** La portada es completa pero no está etiquetada explícitamente como "Portada" (es una observación menor, casi imperceptible).
