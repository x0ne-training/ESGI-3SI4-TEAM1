#!/usr/bin/env python3
"""
quiz.py - Mini quiz console (QCM) en Python (réponses sous forme de texte)
Usage: python quiz.py
"""

import json
import random
import os
import sys

QUESTIONS_FILE = "questions.json"

def load_questions(path):
    """Charge les questions depuis le fichier JSON."""
    if not os.path.exists(path):
        print(f"❌ Fichier de questions introuvable : {path}")
        return []
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    valid = []
    for i, q in enumerate(data):
        if (
            "question" in q
            and "choices" in q
            and "answer" in q
            and isinstance(q["choices"], list)
            and q["answer"] in q["choices"]
        ):
            valid.append(q)
        else:
            print(f"⚠️  Question {i+1} ignorée (format invalide).")
    return valid


def ask_question(q, qnum, total):
    """Affiche une question et récupère la réponse de l'utilisateur."""
    print(f"\nQuestion {qnum}/{total} : {q['question']}")
    choices = q["choices"]
    random.shuffle(choices)

    for i, choice in enumerate(choices, start=1):
        print(f"  {i}. {choice}")

    while True:
        ans = input(f"👉 Ton choix (1-{len(choices)}, q=quitter) : ").strip().lower()
        if ans == "q":
            return None
        if not ans.isdigit():
            print("⚠️  Entre un numéro ou 'q' pour quitter.")
            continue
        n = int(ans) - 1
        if 0 <= n < len(choices):
            return choices[n] == q["answer"]
        else:
            print("⚠️  Numéro hors plage.")


def main():
    """Lance le quiz."""
    questions = load_questions(QUESTIONS_FILE)
    if not questions:
        print("❌ Aucune question valide trouvée. Vérifie ton fichier JSON.")
        sys.exit(1)

    random.shuffle(questions)
    total = len(questions)
    score = 0

    print("======================================")
    print("        🎮  Mini Quiz Python")
    print("======================================")

    for i, q in enumerate(questions, start=1):
        result = ask_question(q, i, total)
        if result is None:
            print("\n👋 Tu as quitté le quiz.")
            break
        if result:
            print("✅ Bonne réponse !")
            score += 1
        else:
            print(f"❌ Mauvaise réponse. La bonne était : {q['answer']}")

    print("\n========== Résultat ==========")
    print(f"Score final : {score}/{total}")
    pct = (score / total * 100)
    print(f"Pourcentage : {pct:.1f}%")

    if pct == 100:
        print("🔥 Parfait ! Tu es imbattable !")
    elif pct >= 70:
        print("👍 Bien joué, tu maîtrises bien !")
    elif pct >= 40:
        print("🙂 Pas mal, continue à t’entraîner.")
    else:
        print("💡 Tu peux faire mieux, recommence !")


if __name__ == "__main__":
    main()
