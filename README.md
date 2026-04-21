# Control de Horas por Asignatura 📋
## Colegio Gonzalo Rivera Laguado

Sistema web para generar boletines de control de horas por asignatura. Diseñado específicamente para el Colegio Gonzalo Rivera Laguado.

## Características

✨ **Interfaz intuitiva**: Formulario claro y bien organizado  
📊 **Vista previa en tiempo real**: Visualiza los cambios mientras completas los datos  
🖨️ **Exportación a PDF**: Genera boletines imprimibles directamente  
📈 **Cálculos automáticos**: Calcula promedios y totales de horas automáticamente  
🎨 **Diseño profesional**: Boletines con identidad visual del colegio  
📱 **Responsive**: Funciona en escritorio y tablet  

## Requisitos

- Python 3.7+
- Flask 2.3.0+

## Instalación

### 1. Clonar o descargar el repositorio

```bash
cd ruta/del/proyecto
```

### 2. Crear entorno virtual (recomendado)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
python app.py
```

La aplicación se abrirá en: **http://localhost:5000**

## Uso

### Para crear un boletín:

1. Abre el navegador en **http://localhost:5000**
2. Haz clic en **"Crear Boletín"**
3. Completa los datos del curso:
   - **Curso/Grado**: Ej. Jardin-01, Primero-A, etc.
   - **Docente Responsable**: Nombre del docente
   - **Año Académico**: Año académico del reporte
4. Configura los períodos académicos
5. Añade las asignaturas con sus horas por período
6. (Opcional) Agrega observaciones
7. La vista previa se actualiza automáticamente en el panel derecho
8. Haz clic en **"🖨️ Imprimir / PDF"** para generar la versión imprimible
9. En la ventana de impresión:
   - Para PDF: Selecciona "Guardar como PDF"
   - Para imprimir: Haz clic en "Imprimir"

### Botones de ayuda:

- **Limpiar**: Reinicia el formulario
- **Cargar ejemplo**: Carga datos de ejemplo para ver el sistema en acción
- **Imprimir / PDF**: Genera el boletín imprimible

## Estructura del proyecto

```
notas/
├── app.py                      # Aplicación Flask
├── requirements.txt            # Dependencias Python
├── README.md                   # Este archivo
├── static/
│   └── logo.png               # Logo del colegio
└── templates/
    ├── index.html              # Página de inicio
    ├── boletin.html            # Editor de boletín
    └── boletin_impresion.html  # Plantilla de impresión
```

## Datos de la institución

- **Institución**: Colegio Gonzalo Rivera Laguado
- **Sistema**: Control de Horas Académicas
- **Versión**: 1.0

## Tecnologías utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Fuentes**: Cormorant Garamond, Outfit (Google Fonts)
- **Generación PDF**: Navegador (print to PDF)

## Funcionalidades principales

### Cálculos automáticos
- Promedio de horas por asignatura
- Total de horas por asignatura
- Promedio general del plan de estudios
- Distribución de carga horaria

### Datos flexibles
- Configurable número de períodos (hasta 8)
- Nombres personalizables de períodos
- Asignaturas y docentes editables
- Observaciones generales

### Salida profesional
- Boletín con encabezado personalizado
- Logo del colegio incluido
- Tabla clara y legible
- Estadísticas de horas
- Apto para impresión y PDF

## Notas de uso

⚠️ **Importante**: La institución está preconfigurada como "Colegio Gonzalo Rivera Laguado"

📌 **Navegadores recomendados**: Chrome, Firefox, Safari, Edge (versiones recientes)

🖨️ **Configuración de impresión**: Se recomienda imprimir en orientación **vertical** (retrato) en tamaño **A4**

## Soporte y contacto

Para reportar problemas o sugerencias, contacta con el administrador del sistema.

---

**Última actualización**: 21 de Abril de 2026
