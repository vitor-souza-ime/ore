# Teorema de Ore em Grafos

Este repositório contém uma implementação em Python que demonstra o **Teorema de Ore** aplicado a grafos não direcionados. O código gera um grafo aleatório, verifica se ele satisfaz a condição de Ore e tenta encontrar um **ciclo Hamiltoniano**.

📌 Arquivo principal: `main.py`  
📌 Repositório: [github.com/vitor-souza-ime/ore](https://github.com/vitor-souza-ime/ore)

---

## 📖 Teorema de Ore
O **Teorema de Ore (1960)** estabelece que:

> Se \( G \) é um grafo simples com \( n \geq 3 \) vértices e, para todo par de vértices não adjacentes \( u, v \), tivermos  
> \[
> \deg(u) + \deg(v) \geq n
> \]
> então \( G \) contém um **ciclo Hamiltoniano**.

Este programa:
1. Gera um grafo aleatório com \( n \) vértices.
2. Verifica se ele satisfaz a condição de Ore.
3. Realiza uma busca exaustiva por um ciclo Hamiltoniano.
4. Plota o grafo, destacando o ciclo Hamiltoniano se encontrado.

---

## 🚀 Execução

### 1. Clonar o repositório
```bash
git clone https://github.com/vitor-souza-ime/ore.git
cd ore
````

### 2. Criar ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o programa

```bash
python main.py
```

---

## 📊 Exemplo de Saída

```
Tentativas até encontrar grafo: 3
Vértices: 8, Arestas: 21
Grau dos vértices: {0: 6, 1: 6, 2: 5, 3: 7, 4: 5, 5: 6, 6: 6, 7: 6}
Cond. de Ore satisfeita? True
Ciclo Hamiltoniano encontrado? Sim
Ciclo Hamiltoniano: (0, 1, 3, 5, 7, 6, 4, 2)
```

O grafo será exibido em uma janela gráfica, com o ciclo Hamiltoniano destacado em **negrito**.

---

## 📦 Dependências

As principais bibliotecas utilizadas são:

* [networkx](https://networkx.org/) — manipulação de grafos
* [matplotlib](https://matplotlib.org/) — plotagem de grafos

Arquivo `requirements.txt` sugerido:

```
networkx
matplotlib
```

---

## 🧩 Estrutura do Código

* `satisfies_ore(G)`: Verifica se o grafo satisfaz a condição de Ore.
* `find_hamiltonian_cycle(G)`: Busca exaustiva por ciclo Hamiltoniano.
* Loop principal: gera grafos até encontrar um que satisfaça Ore.
* Plotagem: usa `spring_layout` para desenhar e destaca o ciclo Hamiltoniano.

---

## 📚 Referências

* Øystein Ore, *Note on Hamilton circuits*, American Mathematical Monthly, 67(1), 55 (1960).
* [NetworkX Documentation](https://networkx.org/documentation/stable/)


```
