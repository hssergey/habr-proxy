import re
from django.conf import settings


def add_symbols(text):
	word_start = 0
	regexp = re.compile("\W")
	index = 0
	using_word = True
	result = ""
	for char in text:
		if len(regexp.findall(char)):
			if using_word and index - word_start == settings.CHARS_AMOUNT:
				result = result + settings.ADDING_STRING
			using_word = False
		elif not using_word:
			using_word = True
			word_start = index
		result = result + char
		index = index + 1
	return result
