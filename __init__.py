"""
Minimal stub of NVIDIA Omniverse 'carb' package
for offline unit-testing inside Codex.
Only implements what our code & tests need.
"""
from types import ModuleType

# Simple logger that mimics carb.log_* API surface
class _Logger:
    def info(self, msg):  print(f"[carb] {msg}")
    def warn(self, msg):  print(f"[carb:WARN] {msg}")
    def error(self, msg): print(f"[carb:ERR] {msg}")

log = _Logger()

# If your code does `from carb import settings`,
# create sub-modules dynamically so the import works:
settings = ModuleType("carb.settings")
settings.get_settings = lambda: {}
