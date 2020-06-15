def contar_caracteres(s):
    """Função que conta os carcteres de uma String
    Ex:
    >>> contar_caracteres('renzo')
    {'e': 1, 'n': 1, 'o': 1, 'r': 1, 'z': 1}

    >>> contar_caracteres('banana')
    {'a': 3, 'b': 1, 'n': 2}

    :param s: string a ser contada

    """
    resultado = {}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1
        # contagem +=1
        # resultado[caracter] = contagem
    return resultado


if __name__ == '__main__':
    print(contar_caracteres('renzo'))
    print()
    print(contar_caracteres('banana'))

# Outra Forma de Fazer a contagem de caracter

#  for caracter in caracteres_ordenados[1:]:
#      if caracter == caracterer_anterior:
#          contagem +=1
#      else:
#          resultado [caracterer_anterior] = caracter
#          caracterer_anterior = caracter
#          contagem = 1

#   resultado[caracterer_anterior] = contagem

#   return resultado

# if __name__ == '__main__':
#    print(contar_caracteres('renzo'))
#    print()
#    print(contar_caracteres('banana'))
