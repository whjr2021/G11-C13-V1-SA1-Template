# Import "pygame", "time" and "random" modules 
import pygame
import time
import random

# Initialize "pygame"
pygame.init() 

# Define image loading function here. Name it as "image_load"
def image_load(location, width, height, x, y):
    img = pygame.image.load(location).convert_alpha()
    img_scaled = pygame.transform.smoothscale(img,(width, height))
    screen.blit(img_scaled,(x,y))
    return img_scaled

# Define a function to display text. Name it as "text_display"
def text_display(size,text,r,g,b,x,y):
    font = pygame.font.Font(None, size)
    text = font.render(text, 1, (r,g,b))
    screen.blit(text, (x,y))

# Student Activity 1-Step 1: Define a function to return obstacle location. Name it as "obs_location"
# 1. Inside function find random x ("stone_x" variable) and y ("stone_y" variable) locations for stone placement where, 
#    stone_x = random.randint(100, carx+100) and stone_y = random.randint(100, cary-100)
# 2. The function must return stone_x, stone_y values. Use 'return' keyword to return function outputs seperated by comma.





# Create a game screen and set its title 
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Car Racing Game")

# Create a "carx", "cary" and "bgy" variables to track car and background positions
carx = 140
cary = 450
bgy = 0

# Create a variable "threshold" and set its value to zero
threshold = 0

# Create a counter variable to keep track of gameloop iterations
counter = 0

# Student Activity 2- Step 2: Call the function obs_location() and store the results in "stone_x" and "stone_y"
stone_x, stone_y = obs_location()

# Create a "red_carx" set to 305, "red_cary" set to 200 to track red car position. 
red_carx = 305
red_cary = 200

# Game loop
carryOn = True
# Create first time point "t1" 
t1 = time.time()
while carryOn:
    # NOTE: The images file and .py file in which image is being used must be in same folder
    
    # Call the function "image_load()" 
    image_load("road.png", 650, 600, 0, 0)
    yellow_car_scaled = image_load("yellow_car.png", 230, 140, carx, cary)
    stone_scaled = image_load("stone.png", 70, 60, stone_x, stone_y)
    red_car_scaled = image_load("red_car.png", 80,130, red_carx, red_cary)
    
    # Check for up, down, left, right, spacebar and enter key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False              
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                cary -= 10
                bgy -= 10
            if event.key == pygame.K_DOWN:
                cary += 10
                bgy += 10
            if event.key==pygame.K_RIGHT:
                if carx <= 320:
                    carx += 10
            if event.key==pygame.K_LEFT:
                if carx >= 50:                          
                    carx -= 10 
            if event.key == pygame.K_SPACE:
                if carx < 260: 
                    carx += 90
            if event.key == pygame.K_RETURN:
                if game_time >= threshold and game_time <= (threshold+10):
                    cary -= 50 
                    threshold += 10
                
    # Reset car and background positions
    if cary <= 30:
        bgy = 0
        cary = 450
        counter += 1 
        # Student Activity 2- Step 2: 
        # Call the function obs_location() and store the result in "stone_x" and "stone_y"

        
    # Create rectangle for car and stone
    yellow_car_rect = yellow_car_scaled.get_rect(topleft = (carx+75,cary))
    yellow_car_rect.width = yellow_car_rect.width/3
    stone_rect = stone_scaled.get_rect(topleft = (stone_x, stone_y))
    # Draw rectangles for car and stone
    pygame.draw.rect(screen,(100,0,100),yellow_car_rect)
    pygame.draw.rect(screen,(0,0,100),stone_rect)
    # Get rectangle for red car
    red_car_rect = red_car_scaled.get_rect(topleft = (red_carx,red_cary))
    pygame.draw.rect(screen,(23,0,250),red_car_rect)
    
    # If car and stone rectangles collide, change yellow car and stone positions
    if yellow_car_rect.collidepoint(stone_rect.x,stone_rect.y):
        cary = 450
        # Student Activity 2- Step 3: 
        # Call the function obs_location() and store the result in "stone_x" and "stone_y"

    
    # If the two cars collide, change car positions 
    if yellow_car_rect.collidepoint(red_car_rect.x,red_car_rect.y):
        carx = 140
        cary = 450
        red_cary = 450
        
    # Display yellow car image upon updating "carx" and "cary" variable values
    screen.blit(yellow_car_scaled,(carx, cary))
    
    # Display the stone upon updating "stone_x" and "stone_y" variable values  
    screen.blit(stone_scaled,(stone_x, stone_y))
    
    # Display red car image upon updating "red_carx" and "red_cary" variable values
    screen.blit(red_car_scaled,(red_carx, red_cary))
    
    # Create second time point "t2" 
    t2 = time.time()
    game_time = t2-t1
    game_time = round(game_time, 2)
    
    # Display game time elapsed
    text_display(35,"TIME ELAPSED: " + str(game_time)+ "seconds",0, 255,255,130,15)
    
    # Display finish line after 5 iterations of game loop
    # Check if "counter" is equal to 5
    if counter == 5:
        # Create and draw the finish line white-colored rectangle at (x,y)=(95, 40) with width=400 and height=30
        finish_line = pygame.Rect(95,40,400,30)
        pygame.draw.rect(screen,(255,255,255),finish_line)
        text_display(40, "----------FINISH----------", 255,0,0,160,45)
        pygame.display.flip()
        
        # End the game loop after displaying finish line
        pygame.time.wait(3000)
        screen.fill((0,100,200))        
        text_display(40,"Finish time: " + str(round(game_time,2))+ " seconds",255,255,255,140,200)       
        text_display(40,"Game Over, Good Luck Next Time!",255,255,255,80,250)       
        pygame.display.flip()
        pygame.time.wait(5000)
        # Break out of 'while' game loop
        break
    
    # Update the contents of the display
    pygame.display.flip()
    
# On the occurence of "pygame.QUIT" event close the game screen.
pygame.quit()