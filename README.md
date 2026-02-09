# Universidad Internacional del Ecuador  
## Procesamiento de Imágenes y Señales  

### Deber 2 — Semana 2  
**FFT y Filtros Digitales en Audio**

---

## 👥 Grupo 6
- DARIO WLADIMIR HERRERA CHÁVEZ  
- JONATHAN FABRICIO GUALLI RAMIREZ  
- JORGE ARMANDO QUIZAMANCHURO FUEL  

---

## 📌 Descripción del proyecto

Este repositorio contiene el desarrollo del **Deber 2** de la asignatura **Procesamiento de Imágenes y Señales**, correspondiente a la **Semana 2**, cuyo objetivo principal es aplicar técnicas de **Transformada Rápida de Fourier (FFT)** y **filtros digitales (IIR y FIR)** para el análisis y procesamiento de señales de audio.

El trabajo se divide en dos partes principales:

1. **Comparación de filtros IIR y FIR** aplicados a una señal de **voz con ruido blanco**, con el fin de determinar el filtro pasa-banda que ofrece mejor desempeño utilizando métricas objetivas.
2. **Análisis espectral de una canción** para identificar frecuencias dominantes de instrumentos musicales (guitarra y batería) y aplicar filtros adecuados para atenuar o resaltar dichos componentes.

---

## 🎯 Objetivos

### Objetivo general
Aplicar técnicas de análisis en el dominio de la frecuencia y diseño de filtros digitales para el procesamiento de señales de audio reales.

### Objetivos específicos
- Analizar señales de audio mediante **FFT y STFT**.
- Diseñar y aplicar **filtros pasa-banda y pasa-altos** de tipo **IIR y FIR**.
- Comparar el desempeño de filtros mediante métricas cuantitativas.
- Identificar rangos de frecuencia característicos de instrumentos musicales.
- Implementar soluciones numéricamente estables para el filtrado digital.

---

## 🧪 Metodología

El proyecto se desarrolla utilizando **Python** y librerías especializadas en procesamiento de señales:

- NumPy  
- SciPy  
- Librosa  
- SoundFile  
- Matplotlib  

Se trabaja con señales de audio en formato WAV, aplicando técnicas de:

- Transformada Rápida de Fourier (FFT)  
- Transformada de Fourier de Tiempo Corto (STFT)  
- Diseño de filtros digitales IIR y FIR  
- Normalización y evaluación de señales  

Para evitar inestabilidades numéricas en filtros IIR de orden alto, se emplean **Second-Order Sections (SOS)** y filtrado de fase cero.

---

## 📘 Notebooks del proyecto

### 📗 Notebook 01 — Voz: IIR vs FIR
**01_voz_iir_vs_fir_pasabanda.ipynb**

En este notebook se realiza:

- Carga de una señal de **voz limpia**.
- Adición de **ruido blanco artificial**.
- Diseño y prueba de al menos **4 filtros pasa-banda**, incluyendo:
  - Filtros **IIR** (Butterworth, Chebyshev, Elliptic).
  - Filtros **FIR** (ventanas Hamming y Kaiser).
- Evaluación del desempeño mediante métricas:
  - **Relación señal a ruido (SNR en dB)**.
  - **Relación de energía en banda**.
- Selección del filtro con mejor desempeño.

---

### 📙 Notebook 02 — Canción: guitarra y batería
**02_cancion_guitarra_bateria.ipynb**

En este notebook se realiza:

- Carga de una **canción en formato WAV**.
- Análisis espectral mediante **STFT** para identificar frecuencias dominantes.
- Aplicación de:
  - **Filtro pasa-altos** para atenuar componentes predominantes de la batería.
  - **Filtro pasa-banda** para resaltar componentes de la guitarra.
- Comparación espectral antes y después del filtrado.
- Exportación de los audios procesados.

---

## 📁 Datos de audio

### Audios originales
Los audios originales (voz limpia y canción) se utilizan como entrada para el procesamiento.


---

### Audios procesados
Los audios generados por los notebooks incluyen:

- Voz con ruido blanco.
- Voz filtrada con filtros IIR y FIR.
- Canción filtrada mediante pasa-altos (batería atenuada).
- Canción filtrada mediante pasa-banda (guitarra resaltada).

Todos los audios procesados se exportan en formato **WAV PCM_16**, garantizando compatibilidad con reproductores estándar.

---

## ▶️ Ejecución

1. Colocar los archivos de audio originales en la carpeta indicada.
2. Instalar las dependencias necesarias.
3. Ejecutar los notebooks **en orden secuencial**:
   1. Notebook 01 — Voz.
   2. Notebook 02 — Canción.

---

## 📌 Observaciones finales

- Los notebooks deben ejecutarse en orden para evitar errores.
- El uso de **SOS** mejora la estabilidad numérica en filtros IIR.
- Este proyecto tiene fines **académicos y demostrativos**, conforme a los contenidos vistos en clase.

---

## 🔗 Enlace al repositorio
https://github.com/TU_USUARIO/UIDE-Procesamiento-Imagenes-Senales-Deber-2
