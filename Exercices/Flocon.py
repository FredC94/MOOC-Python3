import turtle as tu



def flocon(l):
    tu.speed(10000)
    tu.color('#0000ff', '#55ffff')
    tu.begin_fill()
    for i in range(3):
        floc(l)
        tu.rt(120)
    tu.end_fill()


flocon(100)