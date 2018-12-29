'''The main class for creating overlays.'''

__author__ = 'David Ma'

__all__ = [
	'Window',
]

import tkinter as tk

overlays = []

master = tk.Tk()
master.withdraw()

class Window:

	def __init__(self, root: tk.Toplevel, **kwargs):
		'''Initiate an overlay window.

		root: tk.Toplevel, the root of the overlay window.
		size: tuple, the dimension (width, height) of the overlay window.
		transparent: bool, whether to set the overlay background transparent.
		transparency: float [0, 1], the transparency of the overlay.
		draggable: bool, whether the window can be dragged
		'''
		self._root = root

		'''Create the master (tk.Tk) if not exists.'''
		global master

		'''Basic configurations.'''
		self.size = kwargs.get('size', (100, 100))

		'''Hide the title bar.'''
		self._root.overrideredirect(1)
		self._root.update_idletasks()
		self._root.lift()

		'''Make the background transparent.'''
		if kwargs.get('transparent', False):
			self._root.config(bg='systemTransparent')

		'''Make the window draggable.'''
		self.draggable = kwargs.get('draggable', True)
		self._root.bind('<ButtonPress-1>', self._drag_start)
		self._root.bind('<ButtonRelease-1>', self._drag_stop)
		self._root.bind('<B1-Motion>', self._move)
		self._drag_stop(None)

		'''Change the transparency of the overlay.'''
		self._root.wm_attributes('-alpha', kwargs.get('transparency', 1))

		'''Remove the overlay's shadow.'''
		self._root.wm_attributes('-transparent', True)

		'''Make the overlay float on top of everything.'''
		self._root.wm_attributes('-topmost', True)

		'''Add self to overlay collections.'''
		overlays.append(self)

	def hide(self):
		'''Hide this overlay.'''
		self._root.withdraw()

	def show(self):
		'''Show this overlay.'''
		self._root.wm_deiconify()
		self._root.lift()
		self._root.wm_attributes('-topmost', True)

	def destroy(self):
		'''Destroy this overlay.'''
		self._root.destroy()

	def _drag_start(self, event):
		'''The start of moving this overlay.'''
		self.x = event.x
		self.y = event.y

	def _drag_stop(self, event):
		'''The start of moving the overlay.'''
		self.x = None
		self.y = None

	def _move(self, event):
		'''The handler for moving the overlay.'''
		if self.draggable:
			mouse_x = self._root.winfo_pointerx() - self._root.winfo_rootx()
			mouse_y = self._root.winfo_pointery() - self._root.winfo_rooty()
			new_x = self._root.winfo_x() + mouse_x - self.x
			new_y = self._root.winfo_y() + mouse_y - self.y
			self._root.geometry('+%d+%d'%(new_x, new_y))

	@property
	def size(self):
		return self._size

	@size.setter
	def size(self, newSize):
		self._size = newSize
		self._root.geometry('%sx%s'%self._size)

	@staticmethod
	def launch():
		'''Enter the mainloop for all overlays.'''
		master.mainloop()

	@staticmethod
	def hide_all():
		'''Hide all overlays.'''
		for overlay in overlays:
			overlay.hide()

	@staticmethod
	def show_all():
		'''Show all overlays.'''
		for overlay in overlays:
			overlay.show()
