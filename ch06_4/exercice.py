#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import copy
import itertools


def get_even_keys(dictionary):
	return set([key for key in dictionary.keys() if key % 2 == 0])

def join_dictionaries(dictionaries):
	merge_dict = {}
	for dicto in dictionaries:
		merge_dict.update(dicto)
	return merge_dict

def dictionary_from_lists(keys, values):
	dicto = {}
	for item in zip(keys, values):
		dicto[item[0]] = item[1]
	return dicto

def get_greatest_values(dictionnary, num_values):
	liste = [v for v in dictionnary.values()]
	max_liste = []
	for i in range(num_values):
		val_max = max(liste)
		max_liste.append(val_max)
		liste.remove(val_max)
	return max_liste

def get_sum_values_from_key(dictionnaries, key):
	somme = 0
	for d in dictionnaries:
		if key in d:
			somme += d[key]
	return somme


if __name__ == "__main__":
	yeet = {
		69: "Yeet",
		420: "YeEt",
		9000: "YEET",
	}
	print(get_even_keys(yeet))
	print()

	yeet = {
		69: "Yeet",
		420: "YeEt",
		9000: "YEET",
	}
	doot = {
		0xBEEF: "doot",
		0xDEAD: "DOOT",
		0xBABE: "dOoT"
	}
	print(join_dictionaries([yeet, doot]))
	print()
	
	doh = [
		"D'OH!",
		"d'oh",
		"DOH!"
	]
	nice = [
		"NICE!",
		"nice",
		"nIcE",
		"NAIIIIICE!"
	]
	print(dictionary_from_lists(doh, nice))
	print()
	
	nums = {
		"nice": 69,
		"nice bro": 69420,
		"AGH!": 9000,
		"dude": 420,
		"git gud": 1337
	}
	print(get_greatest_values(nums, 1))
	print(get_greatest_values(nums, 3))
	print()

	bro1 = {
		"money": 12,
		"problems": 14,
		"trivago": 1
	}
	bro2 = {
		"money": 56,
		"problems": 406
	}
	bro3 = {
		"money": 1,
		"chichis": 1,
		"power-level": 9000
	}
	print(get_sum_values_from_key([bro1, bro2, bro3], "problems"))
	print(get_sum_values_from_key([bro1, bro2, bro3], "money"))
	print()
