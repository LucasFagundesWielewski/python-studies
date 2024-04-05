def adicionar_sem_duplicatas(lista, valor):
    if valor not in lista:
        lista.append(valor)
    else:
        print(f"O valor '{valor}' já está na lista e não será adicionado novamente.")

# Exemplo de uso
minha_lista = []

adicionar_sem_duplicatas(minha_lista, 10)
adicionar_sem_duplicatas(minha_lista, 20)
adicionar_sem_duplicatas(minha_lista, 10)  # Este valor já existe na lista

print(minha_lista)