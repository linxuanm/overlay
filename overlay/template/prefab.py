'''An abstract template.'''

from overlay import Window

class WindowBase(Window):
	'''The basic window for user interactions.'''

	def __init__(self, focus: bool = True, **kwargs):
		'''Handler for basic binding commands.

		focus: boolean, whether to focus the window on startup.

		'''
		super().__init__()
		if focus:
			self.focus()

class TextWindow(WindowBase):
	'''A basic text-based window.'''

	def __init__(self, content: str, **kwargs):
		'''Creates a window displaying some text.

		content: str, the text to be displayed (dynamic).
		'''
		super().__init__(**kwargs)
		self._content = content

	@property
	def content(self):
		return self._content

	@content.setter
	def content(self, text):
		self._content = text