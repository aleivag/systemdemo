#!/usr/bin/env python3 

import sys
import os
from pathlib import Path
import venv
import subprocess
from setuptools import setup
import time

PYSTEMD_GIT = "https://github.com/facebookincubator/pystemd"

THIS_DIR = Path(__file__).absolute().resolve().parent
MODULE_SRC = THIS_DIR / "systemdemo"
VERSION = "0.1.1" + os.getenv("SYSTEMDEMO_PATCH_VERSION", f".{int(time.time())}")


setup(
    name="systemdemo",
    version=VERSION,
    packages=["systemdemo"],
    author="Alvaro Leiva",
    author_email="aleivag@fb.com",
    url="",
    classifiers=[
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
    ],
    keywords=["systemdemo"],
    description="Testing files for systemd and pystemd",
    package_data={
        "systemdemo": [
          "mon.sh",
          *[
            p.relative_to(MODULE_SRC).as_posix() 
            for p in MODULE_SRC.glob("files/*")
          ]
        ],
    },
    install_requires=[
      "cython", 
      "pygments", 
      "ipython",
      "pystemd",
    ],
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    entry_points={
        'console_scripts': [
            'systemd-emo = systemdemo.demo:demo',
            'start-demo = systemdemo.tmux:start',
            'stop-demo = systemdemo.tmux:stop',
        ]
    },
    license="LGPL-2.1+",
)