import turtle


def draw_a():
    # drawing alphabet a
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    a = turtle.Turtle()
    a.showturtle()
    a.speed(5)
    a.color("yellow")
    a.left(73.5)
    a.forward(103)
    a.right(147)
    a.forward(103)
    a.backward(40)
    a.right(106.5)
    a.forward(37)
    a.hideturtle()

def draw_b():
    # draw b shape
    #import turtle
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    b = turtle.Turtle()
    b.showturtle()
    b.speed(8)
    b.color("pink")
    b.left(90)
    b.forward(100)
    b.right(90)
    b.forward(25)
    for ba in range(18):
        b.forward(4.35)
        b.right(10)
    b.forward(27)
    b.right(180)
    b.forward(27)
    for ba in range(18):
        b.forward(4.37)
        b.right(10)
    b.forward(32)

    b.hideturtle()


def draw_c():
    # drawing alphabet c
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    c = turtle.Turtle()
    c.showturtle()
    c.speed(8)
    c.color("cyan")
    c.left(90)
    c.up()
    c.forward(100)
    c.right(90)
    c.forward(60)
    c.right(180)
    # drawing starts here
    c.down()
    c.forward(15)
    for ca in range(9):
        c.forward(7)
        c.left(10)
    c.forward(20)
    for ca in range(9):
        c.forward(7)
        c.left(10)
    c.forward(22)

    c.hideturtle()


def draw_d():
    # drawing alphabet d
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    d = turtle.Turtle()
    d.speed(5)
    d.color("white")
    d.left(90)
    d.forward(100)
    d.right(90)
    d.forward(15)
    for da in range(9):
        d.forward(7)
        d.right(10)
    d.forward(19)
    for da in range(9):
        d.forward(7.2)
        d.right(10)
    d.forward(22)

    d.hideturtle()


def draw_e():
    # drawing alphabet e
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    e = turtle.Turtle()
    e.speed(5)
    e.color("orange")
    e.left(90)
    e.forward(100)
    e.right(90)
    e.forward(55)
    e.backward(55)
    e.right(90)
    e.forward(50)
    e.left(90)
    e.forward(45)
    e.backward(45)
    e.right(90)
    e.forward(50)
    e.left(90)
    e.forward(60)
    e.hideturtle()


def draw_f():
    # drawing alphabet f
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    f = turtle.Turtle()
    f.speed(5)
    f.color("lime")
    f.left(90)
    f.forward(100)
    f.right(90)
    f.forward(60)
    f.backward(60)
    f.right(90)
    f.forward(50)
    f.left(90)
    f.forward(50)

    f.hideturtle()


def draw_g():
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    g = turtle.Turtle()
    g.speed(9)
    g.color('pink')
    g.up()
    g.left(90)
    g.forward(100)
    g.right(90)
    g.forward(56)
    g.right(90)
    g.forward(5)
    g.right(180)
    g.down()
    # start
    g.left(40)
    for ga in range(5):
        g.forward(2)
        g.left(10)
    g.forward(20)
    for ga in range(9):
        g.forward(4.3)
        g.left(10)

    g.forward(50)

    for ga in range(9):
        g.forward(4.2)
        g.left(10)

    g.forward(11)

    for ga in range(9):
        g.forward(4.2)
        g.left(10)

    g.forward(25)
    g.left(90)
    g.forward(25)

    g.hideturtle()
    return


def draw_h():
    # drawing alphabet h
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    h = turtle.Turtle()
    h.speed(2)
    h.color("cyan")
    h.left(90)
    h.forward(100)
    h.backward(50)
    h.right(90)
    h.forward(60)
    h.left(90)
    h.forward(50)
    h.backward(100)

    h.hideturtle()


def draw_i():
    # drawing alphabet i
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    i = turtle.Turtle()
    i.speed(5)
    i.color("yellow")
    i.left(90)
    i.forward(100)
    i.hideturtle()


def draw_j():
    # drawing alphabet j
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    j = turtle.Turtle()
    j.speed(5)
    j.color("white")
    j.up()
    j.forward(68)
    j.left(90)
    j.forward(100)
    j.down()

    j.right(180)
    j.forward(68)
    for ja in range(18):
        j.forward(5.2)
        j.right(10)
    j.forward(10)
    j.hideturtle()
    return


def draw_k():
    # drawing alphabet k
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    k = turtle.Turtle()
    k.speed(8)
    k.color("cyan")
    k.left(90)
    k.forward(100)
    k.up()
    k.right(180)
    k.forward(50)
    k.left(135)
    k.down()
    # first leg
    k.forward(70)
    k.up()
    k.backward(65)
    k.down()
    k.right(88)
    # second leg
    k.forward(77)

    k.hideturtle()
    return


def draw_l():
    # drawing alphabet l
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    l = turtle.Turtle()
    l.speed(5)
    l.color("pink")
    l.left(90)
    l.forward(100)
    l.backward(100)
    l.right(90)
    l.forward(60)

    l.hideturtle()
    return


