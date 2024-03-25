def move_letters_to_end(word):
    vowels = "aeiouAEIOU"
    for index, letter in enumerate(word):
        if letter in vowels:
            return word[index:] + word[:index]
    return word

word = input("Podaj wyraz: ")
result = move_letters_to_end(word)
print("Wynik: " + result)