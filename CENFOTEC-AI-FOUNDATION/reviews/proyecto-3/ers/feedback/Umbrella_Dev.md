# ERS — Umbrella Dev

## Desglose de Calificación

| Criterio | Máximo | Perdido | Ganado | Notas |
|----------|--------|---------|--------|-------|
| Secciones generales | 10 | 0 | 10 | Portada completa, audiencia, TOC, introducción, justificación clara, participantes con detalles, descripción de propuesta con 12 módulos identificados |
| Objetivos del Sistema (SMART) | 10 | 0 | 10 | 1 objetivo general + 6 específicos; todos con métricas explícitas (100%, 5 pasos, 4 reportes, 3 procesos) y fechas de entrega (Sprint 3, 4, 5; 16 agosto 2026) |
| Requerimientos Funcionales | 50 | 0 | 50 | Requerimientos bien definidos en el JIRA, con buena configuracion y los datos requeridos. |
| Requerimientos No Funcionales | 15 | -3 | 12 | 22 RNF documentados con ID, prioridad y criterios; pero con numeración duplicada (<10, <11, <12> solapados) y contenido repetido (<19 y <20> ambos "Documentación técnica") |
| Matriz de Requerimientos | 5 | 0 | 5 | Solo enlace a Google Sheets externo; matriz no incluida en ERS |
| Modelo Conceptual | 10 | 0 | 10 | Descripción en prosa clara y bien estructurada; pero diagrama UML no incluido en ERS, solo enlace a Miro |
| | 100 | -3 | **97** | |

## Calificación Final: **97 / 100**

### Retroalimentación

**Fortalezas:**

- **Estructura y portada profesional**: Documento bien presentado con Cenfotec logo, Umbrella Dev como nombre de equipo, todos los 6 miembros listados con email, teléfono, rol y análisis reflexivo de fortalezas/debilidades. Muestra cohesión y autoconocimiento del equipo.
- **Objetivos SMART bien formulados**: Los 6 objetivos específicos están excelentemente especificados con métricas concretas (100% de entidades, máximo 5 pasos, respuesta < 3 segundos, 4 reportes KPI, 3 procesos automatizados, 2 predicciones IA) y fechas de entrega ligadas a sprints específicos (26 julio, 2 agosto, 9 agosto, 16 agosto 2026). Esto demuestra planificación estratégica clara.
- **Justificación del problema clara y empática**: Páginas 6 describen bien el problema real (filas largas, comunicación difícil por ruido, experiencia caótica) y cómo la solución (preventas digitales, comanda asistida por IA) lo resuelve. Es tangible y orientado al usuario.
- **Requerimientos funcionales bien definidos**: Cada uno de los requerimientos en JIRA presentan un grado alto de completitud, detalle, simpleza y consistencia. Las dependencias estan bien definidas y cumple con lo esperado
- **Requerimientos no funcionales técnicamente sólidos**: Los 22 RNF cubren seguridad (OAuth 2.0, RBAC, validación input, sesiones seguras), performance (< 3s respuesta), usabilidad, y arquitectura. Criterios de aceptación son específicos (p.ej. "validar MIME/magic bytes", "renombrar con UUID", "HttpOnly/Secure cookies").
- **Identificación clara de módulos**: 12 módulos bien nombrados (Usuarios, Restaurantes, Eventos, Menús, Productos, Combos, Ingredientes, Recetas, Ventas/Pagos, Órdenes, Inventario, Reportes) muestran comprensión del dominio Pop Up.
- **Descripción en prosa del modelo conceptual**: Explica claramente cómo el organizador invita restaurantes, crean menús, clientes ordenan, órdenes se gestionan por comanda, y cómo inventarios alimentan listas de compra.

**Áreas de mejora críticas:**

- **Numeración duplicada en RNF**: Nombres repetidos y descripciones repetidas. Parece que fueron copiados mas no tanto revisados. Lo cual causa una confusion a la hora de la lectura. 

