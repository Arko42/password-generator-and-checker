import re

def check_strength(password, common_file="common.txt"):
    score = 0
    feedback = []

    # Load common passwords
    try:
        with open(common_file, "r") as f:
            common_passwords = f.read().splitlines()
    except FileNotFoundError:
        common_passwords = []

    # Check if password is too common
    if password in common_passwords:
        return "Weak", ["❌ Password is too common."]

    # Length check
    if len(password) < 8:
        feedback.append("❌ Password is too short (min 8 chars).")
        score -= 10
    else:
        score += len(password) * 2
        feedback.append(f"✓ Good length ({len(password)} characters).")

    # Character diversity
    if re.search(r"[A-Z]", password):
        score += 5
        feedback.append("✓ Contains uppercase letters.")
    else:
        feedback.append("❌ Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 5
        feedback.append("✓ Contains lowercase letters.")
    else:
        feedback.append("❌ Add lowercase letters.")

    if re.search(r"[0-9]", password):
        score += 5
        feedback.append("✓ Contains digits.")
    else:
        feedback.append("❌ Add digits.")

    if re.search(r"[^a-zA-Z0-9]", password):
        score += 5
        feedback.append("✓ Contains special characters.")
    else:
        feedback.append("❌ Add special characters.")

    # Pattern checks
    if re.search(r"(123|abc|qwerty)", password.lower()):
        score -= 10
        feedback.append("❌ Contains predictable sequence.")

    if re.search(r"(.)\1{2,}", password):
        score -= 10
        feedback.append("❌ Contains repeated characters.")

    # Final rating
    if score < 20:
        rating = "Weak"
    elif score < 40:
        rating = "Moderate"
    elif score < 60:
        rating = "Strong"
    else:
        rating = "Very Strong"

    return rating, feedback
