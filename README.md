Requirements
pyglet runs under Python 3.8+. Being written in pure Python, it also works on other Python interpreters such as PyPy. Supported platforms are:

Windows 7 or later
Mac OS X 10.3 or later
Linux, with the following libraries (most recent distributions will have these in a default installation):
OpenGL and GLX
GDK 2.0+ or Pillow (required for loading images other than PNG and BMP)
OpenAL or Pulseaudio (required for playing audio)
As of pyglet 2.0, OpenGL 3.3+ is required.

To play a large variety of compressed audio and video files, pyglet can optionally take advantage of FFmpeg.

Installation
pyglet is installable from PyPI:

pip install --upgrade --user pyglet
Installation from source
If you're reading this README from a source distribution, you can install pyglet with:

pip install --upgrade --user .
# or
python setup.py install --user
You can also install the latest development version directly from Github:

pip install --upgrade --user https://github.com/pyglet/pyglet/archive/master.zip
For local development install pyglet in editable mode:

# with pip
pip install -e .
# with setup.py
python setup.py develop
There are no compilation steps during the installation; if you prefer, you can simply add this directory to your PYTHONPATH and use pyglet without installing it. You can also copy pyglet directly into your project folder.

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

Testing
pyglet makes use of pytest for its test suite.

pip install -r tests/requirements.txt --user
# Only run unittests
pytest tests/unit
Please check the testing section in the development guide for more information about running and writing tests.

Contact
pyglet is developed by many individual volunteers, and there is no central point of contact. If you have a question about developing with pyglet, or you wish to contribute, please join the mailing list, discord server, or subreddit.

For legal issues, please contact Alex Holkner.
