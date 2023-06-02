<head>
  <h1>Documentação do Código: Descobridor de dígitos do CPF</h1>
  <p>
    Este código em Python permite descobrir os dígitos verificadores de um CPF com base nos nove primeiros números fornecidos pelo usuário.
  </p>
 </head>
 
<body>
  <h2>Entrada</h2>
  <p>
    O código solicita ao usuário que digite os nove primeiros números do CPF. A entrada é obtida por meio da função <code>input()</code> e armazenada na variável <code>cpf</code>.
  </p>

  <h2>Processamento</h2>
  <ol>
    <li>
      <code>numeros_cpf = cpf.split('.')</code>: Esta linha remove os pontos do CPF digitado pelo usuário e separa os números em blocos de três, armazenando-os em uma lista chamada <code>numeros_cpf</code>.
    </li>
    <li>
      <code>numeros_limpos = []</code>: Criação de uma lista vazia chamada <code>numeros_limpos</code>, que será usada para armazenar os números individuais do CPF.
    </li>
    <li>
      <code>multiplicador_algoritmo = 10</code>: Variável que define o multiplicador utilizado no cálculo do dígito verificador.
    </li>
    <li>
      <code>divisor_algoritmo = 11</code>: Variável que define o divisor utilizado no cálculo do dígito verificador.
    </li>
    <li>
      <code>resultado_soma1 = 0</code>, <code>resultado_soma2 = 0</code>: Variáveis usadas para armazenar as somas parciais dos produtos dos números do CPF pelos respectivos pesos.
    </li>
    <li>
      <code>contador_regressivo1 = 10</code>, <code>contador_regressivo2 = 11</code>: Contadores regressivos usados para calcular os pesos de cada número do CPF.
    </li>
    <li>
      <code>resultado_final1 = 0</code>, <code>resultado_final2 = 0</code>: Variáveis que armazenam o resultado final do cálculo dos dígitos verificadores.
    </li>
    <li>
      <code>primeiro_digito = 0</code>, <code>segundo_digito = 0</code>: Variáveis para armazenar os dígitos verificadores calculados.
    </li>
    <li>
      <code>for i in numeros_cpf:</code>: Este laço percorre os blocos de números do CPF.
    </li>
    <li>
      <code>for item in i:</code>: Este laço percorre cada número dentro de um bloco.
    </li>
    <li>
      <code>numeros_limpos += item</code>: Adiciona cada número individual à lista <code>numeros_limpos</code>, convertendo-o para o tipo inteiro.
    </li>
    <li>
      O próximo bloco de código calcula o primeiro dígito verificador do CPF:
      <ul>
        <li><code>for numero in numeros_limpos:</code>: Percorre os números individuais do CPF.</li>
        <li><code>resultado_soma1 += int(numero) * contador_regressivo1</code>: Realiza a soma ponderada dos números multiplicados pelos pesos.</li>
        <li><code>contador_regressivo1 -= 1</code>: Atualiza o contador regressivo.</li>
        <li><code>resultado_final1 = (resultado_soma1 * multiplicador_algoritmo) % divisor_algoritmo</code>: Aplica o algoritmo do CPF para calcular o primeiro dígito verificador.</li>
        <li><code>primeiro_digito = resultado_final1 if resultado_final1 <= 9 else 0</code>: Verifica se o resultado do cálculo é menor ou igual a 9. Caso positivo, o valor é atribuído à variável <code>primeiro_digito</code>; caso contrário, é atribuído o valor zero.</li>
      </ul>
    </li>
    <li>
      <code>numeros_limpos.append(primeiro_digito)</code>: Adiciona o primeiro dígito verificador à lista <code>numeros_limpos</code> para cálculo do segundo dígito verificador.
    </li>
    <li>
      O próximo bloco de código calcula o segundo dígito verificador do CPF:
      <ul>
        <li><code>for numero in numeros_limpos:</code>: Percorre os números individuais do CPF, incluindo o primeiro dígito verificador.</li>
        <li><code>resultado_soma2 += int(numero) * contador_regressivo2</code>: Realiza a soma ponderada dos números multiplicados pelos pesos.</li>
        <li><code>contador_regressivo2 -= 1</code>: Atualiza o contador regressivo.</li>
        <li><code>resultado_final2 = (resultado_soma2 * multiplicador_algoritmo) % divisor_algoritmo</code>: Aplica o algoritmo do CPF para calcular o segundo dígito verificador.</li>
        <li><code>segundo_digito = resultado_final2 if resultado_final1 <= 9 else 0</code>: Verifica se o resultado do cálculo é menor ou igual a 9. Caso positivo, o valor é atribuído à variável <code>segundo_digito</code>; caso contrário, é atribuído o valor zero.</li>
      </ul>
    </li>
  </ol>

  <h2>Saída</h2>
  <p>
    Por fim, o código exibe a mensagem contendo os dígitos verificadores calculados utilizando a função <code>print()</code>. A mensagem é formatada com o valor de <code>primeiro_digito</code> seguido por <code>segundo_digito</code> e é exibida ao usuário.
  </p>
  <p>
    Exemplo de saída: "O digito do seu CPF é XX" (onde "XX" são os dígitos verificadores calculados).
  </p>
</body>
</html>
