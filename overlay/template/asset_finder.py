'''Resource locator for finding images.'''

__all__ = [
	'Asset',
]

import os
from random import randint
import tkinter as tk
from PIL import Image, ImageTk

class Asset:

	def __init__(self, template: str):
		'''Initiate a asset fetcher by a given template name.

		template: str, the name of the given template.
		'''
		self._template = template
		dir_path = os.path.abspath(__file__)
		dir_path = os.path.dirname(dir_path)
		self._path = os.path.join(dir_path, f'ui/{template}')

	def fetch(self, name: str, size: tuple = None):
		'''Fetch an asset image.

		name: str, the name of the targeted asset.
		'''
		target = None
		for file in os.listdir(self._path):
			file_str = os.path.splitext(os.path.basename(file).lower())
			if file_str[0] == name.lower() and file_str[1] != '.ai':
				target = os.path.join(self._path, file)

		if target == None:
			raise FileNotFoundError(f'The asset \'{name}\' does not exist.')

		img = Image.open(target)
		if size:
			img = img.resize(size, Image.NEAREST)
		return ImageTk.PhotoImage(img)