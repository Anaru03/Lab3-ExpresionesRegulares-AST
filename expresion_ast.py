# Se utiliza librería Graphviz para generar un Grafo dirigido https://graphviz.gitlab.io/download/
from graphviz import Digraph
import os

# Nodo AST
class NodoAST:
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der

# Simplificar operaciones
def simplificador_expresiones(regex):
    resultado = ""
    i = 0
    while i < len(regex):
        c = regex[i]
        if i + 1 < len(regex):
            siguiente = regex[i + 1]
            if siguiente == '+':
                resultado += c + c + '*'
                i += 2
                continue
            elif siguiente == '?':
                resultado += c + '|ε'
                i += 2
                continue
        resultado += c
        i += 1
    return resultado

def insertar_concatenacion(regex):
    resultado = ""
    for i in range(len(regex) - 1):
        c1 = regex[i]
        c2 = regex[i + 1]
        resultado += c1
        if c1 not in '(|' and c2 not in '|)*':
            resultado += '.'
    resultado += regex[-1]
    return resultado

# Shunting yard (Lab2)
def infix_to_postfix(regex):
    precedencia = {'*': 3, '.': 2, '|': 1}
    salida = ''
    pila = []
    for c in regex:
        if c.isalnum() or c == 'ε':
            salida += c
        elif c == '(':
            pila.append(c)
        elif c == ')':
            while pila and pila[-1] != '(':
                salida += pila.pop()
            pila.pop()  # Quita el '('
        else:
            while pila and pila[-1] != '(' and precedencia.get(pila[-1], 0) >= precedencia[c]:
                salida += pila.pop()
            pila.append(c)
    while pila:
        salida += pila.pop()
    return salida

def construir_ast(postfija):
    pila = []
    for c in postfija:
        if c in {'*', '.', '|'}:
            if c == '*':
                nodo = NodoAST(c, pila.pop())
            else:
                der = pila.pop()
                izq = pila.pop()
                nodo = NodoAST(c, izq, der)
            pila.append(nodo)
        else:
            pila.append(NodoAST(c))
    return pila[0] if pila else None

# Graficar con Graphviz
def graficar_ast(nodo, nombre_archivo='arbol_ast'):
    dot = Digraph() # --> Ahí se utiliza el Grafo dirigido
    
    def agregar_nodos(n):
        if n is None:
            return
        dot.node(str(id(n)), n.valor)
        if n.izq:
            dot.edge(str(id(n)), str(id(n.izq)))
            agregar_nodos(n.izq)
        if n.der:
            dot.edge(str(id(n)), str(id(n.der)))
            agregar_nodos(n.der)

    agregar_nodos(nodo)
    dot.render(nombre_archivo, format='pdf', cleanup=True)
    print(f"✅ AST graficado en {nombre_archivo}.pdf")

if __name__ == "__main__":
    expresion = "a+b?(c|d)*"
    print("Expresión original:        ", expresion)

    simplificada = simplificador_expresiones(expresion)
    print("Tras simplificar operadores:", simplificada)

    con_concatenacion = insertar_concatenacion(simplificada)
    print("Tras formatear con '.':     ", con_concatenacion)

    postfija = infix_to_postfix(con_concatenacion)
    print("Expresión postfija:         ", postfija)

    raiz_ast = construir_ast(postfija)
    print("\nÁrbol de sintaxis abstracta (AST):")

    def imprimir_ast(nodo, nivel=0):
        if nodo is not None:
            imprimir_ast(nodo.der, nivel + 1)
            print('    ' * nivel + str(nodo.valor))
            imprimir_ast(nodo.izq, nivel + 1)
    
    imprimir_ast(raiz_ast)
    
    graficar_ast(raiz_ast)

os.startfile('arbol_ast.pdf') # Si se tiene Windows, abre el PDF generado, pero sino se puede abrir manualmente :)