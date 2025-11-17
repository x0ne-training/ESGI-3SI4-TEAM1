import json
import random
import tkinter as tk
from tkinter import messagebox

# Charger les questions depuis le fichier JSON
def load_questions(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    random.shuffle(data)
    return data

# Classe principale du quiz
class QuizApp:
    def __init__(self, root, questions):
        self.root = root
        self.root.title("🎮 Quiz Python")
        self.root.geometry("600x400")
        self.root.config(bg="#282c34")

        self.questions = questions
        self.q_index = 0
        self.score = 0
        self.answer_var = tk.StringVar()

        # Titre
        self.title_label = tk.Label(
            root, text="Mini Quiz de Culture Générale",
            font=("Arial", 18, "bold"), fg="white", bg="#282c34"
        )
        self.title_label.pack(pady=20)

        # Question
        self.question_label = tk.Label(
            root, text="", font=("Arial", 14),
            wraplength=500, justify="center",
            fg="white", bg="#282c34"
        )
        self.question_label.pack(pady=10)

        # Choix (boutons radio)
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(
                root, text="", variable=self.answer_var, value="",
                font=("Arial", 12), bg="#282c34", fg="white",
                selectcolor="#444"
            )
            rb.pack(anchor="w", padx=100)
            self.radio_buttons.append(rb)

        # Bouton "Valider"
        self.submit_button = tk.Button(
            root, text="Valider", command=self.check_answer,
            font=("Arial", 12, "bold"), bg="#61afef", fg="black", width=10
        )
        self.submit_button.pack(pady=20)

        # Démarrer le quiz
        self.load_question()

    def load_question(self):
        """Charge la question suivante"""
        if self.q_index < len(self.questions):
            q = self.questions[self.q_index]
            self.answer_var.set(None)
            self.question_label.config(text=f"Q{self.q_index + 1}. {q['question']}")
            choices = q["choices"]
            random.shuffle(choices)
            for i, choice in enumerate(choices):
                self.radio_buttons[i].config(text=choice, value=choice)
            for j in range(len(choices), len(self.radio_buttons)):
                self.radio_buttons[j].pack_forget()
        else:
            self.show_result()

    def check_answer(self):
        """Vérifie la réponse choisie"""
        selected = self.answer_var.get()
        if not selected:
            messagebox.showwarning("Attention", "Tu dois choisir une réponse !")
            return

        correct = self.questions[self.q_index]["answer"]
        if selected == correct:
            self.score += 1
            messagebox.showinfo("Bonne réponse ✅","Bravo ! C’est la bonne réponse 🎉")
        else:
            messagebox.showerror("Mauvaise réponse ❌", f"La bonne réponse était : {correct}")

        self.q_index += 1
        self.load_question()

    def show_result(self):
        """Affiche le score final"""
        percent = (self.score / len(self.questions)) * 100
        message = f"Score final : {self.score}/{len(self.questions)}\n({percent:.1f}%)"
        if percent == 100:
            message += "\n🔥 Parfait ! Tu es imbattable !"
        elif percent >= 70:
            message += "\n👍 Très bien joué !"
        elif percent >= 40:
            message += "\n🙂 Pas mal, continue à t’entraîner."
        else:
            message += "\n💡 Tu peux faire mieux !"
        messagebox.showinfo("Résultat final", message)
        self.root.destroy()

# --- Programme principal ---
if __name__ == "__main__":
    questions = load_questions("questions.json")
    root = tk.Tk()
    app = QuizApp(root, questions)
    root.mainloop()
