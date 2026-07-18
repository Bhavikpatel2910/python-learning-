import tkinter as tk
from tkinter import scrolledtext

from bot import get_response


class ChatbotUI:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Chatbot")
        self.root.geometry("640x720")
        self.root.minsize(520, 600)
        self.root.configure(bg="#111827")

        self.primary = "#0f172a"
        self.secondary = "#1f2937"
        self.accent = "#38bdf8"
        self.text = "#e5e7eb"
        self.muted = "#9ca3af"

        self._build_ui()
        self._add_bot_message("Hello. Type a message to begin.")

    def _build_ui(self) -> None:
        header = tk.Frame(self.root, bg=self.primary, padx=20, pady=16)
        header.pack(fill="x")

        title = tk.Label(
            header,
            text="Chatbot",
            bg=self.primary,
            fg=self.text,
            font=("Segoe UI", 20, "bold"),
        )
        title.pack(anchor="w")

        subtitle = tk.Label(
            header,
            text="Rule-based chatbot with a desktop UI",
            bg=self.primary,
            fg=self.muted,
            font=("Segoe UI", 10),
        )
        subtitle.pack(anchor="w", pady=(4, 0))

        body = tk.Frame(self.root, bg=self.primary, padx=16, pady=12)
        body.pack(fill="both", expand=True)

        self.chat_box = scrolledtext.ScrolledText(
            body,
            wrap=tk.WORD,
            bg=self.secondary,
            fg=self.text,
            insertbackground=self.text,
            selectbackground=self.accent,
            relief="flat",
            font=("Segoe UI", 11),
            padx=12,
            pady=12,
        )
        self.chat_box.pack(fill="both", expand=True)
        self.chat_box.configure(state="disabled")

        footer = tk.Frame(self.root, bg=self.primary, padx=16, pady=16)
        footer.pack(fill="x")

        self.entry = tk.Entry(
            footer,
            bg="#0b1220",
            fg=self.text,
            insertbackground=self.text,
            relief="flat",
            font=("Segoe UI", 11),
        )
        self.entry.pack(side="left", fill="x", expand=True, ipady=10, padx=(0, 10))
        self.entry.bind("<Return>", self.send_message)

        send_button = tk.Button(
            footer,
            text="Send",
            command=self.send_message,
            bg=self.accent,
            fg="#0f172a",
            activebackground="#7dd3fc",
            activeforeground="#0f172a",
            relief="flat",
            font=("Segoe UI", 11, "bold"),
            padx=18,
            pady=10,
        )
        send_button.pack(side="right")

        self.entry.focus_set()

    def _write_message(self, speaker: str, message: str) -> None:
        self.chat_box.configure(state="normal")
        self.chat_box.insert(tk.END, f"{speaker}: {message}\n\n")
        self.chat_box.see(tk.END)
        self.chat_box.configure(state="disabled")

    def _add_bot_message(self, message: str) -> None:
        self._write_message("Bot", message)

    def _add_user_message(self, message: str) -> None:
        self._write_message("You", message)

    def send_message(self, event=None) -> None:
        user_input = self.entry.get().strip()
        if not user_input:
            return

        self._add_user_message(user_input)
        response = get_response(user_input)
        self._add_bot_message(response)

        self.entry.delete(0, tk.END)

        if user_input.lower() in {"bye", "goodbye", "exit", "quit"}:
            self.entry.configure(state="disabled")


def main() -> None:
    root = tk.Tk()
    ChatbotUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
