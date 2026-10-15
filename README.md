# Suma de Riemann con Manim

- **Curso:** MATE1134 – Cálculo Intermedio, Grupo 1
- **Integrantes:** Sakin Contreras ([@Sakin-UCT](https://github.com/Sakin-UCT)), Kevin Inalaf ([@Kevvyh](https://github.com/Kevvyh)), Javier Gutiérrez ([@HealHost](https://github.com/HealHost))
- **Tema:** Construcción de una suma de Riemann
- **Pregunta central:** ¿Cómo se transforma una región bajo una curva en una suma de áreas de rectángulos?
- **Ejemplo:** f(x) = x² + 1 en [0, 2], con n = 4, 8 y 16 (punto medio).

## Versiones
Python 3.12 y Manim Community 0.22.0.

## Instalación (Windows, PowerShell)
Instalar FFmpeg y LaTeX (MiKTeX, con "instalar paquetes faltantes: siempre"):
```powershell
winget install ffmpeg
```
Luego, desde la carpeta del repositorio:
```powershell
uv python install 3.12
uv venv --python 3.12
.venv\Scripts\activate
uv pip install -r requirements.txt
```

## Ejecución
```powershell
manim -pqh main.py VideoCompleto
```

## Referencias y declaración de IA
- Apunte base: *Introducción a la integral*, Cálculo Intermedio.
- Khan Academy en Español, *Sumas de Riemann de punto medio* (video).
- MateFacil, *Suma de Riemann ¿Qué es? ¿De dónde sale?* (video).
- Documentación de Manim: https://docs.manim.community
- IA: Claude (Anthropic), apoyo en estructura, ejemplo y código.