from Gamescreen import Gamescreen
from Iceball import Iceball
from boss import Boss
from Coin import Coin
from Bullet import Bullet
from User import User
from Background import Background
from Beam import Beam
from Magnet import Magnet
from Speedup import Speedup
from os import system
from time import sleep
import termios
import sys
import select
import tty


sc = Gamescreen()
bg = Background()

u = User()
c = Coin()
bl = Bullet()

while sc.get_trip() < 2:

    b = []
    m = None
    sp = None

    sc.init_field()
    sc.init_trash()

    sc.set_nxt(0)
    sc.set_timer(0)
    sc.set_no(0)
    sc.set_m_no(0)
    sc.set_s_no(0)
    sc.set_disappeared(0)

    while sc.get_disappeared() < sc.get_beams():
        sc.refresh()
        if sc.get_trip() == 1 and sp == None and sc.get_s_no() == 0:
            sp = Speedup()
            sc.set_timer(0)
            sc.set_s_no(1)

        if m != None:
            sc.set_field(m.attract())
        
        if u.in_range(sc.get_field()):
            u.attraction()

        if sp != None:
            if sp.activate(u.get_centre()) == True:
                sp = None
                sc.boost_time()

        sc.set_shield(u.get_shield())

        for i in range(len(b)):
            if b[i].check_collision(u.get_centre()) == True:
                if u.get_shield() == False:
                    u.reduce_health()
                sc.add_trash(b[i])
                sc.inc_disappeared()
                break

        for i in sc.get_trash():
            b.remove(i)

        sc.init_trash()

        if m != None and m.check_collision(u.get_centre()) == True:
            if u.get_shield() == False:
                u.reduce_health()
            del(m)
            m = None

        for i in range(len(b)):
            t = b[i].check_bullets(bl.get_centre())
            if t != -1:
                sc.add_trash(b[i])
                sc.inc_disappeared()
                bl.erase(t)

        for i in sc.get_trash():
            b.remove(i)

        sc.init_trash()
        
        if m != None:
            t = (m.check_bullets(bl.get_centre()))
            for i in t:
                bl.erase(i)
        sc.init_trash()


        bg.update(sc)
        bl.update(sc)
        c.update(sc)

        t = u.move()
        
        if t != 0 and t != 1:
            u.fall()
            bl.new_bullet(t)
        elif t == 0:
            u.fall()

        u.printer(sc)
        sc.add(c.rem(u.get_centre()))

        sc.set_nxt(0)

        if m == None and sc.get_no() > sc.get_beams() / 2 and sc.get_timer() > 10 and sc.get_m_no() < 1:
            m = Magnet()
            sc.set_timer(0)
            sc.set_m_no(1)
        
        for i in range(len(b)):
            if b[i].get_immersed() == 0 and (m == None or m.get_immersed()):
                sc.set_nxt(1) 

        if sc.get_timer() > 10 and sc.get_no() < sc.get_beams():
            b.append(Beam())
            sc.set_timer(0)
            sc.inc_no()

        elif sc.get_nxt() == 0:
            sc.inc_timer()

        sc.set_coin_loc(-1)
        while sc.get_coin_loc() == -1:
            sc.set_coin_loc(c.random_location())

            for i in range(len(b)):
                if b[i].get_immersed() == 0:
                    if b[i].check_location(sc.get_coin_loc()) == -1:
                        sc.set_coin_loc(-1)

        c.create(sc.get_coin_loc(),sc)

        for i in range(len(b)):
            if b[i].update(sc) == 0:
                sc.add_trash(b[i])
                sc.inc_disappeared()

        for i in sc.get_trash():
            b.remove(i)

        sc.init_trash()

        if m != None:
            m.update(sc)

        if sp != None:
            sp.update()
            if sp.in_screen() == False:
                sp = None
        
        if u.get_shield() == True:
            u.shield_duration()
        else:
            u.shield_recover()

        if sp != None:
            sp.display(sc)

        sc.speed_timer()
        sc.set_health(u.get_health())
        
        sc.print_screen()
        sc.init_field()
        sc.init_trash()

        sleep(0.0615)
        system('clear')

    sc.set_trip()

while c.clear_coin() == False:
    sc.refresh()
    bg.update(sc)
    c.update(sc)
    bl.update(sc)

    sc.set_shield(u.get_shield())

    t = u.move()
        
    if t != 0 and t != 1:
        u.fall()
        bl.new_bullet(t)
    elif t == 0:
        u.fall()

    u.printer(sc)
    sc.add(c.rem(u.get_centre()))

    if u.get_shield() == True:
        u.shield_duration()
    else:
        u.shield_recover()

    sc.print_screen()

    sleep(0.0615)
    system('clear')

bo = Boss()
ic = Iceball()

while bo.in_range() == False:
    
    sc.refresh()
    bg.update(sc)
    bl.update(sc)

    bo.entrance()
    bo.printer(sc)

    t = u.move()
        
    if t != 0 and t != 1:
        u.fall()
        bl.new_bullet(t)
    elif t == 0:
        u.fall()

    sc.add_trash(bo.damage(bl.get_centre()))
    
    for bul in sc.get_trash():
        bl.erase(bul)

    sc.init_trash()

    u.printer(sc)

    sc.print_screen()

    sleep(0.0715)
    system('clear')

sc.set_boss(bo.get_health())

while bo.not_dead() == True:
    sc.refresh()

    bg.update(sc)
    bl.update(sc)
    ic.update(sc)

    sc.set_shield(u.get_shield())
    
    t = u.move()
        
    if t != 0 and t != 1:
        u.fall()
        bl.new_bullet(t)
    elif t == 0:
        u.fall()

    bo.move(u.get_centre())
    if bo.breath() == True:
        ic.new_iceball(bo.get_centre())
    
    i = bo.damage(bl.get_centre())
    a = bl.get_centre()

    if sc.get_empty != []:
        for j in i:
            bl.erase(a[j])

    i = u.damage(ic.get_loc())
    
    if u.get_shield() == False:
        for ice in i:
            ic.erase(ice)
            u.reduce_health()

    sc.init_empty()

    u.printer(sc)
    bo.printer(sc)
    sc.set_health(u.get_health())
    sc.set_boss(bo.get_health())

    if u.get_shield() == True:
        u.shield_duration()
    else:
        u.shield_recover()

    sc.print_screen()

    sleep(0.0715)
    system('clear')

sc.print_screen()
sleep(1)

sc.cut()

sc.congratulate()

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, u.get_settings())