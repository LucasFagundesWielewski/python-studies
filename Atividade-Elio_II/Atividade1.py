class Paciente:
    def __init__(self, nome, id_paciente, idade):
        self.nome = nome
        self.id_paciente = id_paciente
        self.idade = idade
        self.anterior = None
        self.proximo = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def inserir_no_inicio(self, nome, id_paciente, idade):
        novo_paciente = Paciente(nome, id_paciente, idade)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo_paciente
        else:
            novo_paciente.proximo = self.cabeca
            self.cabeca.anterior = novo_paciente
            self.cabeca = novo_paciente

    def inserir_no_final(self, nome, id_paciente, idade):
        novo_paciente = Paciente(nome, id_paciente, idade)
        if self.cauda is None:
            self.cabeca = self.cauda = novo_paciente
        else:
            novo_paciente.anterior = self.cauda
            self.cauda.proximo = novo_paciente
            self.cauda = novo_paciente

    def remover_por_id(self, id_paciente):
        atual = self.cabeca
        while atual:
            if atual.id_paciente == id_paciente:
                if atual.anterior:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo
                if atual.proximo:
                    atual.proximo.anterior = atual.anterior
                else:
                    self.cauda = atual.anterior
                return True
            atual = atual.proximo
        return False

    def remover_primeiro(self):
        if self.cabeca:
            if self.cabeca == self.cauda:
                self.cabeca = self.cauda = None
            else:
                self.cabeca = self.cabeca.proximo
                self.cabeca.anterior = None

    def remover_ultimo(self):
        if self.cauda:
            if self.cabeca == self.cauda:
                self.cabeca = self.cauda = None
            else:
                self.cauda = self.cauda.anterior
                self.cauda.proximo = None

    def buscar_por_id(self, id_paciente):
        atual = self.cabeca
        while atual:
            if atual.id_paciente == id_paciente:
                return atual
            atual = atual.proximo
        return None

    def mostrar_todos(self):
        atual = self.cabeca
        while atual:
            print(f"Paciente: {atual.nome}, ID: {atual.id_paciente}, Idade: {atual.idade}")
            atual = atual.proximo

# Exemplo de uso
lista = ListaDuplamenteEncadeada()
lista.inserir_no_inicio("Alice", 1, 30)
lista.inserir_no_final("Bob", 2, 45)
lista.inserir_no_inicio("Carlos", 3, 25)

print("Lista de Pacientes:")
lista.mostrar_todos()

paciente = lista.buscar_por_id(2)
if paciente:
    print(f"\nPaciente encontrado: {paciente.nome}, ID: {paciente.id_paciente}, Idade: {paciente.idade}")
else:
    print("\nPaciente não encontrado.")

if lista.remover_por_id(3):
    print("\nPaciente com ID 3 removido com sucesso.")
else:
    print("\nPaciente com ID 3 não encontrado.")

print("\nLista de Pacientes após remoção:")
lista.mostrar_todos()

lista.remover_primeiro()
print("\nLista de Pacientes após remover o primeiro paciente:")
lista.mostrar_todos()

lista.remover_ultimo()
print("\nLista de Pacientes após remover o último paciente:")
lista.mostrar_todos()
