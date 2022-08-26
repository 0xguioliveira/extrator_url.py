url = "https://bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real"
url2 = "    "

# Sanitização da URL - (A limpeza dos dados são necessárias para conseguimos validar as mesmas)
url = url.strip()

# Validação da URL
if url == "":
    raise ValueError ("A URL está vazia.")   # "raise" é usado quando queremos levantar um erro para o usuário, no caso, uma URL vazia.

# separa base e parametros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao + 1:] # "+ 1 pois o primeiro argumento no fatiamento é inclusivo.
print(url_parametros)

# Busca o valor de um parâmetro
parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)   # Retornará o primeiro caractér, por isso precisamos somar com o tamanho do parâmetro de busca "(len)"
indice_valor = indice_parametro + len(parametro_busca) + 1    # "+1" para não contarmos com o "="
indice_e_comercial = url_parametros.find('&', indice_valor) # procurar o "&" a partir do indice_valor.
if indice_e_comercial == -1: # Ou seja, se não encontrar o "&"
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)
