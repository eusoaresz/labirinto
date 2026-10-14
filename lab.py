from collections import deque

labirinto = [
    "I..##....#.",
    ".#.##.#....",
    ".#......#..",
    "...........",
    ".....#....#",
    "..#....##..",
    ".....#.F...",
    ".........#.",
    ".#.......#.",
    ".....#.....",
    ".....#....."
]

DIRECOES = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # ↑ → ↓ ←

def achar(lab, simbolo):
    for i, linha in enumerate(lab):
        if simbolo in linha:
            return (i, linha.index(simbolo))
    return None


def livre(lab, i, j):
    dentro = 0 <= i < len(lab) and 0 <= j < len(lab[0])
    return dentro and lab[i][j] != '#'


def montar_grafo(lab):
    grafo = {}

    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if not livre(lab, i, j):
                continue

            grafo[(i, j)] = []

            for di, dj in DIRECOES:
                vizinho = (i + di, j + dj)
                if livre(lab, *vizinho):
                    grafo[(i, j)].append(vizinho)

    return grafo


def desenhar(lab, caminho):
    grade = [list(linha) for linha in lab]

    for i, j in caminho:
        if grade[i][j] == '.':
            grade[i][j] = '*'

    for linha in grade:
        print(''.join(linha))

def bfs (grafo, inicio, saida):
    fila = deque([inicio])
    visitados = {inicio: None}

    while fila:
        atual = fila.popleft()

        if atual == saida:
            break

        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados[vizinho] = atual
                fila.append(vizinho)

    caminho = []
    passo = saida

    while passo is not None:
        caminho.append(passo)
        passo = visitados[passo]

    return caminho[::-1]  # Retorna o caminho invertido


def main():
    inicio = achar(labirinto, 'I')
    saida = achar(labirinto, 'F')
    grafo = montar_grafo(labirinto)

    print(f"Inicio: {inicio}")
    print(f"Saida: {saida}")
    print("\nGrafo montado:", grafo)

    caminho = bfs(grafo, inicio, saida)

    print("\nCaminho encontrado:")
    print(caminho)

    print("\nLabirinto com caminho:")
    desenhar(labirinto, caminho)


if __name__ == "__main__":
    main()