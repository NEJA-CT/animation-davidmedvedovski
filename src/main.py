import pyxel
import math
import random


# -------------------------------------------------
# Matrix Transform Functions
# -------------------------------------------------


def mat_translate(tx, ty):
    return [
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1],
    ]


def mat_scale(sx, sy):
    return [
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1],
    ]


def mat_rotate(a):
    c, s = math.cos(a), math.sin(a)
    return [
        [c, -s, 0],
        [s, c, 0],
        [0, 0, 1],
    ]


def mat_mul(A, B):
    M = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for r in range(3):
        for c in range(3):
            M[r][c] = sum(A[r][k] * B[k][c] for k in range(3))
    return M


def apply_matrix(M, x, y):
    tx = M[0][0] * x + M[0][1] * y + M[0][2]
    ty = M[1][0] * x + M[1][1] * y + M[1][2]
    return tx, ty


# -------------------------------------------------
# Rendering Functions
# -------------------------------------------------


def line_transformed(M, x1, y1, x2, y2, col):
    tx1, ty1 = apply_matrix(M, x1, y1)
    tx2, ty2 = apply_matrix(M, x2, y2)
    pyxel.line(tx1, ty1, tx2, ty2, col)


def quad_transformed(M, x1, y1, x2, y2, x3, y3, x4, y4, col, outline=False):
    # Transform each corner
    tx1, ty1 = apply_matrix(M, x1, y1)
    tx2, ty2 = apply_matrix(M, x2, y2)
    tx3, ty3 = apply_matrix(M, x3, y3)
    tx4, ty4 = apply_matrix(M, x4, y4)

    if outline:
        # Draw 4 edge lines
        pyxel.line(tx1, ty1, tx2, ty2, col)
        pyxel.line(tx2, ty2, tx3, ty3, col)
        pyxel.line(tx3, ty3, tx4, ty4, col)
        pyxel.line(tx4, ty4, tx1, ty1, col)

    else:
        # Draw filled quad as two triangles
        pyxel.tri(tx1, ty1, tx2, ty2, tx3, ty3, col)
        pyxel.tri(tx1, ty1, tx3, ty3, tx4, ty4, col)


def tri_transformed(M, x1, y1, x2, y2, x3, y3, col, outline=False):
    tx1, ty1 = apply_matrix(M, x1, y1)
    tx2, ty2 = apply_matrix(M, x2, y2)
    tx3, ty3 = apply_matrix(M, x3, y3)

    if outline:
        pyxel.trib(tx1, ty1, tx2, ty2, tx3, ty3, col)
    else:
        pyxel.tri(tx1, ty1, tx2, ty2, tx3, ty3, col)


def flower_transformed(M, cx, cy, r, col, num_petals=8):
    for i in range(num_petals):
        a0 = (math.pi * 2 / num_petals) * i
        a1 = a0 + 0.4

        x1, y1 = cx + math.cos(a0) * r, cy + math.sin(a0) * r
        x2, y2 = cx + math.cos(a1) * r, cy + math.sin(a1) * r

        tri_transformed(M, cx, cy, x1, y1, x2, y2, col)


def ellipse_transformed(M, cx, cy, rx, ry, col, segments=32, outline=False):
    # Precalculate the points of the circle
    points = []
    for i in range(segments):
        a = (i / segments) * math.tau
        x = cx + math.cos(a) * rx
        y = cy + math.sin(a) * ry
        tx, ty = apply_matrix(M, x, y)
        points.append((tx, ty))

    if outline:
        # Connect successive transformed points
        for i in range(segments):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % segments]
            pyxel.line(x1, y1, x2, y2, col)

    else:
        # Fill by triangulating around the center
        cx_t, cy_t = apply_matrix(M, cx, cy)
        for i in range(segments):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % segments]
            pyxel.tri(cx_t, cy_t, x1, y1, x2, y2, col)


def circle_transformed(M, cx, cy, r, col, segments=32, outline=False):
    # A circle is just an ellipse with the same x/y radius
    ellipse_transformed(M, cx, cy, r, r, col, segments, outline)


pyxel.init(720, 360, title="Matrix Transform Demo")

# assign some random positions for "stars"
stars = []
for _ in range(200):
    stars.append((random.randint(-200, 200), random.randint(-200, 200)))

# state
angle = 0
M = [  # identiy matrix
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]
cx,cy=240,240
cx,cy= cx,cy-30

M=mat_mul(
    mat_translate(cx,cy),mat_mul(mat_rotate(angle),mat_translate(-cx,-cy)),
    ) 

def update():
    global M, angle
    angle += 0.03  # increment rotation every frame

    # Pulsating scale
    s = 1 + 0.5 * math.sin(angle * 2)

    # Transform: scale → rotate → translate
    M_scale = mat_scale(s, s)
    M_rotate = mat_rotate(angle)
    M_translate = mat_translate(100, 75)  # center around (0, 0)

   # M = mat_mul(M_translate, mat_mul(M_rotate, M_scale))


def draw():

    pyxel.cls(0)

    pyxel.rect(0,0,720,60,5)
    pyxel.rect(0,60,720,70,7)
    pyxel.rect(0,70,720,290,8)
    pyxel.rect(0,290,720,300,7)
    pyxel.rect(0,300,720,360,5)

    pyxel.rect(420,150,120,70,15)
    pyxel.elli (405,160,20,40,15)
    pyxel.elli (535,160,20,40,15)
    pyxel.elli (435,150,35,10,7)
    pyxel.elli (485,150,35,10,7)
    win_x,win_y,win_r=500,155,5
    pyxel.circ(win_x,win_y,win_r, 4)
    pyxel.circb(win_x,win_y,win_r, 4)

    win_x,win_y,win_r=450,155,5
    pyxel.circ(450,155,5, 4)
    pyxel.circb(win_x,win_y,win_r, 4)

    pyxel.elli (440,190,60,40,0)

    pyxel.rect(420,85,120,15,0)

    
    pyxel.circ(240,180,82,col=0)
    pyxel.circ(240,180,80,col=7)
    tri_transformed(M,cx, cy, 170, 160, 310, 160, col=8)
    tri_transformed(M,cx, cy, 240, 110, 200, 240, col=8)
    tri_transformed(M,cx, cy, 240, 110, 280, 240, col=8)


pyxel.run(update, draw)