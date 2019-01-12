'''An abstract template.'''

from overlay import Window

class WindowBase(Window):
	'''The basic window for user interactions.'''

	def __init__(self, **kwargs):
		'''Subclass of overlay.Window. All keyword args are pre-defined, but can be overriden. The exception is the transparent keyword, which is always set to True.

		content: str, the content to be displayed.
		'''
		size = kwargs.get('size', (500, 250))
		position = kwargs.get('position', (0, 0))
		alpha = kwargs.get('alpha', 1)
		draggable = kwargs.get('draggable', True)

		'''Just realized how spaghetti this part is.'''
		super().__init__(
			size=size,
			position=position,
			transparent=0,
			alpha=alpha,
			draggable=draggable
		)
		self.center()
		self.focus()

class TextWindow(WindowBase):
	'''A basic text-based window.'''

	def __init__(self, content: str, **kwargs):
		'''Creates a window displaying some text.

		content: str, the text to be displayed.
		'''
		super().__init__(**kwargs)
		self._content = content

	@property
	def content(self):
		return self._content

	@content.setter
	def content(self, text):
		self._content = text