from ..bytebank import Funcionario

class TestClass:


    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        """ Teste para verificar se o calculo de idade está funcionando."""
        # Given-Contexto
        entrada = '13/03/2000'
        esperado = 23

        funcionario_test = Funcionario('test', entrada, 1111)

        resultado = funcionario_test.idade() # When-ação

        assert resultado == esperado # Then-desfecho


    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_carvalo(self):
        """ Teste para verificar o sobrenome"""

        entrada = 'Lucas Carvalho'
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, 11/11/2000, 1111)

        resultado = lucas.sobrenome()

        assert resultado == esperado