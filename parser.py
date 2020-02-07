import os
import sys

class PARSER:

	def __init__(self, opts):
		self.list      = self.target(opts.target)
		self.regex     = self.regex(opts.regex)
		self.regexfile = self.regexfile(opts.regexfile)
		self.depth     = opts.depth

	def target(self, tgt):
		if tgt: