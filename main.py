import random

import pygame

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CAR_WIDTH = 40
CAR_HEIGHT = 80

pygame.init()

#muutujatele väärtuse andmine
background_image = pygame.image.load('bg_rally.jpg')
player_car_image = pygame.image.load('f1_red.png')
blue_car_image = pygame.image.load('f1_blue.png')

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #ekraani parameetrid
pygame.display.set_caption("Automäng") #pealkiri


clock = pygame.time.Clock() #kaadrisagedus

score = 0  #algskoori loomine
font = pygame.font.SysFont(None, 26)

# Loome mängija auto
player_car_rect = player_car_image.get_rect(
    center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 100))  #punase auto ekraani keskele paigutamine

#siniste autode list
blue_cars = []
for i in range(5):
    blue_car_rect = blue_car_image.get_rect(
        center=(random.randint(0, WINDOW_WIDTH - CAR_WIDTH), random.randint(-WINDOW_HEIGHT, 0)))
    blue_cars.append(blue_car_rect)

#pea-loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()  #muutuja saab nuppe vajutades väärtuse
    if keys[pygame.K_LEFT] and player_car_rect.left > 0:  #vasaku noolega liigub auto vasakule
        player_car_rect.move_ip(-5, 0)  #vasaku noole vajutusel liigub auto x telje suhtes vasakule
    if keys[
        pygame.K_RIGHT] and player_car_rect.right < WINDOW_WIDTH:  #parema noolega liigub auto paremale
        player_car_rect.move_ip(5, 0)  #parema noole vajutusel liigub auto x telje suhtes paremale

    for i, blue_car_rect in enumerate(blue_cars): #kasutab funktsiooni random siniste autode tekitamiseks
        blue_car_rect.move_ip(0, 5) #liigutab siniseid autosid allapoole
        if blue_car_rect.bottom >= WINDOW_HEIGHT: #kontrollib kas ükski sinistest autodes on alast väljas, kui jah siis spawnib uue alasse
            blue_car_rect.top = random.randint(-WINDOW_HEIGHT, 0)
            blue_car_rect.centerx = random.randint(0, WINDOW_WIDTH - CAR_WIDTH)
            score += 1
        if blue_car_rect.colliderect(player_car_rect): #kontrollib kas punane auto läheb mõnele sinisele autole vastu, kui jah siis mäng sulgub
            running = False
        blue_cars[i] = blue_car_rect #määrab sinise auto asukoha

    window.blit(background_image, (0, 0)) #määrab tausta
    window.blit(player_car_image, player_car_rect)  #määrab punase auto asukoha
    for blue_car_rect in blue_cars: #siniste autode tsükkel
        window.blit(blue_car_image, blue_car_rect) #tekitab sinise auto pildi ja kordinaadid
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))  # loob tekstiobjekti (font.render()) skoori näitamiseks.

    window.blit(score_text, (WINDOW_WIDTH / 2 -50, WINDOW_HEIGHT - 30)) #skoori asukoht ekraanil
    pygame.display.flip() #ekraani uuendamine

    clock.tick(60)  # määrame fpsiks 60


#tekitab kaotuse korral ekraanile punase kirja "Kaotasid!"
font = pygame.font.SysFont(None, 60)
text = font.render('Kaotasid!', True, (255, 0, 0))
text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
window.blit(text, text_rect)
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()