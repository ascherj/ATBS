# strongPassword.py - A program that detects if a password is strong.
import re

def isStrong(pw):
	mo1 = lengthRegex.search(pw)
	mo2 = lowercaseRegex.search(pw)
	mo3 = uppercaseRegex.search(pw)
	mo4 = numberRegex.search(pw)
	
	if mo1 == None:
		print('Password must have at least eight characters.')
	elif mo2 == None:
		print('Password must have a lowercase character.')
	elif mo3 == None:
		print('Password must have an uppercase character.')
	elif mo4 == None:
		print('Password must have a digit.')
	else:
		return True
	return False

lengthRegex = re.compile(r'\w{8,}')
lowercaseRegex = re.compile(r'[a-z]+')
uppercaseRegex = re.compile(r'[A-Z]+')
numberRegex = re.compile(r'\d+')

while True:
	print('Please enter a password:')
	password = input()
	if isStrong(password):
		print('Your password is strong.')
		break