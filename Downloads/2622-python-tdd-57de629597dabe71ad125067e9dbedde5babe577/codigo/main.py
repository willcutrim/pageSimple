from bytebank import Funcionario


def teste_idade():
    funcionario_teste = Funcionario('test', '29/04/1996', 1111)

    print(f'Teste = {funcionario_teste.idade()}')

teste_idade()