def draw_m():
    # drawing alphabet m
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    m = turtle.Turtle()
    m.speed(5)
    m.color("yellow")
    m.left(90)
    m.forward(100)
    m.right(150)
    m.forward(80)
    m.left(120)
    m.forward(80)
    m.right(150)
    m.forward(100)
    m.hideturtle()
    return

def draw_n():
    # drawing alphabet n
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    n = turtle.Turtle()
    n.speed(8)
    n.color("pink")
    n.left(90)
    n.forward(100)
    n.right(149)
    n.forward(116)
    n.left(149)
    n.forward(100)

    n.hideturtle()


def draw_o():
    # drawing alphabet o
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    o = turtle.Turtle()
    o.speed(8)
    o.color("white")
    o.left(90)
    o.up()
    o.forward(51)
    o.down()
    o.forward(22)

    for oa in range(18):
        o.right(10)
        o.forward(5.25)

    o.forward(40)

    for oa in range(18):
        o.right(10)
        o.forward(5.25)

    o.forward(21)

    o.hideturtle()


def draw_p():
    # draws alphabet p
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    p = turtle.Turtle()
    p.speed(5)
    p.color('cyan')
    p.left(90)
    p.forward(100)
    p.right(90)
    p.forward(30)
    for pa in range(18):
        p.forward(4.5)
        p.right(10)
    p.forward(35)

    p.hideturtle()
    return


def draw_q():
    # draws alphabet q
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    q = turtle.Turtle()
    q.speed(5)
    q.color('yellow')
    q.left(90)
    q.up()
    q.forward(51)
    q.down()
    q.forward(22)

    for qa in range(18):
        q.right(10)
        q.forward(5.25)

    q.forward(40)

    for qa in range(18):
        q.right(10)
        q.forward(5.25)

    q.forward(21)

    q.up()
    q.right(180)
    q.forward(35)
    q.left(90)
    q.forward(38)
    q.down()

    q.right(45)
    q.forward(30)

    q.hideturtle()
    return


def draw_r():
    # draws alphabet r
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    r = turtle.Turtle()
    r.speed(5)
    r.color('orange')
    r.left(90)
    r.forward(100)
    r.right(90)

    r.forward(30)
    for ra in range(18):
        r.forward(4.5)
        r.right(10)

    r.forward(33)
    r.backward(15)

    r.left(132)
    r.forward(65)

    r.hideturtle()
    return


def draw_s():
    # draws alphabet s
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    s = turtle.Turtle()
    s.speed(5)
    s.color('lime')
    s.up()
    s.left(90)
    s.forward(100)
    s.right(90)
    s.forward(56)
    s.right(90)
    s.forward(5)
    s.right(180)
    s.down()

    # start
    s.left(40)
    for sa in range(5):
        s.forward(2)
        s.left(10)
    s.forward(29)

    # going down
    for sa in range(9):
        s.forward(3)
        s.left(10)
    s.forward(15)

    # going right
    for sa in range(9):
        s.forward(3)
        s.left(10)
    s.forward(26)

    # going down again
    for sa in range(9):
        s.forward(3)
        s.right(10)
    s.forward(16)

    # going left
    for sa in range(9):
        s.forward(3)
        s.right(10)
    s.forward(26)

    # going up
    for sa in range(9):
        s.forward(3)
        s.right(10)

    s.hideturtle()
    return


def draw_t():
    # draws alphabet p
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    t = turtle.Turtle()
    t.speed(5)
    t.color('pink')
    t.left(90)
    t.up()
    t.forward(100)
    t.down()
    t.right(90)
    t.forward(60)
    t.backward(30)
    t.right(90)
    t.forward(100)

    t.hideturtle()
    return


def draw_u():
    # draws alphabet p
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    u = turtle.Turtle()
    u.speed(5)
    u.color('white')
    u.up()
    u.right(90)
    u.backward(100)

    u.down()

    # start
    u.forward(75)

    # going right
    for ua in range(9):
        u.forward(4)
        u.left(10)
    u.forward(14)

    # going up
    for ua in range(9):
        u.forward(4)
        u.left(10)
    u.forward(80)

    u.hideturtle()
    return


def draw_v():
    # draws alphabet v
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    v = turtle.Turtle()
    v.speed(5)
    v.color('cyan')
    v.left(90)
    v.up()
    v.forward(100)
    v.down()
    v.right(162)
    v.forward(105)
    v.left(146)
    v.forward(104)

    v.hideturtle()
    return


def draw_w():
    # draws alphabet w
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    w = turtle.Turtle()
    w.speed(8)
    w.color('yellow')
    w.up()
    w.right(90)
    w.backward(100)
    w.down()

    # start
    w.left(14)
    w.forward(103)
    # going up
    w.left(152)
    w.forward(103)
    # turning back down
    w.right(152)
    w.forward(103)
    # going up again
    w.left(152)
    w.forward(104)

    w.hideturtle()
    return


def draw_x():
    # draws alphabet x
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    x = turtle.Turtle()
    x.speed(5)
    x.color('orange')
    x.left(59)
    x.forward(116.5)
    x.left(121)
    x.up()
    x.forward(58)
    x.down()
    x.left(121)
    x.forward(116.5)

    x.hideturtle()
    return


