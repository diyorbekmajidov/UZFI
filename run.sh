#!/bin/bash

ENV_PATH="./env"  # replace with your env path
SCRIPT_PATH="./manage.py"  # replace with your script path

if [[ "$OSTYPE" == "msys" ]]; then  # for Windows
    source $ENV_PATH/Scripts/activate
else  # for macOS/Linux
    source $ENV_PATH/bin/activate
fi

python $SCRIPT_PATH runserver
