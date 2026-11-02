import re

def format_mac(mac):
    clean = re.sub(r'[^0-9a-fA-F]', '', mac)

    if len(clean) != 12:
        return "[ERROR] MAC Address tidak valid!"

    if not re.fullmatch(r'[0-9a-fA-F]{12}', clean):
        return "[ERROR] Format MAC tidak valid!"

    formatted = ":".join(
        clean[i:i+2].upper()
        for i in range(0, 12, 2)
    )

    compact = clean.upper()

    return (
        "\n[+] MAC ADDRESS INFORMATION\n"
        "----------------------------\n"
        f"Formatted : {formatted}\n"
        f"Compact   : {compact}\n"
        f"Length    : {len(clean)} characters"
    )
