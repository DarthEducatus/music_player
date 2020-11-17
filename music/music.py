import pygame


def m1():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('E:/git/pytom/music_player/music/audio/1.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()


def m2():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('E:/git/pytom/music_player/music/audio/2.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()


def m3():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('E:/git/pytom/music_player/music/audio/3.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()


def m4():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('E:/git/pytom/music_player/music/audio/4.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()


def m5():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('E:/git/pytom/music_player/music/audio/5.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()


def m6():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('E:/git/pytom/music_player/music/audio/6.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()


def m7():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('E:/git/pytom/music_player/music/audio/7.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()


def m8():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('E:/git/pytom/music_player/music/audio/8.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()


def m9():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('E:/git/pytom/music_player/music/audio/9.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()


def m10():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('E:/git/pytom/music_player/music/audio/10.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()


def m11():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('E:/git/pytom/music_player/music/audio/11.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()


# def opção(x):
#    if o == 1:
#        v=+1
#    elif o == 2:
#        c=+1
#    else:
#        z=+1
v=0
c=0
z=0
print('Bem vindo quiz musica player')
nome = input('Digite o nome:')
print('Muito bem {}\n'.format(nome))
o = int(input(
    '1) Como voce se sente quando alguem te magoa? \n 1 não liga\n 2 fica encomodado\n 3 Voce fica louco\n digite: '))
if o == 1:
    v = v +1
elif o == 2:
    c = c +1
else:
    z = z +1
o = int(input('2) que estilo de musica voce gosta? \n 1 normal\n 2 lenta\n 3 acelerada\n digite: '))
if o == 1:
    v = v +1
elif o == 2:
    c = c +1
else:
    z = z +1
o = int(input('3) Que tipo de pessoa e? \n 1 incencivel\n 2 participativo\n 3 frajil\n digite: '))
if o == 1:
    v = v +1
elif o == 2:
    c = c +1
else:
    z = z +1
o = int(input('4) Voce costuma sair com colegas? \n 1 nunca\n 2 as vezes\n 3 sempre que tiver chance\n digite: '))
if o == 1:
    v = v +1
elif o == 2:
    c = c +1
else:
    z = z +1
o = int(input('5) O que voce gosta? \n 1 anime\n 2 serie\n 3 outros\n digite: '))
if o == 1:
    v = v +1
elif o == 2:
    c = c +1
else:
    z = z +1
# opção(o)
if v == 3:
    m7()
elif v == 4:
    m8()
elif v == 5:
    m9()
if c == 3:
    m1()
elif c == 4:
    m2()
elif c == 5:
    m3()
elif v == c:
    m10()
elif z == v:
    m11()
if z == 3:
    m4()
elif z == 4:
    m5()
elif z == 5:
    m6()
