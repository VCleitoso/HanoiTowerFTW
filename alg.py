def mover_torre(n, origem, destino, auxiliar, moves):
    if n == 1:
        moves += 1
        print(f"Mover disco 1 da torre {origem} para a torre {destino}, movimentos = {moves}")
        return moves
    moves = mover_torre(n - 1, origem, auxiliar, destino, moves)
    moves += 1
    print(f"Mover disco {n} da torre {origem} para a torre {destino}, movimentos = {moves}")
    moves = mover_torre(n - 1, auxiliar, destino, origem, moves)
    return moves
num_discos_string = input('Digite a quantidade de discos: ')
num_discos = int(num_discos_string)
torre_origem = input ('Digite a torre de origem (1, 2 ou 3): ')
torre_destino = input ('Digite a torre de destino (1, 2 ou 3): ')
torre_auxiliar = input ('Digite a torre auxiliar (1, 2 ou 3): ')
movimentos = 0
movimentos_finais = mover_torre(num_discos, torre_origem, torre_destino, torre_auxiliar, movimentos)
print(f"Total de movimentos: {movimentos_finais}")
