import turtle


def yin_yang(rayon, color1='black', color2='white'):
    """ dessine un logo yin-yang de rayon rayon """

    def yang(rayon, couleur1, couleur2):
        """ dessin du yang à l'intérieur du yin """
        turtle.left(90)
        turtle.up()
        turtle.forward(rayon * 0.35)
        turtle.right(90)
        turtle.down()
        turtle.color(couleur1, couleur2)
        turtle.begin_fill()
        turtle.circle(rayon * 0.12)
        turtle.end_fill()
        turtle.left(90)
        turtle.up()
        turtle.backward(rayon * 0.35)
        turtle.down()
        turtle.left(90)

    def yin(rayon, couleur1, couleur2):
        """ dessine la moitié d'un yin-yang le contour étant en noir"""
        turtle.color("black", couleur1)
        turtle.begin_fill()
        turtle.circle(rayon / 2., 180)  # demi cercle de rayon / 2
        turtle.circle(rayon, 180)  # demi cercle de rayon
        turtle.left(180)
        turtle.circle(-rayon / 2., 180)  # demi cercle intérieur de rayon / 2
        turtle.end_fill()
        yang(rayon, couleur1, couleur2)  # dessine le yang à l'intérieur du yin

    # code de yin_yang
    turtle.reset()
    turtle.width(2)
    yin(rayon, color1, color2)
    yin(rayon, color2, color1)
    turtle.hideturtle()
    return


# code principal
yin_yang(200)  # réalise le logo
