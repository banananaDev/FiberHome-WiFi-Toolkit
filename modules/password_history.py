
import os
from datetime import datetime

HISTORY_DIR = "data"
HISTORY_FILE = os.path.join(HISTORY_DIR, "password_history.txt")

def save_password(password):
    os.makedirs(HISTORY_DIR, exist_ok=True)

    with open(HISTORY_FILE, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {password}\n")

    try:
        os.chmod(HISTORY_FILE, 0o600)
    except OSError:
        pass

    return True


def show_history():
    if not os.path.exists(HISTORY_FILE):
        return "[!] Belum ada riwayat password."

    with open(HISTORY_FILE, "r") as file:
        content = file.read()

    return content or "[!] Riwayat masih kosong."


def export_history():
    if not os.path.exists(HISTORY_FILE):
        return "[!] Tidak ada riwayat untuk diekspor."

    os.makedirs("data", exist_ok=True)

    export_file = "data/password_export.txt"

    with open(HISTORY_FILE, "r") as source:
        content = source.read()

    with open(export_file, "w") as output:
        output.write(content)

    try:
        os.chmod(export_file, 0o600)
    except OSError:
        pass

    return f"[+] Export berhasil: {export_file}"
