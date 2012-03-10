#!/bin/bash

VIRTUAL_ENV=ve
VIRTUAL_ENV_BINARY=virtualenv.py

[ -e $VIRTUAL_ENV_BINARY ] || wget https://raw.github.com/pypa/virtualenv/master/virtualenv.py -O $VIRTUAL_ENV_BINARY
[ -d $VIRTUAL_ENV ] || python $VIRTUAL_ENV_BINARY --no-site-packages $VIRTUAL_ENV

source $VIRTUAL_ENV/bin/activate
pip install -r requirements.txt
