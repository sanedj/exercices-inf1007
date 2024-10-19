#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


def get_fibonacci_number(nombre):
	#if nombre == 0:
	#	return 0
	#elif nombre == 1:
	#	return 1
	#else:
	#	return get_fibonacci_number(nombre - 1) + get_fibonacci_number(nombre - 2)
	return (
		0 if nombre == 0 else
		1 if nombre == 1 else
		get_fibonacci_number(nombre - 1) + get_fibonacci_number(nombre - 2)
	)

def get_fibonacci_sequence(taille):
	liste = []
	valeur = 0
	if taille == 0:
		return liste
	while len(liste) < taille:
		if valeur == 0:
			liste.append(valeur)
		elif valeur == 1:
			liste.append(valeur)
		else:
			liste.append(liste[-1] + liste[-2])
		valeur += 1
	return liste

def get_sorted_dict_by_decimals(dictio):
	return dict(sorted(dictio.items(), key = lambda e: e[1] % 1.0, reverse = False))

def fibonacci_numbers(length):
	valinit = [0, 1]
	for elem in valinit[0:length]:
		yield elem
	last_elems = deque(valinit)
	for i in range(len(valinit), length):
		fibo_number = last_elems[-1] + last_elems[-2]
		last_elems.append(fibo_number)
		last_elems.popleft()
		yield fibo_number

def build_recursive_sequence_generator(initial_values, recursive_def, keep_whole_sequence=False):
	def recursive_generator(length):
		for elem in initial_values[0:length]:
			yield elem
		last_elems = deque(initial_values)
		for i in range(len(initial_values), length):
			current_element = recursive_def(last_elems)
			last_elems.append(current_element)
			if not keep_whole_sequence:
				last_elems.popleft()
			yield current_element
	return recursive_generator



if __name__ == "__main__":
	print([get_fibonacci_number(0), get_fibonacci_number(1), get_fibonacci_number(2)])
	print([get_fibonacci_number(i) for i in range(10)])
	print()

	print(get_fibonacci_sequence(1))
	print(get_fibonacci_sequence(2))
	print(get_fibonacci_sequence(10))
	print()

	spam = {
		2: 2.1,
		3: 3.3,
		1: 1.4,
		4: 4.2
	}
	eggs = {
		"foo": 42.6942,
		"bar": 42.9000,
		"qux": 69.4269,
		"yeet": 420.1337
	}
	print(get_sorted_dict_by_decimals(spam))
	print(get_sorted_dict_by_decimals(eggs))
	print()

	for fibo_num in fibonacci_numbers(10):
		print(fibo_num, end=" ")
	print("\n")

	def fibo_def(last_elems):
		return last_elems[-1] + last_elems[-2]
	fibo = build_recursive_sequence_generator([0, 1], fibo_def)
	for fi in fibo(10):
		print(fi, end=" ")
	print("\n")

	lucas = build_recursive_sequence_generator([2, 1], lambda seq: seq[-1] + seq[-2])
	print(f"Lucas : {[elem for elem in lucas(10)]}")
	perrin = build_recursive_sequence_generator([3, 0, 2], lambda seq: seq[-2] + seq[-3])
	print(f"Perrin : {[elem for elem in perrin(10)]}")
	hofstadter_q = build_recursive_sequence_generator([1, 1], lambda seq: seq[-seq[-1]] + seq[-seq[-2]], True)
	print(f"Hofstadter-Q : {[elem for elem in hofstadter_q(10)]}")
