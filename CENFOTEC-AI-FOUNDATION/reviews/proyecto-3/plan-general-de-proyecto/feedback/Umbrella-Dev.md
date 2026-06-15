# Plan General de Proyecto — Umbrella Dev

## Desglose de Calificación

| Criterio | Máx | Perdido | Ganado | Notas |
|---|---|---|---|---|
| Documento y Estructura | 10 | 0 | 10 | Portada completa, tabla de contenidos precisa, secciones bien organizadas, explicaciones claras |
| Plan de Calidad | 20 | 0 | 20 | Listas de verificación, jerarquía de pruebas clara (Test Plan → Test Cycle → Test Case), pruebas unitarias con JUnit 5 y Mockito, pruebas de rendimiento con Apache JMeter, Definition of Done exhaustiva |
| Plan de Riesgos | 20 | 0 | 20 | 10 riesgos identificados, matriz probabilidad-impacto con color coding, planes de mitigación y contingencia para riesgos de prioridad media-alta |
| Plan de Configuración | 10 | 0 | 10 | GitHub bien documentado, flujo Git claro, reglas de repositorio y convenciones de commits definidas. Buena distribucion de 3 ambientes de despliegue (desarrollo, staging, producción) |
| Plan de Estándares | 20 | 0 | 20 | Estándares gráficos excepcionales (paleta Arctic con códigos HEX, tipografía, componentes detallados); estándares de codificación Java y Angular exhaustivos; estándares de base de datos PostgreSQL completos |
| Plan de Gestión del Tiempo | 20 | 0 | 20 | Muy buen trabajo definiendo la EDT y sus dependencias  |
| | **100** | **0** | **100** | |

## Calificación Final: **100 / 100**

---

## Retroalimentación

**Fortalezas:**

1. **Plan de Estándares excepcional** — Este es el aspecto más destacado del documento. La paleta de colores Arctic está perfectamente definida con códigos HEX y casos de uso específicos. La tipografía (Poppins, DM Sans, JetBrains Mono) está documentada con pesos y tamaños exactos. Los estándares de componentes (botones, inputs, dropdowns, modales, cards) incluyen especificaciones visuales completas con colores de estado, bordes, sombras y animaciones. Los estándares de codificación Java (Spring Boot) incluyen estructura de paquetes clara, JavaDoc obligatorio con formato específico, y reglas detalladas. Los estándares Angular incluyen convención BEM, estructura de features, y TSDoc obligatorio. Los estándares PostgreSQL cubren nomenclatura, tipos de datos, documentación de objetos, y enums. Este nivel de detalle demuestra madurez arquitectónica.

2. **Plan de Calidad estructurado y minucioso** — La jerarquía de pruebas (Test Plan → Test Cycle → Test Case) está claramente definida. Cada caso de prueba incluye 12 elementos mínimos desde identificador hasta evidencia. Las pruebas unitarias con JUnit 5 + Mockito están especificadas para servicios, validaciones, métodos utilitarios, DTOs y controladores críticos. Las pruebas de rendimiento con Apache JMeter incluyen 3 escenarios (25, 50, 100 usuarios concurrentes) con métricas específicas. El Definition of Done es sólido con 4 categorías (Cumplimiento Funcional, Calidad Técnica, Pruebas y Validación, Aprobación Final) con 14 criterios totales.

3. **Gestión integral de riesgos** — 10 riesgos identificados que cubren todas las dimensiones del proyecto (Producto, Configuración, Desarrollo). La matriz probabilidad-impacto está bien documentada con color coding. Los planes de mitigación y contingencia están presentes y son específicos. Riesgos como "miembros del equipo abandonan el curso" y "tiempo insuficiente para desarrollo" son realistas y bien fundamentados.

4. **Administración de configuración clara** — GitHub está bien justificado con 5 razones específicas. La estructura de ramas (Main, QA, Dev) es clara. La convención de nombres [ID-JIRA]-descripcion-funcionalidad está documentada con ejemplos. El flujo de trabajo de 11 pasos desde fetch hasta producción es detallado y lógico. Las reglas del repositorio son exhaustivas: obligatoriedad de ramas por tiquete, integración frecuente, revisión técnica obligatoria, convenciones de commits.

Excelente trabajo equipo, los felciito! Vamos con una base solida para lo que se viene 

