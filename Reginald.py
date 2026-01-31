import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()
print("Get Started!")

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reginald's Slurp Warp DEBUG MODE")
REGINALD_WIDTH = 50
REGINALD_HEIGHT = 60
# Load sound
slurp_sound = pygame.mixer.Sound("slurp.wav")

# Load flower images
flower1 = pygame.image.load("Flower_1.png").convert_alpha()
flower2 = pygame.image.load("Flower_2.png").convert_alpha()

# Load and scale smoothie image
smoothie_raw = pygame.image.load("smoothie.png").convert_alpha()
smoothie_image = pygame.transform.scale(smoothie_raw, (200, 200))
#Load background images
background_start = pygame.image.load("background_start.png").convert()
#Background 21
background_21 = pygame.image.load("background_21.png").convert()
bg12_raw = pygame.image.load("background_12.png").convert()
background_12 = pygame.transform.smoothscale(bg12_raw, (WIDTH, HEIGHT))



#LOAD REGINALD ANIMATION FRAMES
reginald_frames = {
    "down": [
        pygame.transform.scale(pygame.image.load("reginald_down_left.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT)),
        pygame.transform.scale(pygame.image.load("reginald_down_idle.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT)),
        pygame.transform.scale(pygame.image.load("reginald_down_right.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT))
    ],
    "up": [
        pygame.transform.scale(pygame.image.load("reginald_up_left.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT)),
        pygame.transform.scale(pygame.image.load("reginald_up_idle.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT)),
        pygame.transform.scale(pygame.image.load("reginald_up_right.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT))
    ],
    "left": [
        pygame.transform.scale(pygame.image.load("reginald_left_left.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT)),
        pygame.transform.scale(pygame.image.load("reginald_left_idle.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT)),
        pygame.transform.scale(pygame.image.load("reginald_left_right.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT))
    ],
    "right": [
        pygame.transform.scale(pygame.image.load("reginald_right_left.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT)),
        pygame.transform.scale(pygame.image.load("reginald_right_idle.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT)),
        pygame.transform.scale(pygame.image.load("reginald_right_right.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT))
    ]
}

#Bullet FRAMES (DISCO BALL)
bullet_frames = [
    pygame.transform.scale(pygame.image.load("disco1.png").convert_alpha(), (30,30)),
    pygame.transform.scale(pygame.image.load("disco2.png").convert_alpha(), (30,30)),
    pygame.transform.scale(pygame.image.load("disco3.png").convert_alpha(), (30,30)),
]
bullet_frame_count = len(bullet_frames)

#MoonWalking Frames
reginald_moonwalk_frames = {
    "down": [
        pygame.transform.scale(pygame.image.load("reginald_moonwalk_down_step_left.png").convert_alpha(),(REGINALD_WIDTH, REGINALD_HEIGHT)),
        pygame.transform.scale(pygame.image.load("reginald_moonwalk_down_idle.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT)),
        pygame.transform.scale(pygame.image.load("reginald_moonwalk_down_step_right.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT)),
        pygame.transform.scale(pygame.image.load("reginald_moonwalk_down_glide.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT)),
    ],
    "up": [
        pygame.transform.scale(pygame.image.load("reginald_moonwalk_up_step_left.png").convert_alpha(),(REGINALD_WIDTH, REGINALD_HEIGHT)),
        pygame.transform.scale(pygame.image.load("reginald_moonwalk_up_idle.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT)),
        pygame.transform.scale(pygame.image.load("reginald_moonwalk_up_step_right.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT)),
        pygame.transform.scale(pygame.image.load("reginald_moonwalk_up_glide.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT)),
    ],
    "left": [
        pygame.transform.scale(pygame.image.load("reginald_moonwalk_left_step_left.png").convert_alpha(),(REGINALD_WIDTH, REGINALD_HEIGHT)),
        pygame.transform.scale(pygame.image.load("reginald_moonwalk_left_idle.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT)),
        pygame.transform.scale(pygame.image.load("reginald_moonwalk_left_step_right.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT)),
        pygame.transform.scale(pygame.image.load("reginald_moonwalk_left_glide.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT)),
    ],
    "right": [
        pygame.transform.scale(pygame.image.load("reginald_moonwalk_right_step_left.png").convert_alpha(),(REGINALD_WIDTH, REGINALD_HEIGHT)),
        pygame.transform.scale(pygame.image.load("reginald_moonwalk_right_idle.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT)),
        pygame.transform.scale(pygame.image.load("reginald_moonwalk_right_step_right.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT)),
        pygame.transform.scale(pygame.image.load("reginald_moonwalk_right_glide.png").convert_alpha(), (REGINALD_WIDTH, REGINALD_HEIGHT)),
    ],
      
}
                                        ##ANIMATIONS
#Animation Timer
reginald_frame_index = 1
reginald_animation_timer = 0
reginald_animation_speed = 150  # adjust for moonwalk speed

#Animation Control
reginald_direction = "down"
reginald_frame_index = 1 # start at idle frame
reginald_animation_timer = 0
reginald_animation_speed = 150 # ms between frames
#candle frame pictures
candle_frame1 = pygame.image.load("candle1.png").convert_alpha()
candle_frame2 = pygame.image.load("candle2.png").convert_alpha()
candle_frames = [candle_frame1, candle_frame2]

#track animation frame of the candle 
candle_frame_index = 0
candle_animation_timer = 0
candle_animation_speed = 500  # milliseconds between frames
candle_positions = []

#candle frames scales individually
candle_frame1_scaled = pygame.transform.scale(candle_frame1, (150, 155))  # wider candle
candle_frame2_scaled = pygame.transform.scale(candle_frame2, (165, 125))  # thinner candle

candles = [
    {"pos": (WIDTH // 2 - 90, HEIGHT // 2 - 170), "frame1": candle_frame1_scaled, "frame2": candle_frame2_scaled},
    {"pos": (WIDTH // 2 + 10, HEIGHT // 2 - 170), "frame1": candle_frame1_scaled, "frame2": candle_frame2_scaled}
]

#Flower animation
# scale flowers
flower1_scaled = pygame.transform.scale(flower1, (120,120))
flower2_scaled = pygame.transform.scale(flower2, (130,110))

flower_frames = [flower1_scaled, flower2_scaled]
flower_frame_index = 0
flower_animation_timer = 0
flower_animation_speed = 500 # ms speed

#flower positions for room 2,1
flowers = [
    {"pos": (200,350)},
    {"pos": (500,400)},
]

# Small smoothie icon for the HUD
smoothie_icon = pygame.transform.scale(smoothie_raw, (150, 150))
#get a rect that matches the image
smoothie_rect = smoothie_image.get_rect()


# Mark what room that you are in 
# start in room 0
current_room_row = 2
current_room_col = 2
#What room the enemies are in and where they spawn
rooms = [
    [  # Row 0
        {"enemies": [[100, 100], [700, 400]]},  # (0,0)
        {"enemies": [[200, 150]]},              # (0,1)
        {"enemies": [[400, 300], [600, 350]]},   # (0,2)
        {"enemies": [[300, 200]]},              # (0,3)
        {"enemies": [[500, 500]]}               # (0,4)
    ],
    [  # Row 1
        {"enemies": [[150, 100], [650, 400]]},  # (1,0)
        {"enemies": [[250, 250]]},              # (1,1)
        {"enemies": [[400, 400]], "background" : background_12},              # (1,2) 
        {"enemies": [[350, 300], [450, 100]]},   # (1,3)
        {"enemies": [[600, 500]]}               # (1,4)
    ],
    [  # Row 2
        {"enemies": [[100, 500]]},              # (2,0)
        {"enemies": [[300, 300]], "background" : background_21},              # (2,1)
        {"enemies": [], "background": background_start},   # (2,2) START IN THIS ROOM
        {"enemies": [[200, 400]]},              # (2,3)
        {"enemies": [[700, 100]]}               # (2,4)
    ],
    [  # Row 3
        {"enemies": [[250, 150], [600, 350]]},   # (3,0)
        {"enemies": [[150, 450]]},              # (3,1)
        {"enemies": [[400, 200]]},              # (3,2)
        {"enemies": [[350, 500], [450, 300]]},   # (3,3)
        {"enemies": [[600, 150]]}               # (3,4)
    ],
    [  # Row 4
        {"enemies": [[100, 300], [700, 500]]},   # (4,0)
        {"enemies": [[300, 150]]},              # (4,1)
        {"enemies": [[500, 400]]},              # (4,2)
        {"enemies": [[250, 300], [650, 450]]},   # (4,3)
        {"enemies": [[400, 100]]}               # (4,4)
    ]
]

# Enemy setup
enemy_positions = [list(enemy) for enemy in rooms[current_room_row][current_room_col]["enemies"]]
#Draw enemies based on the current room
enemy_size = 40
enemy_speed = 2


# Bullet list
bullets = []
bullet_speed = 5
bullet_size = 5
bullet_cooldown = 300 #ms between shots
last_shot_time = 0



# Clock
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont("Arial", 50)
small_font = pygame.font.SysFont("Arial", 30)

#timer
smoothie_float_timer = 0

#Define the walls ======
wall_thickness = 20
door_width = 100
#top wall
top_wall = pygame.Rect(0,0, WIDTH, wall_thickness)
#Bottom Wall
bottom_wall = pygame.Rect(0, HEIGHT - wall_thickness, WIDTH, wall_thickness)
#Left wall
left_wall = pygame.Rect(0,0,wall_thickness,HEIGHT)
#Right wall
right_wall = pygame.Rect(WIDTH - wall_thickness, 0, wall_thickness, HEIGHT)
#=========================
#Door Openings =========
left_door = pygame.Rect(0, HEIGHT // 2 - door_width // 2, wall_thickness, door_width)
right_door = pygame.Rect(WIDTH - wall_thickness, HEIGHT // 2 - door_width // 2, wall_thickness, door_width)
top_door = pygame.Rect(WIDTH // 2 - door_width // 2, 0, door_width, wall_thickness)
bottom_door = pygame.Rect(WIDTH // 2 - door_width // 2, HEIGHT - wall_thickness, door_width, wall_thickness)
#========================

# Function to generate random smoothie position
def random_smoothie_position():
    # Random spawn position
    x = random.randint(0, WIDTH - 200)
    y = random.randint(0, HEIGHT - 200)

    # Big visual smoothie stays at (x, y)
    smoothie_visual_pos = (x, y)

    # Small hitbox (like 60x60)
    smoothie_hitbox = pygame.Rect(
        x + 70,  # center the hitbox inside the image
        y + 70,
        60,
        60
    )
    return smoothie_visual_pos, smoothie_hitbox

    

# Reginald setup
player_pos = [100, 100]
player_size = REGINALD_WIDTH
player_color = (0, 255, 0)
player_speed = 3
facing_dir = [0,1] # [x,y]
#Warp Setup
warp_distance = 130
warp_cooldown = 1000
last_warp_time = 0

# Smoothie setup
smoothie_visual_pos, smoothie_hitbox = random_smoothie_position()
smoothie_active = False
smoothie_duration = 5000  # ms warp time active
smoothie_start_time = 0
smoothie_respawn_delay = 10000  # ms before new smoothie appears
smoothie_disappeared_time = 0

# Poof effect
poofs = []
poof_duration = 300  # ms

# Game state
game_state = "menu"

#minimap setup
minimap_size = 150 #Total size in pixels
minimap_pos = (WIDTH - minimap_size - 20, 20) #Top right corner with some margin
grid_size = 5 #5x5 grid
cell_size = minimap_size // grid_size #size of each room on the minimap


# Game loop
while True:
    current_time = pygame.time.get_ticks()
    smoothie_float_timer += 0.05

    current_background = rooms[current_room_row][current_room_col]["background"]
    screen.blit(current_background, (0,0))  # Clear background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if game_state == "menu":
        title = font.render("Reginald's Slurp Warp", True, (0, 255, 0))
        instruction = small_font.render("Press ENTER to Slurp", True, (255, 255, 255))
        screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//3))
        screen.blit(instruction, (WIDTH//2 - instruction.get_width()//2, HEIGHT//2))

        if keys[pygame.K_RETURN]:
            print("switching to playing mode!")
            game_state = "playing"
            player_pos = [(WIDTH // 2) - 20, (HEIGHT // 2) - 35]
            last_warp_time = 0
            smoothie_active = False
            smoothie_visual_pos, smoothie_hitbox = random_smoothie_position()

            #candle animation setup here
            candle_frame_index = 0
            candle_animation_timer = 0
            candle_positions = [(WIDTH//2 - 60, HEIGHT //2 - 140), 
                                (WIDTH//2 + 40,HEIGHT // 2 - 140)
                                ]


    elif game_state == "playing":
        moving_x = 0
        moving_y = 0
        is_moonwalking = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
        # Player Movement (Reginald)
        if keys[pygame.K_LEFT]:
            player_pos[0] -= player_speed
            moving_x = -1
        if keys[pygame.K_RIGHT]:
            player_pos[0] += player_speed
            moving_x = 1
        if keys[pygame.K_UP]:
            player_pos[1] -= player_speed
            moving_y = -1
        if keys[pygame.K_DOWN]:
            player_pos[1] += player_speed
            moving_y = 1
        #if moving, update facing direction
        if moving_x != 0 or moving_y != 0:
            facing_dir = [moving_x, moving_y]

        player_rect = pygame.Rect(*player_pos, player_size, player_size)
        # Detect shift key
        # Detect moonwalk mode
        
        # Determine visual facing direction (for sprite)
        if moving_x < 0:
            reginald_direction = "right" if is_moonwalking else "left"
        elif moving_x > 0:
            reginald_direction = "left" if is_moonwalking else "right"
        elif moving_y < 0:
            reginald_direction = "down" if is_moonwalking else "up"
        elif moving_y > 0:
            reginald_direction = "up" if is_moonwalking else "down"

        # Animate only when moving
        if moving_x != 0 or moving_y != 0:
            reginald_animation_timer += clock.get_time()
            if reginald_animation_timer >= reginald_animation_speed:
                reginald_animation_timer = 0
                reginald_frame_index = (reginald_frame_index + 1) % 4  # 4 moonwalk frames
        else:
            reginald_frame_index = 1  # idle frame

        if  (player_rect.colliderect(top_wall) and not player_rect.colliderect(top_door)) or \
            (player_rect.colliderect(bottom_wall) and not player_rect.colliderect(bottom_door)) or \
            (player_rect.colliderect(left_wall) and not player_rect.colliderect(left_door)) or \
            (player_rect.colliderect(right_wall) and not player_rect.colliderect(right_door)):
            # Undo movement
            player_pos[0] -= moving_x * player_speed
            player_pos[1] -= moving_y * player_speed



        



        # === Door Logic with Boundaries ===
        if player_pos[0] < 0:  # Left Door
            if current_room_col > 0:
                current_room_col -= 1
                player_pos[0] = WIDTH - player_size
                enemy_positions = [list(enemy) for enemy in rooms[current_room_row][current_room_col]["enemies"]]
            else:
                player_pos[0] = 0  # Stop at wall

        if player_pos[0] > WIDTH - player_size:  # Right Door
            if current_room_col < grid_size - 1:
                current_room_col += 1
                player_pos[0] = 0
                enemy_positions = [list(enemy) for enemy in rooms[current_room_row][current_room_col]["enemies"]]
            else:
                player_pos[0] = WIDTH - player_size

        if player_pos[1] < 0:  # Up Door
            if current_room_row > 0:
                current_room_row -= 1
                player_pos[1] = HEIGHT - player_size
                enemy_positions = [list(enemy) for enemy in rooms[current_room_row][current_room_col]["enemies"]]
            else:
                player_pos[1] = 0

        if player_pos[1] > HEIGHT - player_size:  # Down Door
            if current_room_row < grid_size - 1:
                current_room_row += 1
                player_pos[1] = 0
                enemy_positions = [list(enemy) for enemy in rooms[current_room_row][current_room_col]["enemies"]]
            else:
                player_pos[1] = HEIGHT - player_size


        # Move enemy toward player
        for enemy in enemy_positions:
        
            if enemy[0] < player_pos[0]:
                enemy[0] += enemy_speed
            elif enemy[0] > player_pos[0]:
                enemy[0] -= enemy_speed

            if enemy[1] < player_pos[1]:
                enemy[1] += enemy_speed
            elif enemy[1] > player_pos[1]:
                enemy[1] -= enemy_speed

        #Shooting Bullets
        if keys[pygame.K_z] and (current_time - last_shot_time) > bullet_cooldown:
            dx, dy = facing_dir
            if dx != 0 and dy != 0:
                dx *= 0.7071
                dy *= 0.7071
            bullets.append([
                player_pos[0] + player_size // 2, 
                player_pos[1] + player_size // 2,
                facing_dir[0],
                facing_dir[1],
                0,  # Start at frame 0
                current_time
            ])
            last_shot_time = current_time

        bullet_animation_speed = 300
            
        # Update and check bullets
        for bullet in bullets[:]:  # [:] means safely editing the list while looping
            bullet[0] += bullet[2] * bullet_speed # x + dx * speed
            bullet[1] += bullet[3] * bullet_speed # Move bullet up


            # Check if it's time to advance the frame
            if current_time - bullet[5] >= bullet_animation_speed:
                bullet[4] = (bullet[4] + 1) % bullet_frame_count
                bullet[5] = current_time  # reset last frame time

            # Draw the current frame
            frame = bullet_frames[bullet[4]]
            screen.blit(frame, (bullet[0], bullet[1]))

            

            # Bullet offscreen
            if bullet[1] < 0 or bullet[0] > WIDTH or bullet[1] < 0 or bullet[1] > HEIGHT:
                bullets.remove(bullet)
                continue  # Skip rest of loop for this bullet

            bullet_rect = pygame.Rect(bullet[0], bullet[1], bullet_size, bullet_size)

            # Check if Bullet hits each enemy
            for enemy in enemy_positions[:]:
                enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_size, enemy_size)
                if bullet_rect.colliderect(enemy_rect):
                    enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_size, enemy_size)
                    bullets.remove(bullet)
                    enemy_positions.remove(enemy)
                    break #break after hit to aviod it from crashing


        # Smoothie pickup
        if smoothie_hitbox and player_rect.colliderect(smoothie_hitbox):
            smoothie_active = True
            smoothie_start_time = current_time
            smoothie_disappeared_time = current_time
            smoothie_hitbox = None
            smoothie_visual_pos = None


        # Warp only if smoothie active
        if smoothie_active and keys[pygame.K_SPACE] and current_time - last_warp_time > warp_cooldown:
            if keys[pygame.K_LEFT]:
                player_pos[0] -= warp_distance
            elif keys[pygame.K_RIGHT]:
                player_pos[0] += warp_distance
            elif keys[pygame.K_UP]:
                player_pos[1] -= warp_distance
            elif keys[pygame.K_DOWN]:
                player_pos[1] += warp_distance

            slurp_sound.play()
            last_warp_time = current_time
            poofs.append({"pos": player_pos.copy(), "start": current_time})

        candle_animation_timer += clock.get_time()

        if candle_animation_timer > candle_animation_speed:
            candle_animation_timer = 0  
            candle_frame_index = (candle_frame_index + 1) % len(candle_frames)
        
        #Draw candle animation
        for candle in candles:
            if candle_frame_index == 0:
                frame = candle["frame1"]
            else:
                frame = candle["frame2"]
            screen.blit(frame, candle["pos"])
            
        if current_room_row == 2 and current_room_col == 1:
            flower_animation_timer += clock.get_time()
            if flower_animation_timer > flower_animation_speed:
                flower_animation_timer = 0
                flower_frame_index = (flower_frame_index + 1) % len(flower_frames)
            #draw flowers
            for flower in flowers:
                frame = flower_frames[flower_frame_index]
                screen.blit(frame, flower["pos"])

        # End warp after smoothie duration
        if smoothie_active and current_time - smoothie_start_time > smoothie_duration:
            smoothie_active = False

        # Respawn smoothie after delay
        if smoothie_hitbox is None and current_time - smoothie_disappeared_time > smoothie_respawn_delay:
            smoothie_visual_pos, smoothie_hitbox = random_smoothie_position()
        

        # Draw smoothie
        if smoothie_hitbox:
            float_offset = math.sin(smoothie_float_timer) * 10
            screen.blit(smoothie_image, (smoothie_visual_pos[0], smoothie_visual_pos[1] + float_offset))

        
        # Draw player
        if is_moonwalking:
            reginald_current_frame = reginald_moonwalk_frames[reginald_direction][reginald_frame_index]
        else:
            reginald_current_frame = reginald_frames[reginald_direction][reginald_frame_index % 3]
        screen.blit(reginald_current_frame, player_pos)

        
        # Draw enemy
        for enemy in enemy_positions:
            pygame.draw.rect(screen, (255, 0, 0), (enemy[0], enemy[1], enemy_size, enemy_size))

        # Draw bullets
        for bullet in bullets:
            pygame.draw.rect(screen, (255, 255, 0), (bullet[0], bullet[1], bullet_size, bullet_size))
        
        #Draw Walls
        pygame.draw.rect(screen, (100,100,100), top_wall)
        pygame.draw.rect(screen, (100,100,100), bottom_wall)
        pygame.draw.rect(screen, (100,100,100), left_wall)
        pygame.draw.rect(screen, (100,100,100), right_wall)

        #DRAW DOORS
        pygame.draw.rect(screen, (200,100,100), top_door)
        pygame.draw.rect(screen, (200,100,100), bottom_door)
        pygame.draw.rect(screen, (200,100,100), left_door)
        pygame.draw.rect(screen, (200,100,100), right_door)

        #BLOCK OFF DOORS THAT LEAD OUTSIDE
        if current_room_row == 0:
            pygame.draw.rect(screen, (100, 100, 100), top_door)  # Wall over top door
        if current_room_row == grid_size - 1:
            pygame.draw.rect(screen, (100, 100, 100), bottom_door)  # Wall over bottom door
        if current_room_col == 0:
            pygame.draw.rect(screen, (100, 100, 100), left_door)  # Wall over left door
        if current_room_col == grid_size - 1:
            pygame.draw.rect(screen, (100, 100, 100), right_door)  # Wall over right door


        # ===Draw Minimap===
        for row in range(grid_size):
            for col in range(grid_size):
                rect_x = minimap_pos[0] + col * cell_size
                rect_y = minimap_pos[1] + row * cell_size
                room_rect = pygame.Rect(rect_x, rect_y, cell_size - 2, cell_size - 2) #Slight margin between rooms

                #draw regular room
                pygame.draw.rect(screen, (80,80,80), room_rect)
            
        #highlight current room
        current_room_rect = pygame.Rect(
            minimap_pos[0] + current_room_col * cell_size,
            minimap_pos[1] + current_room_row * cell_size,
            cell_size - 2,
            cell_size - 2
        )
        pygame.draw.rect(screen, (0, 255, 0), current_room_rect)  # Green = Reginald's room




        if smoothie_active:
            icon_x = 20
            icon_y = 20
            # == Pulse Effect ==
            pulse_scale = 1 + 0.1 * math.sin(smoothie_float_timer * 2) #Pulses just a little bit faster
            pulse_size = int(150 * pulse_scale)
            # Center the pulsing icon
            smoothie_icon_scaled = pygame.transform.scale(smoothie_icon, (pulse_size, pulse_size))
            smoothie_icon_rect = smoothie_icon_scaled.get_rect(center=(icon_x + 32, icon_y + 43))
            #Draw pulsing smoothie icon
            screen.blit(smoothie_icon_scaled, smoothie_icon_rect.topleft)
            #calculate remaining time
            time_passed = current_time - smoothie_start_time
            ratio = max(0, 1 - (time_passed / smoothie_duration))
            #Draw the background circle (gray)
            arc_rect = pygame.Rect(icon_x - 5, icon_y - 5, 60, 60)
            pygame.draw.circle(screen, (80,80,80), arc_rect.center, 30, 5)
            #draw the shrinking arc (cyan)
            if ratio > 0:
                pygame.draw.arc(screen, (0, 255, 255), arc_rect, 0, ratio * 2 * math.pi, 5)
        

        
        # Draw cooldown bar
        cooldown_ratio = min((current_time - last_warp_time) / warp_cooldown, 1)
        bar_x = player_pos[0]
        bar_y = player_pos[1] - 10
        pygame.draw.rect(screen, (80, 80, 80), (bar_x, bar_y, player_size, 5))
        pygame.draw.rect(screen, (0, 255, 255), (bar_x, bar_y, player_size * cooldown_ratio, 5))

        # Draw poof effects
        for poof in poofs[:]:
            elapsed = current_time - poof["start"]
            if elapsed > poof_duration:
                poofs.remove(poof)
                continue
            alpha = 255 - int((elapsed / poof_duration) * 255)
            radius = 30 - int((elapsed / poof_duration) * 25)
            surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(surface, (0, 255, 255, alpha), (radius, radius), radius)
            screen.blit(surface, (poof["pos"][0] + player_size // 2 - radius, poof["pos"][1] + player_size // 2 - radius))
        

    pygame.display.flip()
    clock.tick(60)
