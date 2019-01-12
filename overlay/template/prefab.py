'''An abstract template.'''

__all__ = [
	'TextWindow',
]

import abc
from overlay import Window

class WindowBase(Window):
	'''The basic window for user interactions.'''

	def __init__(self, focus: bool = True, **kwargs):
		'''Handler for basic binding commands.

		focus: boolean, whether to focus the window on startup.
		'''
		super().__init__(**kwargs)
		if focus:
			self.focus()

	def scroll_resize(self, event):
		'''Whether resizable with the mouse wheel.'''
		self.size = tuple(map(lambda x: x + event.delta, self.size))

class TextWindow(WindowBase):
	'''A basic text-based window.'''

	def __init__(self, content: str, **kwargs):
		'''Creates a window displaying some text.

		content: str, the text to be displayed (dynamic).
		'''
		super().__init__(**kwargs)
		self._content = content

	@abc.abstractmethod
	def _update_text(self, text):
		'''Update the text displayed in the overlay.'''
		return

	@property
	def content(self):
		return self._content

	@content.setter
	def content(self, text):
		self._content = text