Syncle - single file synchronization tool
=========================================

Syncle allows you to synchronize single files across your file system and store them into the one directory.
This thing allows to extend standard behaviour of many cloud file synchronization utilites (such as DropBox, SpiderOak, SugarSync and others).

Installation
------------

> Is recommended to install syncle with [pip](http://www.pip-installer.org) and [virtualenv](http://www.virtualenv.org/), but you can also use any other [method](http://wiki.python.org/moin/CheeseShopTutorial) of Python package installing.

### From PyPI

    pip install syncle

### From Git sources

    git clone git://github.com/rdolgushin/syncle.git
    pip install -e syncle/

Usage
-----

You can run syncle from your shell with `syncle` command.

On first run syncle will create `~/.synclerc.yml` (if it does not exist). It has YAML syntax and following structure:

    files:
      - ~/.vimrc
      - ~/.config/openbox/rc.xml
    storage: ~/syncle
    delay: 2

where:

* `files` - list of files for synchronization
* `storage` - local directory for storing this files (usual cloud file synchronization utility folder)
* `delay` - refreshing interval in seconds (by default - 3)

