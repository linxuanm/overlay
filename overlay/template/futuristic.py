'''A futuristic theme.'''

__all__ = [
	'Alert',
]

import tkinter as tk

from .prefab import TextWindow
from .asset_finder import Asset

assets = Asset('futuristic')

class Alert(TextWindow):

	def __init__(self, text: str):
		'''Creates a window displaying some text.

		text: str, the text to be displayed (dynamic).
		'''
		super().__init__(text, transparent=True, size=(650, 325), alpha = 0.85, resizable=1)
		self.root.bg = assets.fetch('TextWindow', size=self.size)
		background = tk.Label(self.root, image=self.root.bg)
		background.config(bg='systemTransparent')
		background.place(x=0, y=0, relwidth=1, relheight=1)