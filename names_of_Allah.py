#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
# SPDX-License-Identifier: GPL-3.0-or-later
"""Tkinter image viewer for the 99 Names of Allah educational slides."""
from pathlib import Path
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

ROOT = Path(__file__).resolve().parent
IMAGES = ROOT / "Pictures"
MIN_SLIDE = 1
MAX_SLIDE = 100  # Historical collection includes a closing slide.


def slide_path(index: int) -> Path:
    if not MIN_SLIDE <= index <= MAX_SLIDE:
        raise ValueError("Slide index must be between 1 and 100")
    return IMAGES / f"{index}.png"


class NamesWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("The 99 Names of Allah")
        self.geometry("840x650")
        self.minsize(580, 460)
        self.index = MIN_SLIDE
        self.photo = None
        self._build()
        self.show_slide()
        self.bind("<Left>", lambda _: self.previous())
        self.bind("<Right>", lambda _: self.next())
        self.bind("<Home>", lambda _: self.go_to(MIN_SLIDE))
        self.bind("<End>", lambda _: self.go_to(MAX_SLIDE))

    def _build(self):
        frame = ttk.Frame(self, padding=18)
        frame.pack(fill="both", expand=True)
        ttk.Label(frame, text="The 99 Names of Allah",
                  font=("Sans", 21, "bold")).pack(pady=(0, 8))
        self.caption = ttk.Label(frame, text="", font=("Sans", 12))
        self.caption.pack()
        self.image_label = ttk.Label(frame, anchor="center")
        self.image_label.pack(fill="both", expand=True, pady=12)
        controls = ttk.Frame(frame)
        controls.pack()
        self.back = ttk.Button(controls, text="Previous", command=self.previous)
        self.back.pack(side="left", padx=8)
        ttk.Button(controls, text="Beginning", command=lambda: self.go_to(1)).pack(
            side="left", padx=8
        )
        self.forward = ttk.Button(controls, text="Next", command=self.next)
        self.forward.pack(side="left", padx=8)
        ttk.Button(controls, text="Exit", command=self.destroy).pack(side="left", padx=8)
        ttk.Label(frame, text="Use ← and → to navigate. The final slide is a closing image.").pack(
            pady=(10, 0)
        )

    def show_slide(self):
        path = slide_path(self.index)
        try:
            with Image.open(path) as source:
                image = source.convert("RGBA")
                image.thumbnail((730, 440), Image.Resampling.LANCZOS)
                self.photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=self.photo, text="")
        except OSError:
            self.photo = None
            self.image_label.configure(image="", text=f"Image unavailable: {path.name}")
        title = "Closing slide" if self.index == MAX_SLIDE else f"Slide {self.index} of 99"
        self.caption.configure(text=title)
        self.back.configure(state="normal" if self.index > MIN_SLIDE else "disabled")
        self.forward.configure(state="normal" if self.index < MAX_SLIDE else "disabled")

    def go_to(self, index: int):
        self.index = max(MIN_SLIDE, min(MAX_SLIDE, index))
        self.show_slide()

    def previous(self):
        self.go_to(self.index - 1)

    def next(self):
        self.go_to(self.index + 1)


if __name__ == "__main__":
    NamesWindow().mainloop()
