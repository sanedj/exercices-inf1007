#!/usr/bin/env python
# -*- coding: utf-8 -*-


def check_brackets(text, brackets):
	opening_brackets = dict(zip(brackets[0::2], brackets[1::2]))
	closing_brackets = dict(zip(brackets[1::2], brackets[0::2]))
	bracket_stack = []

	for chr in text:
		if chr in opening_brackets:
			bracket_stack.append(chr)
		elif chr in closing_brackets:
			if len(bracket_stack) == 0 or bracket_stack[-1] != closing_brackets[chr]:
				return False
			bracket_stack.pop()

	return len(bracket_stack) == 0

def remove_comments(full_text, comment_start, comment_end):
	text = full_text
	while True:
		pos1 = text.find(comment_start)
		pos2 = text.find(comment_end)
		if pos1 == -1 and pos2 == -1:
			return text
		if pos2 < pos1 or (pos1 == -1) != (pos2 == -1):
			return None
		text = text[:pos1] + text[pos2 + len(comment_end):]
		

def get_tag_prefix(text, opening_tags, closing_tags):
	for op in opening_tags:
		if text.startswith(op):
			return (op, None)
	for cl in closing_tags:
		if text.startswith(cl):
			return (None, cl)
	return (None, None)

def check_tags(full_text, tag_names, comment_tags):
	text = remove_comments(full_text, *comment_tags)
	if text is None:
		return False
	
	opening_tags = {f"<{name}>": f"</{name}>" for name in tag_names}
	closing_tags = dict((v, k) for k, v in opening_tags.items())
	tag_stack = []

	while len(text) != 0:
		opening, closing = get_tag_prefix(text, opening_tags.keys(), closing_tags.keys())
		if opening is not None:
			tag_stack.append(opening)
			text = text[len(opening):]
		elif closing is not None:
			if len(tag_stack) == 0 or tag_stack[-1] != closing_tags[closing]:
				return False
			tag_stack.pop()
			text = text[len(closing):]
		else:
			text = text[1:]
	
	return len(tag_stack) == 0


if __name__ == "__main__":
	brackets = ("(", ")", "{", "}", "[", "]")
	yeet = "(yeet){yeet}"
	yeeet = "({yeet})"
	yeeeet = "({yeet)}"
	yeeeeet = "(yeet"
	print(check_brackets(yeet, brackets))
	print(check_brackets(yeeet, brackets))
	print(check_brackets(yeeeet, brackets))
	print(check_brackets(yeeeeet, brackets))
	print()

	spam = "Hello, world!"
	eggs = "Hello, /* OOGAH BOOGAH world!"
	parrot = "Hello, OOGAH BOOGAH*/ world!"
	dead_parrot = "Hello, /*oh brave new */world!"
	print(remove_comments(spam, "/*", "*/"))
	print(remove_comments(eggs, "/*", "*/"))
	print(remove_comments(parrot, "/*", "*/"))
	print(remove_comments(dead_parrot, "/*", "*/"))
	print()

	otags = ("<head>", "<body>", "<h1>")
	ctags = ("</head>", "</body>", "</h1>")
	print(get_tag_prefix("<body><h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("<h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("</h1></body>", otags, ctags))
	print(get_tag_prefix("</body>", otags, ctags))
	print()

	spam = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    </title>"
		"  </head>"
		"  <body>"
		"    <h1>Hello, world</h1>"
		"    <!-- Les tags vides sont ignorés -->"
		"    <br>"
		"    <h1/>"
		"  </body>"
		"</html>"
	)
	eggs = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    <!-- Il manque un end tag"
		"    </title>-->"
		"  </head>"
		"</html>"
	)
	parrot = (
		"<html>"
		"  <head>"
		"    <title>"
		"      Commentaire mal formé -->"
		"      Example"
		"    </title>"
		"  </head>"
		"</html>"
	)
	tags = ("html", "head", "title", "body", "h1")
	comment_tags = ("<!--", "-->")
	print(check_tags(spam, tags, comment_tags))
	print(check_tags(eggs, tags, comment_tags))
	print(check_tags(parrot, tags, comment_tags))
	print()

