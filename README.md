# Overlay
A package that creates and manipulates screen overlays based on tkinter.

## Platforms
- Mac OS
- Linux (not tested)
- Windows (not tested)

## Installation
```sh
pip install overlay
```

## Usage
A basic overlay is created as such:
```python
from overlay import Window

win = Window()
Window.launch()
```

The constructor of the _Window_ class takes the following (optional) parameters:
- __size__: _tuple_, the dimension (width, height) of the overlay window.
- __position__: _tuple_, the position of the overlay (on screen).
- __transparent__: _bool_, whether to set the overlay background transparent.
- __alpha__: _float [0, 1]_, the alpha (transparency) of the overlay.
- __draggable__: _bool_, whether the window can be dragged

Note that the parameters mentioned above can be edited any time as attributes of an instance of _Window_.

In order to edit the content of a overlay, one needs to obtain the root of the overlay, upon which all else shall be build.
```python
import tkinter as tk
from overlay import Window

win = Window()
label = tk.Label(win.root, text="Window_0")
label.pack()
Window.launch()
```

Multiple overlays can be created just as easily:
```python
import tkinter as tk
from overlay import Window

win_0 = Window()
label_0 = tk.Label(win_0.root, text="Window_0")
label_0.pack()
win_1 = Window()
label_1 = tk.Label(win_1.root, text="Window_1")
label_1.pack()
Window.launch()
```

The following program covers a brief explaination on other methods of the _Window_ class.
```python
import tkinter as tk
from time import sleep
from overlay import Window

def other_stuff(text):
	print(text)
	sleep(2)
	win_0.hide() # Hides the overlay.
	sleep(1)
	win_0.show() # Shows the overlay.
	sleep(1)
	Window.hide_all() # Hides all overlays.
	sleep(1)
	Window.show_all() # Shows all overlays.
	sleep(1)
	win_0.destroy() # Kills the overlay.
	sleep(1)
	Window.destroy_all() # Kills all overlays and ends the mainloop.


'''Creates two windows.'''
win_0 = Window()
label_0 = tk.Label(win_0.root, text="Window_0")
label_0.pack()
win_1 = Window()
label_1 = tk.Label(win_1.root, text="Window_1")
label_1.pack()

Window.after(2000, other_stuff, 'Hello World') # Identical to the after method of tkinter.Tk.

Window.launch()
```