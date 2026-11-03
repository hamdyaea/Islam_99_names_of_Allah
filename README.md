# The 99 Names of Allah — Python Desktop Viewer

Developer: Hamdy Abou El Anein
Contact: hamdy.aea@protonmail.com
License: GNU GPL v3 (see LICENSE).

An educational slideshow of the historical 100 images in `Pictures/`
(99 numbered slides and one closing slide). The application has been
modernized from recursive EasyGUI dialogs to a single **Tkinter** window.

## Install and run

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python names_of_Allah.py
```

Tkinter must be installed through your Linux distribution. Use Previous,
Next and Beginning buttons or keyboard arrow keys and Home/End.

## Tests

```sh
python3 -m unittest discover -s tests -v
```

Tests check the full image set, invalid indices and portable paths.
The GUI was also opened and navigated on Manjaro during modernization.
The original code is preserved in the Git branch `old`.

The original images are retained unchanged. Their underlying artwork
and any third-party rights are not reassigned by this modernization.
