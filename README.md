
## Requirements

This code uses [Pyglet](https://github.com/pyglet/pyglet) which is a cross-platform windowing library under Python 3.8+. 
Supported platforms are:

Windows 7 or later
Mac OS X 10.3 or later
Linux, with the following libraries (most recent distributions will have these in a default installation):

## Installation
pyglet is installable from PyPI:

    pip install --upgrade --user pyglet

Contributing
A good way to start contributing to a component of pyglet is by its documentation. When studying the code you are going to work with, also read the associated docs. If you don't understand the code with the help of the docs, it is a sign that the docs should be improved. If you wish to make large changes to any part of pyglet, it's always a good idea to reach out for feedback first. This can avoid wasted effort in cases where someone is already working on something similar, or if your idea can't be accepted for any reason.

A basic outline of how to a contribution is as follows:

Fork the official repository.
In your fork, checkout the branch you wish to contribute to (such as pyglet-1.5-maintenance).
Apply your changes to your fork.
Submit a pull request describing the changes you have made.
Alternatively you can create a patch and submit it to the issue tracker.
When making a pull request, check that you have addressed its respective documentation, both within the code docstrings and the programming guide (if applicable). It is very important to all of us that the documentation matches the latest code and vice-versa.

Consequently, an error in the documentation, either because it is hard to understand or because it doesn't match the code, is a bug that deserves to be reported on a ticket.

Building Docs
pip install -r doc/requirements.txt
python setup.py build_sphinx
Please check the README.md file in the doc directory for more details.

