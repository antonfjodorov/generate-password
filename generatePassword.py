#!/usr/bin/python
#-*- coding: utf-8 -*-
from colorconsole import ColorConsole as Console
import getopt
import os
import pyperclip
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
		msg += '\nUsage:       ./genPw [options] [length]'
		msg += '\n or:    python genPw [options] [length]'
		msg += '\n'
		msg += '\nOptions (can be combined):'
		msg += '\n  -o <C>, --omit <C>  omit one or several characters (C) from the pool of possible'
		msg += '\n                      characters.'
		msg += '\n  -o <G>, --omit <G>  omit a group of characters (G) from the pool of possible,'
		msg += '\n                      characters where G is either of {lowercase, uppercase,'
		msg += '\n                      digits, special}'
		msg += '\n  -c, --copy          copy password to clipboard'
		msg += '\n'
		msg += '\nLength:'
		msg += '\n  [length]            optionally generate a password of another length than 10'
		msg += '\n'
		msg += '\nExamples:'
		msg += '\n  ./genPw                         '+Console.orange('43zJvQJX_a')+'      a password of length 10'
		msg += '\n  ./genPw -c 15                   '+Console.orange('P&FsOetjNyP=IHc')+' a password of length 15, copied'
		msg += '\n                                                  to clipboard. Press Ctrl-V to'
		msg += '\n                                                  paste it.'
		msg += '\n  ./genPw -o ilO 15               '+Console.orange('f!WKGLh5U6r,QRs')+' a password of length 15, no'
		msg += '\n                                                  letters i, l and O'
		msg += '\n  ./genPw --omit uppercase        '+Console.orange('.~f*j0!*17')+'      a password of length 10, no'
		msg += '\n                                                  uppercase chars'
		msg += '\n  ./genPw -o digits -o special -c '+Console.orange('XimoMKZDtT')+'      a password of length 10, no'
		msg += '\n                                                  digits or special chars'
		return msg

if __name__ != "__main__":
	sys.exit(0);

doCopy = False
argNum = len(sys.argv)
p = Program()
if argNum < 2:
	p.genPw()
	print p.getPw()
	sys.exit(0)

try:
	opts, args = getopt.getopt(sys.argv[1:], "cho:", ["clipboard", "help", "omit="])
except getopt.GetoptError as e:
	p.usage()
	sys.exit(1)
for opt, arg in opts:
	if opt == '-c' or opt == '--clipboard':
		doCopy = True
	elif opt == '-h' or opt == '--help':
		print p.usage()
		sys.exit(0)
	elif opt == '-o' or opt == '--omit':
		p.omitChars(arg)
if not args:
	p.genPw()
else:
	try:
		int_arg = int(args[0])
		p.genPw(int_arg)
	except:
		print Console.red('Error'), 'password length must be a number. Your input:', Console.orange(args[0])
		sys.exit(1)
print p.getPw()
if doCopy:
	pyperclip.copy(p.getPw())
	print Console.orange('copied to clipboard')