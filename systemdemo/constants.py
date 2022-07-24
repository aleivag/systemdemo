import sys
from pathlib import Path

MODULE_DIR = Path(__file__).absolute().resolve().parent
FILES = MODULE_DIR / "files"
BIN_DIR = Path(sys.executable).parent

DEBIAN_ROOT = None