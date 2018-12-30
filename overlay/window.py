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

	def __init__(self, **kwargs):
		'''Initiate an overlay window.

		All parameters of this method are cofiguration parameters and
		therefore optional.

		size: tuple, the dimension (width, height) of the overlay window.
		position: tuple, the position of the overlay (on screen).
		transparent: bool, whether to set the overlay background transparent.
		alpha: float [0, 1], the alpha (transparency) of the overlay.
		draggable: bool, whether the window can be dragged
		'''
		self._root = tk.Toplevel();

		'''Hide the title bar.'''
		self._root.overrideredirect(1)
		self._root.update_idletasks()
		self._root.lift()

		'''Basic configurations.'''
		self.size = kwargs.get('size', (100, 100))
		self.position = kwargs.get('position', (0, 0))

		'''Make the background transparent.'''
		self.transparent = kwargs.get('transparent', False)

		'''Change the transparency of the overlay.'''
		self.alpha = kwargs.get('alpha', 1)

		'''Make the window draggable.'''
		self.draggable = kwargs.get('draggable', True)
		self._root.bind('<ButtonPress-1>', self._drag_start)
		self._root.bind('<ButtonRelease-1>', self._drag_stop)
		self._root.bind('<B1-Motion>', self._move)
		self._drag_stop(None)

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
			self.position = new_x, new_y

	@property
	def root(self):
		return self._root

	@property
	def size(self):
		return self._size

	@property
	def position(self):
		return self._position

	@position.setter
	def position(self, newPos):
		self._position = newPos
		self._root.geometry('+%s+%s'%self._position)

	@size.setter
	def size(self, newSize):
		self._size = newSize
		self._root.geometry('%sx%s'%self._size)

	@property
	def transparent(self):
		return self._root['bg'] == 'systemTransparent'

	@transparent.setter
	def transparent(self, newTransparent):
		bg = 'systemTransparent' if newTransparent else 'systemWindowBody'
		self._root.config(bg=bg)

	@property
	def alpha(self):
		return self._root.wm_attributes('-alpha')

	@alpha.setter
	def alpha(self, newAlpha):
		self._root.wm_attributes('-alpha', newAlpha)

	@staticmethod
	def after(milliseconds, func, *args):
		'''Runs the given function with the given args after launch.'''
		master.after(milliseconds, func, *args)

	@staticmethod
	def launch():
		'''Enter the mainloop for the collection of all overlays.'''
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

	@staticmethod
	def destroy_all():
		'''Destroy all overlays and end the mainloop.'''
		for overlay in overlays:
			overlay.destroy()

		master.destroy()
