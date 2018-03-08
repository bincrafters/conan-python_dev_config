#!/bin/bash

set -e
set -x

if [[ "$(uname -s)" == 'Darwin' ]]; then
    if which pyenv > /dev/null; then
        eval "$(pyenv init -)"
    fi
    pyenv activate conan
    find $HOME/.pyenv/versions -name "*.a"
    find $HOME/.pyenv/versions -name "*.*lib"
fi

echo '================================================================================'
python -c 'import pprint; import sysconfig; pprint.pprint([sysconfig.get_config_vars(),sysconfig.get_paths()]);'
echo '================================================================================'

python build.py