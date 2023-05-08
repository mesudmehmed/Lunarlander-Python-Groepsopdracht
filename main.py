# Import
import pygame

# import mixer
from pygame import mixer

import sys

# pygame starten
pygame.init()

# naam van de game instellen
pygame.display.set_caption("Lunar Lander X")
programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)
# schermgroote bepalen
win_width = 1000
win_height = 650
win = pygame.display.set_mode((win_width, win_height))

# Music
mixer.music.load("EpixSpace.wav")
mixer.music.play(-1)

#Sounds
Jet_Rocket = mixer.Sound("JetRocket.wav")
Jet_Rocket.set_volume(0.1)
Round_1 = mixer.Sound("Round_1.wav")
Round_2 = mixer.Sound("Round_2.wav")
Round_3 = mixer.Sound("Round_3.wav")
Round_4 = mixer.Sound("Round_4.wav")




# Images
background = pygame.image.load('background.png')    # background
surface = pygame.image.load('surface.jpg')          # surface
target = pygame.image.load('target.png')            # target
playerImg = pygame.image.load('lander.png')         # racket
boost = pygame.image.load('boost.png')
boostleft = pygame.image.load('boostleft.png')
boostright = pygame.image.load('boostright.png')
# Player
def player(x,y):
    win.blit(playerImg, (x,y))

from Landscape_and_Target import getLandscape_and_Target

# LanderEvents
from LanderEvent import HitTarget
from LanderEvent import Collision

# onze text voor de brandstof bepalen
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
def show_fuel(x, y):
    score = font.render("Fuel: " + str(fuel), True, (255, 255, 255))
    if fuel <= 1000:
          score = font.render("Fuel: " + str(fuel), True, (255, 170, 70))
    if fuel <= 500:
          score = font.render("Fuel: " + str(fuel), True, (255, 0, 0))
    win.blit(score, (x, y))

# Fonts
font_medium = pygame.font.Font(None, 40)
font_big = pygame.font.Font(None, 60)

# Colors
color_green = (0, 130, 0)
color_orange = (255, 170, 70)
color_grey = (205, 205, 205)

# Text
text_pass = 'Gefeliciteerd! Je lander is geland!'                       # 1 green 200
text_fail = 'Helaas! Je bent neergestort...'                            # 2 orange 200
text_space = 'Druk op "SPATIE" om het nog een keer te proberen.'        # 3 grey 300
text_next = 'Druk op "N" om naar het volgende level te gaan!'           # 4 grey 400
text_complete = 'Je hebt alle levels voltooid!'                         # 5 green 400
text_start = 'Druk op "BACKSPACE" om terug te gaan naar start'          # 7 grey 550
text_made = 'Deze game is gemaakt door: Mesud, Johan, Dogus en Joost.'

surf_text_pass = font_big.render(text_pass, True, color_green)
surf_text_fail = font_big.render(text_fail, True, color_orange)
surf_text_space = font_medium.render(text_space, True, color_grey)
surf_text_next = font_medium.render(text_next, True, color_grey)
surf_text_complete = font_medium.render(text_complete, True, color_green)
surf_text_start = font_medium.render(text_start, True, color_grey)
surf_text_made = font_medium.render(text_made, True, color_grey)