def draw_y():
    # draws alphabet y
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    y = turtle.Turtle()
    y.speed(5)
    y.color('lime')
    y.left(90)
    y.up()
    y.forward(99)
    y.right(90)
    y.forward(1)
    y.down()
    y.right(60)
    y.forward(58)
    y.left(120)
    y.forward(58)
    y.backward(58)
    y.right(150)
    y.forward(50)

    y.hideturtle()
    return


def draw_z():
    # drawing alphabet z
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    z = turtle.Turtle()
    z.speed(8)
    z.color("yellow")
    z.up()
    z.left(90)
    z.forward(100)
    z.right(90)
    z.down()
    # drawing starts
    z.forward(58)
    z.right(122)
    z.forward(117)
    z.left(122)
    z.forward(62)

    z.hideturtle()

def draw_1():
    # drawing number 1
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    on = turtle.Turtle()
    on.speed(5)
    on.color("white")
    on.up()
    on.left(90)
    on.forward(100)
    on.right(90)
    on.forward(10)
    on.right(90)
    on.down()
    on.forward(100)

    on.hideturtle()
    return


def draw_2():
    # drawing number 2
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    tw = turtle.Turtle()
    tw.speed(5)
    tw.color("lime")
    tw.left(90)
    tw.up()
    tw.forward(100)
    tw.down()
    tw.right(90)
    tw.forward(60)
    tw.right(90)
    tw.forward(50)
    tw.right(90)
    tw.forward(60)
    tw.left(90)
    tw.forward(50)
    tw.left(90)
    tw.forward(60)

    tw.hideturtle()
    return


def draw_3():
    # drawing number 3
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    th = turtle.Turtle()
    th.speed(5)
    th.color("cyan")
    th.left(90)
    th.up()
    th.forward(100)
    th.right(90)
    th.down()
    th.forward(60)
    th.right(90)
    th.forward(50)
    th.right(90)
    th.forward(50)
    th.backward(50)
    th.left(90)
    th.forward(50)
    th.right(90)
    th.forward(60)

    th.hideturtle()
    return


def draw_4():
    # drawing number 4
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    fo = turtle.Turtle()
    fo.speed(5)
    fo.color("orange")
    fo.left(90)
    fo.up()
    fo.forward(100)
    fo.down()
    fo.backward(50)
    fo.right(90)
    fo.forward(60)
    fo.left(90)
    fo.forward(50)
    fo.backward(100)

    fo.hideturtle()
    return


def draw_5():
    # drawing number 5
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    fi = turtle.Turtle()
    fi.speed(5)
    fi.color("yellow")
    fi.left(90)
    fi.up()
    fi.forward(100)
    fi.right(90)
    fi.forward(60)
    fi.down()
    fi.backward(60)
    fi.right(90)
    fi.forward(50)
    fi.left(90)
    fi.forward(60)
    fi.right(90)
    fi.forward(50)
    fi.right(90)
    fi.forward(60)

    fi.hideturtle()
    return


def draw_6():
    # drawing number 6
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    si = turtle.Turtle()
    si.speed(5)
    si.color("white")
    si.left(90)
    si.up()
    si.forward(100)
    si.right(90)
    si.forward(60)
    si.down()
    si.right(180)
    # start
    si.forward(60)
    si.left(90)
    si.forward(100)
    si.left(90)
    si.forward(60)
    si.left(90)
    si.forward(50)
    si.left(90)
    si.forward(60)

    si.hideturtle()
    return


def draw_7():
    # drawing number 7
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    se = turtle.Turtle()
    se.speed(5)
    se.color("lime")
    se.left(90)
    se.up()
    se.forward(100)
    se.right(90)
    se.down()
    se.forward(60)
    se.right(90)
    se.forward(100)

    se.hideturtle()
    return


def draw_8():
    # drawing number 8
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    ei = turtle.Turtle()
    ei.speed(5)
    ei.color("cyan")
    ei.left(90)
    ei.forward(100)
    ei.right(90)
    ei.forward(60)
    ei.right(90)
    ei.forward(100)
    ei.right(90)
    ei.forward(60)
    ei.right(90)
    ei.forward(50)
    ei.right(90)
    ei.forward(60)

    ei.hideturtle()
    return


def draw_9():
    # drawing number 9
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    ni = turtle.Turtle()
    ni.speed(5)
    ni.color("pink")
    ni.left(90)
    ni.up()
    ni.forward(50)
    ni.right(90)
    ni.forward(60)
    ni.down()
    ni.backward(60)
    ni.left(90)
    ni.forward(50)
    ni.right(90)
    ni.forward(60)
    ni.right(90)
    ni.forward(100)
    ni.right(90)
    ni.forward(60)

    ni.hideturtle()
    return


def draw_0():
    # drawing number 0
    turtle.clearscreen()
    turtle.reset()
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Turtle Master")
    ze = turtle.Turtle()
    ze.speed(5)
    ze.color("orange")
    ze.left(90)
    ze.forward(100)
    ze.right(90)
    ze.forward(60)
    ze.right(90)
    ze.forward(100)
    ze.right(90)
    ze.forward(60)

    ze.hideturtle()
    return