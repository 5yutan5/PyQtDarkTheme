def get_windows_accent():
    import winreg
    # Open the registry key for the current user's personalization settings
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Accent")
    # Read the value of AccentColorMenu
    value = winreg.QueryValueEx(key, "AccentColorMenu")[0]
    # Convert the value to hexadecimal string
    hex_value = hex(value)[2:].zfill(8)
    # Extract the RGB components from the string
    r = int(hex_value[6:8], 16)
    g = int(hex_value[4:6], 16)
    b = int(hex_value[2:4], 16)
    # Close the registry key
    winreg.CloseKey(key)
    # Return the HEX tuple
    return '#%02x%02x%02x' % (r, g, b)




