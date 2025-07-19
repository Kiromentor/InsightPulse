# InsightPulse - Diseño Técnico

## Arquitectura General

### Patrón MVC
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│     Vista       │    │   Controlador   │    │     Modelo      │
│   (Templates)   │◄──►│    (Routes)     │◄──►│   (Analysis)    │
│                 │    │                 │    │                 │
│ - index.html    │    │ - app.py        │    │ - analyzer.py   │
│ - results.html  │    │ - routes.py     │    │ - processor.py  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Estructura de Directorios

```
insight_pulse/
├── app.py                 # Punto de entrada Flask
├── config.py             # Configuración de la aplicación
├── requirements.txt      # Dependencias Python
├── analysis/
│   ├── __init__.py
│   ├── analyzer.py       # Motor de análisis emocional
│   ├── processor.py      # Procesamiento de texto
│   └── visualizer.py     # Generación de datos para gráficos
├── routes/
│   ├── __init__.py
│   └── main.py          # Rutas principales
├── templates/
│   ├── base.html        # Template base
│   ├── index.html       # Formulario principal
│   └── results.html     # Dashboard de resultados
├── static/
│   ├── css/
│   │   └── style.css    # Estilos principales
│   ├── js/
│   │   └── charts.js    # Lógica de visualización
│   └── images/          # Recursos gráficos
└── tests/
    ├── __init__.py
    ├── test_analyzer.py
    ├── test_processor.py
    └── test_routes.py
```

## Componentes Principales

### 1. Analizador Emocional (`analysis/analyzer.py`)

```python
class EmotionAnalyzer:
    def analyze_sentiment(self, text: str) -> dict:
        """
        Retorna: {
            'positive': float,
            'negative': float, 
            'neutral': float,
            'compound': float
        }
        """
    
    def get_emotion_intensity(self, text: str) -> float:
        """Intensidad emocional general (0-1)"""
```

### 2. Procesador de Texto (`analysis/processor.py`)

```python
class TextProcessor:
    def extract_keywords(self, text: str, top_n: int = 10) -> list:
        """Extrae palabras clave más relevantes"""
    
    def identify_themes(self, text: str) -> list:
        """Identifica temas centrales usando clustering"""
    
    def clean_text(self, text: str) -> str:
        """Limpia y normaliza el texto"""
```

### 3. Visualizador (`analysis/visualizer.py`)

```python
class DataVisualizer:
    def prepare_emotion_chart(self, emotions: dict) -> dict:
        """Datos para gráfico de pastel emocional"""
    
    def prepare_keywords_chart(self, keywords: list) -> dict:
        """Datos para gráfico de barras de palabras clave"""
```

## Flujo de Datos

### 1. Procesamiento de Entrada
```
Texto Usuario → Limpieza → Tokenización → Análisis
```

### 2. Pipeline de Análisis
```
Texto Limpio → [Análisis Emocional] → Puntajes
              → [Extracción Keywords] → Palabras Clave  
              → [Detección Temas] → Temas Centrales
```

### 3. Generación de Respuesta
```
Resultados → Formateo JSON → Template Rendering → HTML Response
```

## Tecnologías y Librerías

### Backend
- **Flask**: Framework web principal
- **NLTK**: Procesamiento de lenguaje natural
- **TextBlob**: Análisis de sentimientos
- **scikit-learn**: Clustering y ML básico
- **pandas**: Manipulación de datos

### Frontend
- **Jinja2**: Motor de templates
- **Chart.js**: Visualizaciones interactivas
- **Bootstrap**: Framework CSS responsivo
- **jQuery**: Manipulación DOM y AJAX

## APIs Internas

### Endpoint Principal
```
POST /analyze
Content-Type: application/json
{
    "text": "string",
    "options": {
        "language": "es|en",
        "detailed": boolean
    }
}

Response:
{
    "emotions": {
        "positive": 0.7,
        "negative": 0.1,
        "neutral": 0.2,
        "intensity": 0.8
    },
    "keywords": [
        {"word": "feliz", "score": 0.9},
        {"word": "logro", "score": 0.8}
    ],
    "themes": ["bienestar", "éxito"],
    "summary": "Texto con tono predominantemente positivo..."
}
```

## Consideraciones de Rendimiento

### Optimizaciones
- Cache de modelos NLP en memoria
- Procesamiento asíncrono para textos largos
- Lazy loading de librerías pesadas
- Compresión de respuestas JSON

### Limitaciones
- Máximo 5000 caracteres por análisis
- Timeout de 30 segundos para procesamiento
- Sin persistencia (análisis stateless)

## Seguridad

### Validaciones
- Sanitización de entrada de texto
- Límites de longitud y frecuencia
- Escape de caracteres especiales
- Validación de tipos de datos

### Headers de Seguridad
```python
@app.after_request
def security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    return response
```

## Configuración

### Variables de Entorno
```python
# config.py
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key')
    MAX_TEXT_LENGTH = 5000
    ANALYSIS_TIMEOUT = 30
    DEBUG = os.environ.get('FLASK_ENV') == 'development'
```

## Testing Strategy

### Tipos de Pruebas
- **Unitarias**: Cada componente de análisis
- **Integración**: Flujo completo de procesamiento
- **Funcionales**: Endpoints y respuestas
- **Performance**: Tiempo de respuesta bajo carga

### Coverage Objetivo
- Mínimo 80% de cobertura de código
- 100% de cobertura en lógica de análisis crítica