rect_text_pass = surf_text_pass.get_rect(midbottom = (win_width//2,200))
rect_text_fail = surf_text_pass.get_rect(midbottom = (win_width//2,200))
rect_text_space = surf_text_pass.get_rect(midbottom = (win_width//2,300))
rect_text_next = surf_text_pass.get_rect(midbottom = (win_width//2,400))
rect_text_complete = surf_text_pass.get_rect(midbottom = (win_width//2,400))
rect_text_start = surf_text_start.get_rect(midbottom = (win_width//2,550))
rect_text_made = surf_text_made.get_rect(midbottom = (win_width//2,550))


game_state = 'start'
new_game_state = 'yes'
player_result = ''
all_levels_allowed = False
level = 1
number_of_levels = 4
fuel = 1500

font = pygame.font.Font('freesansbold.ttf', 32)
screen = pygame.display.set_mode((1000, 650), 0, 32)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# while aanmaken die doorgat en ervoor zorgt dat de spel net zo lang doorgaat totdat het fenster afgesloten is
run = True
while run:
    # beweegsnelheid
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if game_state == 'start':
        win.fill((0, 0, 0))  # zwarte kleur
        win.blit(background, (0, 0))  # background
        win.blit(surf_text_made, rect_text_made) #onze namen

        mx, my = pygame.mouse.get_pos() #positie van je muis word bepaald
        button_1 = win.blit(font_big.render('Start Game', True, color_grey), (100,100))    #button 'Start Game'
        if button_1.collidepoint((mx, my)):  #als de x en y coördinaten van je muis op dezelfde plek zitten als de button is er aan de conditie voldaan
            button_1 = button_1 = win.blit(font_big.render('Start Game', True, color_green), (100,100)) #button veranderd in groen als je met je cursor over de buttong gaat
            if click: #Als je klikt word er aan de conditie voldaan.
                game_state = 'game'
                new_game_state = 'yes'

        click = False
        for event in pygame.event.get():        #met de spatiebalk kan je ook starten
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = 'game'
                    new_game_state = 'yes'
            if event.type == pygame.MOUSEBUTTONDOWN:    #geeft het klikken van je muis een waarde
                if event.button == 1:
                    click = True

        pygame.display.update()


    if game_state == 'game':
        pygame.time.delay(20)
        # new_game
        if new_game_state == 'yes':
            new_game_state = 'no'

            if level == 1:
                Round_1.play()
            if level == 2:
                Round_2.play()
            if level == 3:
                Round_3.play()
            if level == 4:
                Round_4.play()

            # de waardes van onze racketje bepalen
            playerX = 20
            playerY = 20
            vel = 5
            boostUPY = 800
            boostUPX = 0
            boostLEFTY = 800
            boostLEFTX = 0
            boostRIGHTY = 800
            boostRIGHTX = 0
            # de brandstofwaarde van ons racketje bepalen


            if level == 1:
                small_x_coordinates, small_y_coordinates, dots_x, dots_y, all_y_at_x_sorted_with_minus_one, targetWidth, targetHeight, target_left_X, target_bottom_Y = getLandscape_and_Target(
                    'landscape_default', win_width)
                saved_fuel = fuel
            elif level == 2:
                small_x_coordinates, small_y_coordinates, dots_x, dots_y, all_y_at_x_sorted_with_minus_one, targetWidth, targetHeight, target_left_X, target_bottom_Y = getLandscape_and_Target(
                    'landscape_xx', win_width)
                saved_fuel = fuel
            elif level == 3:
                small_x_coordinates, small_y_coordinates, dots_x, dots_y, all_y_at_x_sorted_with_minus_one, targetWidth, targetHeight, target_left_X, target_bottom_Y = getLandscape_and_Target(
                    'landscape_voorbeeld_strak', win_width)
                saved_fuel = fuel
            elif level == 4:
                small_x_coordinates, small_y_coordinates, dots_x, dots_y, all_y_at_x_sorted_with_minus_one, targetWidth, targetHeight, target_left_X, target_bottom_Y = getLandscape_and_Target(
                    'landscape_next_level', win_width)
                saved_fuel = fuel




        # level

        # basis background instellen
        win.fill((0, 0, 0))  # zwarte kleur
        win.blit(background, (0, 0))  # background
        win.blit(surface, (0, 550))  # surface
        win.blit(boost, (boostUPX, boostUPY + 20))  # boostUP
        win.blit(boostleft, (boostLEFTX, boostLEFTY + 5))  # boostLEFT
        win.blit(boostright, (boostRIGHTX, boostRIGHTY + 5))  # boostLEFT
        for i in range(len(small_x_coordinates) - 1):
            pygame.draw.line(win, 'grey', (small_x_coordinates[i], small_y_coordinates[i]),
                             (small_x_coordinates[i + 1], small_y_coordinates[i + 1]), 4)
        show_fuel(textX, textY)
        win.blit(target, (target_left_X, target_bottom_Y - targetHeight))
        win.blit(playerImg, (playerX, playerY))  # onze racketje is uiteindelijk volwassen geworden en is goed te zien
        playerY += 2
        boostUPY = 800
        boostUPX = 0
        boostLEFTY = 800
        boostLEFTX = 0
        boostRIGHTY = 800
        boostRIGHTX = 0
        pygame.display.update()
        # controller
        # controller
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerX -= vel
            fuel -= 1
            boostRIGHTY = playerY
            boostRIGHTX = playerX + 30
            Jet_Rocket.play()
        if keys[pygame.K_RIGHT]:
            playerX += vel
            fuel -= 1
            boostLEFTY = playerY
            boostLEFTX = playerX - 28
            Jet_Rocket.play()
        if keys[pygame.K_UP]:
            playerY -= vel
            fuel -= 1
            boostUPY = playerY + 6
            boostUPX = playerX
            Jet_Rocket.play()
        # beperken van onze racket dat tie niet uit de randjes vliegt (wij hebben hem vast in de kooi
        if playerX <= 10:
            playerX = 10
        elif playerX >= 960:
            playerX = 960
        if playerY <= 10:
            playerY = 10
        elif playerY >= 582:
            playerY = 582

        if fuel <= 0:
           if keys[pygame.K_LEFT]:
               fuel = 0
               vel = 0
           if keys[pygame.K_RIGHT]:
               fuel = 0
               vel = 0
           if keys[pygame.K_UP]:
               fuel = 0
               vel = 0

        hitTarget = HitTarget(playerX, playerY, target_left_X, target_bottom_Y)
        if hitTarget:
            Victory_Sound = mixer.Sound("Victory.wav")
            Victory_Sound.play()
            player_result = 'pass'
            game_state = 'end'

        collision = Collision(playerX,playerY,all_y_at_x_sorted_with_minus_one)
        if collision:
            Crash_Sound = mixer.Sound("Death.wav")
            Crash_Sound.play()
            GameOver_Sound = mixer.Sound("Game_Over.wav")
            GameOver_Sound.play()
            player_result = 'fail'
            game_state = 'end'
            fuel = saved_fuel




    if game_state == 'end':
        # basis background instellen
        win.fill((0, 0, 0))  # zwarte kleur
        win.blit(background, (0, 0))  # background
        # onderstaande weg als andere vormgeving van eindscherm

        if player_result == 'pass' and level < number_of_levels:
            # screen
            win.blit(surf_text_pass, rect_text_pass)  # 1
            win.blit(surf_text_space, rect_text_space)  # 3
            win.blit(surf_text_next, rect_text_next)  # 4
            win.blit(surf_text_start, rect_text_start)  # 7

            mx, my = pygame.mouse.get_pos()  # positie van je muis word bepaald
            button_2 = win.blit(font_big.render('Ga naar het volgende level!', True, color_grey), (240, 440))  # button 'volgende level'

            if button_2.collidepoint((mx,my)):  # als de x en y coördinaten van je muis op dezelfde plek zitten als de button is er aan de conditie voldaan
                button_1 = button_1 = win.blit(font_big.render('Ga naar het volgende level!', True, color_green), (240, 440))  # button veranderd in groen als je met je cursor over de buttong gaat
                if click:  # Als je klikt word er aan de conditie voldaan.
                    game_state = 'game'
                    new_game_state = 'yes'
                    level += 1

            # keys
            click = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:  # geeft het klikken van je muis een waarde
                    if event.button == 1:
                        click = True


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_state = 'game'
                        new_game_state = 'yes'


                    if event.key == pygame.K_n:
                        game_state = 'game'
                        new_game_state = 'yes'

                        level += 1
                    if event.key == pygame.K_BACKSPACE:
                        game_state = 'start'
                        new_game_state = 'yes'
                        player_result = ''
                        level = 1






        if player_result == 'fail':
            # screen
            win.blit(surf_text_fail, rect_text_fail)  # 2
            win.blit(surf_text_space, rect_text_space)  # 3
            win.blit(surf_text_start, rect_text_start)  # 7

            mx, my = pygame.mouse.get_pos()  # positie van je muis word bepaald
            button_2 = win.blit(font_big.render('Probeer opnieuw', True, color_grey), (350, 350))  # button 'Probeer opnieuw'

            if button_2.collidepoint((mx,my)):  # als de x en y coördinaten van je muis op dezelfde plek zitten als de button is er aan de conditie voldaan
                button_1 = button_1 = win.blit(font_big.render('Probeer opnieuw', True, color_green), (350, 350))  # button veranderd in groen als je met je cursor over de buttong gaat
                if click:  # Als je klikt word er aan de conditie voldaan.
                    game_state = 'game'
                    new_game_state = 'yes'
                    player_result = ''

            # keys
            click = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:  # geeft het klikken van je muis een waarde
                    if event.button == 1:
                        click = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_state = 'game'
                        new_game_state = 'yes'
                        player_result = ''

                    if event.key == pygame.K_BACKSPACE:
                        game_state = 'start'
                        new_game_state = 'yes'
                        player_result = ''
                        level = 1




        if player_result == 'pass' and level == number_of_levels:
            # screen
            win.blit(surf_text_pass, rect_text_pass)  # 1
            win.blit(surf_text_space, rect_text_space)  # 3
            win.blit(surf_text_complete, rect_text_complete)  # 5
            win.blit(surf_text_start, rect_text_start)  # 7

            all_levels_allowed = True

            # keys
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_state = 'game'
                        new_game_state = 'yes'
                        player_result = ''

                    if event.key == pygame.K_BACKSPACE:
                        game_state = 'start'
                        new_game_state = 'yes'
                        player_result = ''
                        level = 1















    pygame.display.update()




