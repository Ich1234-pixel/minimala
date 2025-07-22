import tkinter as tk
from tkinter import simpledialog, messagebox
import datetime, webbrowser, random

root = tk.Tk()
root.title("Minimalia v1.0 ein Raum der Ruhe")
root.geometry("400x600")

# Affirmationen
def open_affirmations():
    win = tk.Toplevel(root)
    win.title("🕊️ Affirmation")
    affirmations = [
        "Du bist genug.",
        "Es darf leicht sein.",
        "Du bist sicher in diesem Moment.",
        "Alles, was du fühlst, darf da sein.",
        "Du brauchst gerade nichts zu leisten.",
        "Du darfst einfach nur atmen.",
        "Du bist nicht allein.",
        "Du bist wertvoll – genau jetzt.",
    ]
    chosen = random.choice(affirmations)
    tk.Label(win, text=chosen, font=("Helvetica", 16), fg="#445").pack(pady=30)

# Tagebuch
def open_diary():
    win = tk.Toplevel(root)
    win.title("📖 Erlebnis-Tagebuch")
    text = tk.Text(win, width=60, height=20)
    text.pack(padx=10, pady=10)
    def save():
        content = text.get("1.0", tk.END).strip()
        if content:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            with open("erlebnisse.txt", "a") as f:
                f.write(f"\n---\n{timestamp}\n{content}\n")
            messagebox.showinfo("Gespeichert", "Dein Eintrag wurde gespeichert.")
            win.destroy()
    tk.Label(win, text="Du kannst alles schreiben. Es wird sicher gespeichert.", fg="gray").pack()
    tk.Button(win, text="Speichern & Schließen", command=save).pack(pady=5)

# Gesprächsraum
def open_chatroom():
    win = tk.Toplevel(root)
    win.title("💬 Gesprächsraum")
    history = tk.Text(win, width=60, height=15, state="disabled")
    history.pack(padx=10, pady=5)
    entry = tk.Entry(win, width=60)
    entry.pack(padx=10)
    def respond():
        msg = entry.get().strip()
        if msg:
            history.config(state="normal")
            history.insert(tk.END, f"Du: {msg}\n")
            reply = "Minimalia: Ich bin bei dir. Du darfst dich so fühlen.\n"
            history.insert(tk.END, reply)
            history.config(state="disabled")
            entry.delete(0, tk.END)
    tk.Button(win, text="Senden", command=respond).pack(pady=5)

# Atemhilfe
def open_breathing():
    win = tk.Toplevel(root)
    win.title("🌬️ Atemhilfe – 4-7-8 Methode")
    steps = ["🫁 Einatmen: 4 Sekunden", "⏳ Luft anhalten: 7 Sekunden", "🌬️ Ausatmen: 8 Sekunden"]
    index = tk.IntVar(value=0)
    label = tk.Label(win, text=steps[0], font=("Helvetica", 16))
    label.pack(pady=30)
    def next_step():
        i = index.get() + 1
        if i < len(steps):
            label.config(text=steps[i])
            index.set(i)
        else:
            label.config(text="✅ Übung beendet. Du kannst wieder von vorne beginnen.")
            index.set(0)
    tk.Button(win, text="⏭ Nächster Schritt", command=next_step).pack()

# Musikstream
def open_music():
    win = tk.Toplevel(root)
    win.title("🎵 Sanfte Musik")
    tk.Label(win, text="Wähle eine Quelle für ruhige Musik:", font=("Helvetica", 12)).pack(pady=10)
    tk.Button(win, text="YouTube: Klavier + Regen", command=lambda: webbrowser.open("https://www.youtube.com/watch?v=l1sKrQ5e0sY")).pack(pady=5)
    tk.Button(win, text="ZenRadio", command=lambda: webbrowser.open("https://www.zenradio.com/")).pack(pady=5)
    tk.Button(win, text="CalmRadio", command=lambda: webbrowser.open("https://calmradio.com/")).pack(pady=5)

# Zen-Modus
def open_zen_mode():
    win = tk.Toplevel(root)
    win.title("🧘 Zen-Modus")
    win.geometry("400x200")
    win.configure(bg="black")
    tk.Label(win, text="🌌 Du darfst einfach nur atmen.", font=("Helvetica", 14), fg="lightblue", bg="black").pack(expand=True)

# To-Do Liste
def open_todo():
    win = tk.Toplevel(root)
    win.title("📋 To-Do Liste")
    listbox = tk.Listbox(win, width=50, height=10)
    listbox.pack(padx=10, pady=10)
    def add_task():
        task = simpledialog.askstring("Neue Aufgabe", "Was willst du tun?")
        if task:
            listbox.insert(tk.END, task)
    def save():
        with open("todo.txt", "w") as f:
            for item in listbox.get(0, tk.END):
                f.write("- " + item + "\n")
        messagebox.showinfo("Gespeichert", "To-Do Liste gespeichert.")
        win.destroy()
    tk.Button(win, text="Aufgabe hinzufügen", command=add_task).pack()
    tk.Button(win, text="Speichern & Schließen", command=save).pack(pady=5)

# Launcher-Buttons
tk.Label(root, text="🌙 Willkommen bei Minimalia", font=("Helvetica", 16)).pack(pady=10)
tk.Button(root, text="📖 Erlebnis-Tagebuch", command=open_diary).pack(fill="x", padx=40, pady=5)
tk.Button(root, text="💬 Gesprächsraum", command=open_chatroom).pack(fill="x", padx=40, pady=5)
tk.Button(root, text="🌬️ Atemhilfe", command=open_breathing).pack(fill="x", padx=40, pady=5)
tk.Button(root, text="🎵 Sanfte Musik", command=open_music).pack(fill="x", padx=40, pady=5)
tk.Button(root, text="🕊️ Affirmation", command=open_affirmations).pack(fill="x", padx=40, pady=5)
tk.Button(root, text="🧘 Zen-Modus", command=open_zen_mode).pack(fill="x", padx=40, pady=5)
tk.Button(root, text="📋 To-Do Liste", command=open_todo).pack(fill="x", padx=40, pady=5)
tk.Button(root, text="❌ Beenden", command=root.quit).pack(fill="x", padx=40, pady=20)

root.mainloop()
