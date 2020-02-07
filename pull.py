import sys
import os

class PULL:

	WHITE = '\033[0m'
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'
	LINEUP = '\033[F'

	MIXTURE = {
		'WHITE': '\033[0m',
		'PURPLE': '\033[95m',
		'CYAN': '\033[96m',
		'DARKCYAN': '\033[36m',
		'BLUE': '\033[94m',
		'GREEN': '\033[92m',
		'YELLOW': '\033[93m',
		'RED': '\033[91m',
		'BOLD': '\033[1m',
		'UNDERLINE': '\033[4m',
		'END': '\033[0m',
		'LINEUP': '\033[F'
	}

	VACANT = {
		'WHITE': '',
		'PURPLE': '',
		'CYAN': '',
		'DARKCYAN': '',
		'BLUE': '',
		'GREEN': '',
		'YELLOW': '',
		'RED': '',
		'BOLD': '',
		'UNDERLINE': '',
		'END': '',
		'LINEUP': ''
	}


	def __init__(self):
		if not self.support_colors:
			self.win_colors()

	def support_colors(self):
		plat = sys.platform
		supported_platform = plat != 'Pocket PC' and (plat != 'win32' or \
														'ANSICON' in os.environ)
		is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
		if not supported_platform or not is_a_tty:
			return False
		return True


	def win_colors(self):
		self.WHITE = ''
		self.PURPLE = ''
		self.CYAN = ''
		self.DARKCYAN = ''
		self.BLUE = ''
		self.GREEN = ''
		self.YELLOW = ''
		self.RED = ''
		self.BOLD = ''
		self.UNDERLINE = ''
		self.END = ''
		self.MIXTURE = {
			'WHITE': '',
			'PURPLE': '',
			'CYAN': '',
			'DARKCYAN': '',
			'BLUE': '',
			'GREEN': '',
			'YELLOW': '',
			'RED': '',
			'BOLD': '',
			'UNDERLINE': '',
			'END': '',
			'LINEUP': ''
		}

		for (key, val) in self.MIXTURE.items():
			self.MIXTURE[ key ] = ''

	def run(self, string):
		print(
			"{colora}[']{colorb} {string}".format(
				colora=self.DARKCYAN,
				colorb=self.END,
				string=string
			)
		)

	def info(self, string):
		print(
			"{colora}[*]{colorb} {string}".format(
				colora=self.YELLOW,
				colorb=self.END,
				string=string
			)
		)

	def liner(self, ln, keyid, liner):
		print(
			"{colora}Ln {ln}{colorb}: [{keyid}] : {liner}".format(
				colora=self.GREEN,
				colorb=self.END,
				ln=ln,
				keyid=self.RED+keyid+self.END,
				liner=liner
			)
		)

	def halt(self, string, exit=0):
		print(
			"{colora}[~]{colorb} {string}".format(
				colora=self.RED,
				colorb=self.END,
				string=string
			)
		)

		if exit:
			sys.exit(exit)

	def linebreak(self, brr=1):
		sys.stdout.write("\n" * brr)