"""This script is inspired by darkdetect(https://github.com/albertosottile/darkdetect)."""
from __future__ import annotations

import ctypes
from ctypes import c_void_p

try:
    # macOS Big Sur+ use "a built-in dynamic linker cache of all system-provided libraries"
    _objc = ctypes.cdll.LoadLibrary("libobjc.dylib")
except OSError:
    import ctypes.util

    # revert to full path for older OS versions and hardened programs
    _objc = ctypes.cdll.LoadLibrary(ctypes.util.find_library("objc"))  # type: ignore

_objc.objc_getClass.restype = c_void_p
_objc.sel_registerName.restype = c_void_p

msg_prototype = ctypes.CFUNCTYPE(c_void_p, c_void_p, c_void_p, c_void_p)
msg = msg_prototype(("objc_msgSend", _objc), ((1, "", None), (1, "", None), (1, "", None)))

_MAC_ACCENT_COLORS = {
    None: None,
    "-1": "graphite",
    "0": "red",
    "1": "orange",
    "2": "yellow",
    "3": "green",
    "4": "blue",
    "5": "purple",
    "6": "pink",
}


def _utf8(s: str | bytes):
    return s.encode("utf8") if not isinstance(s, bytes) else s


def _n(name: str):
    return _objc.sel_registerName(_utf8(name))


def _c(classname: str):
    return _objc.objc_getClass(_utf8(classname))


def get_mac_accent() -> str | None:
    """Get system accent color on Mac."""
    pool = msg(_c("NSAutoreleasePool"), _n("alloc"))
    pool = msg(pool, _n("init"))

    std_user_def = msg(_c("NSUserDefaults"), _n("standardUserDefaults"))

    key = msg(_c("NSString"), _n("stringWithUTF8String:"), _utf8("AppleAccentColor"))
    accent_id = msg(std_user_def, _n("stringForKey:"), c_void_p(key))
    accent_id = msg(accent_id, _n("UTF8String"))

    accent_id = None if accent_id is None else ctypes.string_at(accent_id).decode()

    msg(pool, _n("release"))
    return _MAC_ACCENT_COLORS.get(accent_id)
