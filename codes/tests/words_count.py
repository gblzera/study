def words_count(text):
    words = text.split() #divide o texto em palavras base nos espaços
    return len(words) #retorna o número de palavras

define_text = input("Digite um texto: ")

word_count = words_count(define_text)
print("O texto possui", word_count, "palavras.")