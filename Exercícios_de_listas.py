# Exercícios
# 1- Crie uma lista chamada livros contendo 3 livros diferentes e exiba a lista na tela.
livros = ["Grandes sertões veredas","Vidas secas","Os Sertões"]
print(livros)
# 2- Usando a lista livros, exiba apenas o primeiro e o último elemento.
livros.pop(1)
print(livros)
# 3- Adicione mais dois livros à lista livros usando o método append() e exiba a lista atualizada.
livros.append("Torto Arado")
livros.append("Capitães da Areia")
print(livros)
# 4- Insira o livro "Duna" na segunda posição da lista livros usando insert().
livros.insert(1,"Duna")
print(livros)
# 5- Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado".
# livros.remove("Silêncio dos inocentes")
# livro_específico = "Silêncio dos inocentes"
# if livro_específico in livros:
#     print(f"{livro_específico} está na lista.")
# else:
#     print(f"{livro_específico} não está na lista.")
# print(livros)
# 6- Crie uma lista chamada números com os valores [1, 2, 3, 2, 4, 2, 5]. Mostre quantas vezes o número 2 aparece na lista.

# 7- Percorra a lista livros e exiba cada livro com a frase: "O livro <nome do livro> é interessante"

# 8- Dada a lista idades = [12, 18, 25, 14, 30], use um laço para exibir somente as idades maiores ou iguais a 18.

# 9- Crie uma lista valores = [10, 20, 30, 40]. Use um laço for para calcular manualmente a soma de todos os valores.

# 10- Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo:
# notas = [[7, 8, 9], [6, 5, 7]]. No fim, imprima a média de cada aluno.

# 11- Usando list comprehension, crie um tabuleiro de xadrez vazio e depois adicione todas as peças do jogo na posição inicial. Para melhorar a visualização do tabuleiro, identifique as posições do tabuleiro da seguinte forma:

# [ ] - para posições vazias
# tor - para a torre
# cav - para o cavalo
# bis - para o bispo
# rai - para a rainha
# rei - para o rei
# pea - para o peão
# Por fim imprima o tabuleiro na tela, deixando cada linha da matriz abaixo da outra. (Dica você pode usar a biblioteca numpy para auxiliar na impressão da matriz)