# Laboratorio 3 - Autómatas y Expresiones Regulares

**Universidad del Valle de Guatemala**  
**Facultad de Ingeniería**  
**Ingeniería en Ciencia de la Computación y TI**  
**Curso:** Teoría de la Computación.

---

## 📌 Descripción

Este laboratorio consiste en dos partes:

- **Ejercicio 1 (75%)**: Conversión de expresiones regulares de infix a postfix y generación de su Árbol de Sintaxis Abstracta (AST).
- **Ejercicio 2 (25%)**: Aplicación del Lema de Arden para obtener la expresión regular de un Autómata Finito.

Se utilizó Python y la librería Graphviz para graficar los árboles sintácticos.


---

## ▶️ Video de ejecución

🔗 [Ver video en YouTube)](https://www.youtube.com/watch?v=07VDLkObv84)

Este video muestra:
- Ejecución completa del script `expresion_ast.py`
- Resultados generados para cada expresión
- Explicación breve del código y funciones clave

---

## 📈 Resultados

### Expresión 1: `(a*|b*)+`
- Simplificada: `(a*|b*)(a*|b*)*`
- Postfija: `a*b*|a*b*|*.`
- AST: `AST_expresion_1.png`

### Expresión 2: `((ε|a)|b*)*`
- Postfija: `εa|b*|*`
- AST: `AST_expresion_2.png`

### Expresión 3: `(a|b)+abb(a|b)*`
- Simplificada: `(a|b)(a|b)*abb(a|b)*`
- Postfija: `ab|ab|*.a.b.b.ab|*.`
- AST: `AST_expresion_3.png`

### Expresión 4: `0?(1?)?0*`
- Simplificada: `0|ε((1.?)|ε)0*`
- Postfija: `0ε1.?ε|.0*.|`
- AST: `AST_expresion_4.png`

---

## 🛠️ Requisitos

1. Tener Python instalado
2. Instalar Graphviz (programa y librería)

```bash
# En sistemas basados en Debian
sudo apt install graphviz

# Instalar la librería de Python
pip install graphviz
```

#### Se utiliza librería Graphviz para generar un Grafo dirigido https://graphviz.gitlab.io/download/

---

## 💻 Cómo ejecutar

```bash
py expresion_ast.py
```

El script procesará las expresiones del archivo `expresiones.txt`, generará la forma postfix, construirá su AST y guardará las imágenes como `AST_expresion_#.png`.

---

## 🧠 Ejercicio 2

Puedes encontrar la resolución del Ejercicio 2 (Lema de Arden) en el archivo:

```
/ejercicio2/lema_de_arden.pdf
```

Incluye procedimiento paso a paso, justificación teórica y expresión regular obtenida desde el autómata.
