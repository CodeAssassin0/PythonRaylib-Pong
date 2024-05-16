from pyray import *
import random

width = 800
height = 600

didStartGame = False

init_window(width, height, "PONG")

scorePaddle1 = 0
scorePaddle2 = 0

paddle1X = 40
paddle1Y = height/2
paddle1Rec = Rectangle(int(paddle1X), int(paddle1Y), 20, 80)
paddle1CollisionRec = Rectangle(int(paddle1X + 15), int(paddle1Y), 5, 80)

paddle2X = width - 60
paddle2Y = height/2
paddle2Rec = Rectangle(int(paddle2X), int(paddle2Y), 20, 80)
paddle2CollisionRec = Rectangle(int(paddle2X - 5), int(paddle2Y), 5, 80)

paddleVelocity = -1.15

ballX = width/2
ballY = height/2
ballVelocityX = 0.5
ballVelocityY = 0.5
ballVelocityList = [-0.5, 0.5]
ballRec = Rectangle(int(ballX), int(ballY), 10, 10)

while(not window_should_close()):
    paddle1Rec = Rectangle(int(paddle1X), int(paddle1Y), 20, 80)
    paddle2Rec = Rectangle(int(paddle2X), int(paddle2Y), 20, 80)
    ballRec = Rectangle(int(ballX), int(ballY), 10, 10)
    paddle1CollisionRec = Rectangle(int(paddle1X + 25), int(paddle1Y), 5, 80)
    paddle2CollisionRec = Rectangle(int(paddle2X - 5), int(paddle2Y), 5, 80)

    begin_drawing()
    clear_background(BLACK)

    if (didStartGame):
        draw_rectangle(int(paddle1Rec.x), int(paddle1Rec.y), int(paddle1Rec.width), int(paddle1Rec.height), WHITE)
        draw_rectangle(int(paddle2Rec.x), int(paddle2Rec.y), int(paddle2Rec.width), int(paddle2Rec.height), WHITE)
        draw_circle(int(ballX - 5), int(ballY - 5), 10, WHITE)
        draw_text(str(scorePaddle1), int(width/2 - 100), 20, 20, WHITE)
        draw_text(str(scorePaddle2), int(width/2 + 100), 20, 20, WHITE)

        ballY += ballVelocityY
        ballX += ballVelocityX

        if (ballY >= height):
            ballVelocityY *= -1
        if (ballY <= 0):
            ballVelocityY *= -1

        if (is_key_down(KeyboardKey.KEY_W)):
            paddle1Y += paddleVelocity
        
        if (is_key_down(KeyboardKey.KEY_S)):
            paddle1Y -= paddleVelocity
        
        if (is_key_down(KeyboardKey.KEY_UP)):
            paddle2Y += paddleVelocity

        if (is_key_down(KeyboardKey.KEY_DOWN)):
            paddle2Y -= paddleVelocity
        
        if(ballX < paddle1CollisionRec.x + paddle1CollisionRec.width and ballY < paddle1CollisionRec.y + paddle1CollisionRec.height and ballY > paddle1CollisionRec.y and ballX > paddle1CollisionRec.x):
            ballVelocityX *= -1

        if(ballX > paddle2CollisionRec.x and ballY < paddle2CollisionRec.y + paddle2CollisionRec.height and ballY > paddle2CollisionRec.y and ballX < paddle2CollisionRec.x + paddle2CollisionRec.width):
            ballVelocityX *= -1

        if(ballX > paddle2X + 20):
            scorePaddle1 += 1
            ballX = width/2
            ballY = height/2
            ballVelocityX = random.choice(ballVelocityList)
            ballVelocityY = random.choice(ballVelocityList)
        if(ballX < paddle1X):
            scorePaddle2 += 1
            ballX = width/2
            ballY = height/2
            ballVelocityX = random.choice(ballVelocityList)
            ballVelocityY = random.choice(ballVelocityList)

        if (scorePaddle1 == 5):
            draw_text("Player 1 Won", int(width/2 - 150), int(height/2), 35, WHITE)
            draw_text("Press r to Restart", int(width/2 - 150), int(height/2 + 100), 20, WHITE)
            ballX = width/2
            ballY = 60
            ballVelocityX = 0
            ballVelocityY = 0
            if (is_key_pressed(KeyboardKey.KEY_R)):
                scorePaddle1 = 0
                scorePaddle2 = 0
                ballX = width/2
                ballY = height/2
                ballVelocityX = random.choice(ballVelocityList)
                ballVelocityY = random.choice(ballVelocityList)
        
        if (scorePaddle2 == 5):
            draw_text("Player 2 Won", int(width/2 - 150), int(height/2), 35, WHITE)
            draw_text("Press r to Restart", int(width/2 - 150), int(height/2 + 100), 20, WHITE)
            ballX = width/2
            ballY = 60
            ballVelocityX = 0
            ballVelocityY = 0
            if (is_key_pressed(KeyboardKey.KEY_R)):
                scorePaddle1 = 0
                scorePaddle2 = 0
                ballX = width/2
                ballY = height/2
                ballVelocityX = random.choice(ballVelocityList)
                ballVelocityY = random.choice(ballVelocityList)

    else:
        draw_text("Press S to Start", int(width/2 - 150), int(height/2), 40, WHITE)
        if (is_key_pressed(KeyboardKey.KEY_S)):
            didStartGame = True

    end_drawing()

close_window()