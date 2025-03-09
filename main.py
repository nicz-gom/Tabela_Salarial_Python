#Tabela Salarial
print("Olá! - Painel do Gestor")
acesso = (input("informe seu nome: "))
print(f"Seja bem vindo, {acesso}! Essa é sua Tabela Salarial")

#parâmetros do programa
parametro_tamanho_array = 2
parametro_valor_departamento_1 = 22
parametro_valor_departamento_2 = 12

class funcionario:
    def __init__(self, nome, depto, horas, salario):
        self.nome = nome
        self.depto = depto
        self.horas = horas
        self.salario = 0

        #transformando os elementos da classe em string
    def __str__(self):
        return f"Nome: {self.nome}, Departamento: {self.depto}, Horas Trabalhadas: {self.horas}, Salário: {self.salario}"

storage = []

#calcular o salario base
def salario_base(lista_funcionarios):
    for x in range(parametro_tamanho_array):
        comparador_depto = lista_funcionarios[x].depto
        horas = lista_funcionarios[x].horas

        if comparador_depto == 1:
            if horas > 40: 
                horas_extras = horas - 40 #quantidade de horas extras
                resultado = (horas - horas_extras)*parametro_valor_departamento_1 #retirando essa diferença
                lista_funcionarios[x].salario = resultado
            else:
                resultado = horas*parametro_valor_departamento_1
                lista_funcionarios[x].salario = resultado

        elif comparador_depto == 2:
            if horas > 40: 
                horas_extras = horas - 40 #quantidade de horas extras
                resultado = (horas - horas_extras)*parametro_valor_departamento_2 #retirando essa diferença
                lista_funcionarios[x].salario = resultado
            else:
                resultado = horas*parametro_valor_departamento_2
                lista_funcionarios[x].salario = resultado

    return lista_funcionarios

def horas_extras(lista_funcionarios):
    for x in range(parametro_tamanho_array):
        comparador = lista_funcionarios[x].depto

        if comparador == 1:
            if lista_funcionarios[x].horas > 40:
                vHoras_extras = lista_funcionarios[x].horas - 40
                resultado = vHoras_extras*2*parametro_valor_departamento_1

                lista_funcionarios[x].salario = lista_funcionarios[x].salario + resultado
        elif comparador == 2:
            if lista_funcionarios[x].horas > 40:
                vHoras_extras = lista_funcionarios[x].horas - 40
                resultado = vHoras_extras*2*parametro_valor_departamento_2

                lista_funcionarios[x].salario = lista_funcionarios[x].salario + resultado
    
    return lista_funcionarios

def insalubridade(Copia_storage, lista_funcionarios):
    for x in range(parametro_tamanho_array):
        comparador = lista_funcionarios[x].depto
        lista_convertida = float(Copia_storage[x].salario)

        if comparador == 2:
            resultado = float(lista_convertida*0.15)
            lista_funcionarios[x].salario = float(resultado + lista_funcionarios[x].salario)

    return lista_funcionarios

def bonificacao_1 (Copia_storage, lista_funcionario):
    for x in range(parametro_tamanho_array):
        comparador = lista_funcionario[x].horas
        lista_convertida = float(Copia_storage[x].salario)

        if comparador > 20:
            resultado = float(lista_convertida*0.03)
            lista_funcionario[x].salario = float(resultado +  lista_funcionario[x].salario)

    return lista_funcionario

#inserção dos valores no vetor
for x in range(parametro_tamanho_array):
    print(f"\n---Cadastre seu funcionário - ({x + 1})!---")
    nome = input("Digite o nome: ")
    depto = input("Digite o departamento: ")
    horas = input("Informe a quantidade de horas que esse funcionario trabalha: ")

    #converter os valores para inteiro
    depto = int(depto)
    horas = int(horas)

    #adicionando os valor no vetor
    funcionario_cadastrado = funcionario(nome, depto, horas, 0)
    storage.append(funcionario_cadastrado) 

#passando os valores do vetor para a função que irá calcular o salário base
salario_base(storage)

#isso vai facilitar, pois eu copiei o vetor com o salario base para poder chamá-lo sempre que precisar
import copy
vSalario_Base = copy.deepcopy(storage)

#passando os valores para a função horas_extras para calcular as horas a mais que 40
horas_extras(storage)

#passando os valores para a função insalubridade para acrescentar ao salario
insalubridade(vSalario_Base, storage)

#passando os valores para a função bonificação para acrescentar ao salario
bonificacao_1(vSalario_Base, storage)

print("\n")

for x in range(parametro_tamanho_array):
    print(storage[x])
    
print("\n\n\n")