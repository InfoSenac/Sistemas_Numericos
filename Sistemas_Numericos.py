import streamlit as st

def binario_para_decimal(binario: str) -> int:
    """Converte um número binário (string) para decimal (inteiro)."""
    decimal = 0
    tamanho = len(binario)
    for i in range(tamanho):
        digito = int(binario[tamanho - 1 - i])  # Obtém o dígito binário
        peso = 2 ** i  # Calcula a potência de 2 correspondente
        decimal = decimal + digito * peso  # Soma ao total
    return decimal
    

def decimal_para_binario(decimal: int) -> str:
    """Converte um número decimal (inteiro) para binário (string)."""
    binario = ""
    while decimal > 0:
        resto = decimal % 2  # Obtém o resto da divisão por 2
        binario = str(resto) + binario  # Adiciona o bit na frente
        decimal = decimal // 2  # Reduz o número decimal
    if binario:
        return binario
    else:
        return "0" # Retorna "0" se o número for 0
        

def octal_para_decimal(octal: str) -> int:
    """Converte um número octal (string) para decimal (inteiro)."""
    decimal = 0
    tamanho = len(octal)
    for i in range(tamanho):
        digito = int(octal[tamanho - 1 - i])  # Obtém o dígito octal
        peso = 8 ** i  # Calcula a potência de 8 correspondente
        decimal = decimal + digito * peso  # Soma ao total
    return decimal
    

def decimal_para_octal(decimal: int) -> str:
    """Converte um número decimal (inteiro) para octal (string)."""
    octal = ""
    while decimal > 0:
        resto = decimal % 8  # Obtém o resto da divisão por 8
        octal = str(resto) + octal  # Adiciona o dígito na frente
        decimal = decimal // 8  # Reduz o número decimal
    if octal:
        return octal
    else:
        return "0" # Retorna "0" se o número for 0
        

def hexadecimal_para_decimal(hexadecimal: str) -> int:
    """Converte um número hexadecimal (string) para decimal (inteiro)."""
    valores = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
               "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}  # Mapeia caracteres hexadecimais para valores decimais
    hexadecimal = hexadecimal.upper()  # Converte para maiúsculas para garantir correspondência
    decimal = 0
    tamanho = len(hexadecimal)
    for i in range(tamanho):
        digito = hexadecimal[tamanho - 1 - i]  # Obtém o caractere correspondente
        valor_decimal = valores[digito]  # Converte para o valor decimal
        peso = 16 ** i  # Calcula a potência de 16 correspondente
        decimal = decimal + valor_decimal * peso  # Soma ao total
    return decimal
    

def decimal_para_hexadecimal(decimal: int) -> str:
    """Converte um número decimal (inteiro) para hexadecimal (string)."""
    valores = "0123456789ABCDEF"  # Mapeia valores de 0 a 15 para caracteres hexadecimais
    hexadecimal = ""
    while decimal > 0:
        resto = decimal % 16  # Obtém o valor do dígito hexadecimal
        hexadecimal = valores[resto] + hexadecimal  # Adiciona o caractere correspondente na frente
        decimal = decimal // 16  # Reduz o número decimal
    if hexadecimal:
        return hexadecimal
    else:
        return "0" # Retorna "0" se o número for 0
        

st.title(':orange[Sistemas Numéricos] :sunglasses:')
st.markdown('### Feito por Antônio Márcio - Senac Lafaiete')

st.markdown('## ⚠️ *Decimal*')

decimal_binario = st.number_input(
    label='Digite o número decimal a ser convertido em binário:',
    placeholder='Digite somente números',
    min_value=0,
    )
st.write("### Binário: ", decimal_para_binario(decimal_binario))

binario_decimal = st.text_input(
    label='Digite o número binário a ser convertido em decimal:',
    placeholder='Digite somente números 0 e 1'
    )
st.write("### Decimal: ", binario_para_decimal(binario_decimal))

st.markdown('## ⚠️ *Octal*')

decimal_octal = st.number_input(
    label='Digite o número decimal a ser convertido em octal:',
    placeholder='Digite somente números',
    min_value=0,
    )
st.write("### Octal: ", decimal_para_octal(decimal_octal))

octal_decimal = st.text_input(
    label='Digite o número octal a ser convertido em decimal:',
    placeholder='Digite somente números'
    )
st.write("### Decimal", octal_para_decimal(octal_decimal))

st.markdown('## ⚠️ *Hexadecimal*')

decimal_hexa = st.number_input(
    label='Digite o número decimal a ser convertido em hexadecimal:',
    placeholder='Digite somente números',
    min_value=0,
    )
st.write("### Hexadecimal: ", decimal_para_hexadecimal(decimal_hexa))

hexa_decimal = st.text_input(
    label='Digite o número hexadecimal a ser convertido em decimal:',
    placeholder='Digite somente letras e números'
    )
st.write("### Decimal:", hexadecimal_para_decimal(hexa_decimal))
