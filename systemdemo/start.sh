#/bin/bash

VIRTUAL_ENV="`pwd`/venv"

exec sudo systemd-run --pty \
                 --property BindReadOnlyPaths=${VIRTUAL_ENV}/bin/systemd-emo:/usr/local/bin/systemd-emo  \
                 --property BindReadOnlyPaths=`pwd`/files/tmux.conf:/root/.tmux.conf \
                 --property BindReadOnlyPaths=`pwd`/files/bash_profile:/root/.bash_profile \
                 -E OG_PATH=`pwd` \
                 tmux