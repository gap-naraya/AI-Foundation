# Plan General de Proyecto — Grupo CoffeeCommits

## Desglose de Calificación

| Criterio | Máx | Perdido | Ganado | Notas |
|---|---|---|---|---|
| Documento y Estructura | 10 | 0 | 10 | Portada completa, tabla de contenidos precisa, secciones bien organizadas y explicaciones claras |
| Plan de Calidad | 20 | 0 | 20 | Listas de verificación, jerarquía de pruebas clara (Test Plan → Test Cycle → Test Case), pruebas unitarias con JUnit 5 y Jasmine/Karma, pruebas de rendimiento con Postman y JMeter, Definition of Done exhaustiva |
| Plan de Riesgos | 20 | 0 | 20 | 12 riesgos identificados en todas las áreas, matriz probabilidad-impacto con color coding, planes de mitigación y contingencia para riesgos críticos |
| Plan de Configuración | 10 | -1 | 9 | Herramientas, flujo Git, reglas de repositorio y convenciones de commits bien definidas. Falta especificación explícita de 3 ambientes de despliegue (desarrollo, staging, producción) |
| Plan de Estándares | 20 | 0 | 20 | Paleta de colores con códigos HEX, tipografía, nomenclatura de controles y componentes de interfaz excepcionalmente detallados; estándares de codificación y documentación exhaustivos |
| Plan de Gestión del Tiempo | 20 | -3 | 17 | WBS y diagrama de red presentes pero con nodos sin etiquetas claras que indiquen paquetes de trabajo específicos o dependencias con duraciones |
| | **100** | **-4** | **96** | |

## Calificación Final: **96 / 100**

---

## Retroalimentación

**Fortalezas:**

1. **Plan de Calidad profundamente estructurado** — El enfoque a la gestión de pruebas es excepcional. La jerarquía de pruebas está claramente definida con Test Plans → Test Cycles → Test Cases, una plantilla de caso de prueba completa que cubre todos los campos necesarios, y la integración de herramientas especializadas (JUnit 5 + Mockito para backend, Jasmine + Karma para frontend) demuestra madurez técnica. El Definition of Done es particularmente sólido con 11 criterios más 5 acuerdos generales del equipo.

2. **Gestión de riesgos integral y bien balanceada** — Identificaron 12 riesgos cubriendo cuatro dimensiones del proyecto (equipo, tiempo, tecnología, presupuesto), cada uno con probabilidad, impacto y severidad claramente evaluados. La matriz probabilidad-impacto es visualmente clara con color coding. Todos los riesgos de severidad media-baja, media-alta y alta tienen planes de mitigación *y* contingencia definidos, demostrando pensamiento preventivo y reactivo.

3. **Estándares visuales y de codificación extraordinariamente detallados** — La paleta de colores incluye 11 colores con códigos HEX específicos y casos de uso claros (fondos, acentos, estados de error/éxito). La nomenclatura de controles (btn, txt, ddl, tbl, lst, chk, rdb, lbl) es consistente y facilitará el desarrollo en paralelo. Los estándares de codificación cubren Java (con JavaDoc obligatorio), Angular/JavaScript, bases de datos con nomenclatura snake_case, y documentación en múltiples lenguajes.

**Áreas de mejora:**

1. **Ambientes de despliegue no explícitamente definidos**: El Plan de Configuración describe Git Flow, convenciones de commits y reglas del repositorio, pero no define claramente los 3 ambientes de despliegue esperados (Desarrollo, Staging, Producción). Aunque mencionan "main" como estable, falta especificar dónde se prueba antes de producción y cómo se maneja la promoción entre ambientes.

2. **Estructura de desglose de trabajo (WBS) necesita etiquetas descriptivas**: El diagrama WBS muestra nodos numerados (1.1.1 a 1.11.3) pero no identifica qué representa cada nodo. Debería incluir nombres de paquetes de trabajo claros como "Módulo de Autenticación", "Gestión de Ligas y Torneos", "Generación de Fixtures", "Transmisión en Vivo", etc. Esto dificultaría el seguimiento efectivo del proyecto sin entender la descomposición de trabajo.

3. **Diagrama de red carece de claridad en tasks y duraciones**: El diagrama de red muestra conexiones entre nodos con color coding, pero falta: (a) nombres claros de tareas en cada nodo, (b) duraciones estimadas de cada actividad, (c) identificación explícita del camino crítico, (d) hitos clave del proyecto. Esto impide que el equipo identifique rápidamente cuáles tareas son críticas versus flexibles.

¡Excelente trabajo del equipo CoffeeCommits! Este Plan General demuestra disciplina, pensamiento sistemático y atención al detalle. Los ajustes finales en WBS, diagrama de red y especificación de ambientes completarían un documento de clase mundial.
