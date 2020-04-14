$ python3 -m hello

>>> import importlib
>>> importlib.import_module('hello')
Hello World!
<module 'hello' from '/home/username/hello.py'>

>>> import hello  # First import
Hello World!
>>> import hello  # Second import, which does nothing
>>> import importlib
>>> importlib.reload(hello)
Hello World!
<module 'hello' from '/home/username/hello.py'>

>>> import hello  # First import
Hello World!
>>> import hello  # Second import, which does nothing
>>> import imp
>>> imp.reload(hello)
Hello World!
<module 'hello' from '/home/username/hello.py'>

Using runpy.run_module() and runpy.run_path()
	

>>> runpy.run_module(mod_name='hello')
Hello World!
{'__name__': 'hello',
    ...
'_': None}}

>>> exec(open('hello.py').read())
'Hello World!'

>>> execfile('hello.py')
Hello World!
