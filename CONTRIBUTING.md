# Cómo contribuir / How to contribute

Requisitos del ejercicio: cada persona del grupo debe enviar **al menos 1 pull request desde su fork**, y cada pull request debe ser **aprobado por al menos 1 persona** antes de mezclarse.

## Pasos (todo desde la web de GitHub, sin instalar nada)

1. **Fork**: en la página del repositorio, pulsa **Fork** → **Create fork**.
2. **Rama nueva**: en tu fork, abre el selector de ramas (`main`), escribe un nombre (por ejemplo `analisis-tu-nombre`) y pulsa **Create branch**.
3. **Tu parte del análisis**: en esa rama, **Add file → Create new file** y crea `analisis/0X_tu_tema.py` (puedes copiar la estructura de `analisis/01_resumen_general.py`). Si generas figuras, súbelas a `figuras/` con **Add file → Upload files**.
4. **Tu nombre**: edita `README.md` y escribe tu nombre, tu usuario de GitHub y tu parte en la tabla de participantes; añade 2–3 líneas en la sección *Resultados*.
5. **Pull request**: vuelve a tu fork, pulsa **Contribute → Open pull request → Create pull request**.
6. **Revisión**: otra persona del grupo abre el pull request, pulsa **Files changed → Review changes → Approve** y después **Merge pull request**.
7. **Limpieza**: tras el merge, pulsa **Delete branch** y, en tu fork, **Sync fork**.

## Reparto sugerido

| Parte | Script | Pregunta |
|---|---|---|
| 1 | `01_resumen_general.py` | Filas, columnas, valores faltantes y estadísticos básicos (**hecho**) |
| 2 | `02_especies_islas.py` | ¿Cuántos pingüinos hay por especie y por isla? |
| 3 | `03_masa_corporal.py` | ¿Cómo varía la masa corporal entre especies y sexos? |
| 4 | `04_pico.py` | Longitud vs. profundidad del pico por especie (diagrama de dispersión) |
| 5 | `05_aletas.py` | Distribución de la longitud de la aleta por especie (histograma o boxplot) |
| 6 | `06_correlaciones.py` | Matriz de correlación entre las variables numéricas |

---

**English summary:** fork the repository, create a branch, add your script in `analisis/` (and figures in `figuras/`), add your name to the README table, and open a pull request. Another group member must approve it before merging.
