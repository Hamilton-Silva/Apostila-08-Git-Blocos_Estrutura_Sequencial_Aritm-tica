import random
import math

# Código implementado com utilização de boas práticas, tais como modularização, tipagem de funções, 
# parâmetros com valores padrão, docstrings e comentários 
  

# Gera função auxiliar para exibir valores formatados com título
def exibir_resultado(titulo: str, resultado: str):
    print(f"\n{titulo}\n{'-' * len(titulo)}\n{resultado}\n")

# Exercício 1.1 - Gera a inserção de um valor inteiro
def inserir_ou_gerar_inteiro(minimo: int = 1, maximo: int = 100) -> int:
    escolha = input(f"1.1 - Deseja inserir um valor inteiro? (S/N) [Valor padrão: entre {minimo} e {maximo}]: ").strip().upper()
    if escolha == 'S':
        return int(input(f"Insira um valor inteiro entre {minimo} e {maximo}: "))
    return random.randint(minimo, maximo)

# Exercício 1.2 - Gera a inserção de um valor real
def inserir_ou_gerar_real(minimo: float = 1.0, maximo: float = 10.0) -> float:
    escolha = input(f"1.2 - Deseja inserir um valor real? (S/N) [Valor padrão: entre {minimo} e {maximo}]: ").strip().upper()
    if escolha == 'S':
        return float(input(f"Insira um valor real entre {minimo} e {maximo}: "))
    return random.uniform(minimo, maximo)

# 1.3 Gera a inserção de um valor de Celsius no intervalo [20, 30] e converte para Fahrenheit
def inserir_ou_gerar_celsius(minimo: float = 20.0, maximo: float = 30.0) -> float:
    escolha = input(f"1.3 - Deseja inserir um valor de Celsius? (S/N) [Valor padrão: entre {minimo} e {maximo}]: ").strip().upper()
    if escolha == 'S':
        return float(input(f"Insira um valor de Celsius entre {minimo} e {maximo}: "))
    return random.uniform(minimo, maximo)

def converter_celsius_para_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32

# 1.4 Calcula o delta (discriminante) de uma equação do segundo grau
def calcular_delta(a: float, b: float, c: float) -> float:
    return b**2 - 4 * a * c

# 1.5 Calcula a raiz cúbica do antecessor e a raiz quadrada do sucessor de um número inteiro
def calcular_raizes_antecessor_sucessor(numero: int) -> tuple:
    antecessor = numero - 1
    sucessor = numero + 1
    raiz_cubica_antecessor = antecessor**(1/3)
    raiz_quadrada_sucessor = math.sqrt(sucessor)
    return raiz_cubica_antecessor, raiz_quadrada_sucessor

# 1.6 Gera a inserção de medidas e preço por m² no intervalo [60, 70] e calcula o valor total do terreno
def inserir_ou_gerar_preco_m2(minimo: float = 60.0, maximo: float = 70.0) -> float:
    escolha = input(f"1.6 - Deseja inserir o preço por metro quadrado? (S/N) [Valor padrão: entre {minimo} e {maximo}]: ").strip().upper()
    if escolha == 'S':
        return float(input(f"Insira o preço por metro quadrado entre {minimo} e {maximo}: "))
    return random.uniform(minimo, maximo)

def calcular_valor_terreno(largura: float, comprimento: float, preco_m2: float) -> float:
    area = largura * comprimento
    return area * preco_m2

# 1.7 Gera a inserção do ano de nascimento no intervalo [1980, 2000] e o ano atual no intervalo [2010, 2020].
def inserir_ou_gerar_ano_nascimento(minimo: int = 1980, maximo: int = 2000) -> int:
    escolha = input(f"1.7 - Deseja inserir o ano de nascimento? (S/N) [Valor padrão: entre {minimo} e {maximo}]: ").strip().upper()
    if escolha == 'S':
        return int(input(f"Insira o ano de nascimento entre {minimo} e {maximo}: "))
    return random.randint(minimo, maximo)

def inserir_ou_gerar_ano_atual(minimo: int = 2010, maximo: int = 2020) -> int:
    escolha = input(f"1.7 - Deseja inserir o ano atual? (S/N) [Valor padrão: entre {minimo} e {maximo}]: ").strip().upper()
    if escolha == 'S':
        return int(input(f"Insira o ano atual entre {minimo} e {maximo}: "))
    return random.randint(minimo, maximo)

def calcular_idade(ano_nascimento: int, ano_atual: int) -> int:
    return ano_atual - ano_nascimento

# Gera a função principal para executar todos os exercícios acima
def main():
    # 1.1
    inteiro_gerado = inserir_ou_gerar_inteiro()
    exibir_resultado("1.1 - Valor inteiro gerado", f"{inteiro_gerado}")

    # 1.2
    real_gerado = inserir_ou_gerar_real()
    exibir_resultado("1.2 - Valor real gerado", f"{real_gerado:.2f}")

    # 1.3
    celsius = inserir_ou_gerar_celsius()
    fahrenheit = converter_celsius_para_fahrenheit(celsius)
    exibir_resultado("1.3 - Temperatura em Celsius e Fahrenheit", f"{celsius:.2f}°C -> {fahrenheit:.2f}°F")

    # 1.4
    a = inserir_ou_gerar_real()
    b = inserir_ou_gerar_real()
    c = inserir_ou_gerar_real()
    delta = calcular_delta(a, b, c)
    exibir_resultado("1.4 - Cálculo de Delta", f"a={a:.2f}, b={b:.2f}, c={c:.2f}, Delta = {delta:.2f}")

    # 1.5
    num = inserir_ou_gerar_inteiro()
    raiz_cubica, raiz_quadrada = calcular_raizes_antecessor_sucessor(num)
    exibir_resultado("1.5 - Raízes do antecessor e sucessor",
                     f"Número: {num}, Raiz cúbica do antecessor: {raiz_cubica:.2f}, Raiz quadrada do sucessor: {raiz_quadrada:.2f}")

    # 1.6
    largura = inserir_ou_gerar_real()
    comprimento = inserir_ou_gerar_real()
    preco_m2 = inserir_ou_gerar_preco_m2()
    valor_total_terreno = calcular_valor_terreno(largura, comprimento, preco_m2)
    exibir_resultado("1.6 - Valor total do terreno",
                     f"Largura: {largura:.2f}m, Comprimento: {comprimento:.2f}m, Preço por m²: R${preco_m2:.2f}, Valor total: R${valor_total_terreno:.2f}")

    # 1.7
    ano_nascimento = inserir_ou_gerar_ano_nascimento()
    ano_atual = inserir_ou_gerar_ano_atual()
    idade = calcular_idade(ano_nascimento, ano_atual)
    exibir_resultado("1.7 - Idade calculada",
                     f"Ano de nascimento: {ano_nascimento}, Ano atual: {ano_atual}, Idade: {idade} anos")

# Executa o programa principal
if __name__ == "__main__":
    main()
