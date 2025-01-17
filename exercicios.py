import json
import xml.etree.ElementTree as ET

#exercicio 1

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K

print(f"O valor da variável SOMA é: {SOMA}")

#exercicio 2

def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

num = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")


#exercicio 3

# Função para processar o faturamento diário
def processar_faturamento(faturamento):
    # Filtrar dias com faturamento válido (não zero)
    valores_validos = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

    # Calcular menor valor, maior valor e média
    menor = min(valores_validos)
    maior = max(valores_validos)
    media = sum(valores_validos) / len(valores_validos)

    # Contar dias com faturamento acima da média
    dias_acima_media = len([valor for valor in valores_validos if valor > media])

    return menor, maior, media, dias_acima_media

# Função para carregar dados de um arquivo JSON
def carregar_dados_json(arquivo):
    with open(arquivo, "r") as file:
        return json.load(file)

# Função para carregar dados de um arquivo XML
def carregar_dados_xml(arquivo):
    tree = ET.parse(arquivo)
    root = tree.getroot()

    faturamento = []
    for row in root.findall("row"):
        dia = int(row.find("dia").text)
        valor = float(row.find("valor").text)
        faturamento.append({"dia": dia, "valor": valor})
    return faturamento

# Escolher qual arquivo carregar (JSON ou XML)
tipo_arquivo = input("Digite o tipo de arquivo (json/xml): ").strip().lower()
arquivo = input("Digite o nome do arquivo (com extensão): ").strip()

if tipo_arquivo == "json":
    faturamento = carregar_dados_json(arquivo)
elif tipo_arquivo == "xml":
    faturamento = carregar_dados_xml(arquivo)
else:
    print("Tipo de arquivo não suportado!")
    exit()

# Processar os dados
menor, maior, media, dias_acima_media = processar_faturamento(faturamento)

# Exibir os resultados
print(f"Menor faturamento: R${menor:.2f}")
print(f"Maior faturamento: R${maior:.2f}")
print(f"Média mensal: R${media:.2f}")
print(f"Dias acima da média: {dias_acima_media}")

#exercicio 4

faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento.values())

print("Percentual de representação por estado:")
for estado, valor in faturamento.items():
    percentual = (valor / total) * 100
    print(f"{estado}: {percentual:.2f}%")

#exercicio 5

def reverse_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

string = input("Informe uma string para inverter: ")
print(f"String invertida: {reverse_string(string)}")



