#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get_first_part_of_name(name):
	return "Bonjour, " + (name.split('-')[0]).capitalize()

def get_random_sentence(animals, adjectives, fruits):
	return f"Aujourd'hui, j'ai vu un {random.choice(animals)} s'emparer d'un panier {random.choice(adjectives)} plein de {random.choice(fruits)}."

def format_date(year, month, day, hours, minutes, seconds):	
	return f"{year:04}-{month:02}-{day:02} {hours:02}:{minutes:02}:{seconds:06.3f}"

def encrypt(text, shift):
	new_text = ""
	for lettre in text:
		encrypted_letter = lettre
		# Crypter seulement les caractères alphabétiques.
		if lettre.isalpha():
			index = ord(lettre.upper()) - ord("A")
			encrypted_index = (index + shift) % 26
			encrypted_letter = chr(ord("A") + encrypted_index)
		new_text += encrypted_letter
	return new_text

def decrypt(encrypted_text, shift):
	return encrypt(encrypted_text, -shift)	


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))

	print(format_date(1970, 1, 12, 12, 3, 45.6789))

	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
