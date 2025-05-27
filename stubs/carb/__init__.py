class Float4(tuple):
    def __new__(cls, r=0.0, g=0.0, b=0.0, a=1.0):
        return tuple.__new__(cls, (r, g, b, a))


def log_warn(msg):
    print(f"[carb warn] {msg}")


def log_error(msg):
    print(f"[carb error] {msg}")


from . import settings, tokens, dictionary, events, input  # noqa: F401

__all__ = [
    "Float4",
    "log_warn",
    "log_error",
    "settings",
    "tokens",
    "dictionary",
    "events",
    "input",
]
