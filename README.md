Syncle - single file synchronization tool
=========================================

Syncle allows you to synchronize single files across your file system and store them into the one directory.
This thing allows to extend standard behaviour of many cloud file synchronization utilites (such as DropBox, SpiderOak, SugarSync and others).

Installation
------------

### From PyPI

Something like

    pip install syncle

### From git sources

Something like

    git clone git://github.com/rdolgushin/syncle.git
    pip install -e syncle/

or

    git clone git://github.com/rdolgushin/syncle.git
    cd syncle/
    python setup.py install

Usage
-----

You can run syncle from your shell with `syncle` command.

On first run syncle will create `~/.synclerc.yml` (if it does not exist). It has YAML syntax and following structure:

    files:
      - ~/.vimrc_test
      - ~/.config_test
    storage: ~/tmp/test
    delay: 2
