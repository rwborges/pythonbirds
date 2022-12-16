class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=0):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    print(Pessoa.metodo_estatico(), wendel.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), wendel.nome_e_atributos_de_classe())