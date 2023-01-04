class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=0):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'


class Mutante(Pessoa):
    olhos = 1


if __name__ == '__main__':
    ruan = Mutante(nome='Ruan')
    wendel = Homem(ruan, nome='Wendel')
    print(Pessoa.cumprimentar(wendel))
    for filho in wendel.filhos:
        print(filho.nome)
    wendel.sobrenome = 'Borges'
    del wendel.filhos
    wendel.olhos = 1
    del wendel.olhos
    print(wendel.__dict__)
    print(ruan.__dict__)
    print(Pessoa.olhos)
    print(ruan.olhos)
    print(wendel.olhos)
    print(id(Pessoa.olhos), id(ruan.olhos), id(wendel.olhos))
    print(Pessoa.metodo_estatico(), wendel.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), wendel.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anônimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(ruan, Pessoa))
    print(isinstance(ruan, Homem))
    print(ruan.olhos)
    print(wendel.cumprimentar())
    print(ruan.cumprimentar())
