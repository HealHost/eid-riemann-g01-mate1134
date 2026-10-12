# Suma de Riemann con Manim

**Curso:** MATE1134 – Cálculo Intermedio, Grupo 1
**Integrantes:** Sakin Contreras, Kevin Inalaf, Javier Gutiérrez (GitHub: COMPLETAR)
**Tema:** Construcción de una suma de Riemann
**Pregunta central:** ¿Cómo se transforma una región bajo una curva en una suma de áreas de rectángulos?
**Ejemplo:** f(x) = x² + 1 en [0, 2], con n = 4, 8 y 16.

## Versiones
Python 3.12 y Manim Community 0.22.0.

## Instalación

**1. Instalar FFmpeg (programa del sistema)**

Fedora:
```bash
sudo dnf install ffmpeg-free
```

Windows (PowerShell):
```powershell
winget install ffmpeg
```

Comprobar: `ffmpeg -version`

**2. Instalar Python y Manim**

Linux:
```bash
uv python install 3.12
uv venv --python 3.12
source .venv/bin/activate
uv pip install -r requirements.txt
```

Windows (PowerShell):
```powershell
uv python install 3.12
uv venv --python 3.12
.venv\Scripts\activate
uv pip install -r requirements.txt
```

## Ejecución
Desde la carpeta raíz, con el entorno activo:

```bash
manim -pqh main.py VideoCompleto
```

## Archivos
- `main.py`: une las tres escenas.
- `config.py`: función, intervalo y estilo compartido.
- `escenas/`: una escena por integrante.
- `guion.md`: narración y cálculos.

## Referencias y declaración de IA
Ver el código de ética (entregado en Blackboard)