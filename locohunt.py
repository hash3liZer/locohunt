import argparse
import sys
import os
import csv

def main():
	parser = argparse.ArgumentParser()

	parser.add_argument('-t', '--target', dest="target", default="", type=str)
	parser.add_argument('-r', '--regex', dest="regex", default="", type=str)
	parser.add_argument('-f', '--regex-file', dest="regfile", default="", type=str)
	parser.add_argument('-d', '--depth', dest="depth", default=0, type=int)

	opts = parser.parse_args()

	parser = PARSER(opts)

if __name__ == "__main__":
	main()