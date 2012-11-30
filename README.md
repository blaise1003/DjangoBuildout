VASChances
==========

Django VAS buildout


1.0
===

This buildout makes a Django environment with src/vas.chances simple project


Installation
============

1. Create a virtualenv with python2.7::
	$ mkdir Shop4Win
	$ cd Shop4Win
	$ python2.7 ../virtualenv.py --distribute --no-site-packages .
2. Activate virtualenv::
	$ source bin/activate
3. Clone GIT repository from GitHub::
	$ git clone git@github.com:blaise1003/VASChances.git buildout
4. Bootstrap buildout::
	$ cd buidlout
	$ python bootsrap.py
5. Compile buildout::
	$ ./bin/buildout -Nvv
6. After compiling buildout, you have to create db from project models::
	$ ./bin/django syncdb


Start application
=================

To start Django application run command from buildout directory::
	$ ./bin/django runserver 0.0.0.0:10000


