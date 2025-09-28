# 🦸 Family CyberHero Incident Response Playbook

A simple, fun project for families with kids (ages 6–12) to learn **incident response** and **protecting data** by pretending to run a mini business.

---

## 👩‍💻 PART 1 — Build the Repository (step-by-step)

### 1) Create your GitHub repo
1. Log in to https://github.com → click the **+** (top right) → **New repository**  
2. **Name:** `family-cyberhero-ir-playbook`  
3. **Description:** Fun, kid-friendly Incident Response Playbook where families role-play as small business owners protecting their data.  
4. Visibility: **Public**  
5. Check **Add a README file**  
6. **License:** MIT  
7. Click **Create repository**

### 2) Make folders (right on GitHub)
- Click **Add file → Create new file**
- Name it: `playbook/.gitkeep` → **Commit new file**
- Repeat for:
  - `scripts/.gitkeep`
  - `assets/.gitkeep`

You now have folders: `playbook`, `scripts`, `assets`.

### 3) Add the Family Playbook
- Open the `playbook` folder → **Add file → Create new file**  
- **Filename:** `incident_playbook.md`  
- Paste the content from **PART 2** below → **Commit new file**

### 4) Add Optional Extras (code)
We’ll add two simple scripts and one printable worksheet.

- In `scripts/` → **Add file → Create new file**  
  - **Filename:** `password_checker.py`  
  - Paste the code from **PART 3A** → **Commit new file**
- In `scripts/` → **Add file → Create new file**  
  - **Filename:** `risk_register.py`  
  - Paste the code from **PART 3B** → **Commit new file**
- In `assets/` → **Add file → Create new file**  
  - **Filename:** `worksheets.md`  
  - Paste the content from **PART 4** → **Commit new file**

---

## 🎭 PART 2 — Family Playbook (parents & kids use this)

**File:** `playbook/incident_playbook.md`

### 🎬 How to Play (15–20 minutes, paper + pencil)
You’ll run a pretend small business and stop cyber villains together.

#### Step 1: Name Your Business ✍️
Pick a business: Ice Cream Shop 🍦 · Pet Salon 🐾 · Space Travel 🚀 · Game Studio 🎮  
Write: *“We are the Galactic Donut Shop.”*  
Bonus: draw a logo!

#### Step 2: Your Crown Jewels 💎
Ask: “What must we protect?”  
Examples: recipes, customer list, tablet/laptop, designs.  
List 3–5 important **assets**.

#### Step 3: Meet the Villains 👾
- **Password Pirate** — steals weak passwords  
- **Phishy Fish** — sends fake links  
- **Virus Vulture** — sneaks into devices  
Draw lines from villains → the assets they’d attack.

#### Step 4: Build Defenses 🛡️
- Password Pirate → long, strong passwords (passphrases)  
- Phishy Fish → don’t click weird links; check sender  
- Virus Vulture → install updates & use antivirus  
Parents explain each in 1 sentence.

#### Step 5: Cyber Drill 🚨
Parent says: “Oh no, Virus Vulture attacked the shop tablet!”  
Kids do the 4 moves (say them out loud):
1) **Detect** — “We saw the problem.”  
2) **Respond** — “Shut it down/log out/report it.”  
3) **Recover** — “Turn back on safely/restore from backup.”  
4) **Lessons Learned** — “Keep updates on / new rule we’ll follow.”

Celebrate! You protected your business like CyberHeroes. 🦸

---

## 🧩 PART 3 — Optional Extras (code + how to run)

> These are 100% optional. The playbook works great without code.  
> If you want to try them, follow the **Run Instructions** below.

### 3A) `scripts/password_checker.py`
A tiny program that scores passwords and gives tips.

```python
#!/usr/bin/env python3
"""
Family Password Checker (Beginner-friendly)
- Scores password strength (0-100)
- Gives simple tips for improvement
- For learning ONLY (do NOT paste real passwords)
"""

import re

COMMON_WEAK = {
    "password", "123456", "qwerty", "letmein", "abc123", "iloveyou",
    "admin", "welcome", "dragon", "monkey", "football", "baseball"
}

def score_password(pw: str) -> (int, list):
    tips = []
    score = 0

    # Basic length points
    length = len(pw)
    if length >= 16:
        score += 40
    elif length >= 12:
        score += 30
    elif length >= 8:
        score += 20
    elif length > 0:
        score += 10
    else:
        tips.append("Password cannot be empty.")
        return 0, tips

    # Character variety
    if re.search(r"[a-z]", pw): score += 10
    else: tips.append("Add lowercase letters.")

    if re.search(r"[A-Z]", pw): score += 10
    else: tips.append("Add uppercase letters.")

    if re.search(r"\d", pw): score += 10
    else: tips.append("Add numbers.")

    if re.search(r"[^\w\s]", pw): score += 10
    else: tips.append("Add symbols (e.g., ! ? #).")

    # Repetition & sequences
    if re.search(r"(.)\1\1", pw):
        tips.append("Avoid repeating the same character 3+ times.")
        score -= 10

    # Very common/weak patterns
    lowered = pw.lower()
    if any(w in lowered for w in COMMON_WEAK):
        tips.append("Avoid common words (e.g., 'password', '123456').")
        score -= 15

    # Passphrase bonus
    if "-" in pw or " " in pw:
        # Encourage passphrases with separators
        score += 5

    # Clamp score
    score = max(0, min(score, 100))

    # High-level improvement if needed
    if score < 70 and "Use a longer passphrase (4+ words)." not in tips:
        tips.append("Use a longer passphrase (4+ words).")

    return score, tips

def main():
    print("Family Password Checker (examples only)")
    print("Type 'quit' to exit.\n")

    while True:
        pw = input("Try a password/passphrase: ").strip()
        if pw.lower() == "quit":
            print("Goodbye! Protect those crown jewels! 🛡️")
            break

        score, tips = score_password(pw)
        print(f"\nScore: {score}/100")
        if score >= 80:
            print("Verdict: Strong 👏")
        elif score >= 60:
            print("Verdict: Okay 👍 (can be stronger)")
        else:
            print("Verdict: Weak ⚠️")

        if tips:
            print("Tips:")
            for t in tips:
                print(f" - {t}")
        print("")

if __name__ == "__main__":
    main()

