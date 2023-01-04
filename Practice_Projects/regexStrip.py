# regexStrip.py - A program that uses regular expressions to strip a string.

import re
def regexStrip(text, replacement = None):
	whitespaceList = stripRegex.findall(text)

	if replacement == None:
		if len(whitespaceList) != 0:
			text = stripRegex.sub('', text)
			return text
		else:
			return 'Your text is already stripped of whitespace.'
	else:
		text = re.sub(f'^{replacement}+', '', text)
		text = re.sub(f'{replacement}+$', '', text)
		return text

stripRegex = re.compile(r'^\s+|\s+$')
myString = '     This string has a lot of whitespace     '

print('Original string: ' + myString)
print('Modified string (whitespace removed): ' + regexStrip(myString))