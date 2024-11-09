#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def format_bill_total(data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	sous_total = 0
	for achat in data:
		sous_total = sous_total + achat[INDEX_QUANTITY] * achat[INDEX_PRICE]
	taxes, total = sous_total * 0.15, sous_total * 1.15
	bill_total = [
		("SOUS TOTAL", sous_total), 
		("TAXES     ", taxes), 
		("TOTAL     ", total)
	]
	result = ""
	for bd in bill_total:
		result += f"{bd[0]} {bd[1]:>10.2f} $" "\n"
	return result

def format_bill_items(data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	bill_items = []
	longueur = 0
	for no_items in data:
		if len(no_items[INDEX_NAME]) > longueur:
			longueur = len(no_items[INDEX_NAME])
	result = ""
	for item in data:
		result += f"{item[INDEX_NAME]:{longueur}} {item[INDEX_PRICE]*item[INDEX_QUANTITY]:>10.2f} $" "\n"
	
	return result

def format_number(number, num_decimal_digits):
	return f'{number:,.{num_decimal_digits}f}'.replace(',',' ')

def get_triangle(num_rows):
	largeur_int = num_rows * 2 - 1
	largeur_tot = largeur_int + 2
	liste = []
	for i in range(0, num_rows):
		string_A = 'A' * (1 + 2 * i)
		liste.append('+' + string_A.center(largeur_int) + '+')

	return "+"*largeur_tot + "\n" + "\n".join(liste) + "\n" + "+"*largeur_tot


if __name__ == "__main__":
	purchases = [
		("chaise ergonomique", 1, 399.99),
		("g-fuel", 69, 35.99),
		("blue screen", 2, 39.99)
	]
	print(format_bill_items(purchases).strip())
	print("- - - - - - - - - - - - - - - - - - -")
	print(format_bill_total(purchases).strip())

	print("\n------------------")

	print(format_number(-1420069.0678, 2))

	print("\n------------------")

	print(get_triangle(2))
	print(get_triangle(5))
