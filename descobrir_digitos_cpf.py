cpf = input('Digite os nove primeiros números do CPF: ')

numeros_cpf = cpf.split('.') # Retira os pontos e separa em blocos de três para cada valor.
numeros_limpos = []

multiplicador_algoritmo = 10
divisor_algoritmo = 11
resultado_soma1 = 0
resultado_soma2 = 0
contador_regressivo1 = 10
contador_regressivo2 = 11
resultado_final1 = 0
resultado_final2 = 0
primeiro_digito= 0
segundo_digito = 0

for i in numeros_cpf: # Estrutura para separar cada "bloco" de valor dentro da lista
    for item in i: # Estrutura para individualizar cada número para que possa ser feito uma soma.
        numeros_limpos += item

for numero in numeros_limpos:
    resultado_soma1 += int(numero) * contador_regressivo1
    contador_regressivo1 -= 1

resultado_final1 = (resultado_soma1 * multiplicador_algoritmo) % divisor_algoritmo

primeiro_digito = resultado_final1 if resultado_final1 <= 9 else 0

numeros_limpos.append(primeiro_digito) # Para verificar o segundo digito, é necessário fazer um cálculo com o primeiro.

for numero in numeros_limpos:
    resultado_soma2 += int(numero) * contador_regressivo2
    contador_regressivo2 -= 1

resultado_final2 = (resultado_soma2 * multiplicador_algoritmo) % divisor_algoritmo

segundo_digito = resultado_final2 if resultado_final1 <= 9 else 0
 
print(f'O digito do seu CPF é {str(primeiro_digito) + str(segundo_digito)}.')
