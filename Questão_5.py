"""5 - Duas amigas estabeleceram o código abaixo para que suas mensagens não
fossem lidas pelas demais pessoas.
0 12 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
' ' a b c d e f g h i j k l m n o p q r s t u v w x y z
Observe que cada letra equivale a um número entre 1 e 26 e o espaço ao 0.
Faça um método para "traduzir", que recebe uma lista com uma mensagem
(secreta) e "traduz" a sequência armazenada em uma lista."""

letters = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def translate(phrase):
    new_phrase = []
    phrase_list = phrase.split(',')
    for letter in phrase_list:
        new_phrase.append(letters[int(letter)])
    return ''.join(new_phrase)


while True:
    phrase = input("Digite a mensagem codificada separada por vírgulas:\n")
    print(translate(phrase))
