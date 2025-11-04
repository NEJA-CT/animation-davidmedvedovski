# Pyxel Web + Codespaces Starter

This template gives students a **zero-install** Python game loop in the browser using **Pyxel Web**—perfect for Chromebooks.  
It runs a small HTTP server inside Codespaces and loads your `src/main.py` via a `<pyxel-run>` tag.

## Quick start (students)
1. Open the assignment → **Open in Codespaces**.
2. Open the Preview with Shift-Ctrl-P and type "Live Preview: Start Server"
3. Edit `src/main.py` → **save** → **refresh the browser** to see changes. The page should update on save.

## Publishing (optional)
When you want to share final projects without Codespaces:
- Convert to a standalone HTML bundle (host anywhere):  
  `pyxel package` → `pyxel app2html` (see Pyxel docs)
- Or use the official **Pyxel Web Launcher** pattern to run straight from GitHub:  
  `https://kitao.github.io/pyxel/wasm/launcher/?run=USER.REPO.src.main`

## Repo layout
```
.
├─ .devcontainer/
│  └─ devcontainer.json      # Sets up Python + forwards port 8000 + auto-starts server
├─ assets/                   # Put .pyxres or images/sfx here (kept via .gitkeep)
├─ src/
│  └─ main.py                # Your Pyxel sketch (update/draw loop)
├─ index.html                # Loads pyxel.js and runs src/main.py in the browser
└─ README.md
```

## Notes
- On the web, only **Pyodide-supported** Python packages can be imported.
- Keep resolutions modest (e.g., 160×120 or 256×144) for smooth 60 FPS.
- Press **Q** in the sketch to quit the app loop.
