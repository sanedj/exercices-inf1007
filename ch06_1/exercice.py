#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        values = []

        while len(values) < 10:
            values.append(input('Veuillez me fournir une valeur: '))

    valeurs_num = [float(value) for value in values if value.isdigit()]
    valeurs_str = [value for value in values if not value.isdigit()]

    return sorted(valeurs_num) + sorted(valeurs_str)


def anagrams(words: list = None) -> bool:
    if words is None:

        words = []
        while len(words) < 2:
            words.append(input('Veuillez me fournir un mot: '))

    return sorted(words[0]) == sorted(words[1])


def contains_doubles(items: list) -> bool:
    return len(items) != len(set(items))


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_student = {}
    for key, value in student_grades.items():
        moy = sum(value) / len(value)

        if len(best_student) == 0 or list(best_student.values())[0] < moy:
            best_student = {key: moy}

    return best_student


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    frequence_app = {}
    for lettre in sentence:
        frequence_app[lettre] = sentence.count(lettre)

    sorted_keys = sorted(frequence_app, key=frequence_app.__getitem__, reverse=True)
    for key in sorted_keys:
        if frequence_app[key] > 5:
            print(f"Le caractère {key} revient {frequence_app[key]} fois.")

    return frequence_app


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    nom_recette = input('What is the name of your recipe')
    ingredients = input('What are the necessary ingredients')
    return {nom_recette: ingredients}


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    nom = input("Recipe's name")
    
    if nom in ingredients:
        print(ingredients[nom])
    else:
        print('Recipe is not in the book')
        print_recipe(ingredients)


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
