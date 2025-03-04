import pygame as pg
import random as ran

if not pg.get_init():
    pg.init()

ball_x_speed = ran.randint(8,11)
ball_y_speed = ran.randint(8,11)
left_score = 0
right_score = 0
width = 1000
height = 650
window = pg.display.set_mode((width, height))
clock = pg.time.Clock()
ball_rect = pg.Rect(100,100,35,35)
back = pg.transform.scale(pg.image.load('back.png'),(1000,700))
font = pg.font.Font('comic.ttf',30)
fon = pg.font.Font('comic.ttf',20)
fonts = pg.font.Font('comic.ttf',60)
WINNER = None
#variables


game_on = True
ball_x =1000/2-25
ball_y = 650/2-25
white = (255,255,255)
black = (0,0,(0.4/1)*255)
rect_dimensions = (30,120)


text = fon.render('Press esc to end ',True,white)
left_player_x = 5
left_player_y = 0

right_player_x = 1000-35
right_player_y = 0
left_rect = pg.rect.Rect(((left_player_x,left_player_y),(rect_dimensions)))
right_rect = pg.rect.Rect(((right_player_x,right_player_y),(rect_dimensions)))

#create a looop

while game_on is True:
    
    left_score_text = font.render('Score :  '+ str(left_score),True,(0,0,0))
    right_score_text = font.render('Score :  '+ str(right_score),True,(0,0,0))
    window.blit(back,(0,0))
    border =  pg.draw.rect(window,(0,0,0),((1000/2-15,0),(30,650)), 0, border_radius=15)
    #render visuals
    window.blit(text,(10,600))
    window.blit(left_score_text,(100,20))
    window.blit(right_score_text,(width - right_score_text.get_width()-100,20))
    

    win_text = fonts.render( str(WINNER) + '  WINS',True,white)
    if left_score > right_score:
        WINNER = 'LEFT PLAYER'
    if left_score < right_score:
        WINNER = 'RIGHT PLAYER'
    if left_score == right_score:
        WINNER = 'NO ONE'
        
    for event in pg.event.get():
        if event.type == pg.QUIT:
            window.blit(win_text,(10,600))
            pg.time.delay(2000)
            game_on = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                window.blit(win_text,(1000/2-win_text.get_width()/2,650/2-win_text.get_height()/2))
                pg.time.delay(2000)
                game_on = False
        #make player motion
            
    keystate = pg.key.get_pressed()
    if keystate[pg.K_UP] :
        right_rect.y -= 15
    if keystate[pg.K_DOWN] :
         right_rect.y += 15
    if keystate[pg.K_w] :
        left_rect.y -= 15
    if keystate[pg.K_s] :
        left_rect.y += 15
     #make plr rects
    left_player =  pg.draw.rect(window,black,left_rect, 0, border_radius=15)
    right_player =  pg.draw.rect(window,black,right_rect, 0, border_radius=15)
    
    #create eviron
    
     #motion restrictions
    if left_rect.y < -3:
        left_rect.y = -3
    if (left_rect.y + 120) > 653:
        left_rect.y = 653 -120

    if right_rect.y < -3:
        right_rect.y = -3
    if (right_rect.y + 120) > 653:
        right_rect.y = 653 -120

    ball_rect.x += ball_x_speed
    ball_rect.y += ball_y_speed

    if ball_rect.left <= 0 or ball_rect.right >= width:
        ball_x_speed *= -1
    
    if ball_rect.top <= 0 or ball_rect.bottom >= height:
        ball_y_speed *= -1
    if ball_rect.left <= 0:
        right_score += 1
        
    if ball_rect.right >= 1000:
        left_score += 1
    if left_rect.colliderect(ball_rect):
        ball_x_speed *= -1
        ball_y_speed *= -1
    if right_rect.colliderect(ball_rect):
        ball_x_speed *= -1
        ball_y_speed *= -1
    
        
    pg.draw.ellipse(window,(255,255,255),ball_rect)
    pg.display.update()
    clock.tick(60)    
pg.quit()
