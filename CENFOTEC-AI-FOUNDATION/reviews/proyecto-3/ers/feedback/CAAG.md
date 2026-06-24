# ERS — CAAG

## Grade Breakdown

| Criterio | Máximo | Perdido | Ganado | Notas |
|----------|--------|---------|---------|-------|
| Secciones generales del documento | 10 | -1 | 9 | Portada, tabla de contenidos, introducción, justificación, participantes, y descripción están completos. Falta una página explícita de audiencia identificada. |
| Objetivos del Sistema (SMART) | 10 | -8 | 2 | DEBILIDAD CRÍTICA: Los objetivos presentados (OE-01 a OE-05) son requerimientos funcionales, no objetivos del sistema. Confunden implementación con propósito. Ejemplos: OE-01 "permitir registro e inicio de sesión" = RF-01; OE-02 "registrar métricas" = RF-07; OE-03 "generar dashboards" = RF-16. El rubric requiere "Claramente diferenciados de requerimientos". Los objetivos reales deberían ser outcomes (ej: "Reducir tiempo de evaluación cognitiva en 80%", "Mejorar retención de memoria en 25% después de 3 meses"). Este es un error conceptual fundamental en ingeniería de requisitos. |
| Requerimientos Funcionales | 50 | -10 | 42 | 25 RF bien estructurados en 6 módulos con ID, descripción, prioridad, datos entrada/salida. Deducción: los criterios de aceptación remiten a Jira en lugar de estar completos en el documento, esto dificulta la evaluación de completitud sin acceso externo. Deben de consolidarse en JIRA todo. Faltan los datos de los juegos que se van a desarrollar |
| Requerimientos No Funcionales | 15 | 0 | 15 | 8 RNF completos, medibles y bien definidos. Buena cobertura de performance, seguridad, accesibilidad y privacidad. |
| Matriz de Requerimientos | 5 | 0 | 5 | Matriz clara y completa que demuestra trazabilidad entre RF/RNF y objetivos del sistema. |
| Modelo Conceptual | 10 | 0 | 10 | Diagrama UML detallado con descripción en prosa clara. Incluye todas las entidades principales y relaciones. Link a diagrama en Diagrams.net. |
| | **100** | **-19** | **81** | |

## Final Grade: **81 / 100**

### Feedback

### Retroalimentación

**Fortalezas:**
- Documento bien estructurado, profesional y organizado en su presentación.
- 25 requerimientos funcionales bien clasificados en 6 módulos lógicos con detalles completos (ID, descripción, prioridad, datos entrada/salida).
- 8 requerimientos no funcionales completamente definidos con criterios medibles para seguridad, performance, accesibilidad y privacidad.
- Modelo conceptual UML detallado con descripción en prosa clara que facilita la comprensión de la arquitectura.
- Demostración de madurez técnica en la consideración de requisitos críticos (JWT, bcrypt, Ley 8968 de Costa Rica, WCAG 2.1 AA).

**Áreas de mejora:**
- **Sección de audiencia faltante:** No hay página explícita de "Audiencia Identificada".
- **Error conceptual crítico en objetivos del sistema:** Los objetivos (OE-01 a OE-05) son requerimientos funcionales, no objetivos de negocio. Objetivos deben ser outcome-focused, no describir qué construir, sino qué valor generan: por ejemplo: "Reducir evaluación cognitiva de 2 semanas a 80% automático", "Mejorar retención de memoria en 25% en 3 meses de uso", "Detectar regresión de 2 semanas a 48 horas".
- **Consistencia en los requerimientos:** Es importante que para el documento de diseño toda la informacion se vea reflejada en JIRA, no debe de estar dividida entre la ERS y JIRA. Entonces favor mover los datos de manera correcta a la herramienta de gestion. Cualquier duda de como organizar eso me avisan.
- **Definicion de los juegos no esta clara:** se mencionan 12 diferentes juegos, pero no se aclara ni cuales son ni como vana. funcionar, por lo que queda en el aire que es lo que se debe de construir. Hay que crear historias de usuario para esto porque si no, no hay forma de que ustedes mismos puedan construir los juegos de la manera en la que se espera.