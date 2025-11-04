#!/bin/bash
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
  source .venv/bin/activate
  pip install --upgrade pip
  pip install pyxel==2.5.7
  pip install livereload
else
  source .venv/bin/activate
fi
python serve.py