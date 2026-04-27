import math
import re


def estimate_entropy(password: str, pool_size: int) -> float:
    if not password or pool_size <= 0:
        return 0.0
    return len(password) * math.log2(pool_size)


def character_pool_size(password: str) -> int:
    pool = 0
    if re.search(r"[a-z]", password):
        pool += 26
    if re.search(r"[A-Z]", password):
        pool += 26
    if re.search(r"[0-9]", password):
        pool += 10
    if re.search(r"[^a-zA-Z0-9]", password):
        pool += 32
    return pool


def strength_score(password: str):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
        feedback.append("Use at least 12 characters for stronger passwords.")
    else:
        feedback.append("Password is too short; use at least 8 characters.")

    if re.search(r"[a-z]", password):
        score += 10
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 15
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[0-9]", password):
        score += 15
    else:
        feedback.append("Add digits.")

    if re.search(r"[^a-zA-Z0-9]", password):
        score += 20
    else:
        feedback.append("Add symbols (e.g. !@#$).")

    pool_size = character_pool_size(password)
    entropy = estimate_entropy(password, pool_size)

    if entropy >= 60:
        score += 15
    elif entropy >= 45:
        score += 8
    else:
        feedback.append("Increase entropy using more character variety and length.")

    score = min(score, 100)

    if score >= 80:
        rating = "Strong"
    elif score >= 60:
        rating = "Medium"
    else:
        rating = "Weak"

    return score, rating, entropy, feedback


def main() -> None:
    print("Password Strength Checker")
    password = input("Enter password to evaluate: ").strip()

    score, rating, entropy, feedback = strength_score(password)
    print(f"\nScore: {score}/100")
    print(f"Strength: {rating}")
    print(f"Estimated entropy: {entropy:.2f} bits")

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print(f"- {item}")


if __name__ == "__main__":
    main()
