#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import string
import sys

class Program(object):
	def __init__(self):
		self._charGroups = {
			'uppercase':string.ascii_uppercase,
			'lowercase':string.ascii_lowercase,
			'digits':   string.digits,
			'special':  '%`\'()*+-,./:;<>=!_&~{}|^?$#@"'
		}
		self._chars = self._charGroups['uppercase'] + self._charGroups['lowercase'] + self._charGroups['digits'] + self._charGroups['special']
		self._pw = ''
	def getPw(self):
		return self._pw
	def omitChars(self, cs):
		if cs in self._charGroups.keys():
			self._chars = self._chars.replace(self._charGroups[cs],'')
		else:
			for c in cs:
				self._chars = self._chars.replace(c,'')
	def genPw(self, L=10):
		for i in range(L):
			self._pw += self._chars[ord(os.urandom(1)) % len(self._chars)]
	def usage(self):
		msg = ''
		msg += 'Generate random password.'
		msg += '\n'
		msg += '\nUsage:\t     ./genPw [options] [length]'
		msg += '\n or:\tpython genPw [options] [length]'
		msg += '\n'
		msg += '\nOptions:'
		msg += '\n  -o <C>, omit <C>\tomit one or several characters (C) from the pool of possible characters'
		msg += '\n  -o <G>, omit <G>\tomit a group of characters (G) from the pool of possible characters,'
		msg += '\n                    \twhere G is either of {lowercase, uppercase, digits, special}'
		msg += '\nLength:'
		msg += '\n  [length]\t\toptionally generate a password of another length than 10'
		msg += '\n'
		msg += '\nExamples:'
		msg += '\n  ./genPw\t\t\t43zJvQJX_a\t\ta password of length 10'
		msg += '\n  ./genPw 20\t\t\tP&FsOetjNyP=IHc2wpUf\ta password of length 20'
		msg += '\n  ./genPw -o ilO 15\t\tf!WKGLh5U6r,QRs\t\ta password of length 15, without i, l and O'
		msg += '\n  ./genPw omit uppercase\t.~f*j0!*17\t\ta password of length 10, without uppercase characters'
		return msg

if __name__ == "__main__":
	p = Program()
	if len(sys.argv) < 2:
		p.genPw()
	else:
		if 'help' in sys.argv[1]:
			print p.usage()
			sys.exit(0)
		elif 'omit' in sys.argv[1] or '-o' in sys.argv[1]:
			p.omitChars(sys.argv[2])
			if len(sys.argv) == 3:
				p.genPw()
			elif len(sys.argv) == 4:
				p.genPw(int(sys.argv[3]))
		else:
			p.genPw(int(sys.argv[1]))
	print p.getPw()
