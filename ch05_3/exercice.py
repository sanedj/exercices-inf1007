#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def get_num_letters(text):
	new_text = ""
	if text.isalnum():
		nombre = len(text)
	else:
		for charac in text:
			if charac.isalnum():
				new_text = new_text + charac
				continue
			if not charac.isalnum():
				continue
		nombre = len(new_text)
	return nombre

def get_word_length_histogram(text):
	histogramme = [0]
	for mot in text.split():
		longueur = get_num_letters(mot)
		if longueur >= len(histogramme):
			histogramme += [0] * (longueur - len(histogramme) + 1)
		histogramme[longueur] += int(longueur != 0)
	return histogramme

def format_histogram(histogram):
	ROW_CHAR = "*"
	total = ""
	liste = list(enumerate(histogram))
	for i in range(1, len(liste)):
		ligne = " " + str(liste[i][0]) + " " + ROW_CHAR * int(liste[i][1])
		total = total + ligne + "\n"
	return total

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	hauteur = max(histogram)
	resultat = ""
	for i in range(hauteur - 1, -1, -1):
		resultat += "".join([BLOCK_CHAR if elem >= i + 1 else " " for elem in histogram[1:]]) + "\n"
	resultat += LINE_CHAR * len(histogram)
	return resultat


if __name__ == "__main__":
	word = "est?"
	print(f"The number of characters for '{word}' is: {get_num_letters(word)}")
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
