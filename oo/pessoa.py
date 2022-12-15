class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=0):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá'


if __name__ == '__main__':
    ruan = Pessoa(nome='Ruan')
    wendel = Pessoa(ruan, nome='Wendel')
    print(Pessoa.cumprimentar(wendel))
    for filho in wendel.filhos:
        print(filho.nome)
    wendel.sobrenome = 'Borges'
    del wendel.filhos
    wendel.olhos = 1
    del wendel.olhos
    print(wendel.__dict__)
    print(ruan.__dict__)
    Pessoa.olhos = 2
    print(Pessoa.olhos)
    print(ruan.olhos)
    print(wendel.olhos)
    print(id(Pessoa.olhos), id(ruan.olhos), id(wendel.olhos))