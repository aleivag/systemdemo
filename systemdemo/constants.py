import sys
from pathlib import Path

MODULE_DIR = Path(__file__).absolute().resolve().parent
FILES = MODULE_DIR / "files"
BIN_DIR = Path(sys.executable).parent
VENV_ROOT = BIN_DIR.parent

DEBIAN_ROOT = VENV_ROOT / "debian-root"