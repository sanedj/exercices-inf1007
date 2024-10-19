#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    return len(string) % 2 == 0


def remove_third_char(string: str) -> str:
    return string[:2] + string[3:]


def replace_char(string: str, old_char: str, new_char: str) -> str:
    new_string = ""
    for i in string:
        if i != old_char:
            new_string += i
        else:
            new_string += new_char
    return new_string


def get_number_of_char(string: str, char: str) -> int:
    nb_de_recu = 0
    for charac in string:
        if charac == char:
            nb_de_recu += 1
        else:
            continue
    return nb_de_recu


def get_number_of_words(sentence: str, word: str) -> int:
    liste = sentence.split(' ')
    recurrences = 0
    for mot in liste:
        if mot == word:
            recurrences += 1
    return recurrences


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans {chaine} est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
