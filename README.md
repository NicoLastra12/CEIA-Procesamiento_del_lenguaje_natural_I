# Procesamiento del Lenguaje Natural I — Desafíos
 
**Especialización en Inteligencia Artificial (CEIA) - FIUBA**
 
Resolución de los desafíos de la materia Procesamiento del Lenguaje Natural I. Cada desafío es una notebook que se puede correr de inicio a fin, con el análisis de cada experimento y las decisiones tomadas.
 
Las consignas y el material de clase están en el repositorio de la cátedra: [procesamiento_lenguaje_natural](https://github.com/FIUBA-Posgrado-Inteligencia-Artificial/procesamiento_lenguaje_natural), rama **nov_2026**.
 
## Alumno
 
* Nicolás Lastra

## Profesores
 
* Josselyn Ordóñez
* Fernando Silva

## Contenido
 
1. [Puesta en marcha rápida](#puesta-en-marcha-rápida)
2. [Estructura del repositorio](#estructura-del-repositorio)
3. [Entorno local y notebooks](#entorno-local-y-notebooks)
4. [Criterios de trabajo](#criterios-de-trabajo)

## Puesta en marcha rápida
 
```bash
git clone https://github.com/NicoLastra12/CEIA-Procesamiento_del_lenguaje_natural_I.git
cd CEIA-Procesamiento_del_lenguaje_natural_I
uv sync
uv run python -m ipykernel install --user --name ceia_procesamiento_lenguaje_natural_1 --display-name "ceia_procesamiento_lenguaje_natural_1"
```
 
Después, abrir cualquier notebook de `notebooks/` con Jupyter o VS Code y elegir el kernel `ceia_procesamiento_lenguaje_natural_1`. Los datasets se descargan desde las propias notebooks, salvo los corpus chicos que están versionados en `docs/data/`.
 
## Estructura del repositorio
 
```
.
├── notebooks/                    # Una notebook por desafío (lo que se entrega)
│   ├── 01_Desafio_vectorizacion_y_naive_bayes.ipynb
│   └── 02_Desafio_embeddings_gensim.ipynb
├── docs/
│   ├── img/                      # Capturas y gráficos que se citan en las notebooks
│   └── data/                     # Corpus versionados (Don Quijote para el Desafío 2)
├── pyproject.toml                # Dependencias del entorno local (uv)
├── uv.lock                       # Versiones exactas del entorno local
└── .gitignore
```
 
## Entorno local y notebooks
 
### Entorno local
 
Se maneja con [uv](https://docs.astral.sh/uv/). `uv.lock` fija las versiones exactas, así las notebooks dan los mismos resultados en cualquier PC.
 
```bash
uv sync                  # librerías de los desafíos + Jupyter
uv sync --group deep     # además, TensorFlow (para los desafíos con redes neuronales)
```
 
### Notebooks
 
Todas arrancan con el mismo formato: encabezado, planteo del problema y fuente de datos, consigna, y una sección por punto, cada una con su celda de **Análisis**. Cierran con las conclusiones.
 
## Criterios de trabajo
 
**Una notebook por desafío, autocontenida.** Define dentro de la propia notebook todas las funciones que usa (no depende de módulos externos del repo), se corre de inicio a fin sin errores y deja escrito el análisis de cada experimento, como pide la cátedra. Los datos se descargan desde la notebook o, si son chicos, se leen de `docs/data/`.

**Corpus versionados.** Cuando la fuente no garantiza que el archivo sea siempre el mismo (Project Gutenberg corrige sus textos sin aviso), el corpus se versiona en `docs/data/` para que los resultados sean reproducibles.
 
**Semilla fija.** Todas las notebooks usan `SEED = 42` para que los resultados sean reproducibles.
