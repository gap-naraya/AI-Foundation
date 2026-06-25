# ERS — Pied Piper

## Desglose de Calificación

| Criterio | Máximo | Perdido | Ganado | Notas |
|----------|--------|---------|--------|-------|
| Secciones generales | 10 | 0 | 10 | Portada, audiencia, tabla de contenidos, introducción, justificación, participantes y descripción de propuesta completas y bien estructuradas |
| Objetivos del Sistema (SMART) | 10 | 0 | 10 | 1 objetivo general + 7 específicos; todos cumplen criterios SMART con métricas claras (100%, 30 días, 90 días) |
| Requerimientos Funcionales | 50 | 0 | 50 | 95 requerimientos identificados en matriz con trazabilidad.  |
| Requerimientos No Funcionales | 15 | 0 | 15 | 16 RNF bien especificados con prioridad, descripción, criterios medibles (< 1 s, 10 s timeout, JMeter, 5 intentos, 30 min) y dependencias |
| Matriz de Requerimientos | 5 | 0 | 5 | Matriz de trazabilidad excelente (95 RF × 7 objetivos); todas las relaciones claras |
| Modelo Conceptual | 10 | 0 | 10 | Modelo UML con 11 entidades y relaciones bien definidas; descripción en prosa explicita conexión entre gestión ambiental y turismo sostenible; versión interactiva en Draw.io disponible |
| | 100 | 0 | **100** | |

## Calificación Final: **100 / 100**

### Retroalimentación

**Fortalezas:**

- **Documento profesional y completo**: La estructura sigue estándares de la industria con portada impactante, tabla de contenidos clara de 3 niveles y secciones bien diferenciadas. La presentación visual es excelente.
- **Justificación sólida y fundamentada**: La sección de justificación no es genérica; incluye datos específicos del Programa País de Carbono Neutralidad (PPCN) de Costa Rica mostrando que en 2017 solo 96 empresas (0,45% del parque empresarial) habían adoptado certificación. Respalda la necesidad con fuentes académicas reales (Avendaño 2017, Valenciano 2024).
- **Objetivos SMART bien articulados**: Los 7 objetivos específicos son medibles y limitados en tiempo. Por ejemplo: "reducir a no más de 30 días el tiempo promedio de auditoría" y "garantizar aviso 90 días antes del vencimiento". Están claramente diferenciados de los requerimientos.
- **Requerimientos no funcionales excepcionales**: Los 16 RNF son específicos, verificables y técnicamente rigurosos. Incluyen criterios cuantitativos (< 1 segundo, percentil 90 < 2s, percentil 99 < 3s para latencia), referencias a herramientas concretas (JMeter, JUnit, Karma, MockMvc), y mecanismos de seguridad detallados (BCrypt, RS256, CSRF, rate limiting).
- **Matriz de trazabilidad exhaustiva**: La matriz de 95 requerimientos × 7 objetivos demuestra claridad de alcance. Cada requerimiento está vinculado a al menos un objetivo; ninguno queda sin justificación.
- **Modelo conceptual con profundidad**: El modelo UML no es superficial. La descripción en prosa explica cómo las "fuentes de emisión" generan "emisiones de carbono" que conforman la "huella de carbono", y cómo esta se valida mediante "auditoría" para generar "certificaciones" que construyen "reputación" (que a su vez influye en el itinerario que un viajero planea). La conexión entre dos dominios (ambiental + turismo) es clara.
- **Gestión de equipo bien documentada**: La sección de participantes incluye rol, email, teléfono y ubicación de cada integrante, con coordinaciones claras (General, Desarrollo, Calidad, Soporte). Esto refleja profesionalismo y organización.
- **Módulos funcionales claramente definidos**: Los 9 módulos (Autenticación, Gestión de emisiones, Auditorías, Directorio de auditores, Certificaciones, Perfil de reputación, Alertas, Benchmark, EcoRuta) cubren todo el dominio sin solapamientos.

**Áreas de mejora:**

- **Ninguna, estoy muy orgulloso y contento con este resultado! Los felicito asi es como se inicia con bases fuertes un proyecto de software!**