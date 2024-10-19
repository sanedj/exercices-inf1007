#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 1:
        return -number
    return number 


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    liste = []
    for lettre in prefixes:
        combinaison = str(lettre) + suffixe
        liste.append(combinaison)
    return liste


def prime_integer_summation() -> int:
    nbs_premiers = [2, 3, 5]
    number = 6
    while len(nbs_premiers) < 100:
        is_prime = True
        for i in range(2, number // 2):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            nbs_premiers.append(number)
        number += 1

    return sum(nbs_premiers)


def factorial(number: int) -> int:
    fact = 1
    for i in range(number, 0, -1):
        fact *= i
    return fact


def use_continue() -> None:
    for i in range (1, 11):
        if i == 5:
            continue
        print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    acceptance = []
    for groupe in groups:
        if len(groupe) <= 3 or len(groupe) > 10:
            acceptance.append(False)
            continue
        if 25 in groupe:
            acceptance.append(True)
            continue
        if (min(groupe) < 18) or (max(groupe) > 70 and 50 in groupe):
            acceptance.append(False)
            continue
        acceptance.append(True)
    return acceptance


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
