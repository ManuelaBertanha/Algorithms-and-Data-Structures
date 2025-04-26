
# Ordenação por inserção: algoritmo eficiente para ordenar um número pequeno de elementos 


def insertion_sort(sequence, n):
    for i in range(1, n):  # Itera por cada elemento da sequência
        key = sequence[i]  # Armazena em 'key' o elemento que vai ser ordenado
        j = i - 1          # Armazena em 'j' o índice do elemento imediatamente anterior a 'key'
        
        # Insert 'key' into the sorted subarray sequence[0 : j]
        while j >= 0 and sequence[j] > key:
            sequence[j + 1] = sequence[j]  # Atribui o maior valor para a posição imediatamente à direita [j + 1]
            j -= 1                         # Continua percorrendo os valores da direira para a esquerda 
        sequence[j + 1] = key              # Insere o valor 'key' na posição correta da ordenação


def main():
    sequence = [7, 2, 9, 1, 5, 0, 8, 4, 6, 3, 9, 0, 11, 125, 13, 2, 500]
    insertion_sort(sequence, len(sequence))

    print(sequence)


main()
