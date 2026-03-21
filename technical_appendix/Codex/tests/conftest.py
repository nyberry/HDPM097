from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
