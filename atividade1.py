class Aluno:
    def _init_(self, nome, matricula, media):
        self.nome = nome
        self.matricula = matricula
        self.media = media
        self.proximo = None

class ListaAlunos:
    def _init_(self):
        self.head = None

    def inserir_aluno(self, nome, matricula, media):
        novo_aluno = Aluno(nome, matricula, media)
        novo_aluno.proximo = self.head
        self.head = novo_aluno

    def remover_aluno(self, matricula):
        atual = self.head
        anterior = None

        while atual is not None:
            if atual.matricula == matricula:
                if anterior is None:
                    self.head = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return
            anterior = atual
            atual = atual.proximo

        print(f"Aluno com a matrícula {matricula} não encontrado na lista.")

    def buscar_aluno(self, matricula):
        atual = self.head
        while atual is not None:
            if atual.matricula == matricula:
                print(f"Nome: {atual.nome}\nMatrícula: {atual.matricula}\nMédia: {atual.media}\n")
                return
            atual = atual.proximo

        print(f"Aluno com a matrícula {matricula} não encontrado na lista.")

    def imprimir_alunos(self):
        atual = self.head
        while atual is not None:
            print(f"Nome: {atual.nome}\nMatrícula: {atual.matricula}\nMédia: {atual.media}\n")
            atual = atual.proximo

# Exemplo de utilização
lista_alunos = ListaAlunos()
lista_alunos.inserir_aluno("João", 123, 8.5)
lista_alunos.inserir_aluno("Maria", 456, 9.0)
lista_alunos.inserir_aluno("Pedro", 789, 7.8)

print("Lista de Alunos:")
lista_alunos.imprimir_alunos()

print("\nBusca por aluno com matrícula 456:")
lista_alunos.buscar_aluno(456)

print("\nRemovendo aluno com matrícula 456:")
lista_alunos.remover_aluno(456)

print("\nLista de Alunos atualizada:")
lista_alunos.imprimir_alunos()