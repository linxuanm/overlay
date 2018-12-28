'''The main class for creating overlays.'''

__author__ = 'David Ma'

__all__ = [
	'Window',
]

import tkinter as tk

windows = []

class Window:

	def __init__(self, root: tk.Tk = None, **kwargs):
		'''Initiates an overlay window.

		root: tk.Tk, the root of the overlay window.
		size: tuple, the dimension (width, height) of the overlay window.
		transparent: bool, whether to set the overlay background transparent.
		transparency: float [0, 1], the transparency of the overlay.
		'''
		self._root = root

		'''Basic configurations.'''
		self.size = kwargs.get('size', (100, 100))

		'''Hide the title bar.'''
		self._root.overrideredirect(1)
		self._root.update_idletasks()
		self._root.lift()

		'''Make the background transparent.'''
		if kwargs.get('transparent', False):
			self._root.config(bg='systemTransparent')

		'''Remove the overlay's shadow.'''
		self._root.wm_attributes('-transparent', True)

		'''Make the overlay float on top of everything.'''
		self._root.wm_attributes('-topmost', True)

	@property
	def size(self):
		return self._size

	@size.setter
	def size(self, newSize):
		self._size = newSize
		self._root.geometry('%sx%s'%self._size)
