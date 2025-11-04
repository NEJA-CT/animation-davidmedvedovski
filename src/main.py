import pyxel

W, H = 160, 120
x, y = 10, 10
dx, dy = 1, 1


def update():
    global x, y, dx, dy
    # Quit with Q
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    # Simple movement demo
    x += dx
    y += dy
    if x <= 0 or x >= W - 10:
        dx = -dx
    if y <= 0 or y >= H - 10:
        dy = -dy
 

def draw():
    pyxel.cls(0)              # clear screen to color 0 (black)
    pyxel.text(4, 4, "Hello Pyxel Web!", 7)
    pyxel.rect(x, y, 10, 10, 11)  # small bouncing square


pyxel.init(W, H, title="Pyxel Web (Codespaces)")
pyxel.run(update, draw)
