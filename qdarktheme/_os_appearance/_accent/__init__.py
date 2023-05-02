import platform


def _check_macos_supported_version():
    sys_ver = platform.mac_ver()[0]  # typically 10.14.2 or 12.3
    major = int(sys_ver.split(".")[0])
    if major < 10:
        return False
    if major >= 11:
        return True
    minor = int(sys_ver.split(".")[1])
    return minor >= 14

def _check_windows_supported_version():
    try:
        sys_ver = platform.win32_ver()[1].split(".")[-1]
        return(int(sys_ver) >= 22000)  # windows 11 only
    except:
        return False

def _dummy_accent_detector() -> None:
    return None


def _select_accent_detector():
    if platform.system() == "Darwin":
        if _check_macos_supported_version():
            from qdarktheme._os_appearance._accent._mac_detect import get_mac_accent
            return get_mac_accent
        return _dummy_accent_detector
    if platform.system() == "Windows":
        if _check_windows_supported_version():
            from qdarktheme._os_appearance._accent._win_detect import get_windows_accent
            return get_windows_accent
        return _dummy_accent_detector
    return _dummy_accent_detector


accent = _select_accent_detector()
