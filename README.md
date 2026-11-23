# Procesamiento del Lenguaje Natural I - Desafíos
 
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
uv sync --group deep
uv run python -m ipykernel install --user --name ceia_procesamiento_lenguaje_natural_1 --display-name "ceia_procesamiento_lenguaje_natural_1"
```
 
Después, abrir cualquier notebook de `notebooks/` con Jupyter o VS Code y elegir el kernel `ceia_procesamiento_lenguaje_natural_1`. Los datasets se descargan desde las propias notebooks, salvo los corpus chicos, que están versionados en `docs/data/`. Para usar la GPU con TensorFlow en Windows, ver [Redes neuronales con GPU](#redes-neuronales-con-gpu-desafío-3-en-adelante).
 
## Estructura del repositorio
 
```
.
├── notebooks/                    # Una notebook por desafío (lo que se entrega)
│   ├── Desafio_1.ipynb           # Vectorización de documentos y Naïve Bayes
│   ├── Desafio_2.ipynb           # Embeddings propios con Gensim (Word2Vec)
│   └── Desafio_3.ipynb           # Modelo de lenguaje por caracteres (SimpleRNN, LSTM, GRU)
├── docs/
│   ├── img/                      # Capturas y gráficos que se citan en las notebooks
│   ├── data/                     # Corpus versionados (Don Quijote para los Desafíos 2 y 3)
│   └── models/                   # Modelos entrenados y resultados del Desafío 3
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

### Redes neuronales con GPU (Desafío 3 en adelante)

TensorFlow solo usa la GPU en Linux: desde la versión 2.11 ya no tiene soporte de GPU en Windows nativo. En Windows, el entorno se corre dentro de **Ubuntu en WSL2**:

1. Instalar Ubuntu en WSL2 desde PowerShell: `wsl --install -d Ubuntu`.
2. Tener actualizado el driver de NVIDIA **de Windows**. WSL2 lo usa directamente: no hay que instalar drivers dentro de Ubuntu. Se verifica con `nvidia-smi` desde Ubuntu.
3. Clonar el repo dentro del home de Linux (no en `/mnt/c/...`, que es mucho más lento) e instalar el entorno con el grupo `deep`:

   ```bash
   uv sync --group deep
   ```

   En Linux y WSL2 se instala `tensorflow[and-cuda]`, que trae CUDA y cuDNN como paquetes de Python. En Windows nativo y macOS se instala TensorFlow sin GPU.
4. Abrir el repo desde VS Code con la extensión **WSL** (`code .` desde Ubuntu) y elegir el kernel del proyecto.

La primera celda de cada notebook con redes neuronales indica si TensorFlow detectó la GPU. Sin GPU las notebooks corren igual, pero el entrenamiento tarda mucho más.

Si en WSL2 TensorFlow no detecta la GPU, puede que no encuentre las librerías de CUDA instaladas por pip. Se resuelve exportando `LD_LIBRARY_PATH` con las carpetas `lib` de los paquetes `nvidia-*` del `.venv` antes de abrir Jupyter o VS Code:

```bash
export LD_LIBRARY_PATH=$(ls -d .venv/lib/python3.12/site-packages/nvidia/*/lib | tr "\n" ":")/usr/lib/wsl/lib:$LD_LIBRARY_PATH
```
 
### Notebooks
 
Todas arrancan con el mismo formato: encabezado, planteo del problema y fuente de datos, consigna, y una sección por punto, cada una con su celda de **Análisis**. Cierran con las conclusiones.
 
## Criterios de trabajo
 
**Una notebook por desafío, autocontenida.** Define dentro de la propia notebook todas las funciones que usa (no depende de módulos externos del repo), se corre de inicio a fin sin errores y deja escrito el análisis de cada experimento, como pide la cátedra. Los datos se descargan desde la notebook o, si son chicos, se leen de `docs/data/`.

**Corpus versionados.** Cuando la fuente no garantiza que el archivo sea siempre el mismo (Project Gutenberg corrige sus textos sin aviso), el corpus se versiona en `docs/data/` para que los resultados sean reproducibles.

**Modelos versionados.** En los desafíos con redes neuronales, los modelos entrenados y sus resultados se guardan en `docs/models/`. Con `ENTRENAR = False` (valor por defecto) la notebook los carga y corre de inicio a fin en pocos minutos, sin GPU. Con `ENTRENAR = True` vuelve a entrenar y los reemplaza. El Desafío 3 se entrenó en una GPU local con Ubuntu en WSL2.
 
**Semilla fija.** Todas las notebooks usan `SEED = 42` para que los resultados sean reproducibles. En el entrenamiento con GPU, cuDNN no es completamente determinístico, así que reentrenar puede dar valores levemente distintos.