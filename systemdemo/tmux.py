

import os
import shutil

import pystemd
from systemdemo.constants import FILES, MODULE_DIR, BIN_DIR

SH = shutil.which("sh")

def start():

    os.execve(
        shutil.which("sh"),
        (
            shutil.which("sh"),
            "-c",
            f"""
exec sudo systemd-run --pty \
    --property BindReadOnlyPaths={BIN_DIR}/systemd-emo:/usr/local/bin/systemd-emo  \
    --property BindReadOnlyPaths={BIN_DIR}/stop-demo:/usr/local/bin/stop-demo  \
    --property BindReadOnlyPaths={FILES / 'tmux.conf'}:/root/.tmux.conf \
    --property BindReadOnlyPaths={FILES / 'bash_profile'}:/root/.bash_profile \
    -E OG_PATH={MODULE_DIR} \
    tmux
            """

        ),
        {
            **os.environ,
        }
    )

def stop():
    with pystemd.SDManager() as manager:
        unit_name = pystemd.dbuslib.path_decode(
            manager.Manager.GetUnitByPID(os.getpid()), 
            b'/org/freedesktop/systemd1/unit'
        )
    
    with pystemd.SDUnit(unit_name) as unit:
        unit.Unit.Stop(b"replace")