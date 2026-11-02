import string

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Minimal 8 karakter")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Tambahkan huruf kecil")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Tambahkan huruf besar")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Tambahkan angka")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Tambahkan simbol")

    levels = {
        0: "Sangat Lemah",
        1: "Sangat Lemah",
        2: "Lemah",
        3: "Sedang",
        4: "Kuat",
        5: "Sangat Kuat"
    }

    result = f"[{levels[score]}] ({score}/5)"

    if feedback:
        result += "\nSaran:\n- " + "\n- ".join(feedback)

    return result
