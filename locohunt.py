import argparse
import sys
import os
import csv
from pull import PULL
from parser import PARSER

class LOCOHUNT:

	def __init__(self, prs):
		self.tgtlist = prs.list
		self.regexs  = prs.regexs
		self.depth   = prs.depth

	def engage(self):
		return

def main():
	parser = argparse.ArgumentParser()

	parser.add_argument('-t', '--target', dest="target", default="", type=str)
	parser.add_argument('-r', '--regex', dest="regex", default="", type=str)
	parser.add_argument('-f', '--regex-json', dest="regfile", default="", type=str)
	parser.add_argument('-d', '--depth', dest="depth", default=0, type=int)

	opts = parser.parse_args()
	parser = PARSER(opts)

	print(parser.list)

	#locohunt = LOCOHUNT(parser)
	#locohunt.engage()

if __name__ == "__main__":
	main()