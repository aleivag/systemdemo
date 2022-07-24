#!/usr/bin/env python3 

import os, sys
from pathlib import Path

SOCAL_DIR = Path(__file__).absolute().parent.parent
PYTHON_BIN = SOCAL_DIR / "venv/bin/python3"
if Path(sys.executable) != PYTHON_BIN:
    os.execve(PYTHON_BIN, (PYTHON_BIN, Path(__file__).absolute()), os.environ)
    print("not this line")


from pystemd.systemd1.manager import Manager
from pystemd.systemd1.unit import Unit

with Manager() as manager:
    unit = Path(manager.GetUnitByPID(os.getpid()).decode()).name.removesuffix("_2eservice") + ".service"
    print(unit)

with Unit(unit) as u:
    print(u.GetProcesses())
    # print(dir(u.Service))

