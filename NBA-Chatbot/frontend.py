import threading
import tkinter as tk
from tkinter import scrolledtext

from chatbot import answer_question


def _add_basketball_line(output, text):
    for line in str(text).splitlines() or [""]:
        output.insert(tk.END, f"🏀 {line}\n")
    output.see(tk.END)


def launch_gui():
    window = tk.Tk()
    window.title("NBA Terminal")
    window.geometry("760x520")
    window.configure(bg="black")

    output = scrolledtext.ScrolledText(
        window,
        bg="black",
        fg="white",
        insertbackground="white",
        font=("Menlo", 13),
        wrap=tk.WORD,
        relief=tk.FLAT,
        padx=16,
        pady=16,
    )
    output.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)

    output.insert(tk.END, "🏀 NBA terminal ready. Ask a question below.\n")
    output.insert(tk.END, "🏀 ")
    output.mark_set(tk.INSERT, tk.END)
    input_start = output.index(tk.INSERT)
    busy = False

    def ask(event=None):
        nonlocal busy, input_start
        if busy:
            return "break"

        text = output.get(input_start, "end-1c").strip()
        if not text:
            return "break"

        output.insert(tk.END, "\n")
        _add_basketball_line(output, "NBA Desk: loading latest data...")
        output.configure(state=tk.DISABLED)
        busy = True
        output.see(tk.END)

        def fetch_answer():
            try:
                response = answer_question(text)
            except Exception as error:
                response = f"Unable to get an answer: {error}"
            window.after(0, show_answer, response)

        threading.Thread(target=fetch_answer, daemon=True).start()
        return "break"

    def show_answer(response):
        nonlocal busy, input_start
        output.configure(state=tk.NORMAL)
        _add_basketball_line(output, f"NBA Desk: {response}")
        output.insert(tk.END, "🏀 ")
        output.mark_set(tk.INSERT, tk.END)
        input_start = output.index(tk.INSERT)
        output.see(tk.END)
        busy = False
        output.focus_set()

    def prevent_history_edit(event=None):
        output.focus_set()
        if output.compare(tk.INSERT, "<", input_start):
            output.mark_set(tk.INSERT, tk.END)
        return "break"

    def prevent_prompt_delete(event=None):
        if output.compare(tk.INSERT, "<=", input_start):
            return "break"

    output.bind("<Return>", ask)
    output.bind("<Button-1>", prevent_history_edit)
    output.bind("<BackSpace>", prevent_prompt_delete)
    output.focus_set()
    window.mainloop()


if __name__ == "__main__":
    launch_gui()
