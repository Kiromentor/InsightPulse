# InsightPulse - Requisitos del Proyecto

## Descripción General
InsightPulse es una aplicación web de análisis emocional y semántico de textos que permite a los usuarios ingresar contenido textual (diarios, reflexiones, feedback) y obtener insights visualizados sobre el estado emocional y temas centrales.

## Requisitos Funcionales

### 1. Interfaz de Usuario
- **RF-001**: Formulario web simple para ingreso de texto
- **RF-002**: Campo de texto multilínea con validación básica
- **RF-003**: Botón de análisis que procese el contenido
- **RF-004**: Dashboard de resultados con visualizaciones

### 2. Análisis Emocional
- **RF-005**: Clasificación de sentimientos: positivo, negativo, neutral
- **RF-006**: Puntajes numéricos de confianza para cada emoción
- **RF-007**: Análisis de intensidad emocional general del texto

### 3. Análisis Semántico
- **RF-008**: Extracción de palabras clave más relevantes
- **RF-009**: Identificación de temas centrales del texto
- **RF-010**: Frecuencia de términos importantes

### 4. Visualización
- **RF-011**: Gráfico de pastel para distribución emocional
- **RF-012**: Gráfico de barras para palabras clave
- **RF-013**: Métricas numéricas destacadas
- **RF-014**: Interfaz responsive y amigable

## Requisitos Técnicos

### 1. Backend
- **RT-001**: Framework Flask para servidor web
- **RT-002**: Python 3.8+ como lenguaje principal
- **RT-003**: Procesamiento de texto con NLTK/spaCy
- **RT-004**: Análisis de sentimientos con TextBlob o VADER

### 2. Frontend
- **RT-005**: HTML5 con templates Jinja2
- **RT-006**: CSS3 para estilos responsivos
- **RT-007**: JavaScript para interactividad
- **RT-008**: Chart.js para visualizaciones

### 3. Arquitectura
- **RT-009**: Estructura modular separando lógica de negocio
- **RT-010**: Manejo de errores y validaciones
- **RT-011**: Logging para debugging y monitoreo

## Requisitos No Funcionales

### 1. Rendimiento
- **RNF-001**: Tiempo de respuesta < 3 segundos para análisis
- **RNF-002**: Soporte para textos hasta 5000 caracteres
- **RNF-003**: Interfaz fluida sin bloqueos

### 2. Usabilidad
- **RNF-004**: Interfaz intuitiva sin necesidad de tutorial
- **RNF-005**: Mensajes de error claros y útiles
- **RNF-006**: Feedback visual durante procesamiento

### 3. Mantenibilidad
- **RNF-007**: Código documentado y bien estructurado
- **RNF-008**: Pruebas unitarias automatizadas
- **RNF-009**: Configuración centralizada

## Casos de Uso Principales

### CU-001: Analizar Entrada de Diario
**Actor**: Usuario
**Flujo**:
1. Usuario ingresa texto de reflexión personal
2. Sistema procesa y analiza emociones
3. Sistema identifica temas principales
4. Usuario visualiza resultados en dashboard

### CU-002: Evaluar Feedback
**Actor**: Usuario
**Flujo**:
1. Usuario ingresa comentarios o feedback recibido
2. Sistema determina tono emocional
3. Sistema extrae puntos clave
4. Usuario obtiene insights para mejorar

## Limitaciones y Restricciones
- Análisis en español e inglés únicamente
- Sin persistencia de datos (análisis en tiempo real)
- Ejecución local sin servicios externos
- Interfaz web básica sin autenticación