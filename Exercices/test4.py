n = 4
x  = 2

import turtle

for i in range(1, n + 1):
    turtle.goto(x + rayon * cos(i * 2 * pi / n), y + rayon * sin(i * 2 * pi / n))
