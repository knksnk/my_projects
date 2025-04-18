animation_index = 0
animation_counter = 0

def main():
    import sys
    import random
    import math
    import time
    from PIL import Image, ImageEnhance, ImageOps
    from random import choice   
    
    pygame.init()
    
    tile_width, tile_height = 40, 40
    tiles_x, tiles_y = 50, 37
    floor_width = tile_width * tiles_x
    floor_height = tile_height * tiles_y
    floor_surface = pygame.Surface((floor_width, floor_height))
    backgrey_images = [pygame.image.load(f'backgrey{i}.png') for i in range(1, 11)]
    backgrey_images = [pygame.transform.scale(img, (tile_width, tile_height)) for img in backgrey_images]
    
    for y in range(tiles_y):
        for x in range(tiles_x):
            tile_image = choice(backgrey_images)
            floor_surface.blit(tile_image, (x * tile_width, y * tile_height))
    
    pygame.image.save(floor_surface, 'floor.png')
    
    wall_images = [pygame.image.load(f'wall{i}.png') for i in range(1, 7)]
    wall_images = [pygame.transform.scale(img, (tile_width, tile_height)) for img in wall_images]
    wall = pygame.Surface((floor_width, floor_height))
    for y in range(tiles_y):
        for x in range(tiles_x):
            tile_image = choice(wall_images)
            wall.blit(tile_image, (x * tile_width, y * tile_height))
    
    pygame.image.save(wall, 'wall.png')
    
    def filterr(image, name, r, g, b, a):
        fil = Image.new("RGBA", image.size, (r, g, b, 50))
        filtered_image = Image.alpha_composite(image, fil)
        filtered_image.save(name+".png")
        
    image1 = Image.open("wall.png").convert("RGBA")
    image2 = Image.open("floor.png").convert("RGBA")
    

    def adjust_brightness_contrast(image, brightness_factor=random.uniform(0.2, 0.9), contrast_factor=0.5):
        enhancer_brightness = ImageEnhance.Brightness(image)
        image = enhancer_brightness.enhance(brightness_factor)
        enhancer_contrast = ImageEnhance.Contrast(image)
        image = enhancer_contrast.enhance(contrast_factor)
        return image
    
    image = Image.open("floor.png")
    final_image = adjust_brightness_contrast(image)
    final_image.save("floor.png")
    
    image = Image.open("wall.png")
    final_image = adjust_brightness_contrast(image)
    final_image.save("wall.png")
    
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    GRAY = (128, 128, 128)
    DARK_BLUE = (0, 0, 230)
    LIGHT_BLUE = (140, 150, 160)
    LIGHT_BROWN = (210, 180, 140)
    LIGHT_BLUE = (173, 216, 230)
    DARK_GREEN = (0, 100, 0)    
    
    hero_images = [pygame.image.load(f'hero{i}.png') for i in range(1, 4)]  # Загружаем изображения игрока
    hero_images = [pygame.transform.scale(img, (img.get_width() // 2, img.get_height() // 2)) for img in hero_images]
    
    animation_speed = 0.3
    
    player_x, player_y = 0, 0
    camera_x, camera_y = 0, 0
    tile_size = 50
    room_min_size = 6
    room_max_size = 10
    num_rooms = 6
    corridor_width = 100
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    MAP_WIDTH, MAP_HEIGHT = 2000, 1500
    player_width, player_height = 25, 25
    player_speed = 3
    barrier_offset = 0
    barrier_width = player_width + barrier_offset * 2
    barrier_height = player_height + barrier_offset * 2

    portal_images = [pygame.image.load(f"portal{i}.png") for i in range(1, 5)]
    for i in range(4):
        portal_images[i] = pygame.transform.scale(portal_images[i], (60, 80))
        
    
    class Portal:
        def __init__(self, portal_images):
            self.portal_images = portal_images
            self.portal_rect = None
            self.frame_index = 0
            self.animation_timer = 0
            self.portal_active = False
            self.fl = True
            self.portal_spawn_time = 0
            self.portal_duration = 5 
    
        def spawn_portal(self, player_x, player_y):
            self.portal_rect = pygame.Rect(player_x, player_y, 60, 50)
            self.portal_active = True
            self.portal_spawn_time = time.time()
    
        def update(self):
            if self.portal_active:
                current_time = time.time()
                if current_time - self.portal_spawn_time > self.portal_duration:
                    self.portal_active = False
                    self.restart_game()
                else:
                    self.animation_timer += 1
                    if self.animation_timer % 10 == 0:
                        self.frame_index = (self.frame_index + 1) % len(self.portal_images)
    
        def draw(self, screen, camera_x, camera_y):
            if self.portal_active:
                current_portal_image = self.portal_images[self.frame_index]
                screen.blit(current_portal_image, (self.portal_rect.x - camera_x, self.portal_rect.y - camera_y))
    
        def restart_game(self):
            screen.fill((0, 0, 0))
            pygame.display.update()
            time.sleep(2)
        
    
            main()


    portal = Portal(portal_images)
    
    
    class Money:
        def __init__(self):
            if (portal.fl):
                self.coins = 0
    
        def add_coins(self, amount):
            self.coins += amount
    
        def draw(self, surface):
            pygame.draw.circle(surface, (255, 165, 0), (30, 120), 15)
            pygame.draw.circle(surface, (255, 255, 0), (30, 120), 10)
    
            font = pygame.font.Font(None, 24)
            text = font.render(str(self.coins), True, (255, 255, 255))
            surface.blit(text, (50, 112)) 
    

    class Health:
        def __init__(self):
            self.max_health = 6 
            self.current_health = self.max_health
    
        def decrease_health(self, amount):
            if self.current_health > 6:
                self.current_health = 6
            self.current_health = max(0, self.current_health - amount)
            
        def draw(self, surface):
            pygame.draw.rect(surface, (255, 0, 0), (10, 10, 180, 15)) 
            pygame.draw.rect(surface, (0, 255, 0), (10, 10, (180 * self.current_health / self.max_health), 15)) 
            font = pygame.font.Font(None, 24)
            text = font.render(f'{self.current_health}/{self.max_health}', True, (0, 0, 0)) 
            surface.blit(text, (195, 10))
        
    
    class Shield:
        def __init__(self):
            self.max_shield = 4
            self.current_shield = self.max_shield
            self.recharge_interval = 30000 
            self.last_recharge_time = pygame.time.get_ticks() 
    
        def decrease_shield(self, amount):
            self.current_shield = max(0, self.current_shield - amount) 
    
        def recharge_shield(self):
            current_time = pygame.time.get_ticks()
            if current_time - self.last_recharge_time >= self.recharge_interval:
                if self.current_shield < self.max_shield:
                    self.current_shield = min(self.max_shield, round(self.current_shield + 1, 1))
                self.last_recharge_time = current_time
    
        def draw(self, surface):
            pygame.draw.rect(surface, (105, 105, 105), (10, 35, 180, 15))
            pygame.draw.rect(surface, (0, 255, 255), (10, 35, (180 * self.current_shield / self.max_shield), 15))
            font = pygame.font.Font(None, 24)
            text = font.render(f'{self.current_shield}/{self.max_shield}', True, (0, 0, 0))
            surface.blit(text, (195, 35)) 
            
            
    class Charges:
        def __init__(self):
            self.max_charges = 180
            self.current_charges = self.max_charges
    
        def shoot(self):
            if self.current_charges > 0:
                self.current_charges -= 1
                return True
            return False
    
        def draw(self, surface):
            pygame.draw.rect(surface, DARK_BLUE, (10, 60, (180 * self.current_charges / self.max_charges), 15))
            font = pygame.font.Font(None, 24)
            text = font.render(f'{self.current_charges}/{self.max_charges}', True, BLACK)
            surface.blit(text, (195, 60))
    
    class Enemy:
        def __init__(self, rooms, num_enemies_range=(3, 5), enemy_images=None):
            if enemy_images is None:
                try:
                    enemy_images = [
                        pygame.image.load('enemy1.png'),
                        pygame.image.load('enemy2.png'),
                        pygame.image.load('enemy3.png'),
                    ]
                except pygame.error as e:
                    print(f"Error loading enemy images: {e}")
                    enemy_images = []  # Пустой список в случае ошибки
            
            self.enemy_images = [pygame.transform.scale(img, (img.get_width() * 1.5, img.get_height() * 1.5)) for img in enemy_images]
            
            self.rooms = rooms
            self.enemies = []
            self.num_enemies = random.randint(*num_enemies_range)
    
            self.enemy_index = 0
            self.frame_count = 0
            self.enemy_bullets = []
            self.shoot_intervals = []
            self.shoot_timers = []
            self.move_interval = 60
            self.move_timer = 0
            self.directions = []
            self.speed = 2
            self.hits_taken = 0
    
            self.generate_enemies(player_x, player_y)
    
        def take_hit(self):
            self.hits_taken += 1
            if self.hits_taken >= 3:
                return True
            return False 
    
        def generate_enemies(self, player_x, player_y):
            for room in self.rooms:
                enemies_in_radius = 0
                for _ in range(self.num_enemies):
                    x = random.randint(room.left + 20, room.right - 20)
                    y = random.randint(room.top + 20, room.bottom - 20)
                    distance_to_player = math.sqrt((player_x - x) ** 2 + (player_y - y) ** 2)
                    
                    if distance_to_player <= 10000:
                        if enemies_in_radius >= 5:
                            continue
                        enemies_in_radius += 1
    
                    enemy_rect = pygame.Rect(x, y, self.enemy_images[0].get_width(), self.enemy_images[0].get_height())
                    self.enemies.append(enemy_rect)
                    self.directions.append((random.choice([-1, 1]), random.choice([-1, 1])))
                    self.shoot_intervals.append(random.randint(80, 150))
                    self.shoot_timers.append(0)  #
    
        def move_enemies(self, rooms, chests, boxes, is_in_bounds, player_x, player_y):
            self.move_timer += 1
            if self.move_timer >= self.move_interval:
                for i, enemy_rect in enumerate(self.enemies):
                    # Рассчитываем направление к игроку
                    dx = player_x - enemy_rect.x
                    dy = player_y - enemy_rect.y
                    if abs(dx) > abs(dy):
                        if dx > 0:
                            move_x = 1
                        else:
                            move_x = -1
                        move_y = random.choice([-1, 0, 1])
                    else:
                        if dy > 0:
                            move_y = 1
                        else:
                            move_y = -1
                        move_x = random.choice([-1, 0, 1])
                    self.directions[i] = (move_x, move_y)
                self.move_timer = 0
        
            for i, enemy_rect in enumerate(self.enemies):
                move_x, move_y = self.directions[i]
                new_x = enemy_rect.x + move_x * self.speed
                new_y = enemy_rect.y + move_y * self.speed
                barrier_rect = pygame.Rect(new_x, new_y, enemy_rect.width, enemy_rect.height)
                chest_rects = chests.get_chest_rects()
                box_rects = boxes.get_box_rects()

                if is_in_bounds(barrier_rect, rooms, [], chest_rects, box_rects, None, False):
                    enemy_rect.x = new_x
                    enemy_rect.y = new_y
    
        def shoot_bullets(self, player_x, player_y):
            for i, enemy_rect in enumerate(self.enemies):
                self.shoot_timers[i] += 1  # Увеличиваем таймер каждого врага
                if self.shoot_timers[i] >= self.shoot_intervals[i]:
                    dx = player_x - enemy_rect.x
                    dy = player_y - enemy_rect.y
                    angle = math.atan2(dy, dx)
                    speed = 5
                    bullet_dx = math.cos(angle) * speed
                    bullet_dy = math.sin(angle) * speed
                    bullet_rect = pygame.Rect(enemy_rect.centerx, enemy_rect.centery, 10, 10) 
                    self.enemy_bullets.append((bullet_rect, bullet_dx, bullet_dy))
                    self.shoot_timers[i] = 0
    
        def update_bullets(self, player_rect, shield, health):
            new_bullets = []
            for bullet in self.enemy_bullets:
                bullet_rect, bullet_dx, bullet_dy = bullet
                bullet_rect.x += bullet_dx
                bullet_rect.y += bullet_dy
                
                if bullet_rect.colliderect(player_rect):
                    if shield.current_shield > 0:
                        shield.decrease_shield(1)
                    else:
                        if health.current_health> 0:
                            health.decrease_health(1)                    
                    continue

                chest_rects = chests.get_chest_rects()
                box_rects = boxes.get_box_rects()
                if any(bullet_rect.colliderect(chest) for chest in chest_rects) or \
                   any(bullet_rect.colliderect(box) for box in box_rects) or \
                   not is_in_bounds(bullet_rect, rooms, [], chest_rects, box_rects, None, False):
                    continue 

                new_bullets.append(bullet)

            self.enemy_bullets = new_bullets
    
    
        def update(self, screen_width, screen_height, rooms, chests, boxes):
            self.frame_count += 1
            if self.frame_count % 10 == 0:
                self.enemy_index = (self.enemy_index + 1) % len(self.enemy_images)    
            self.update_bullets(rooms, chests, boxes)
    
        def draw(self, screen, camera_x, camera_y):
            for enemy_rect in self.enemies:
                screen.blit(self.enemy_images[self.enemy_index], (enemy_rect.x - camera_x, enemy_rect.y - camera_y))
    
            for bullet_rect, _, _ in self.enemy_bullets:
                pygame.draw.rect(screen, (255, 0, 0), (bullet_rect.x - camera_x, bullet_rect.y - camera_y, 10, 10))
    
        def get_enemy_rects(self):
            return self.enemies
        
 
    class Boxes:
        def __init__(self, rooms, chests, box_image_path='box.png', num_clusters_range=(1, 3), num_boxes_per_cluster_range=(5, 6), box_size=(30, 30)):
            self.rooms = rooms
            self.chests = chests
            self.box_image = pygame.image.load(box_image_path)
            self.box_image = pygame.transform.scale(self.box_image, box_size)
            self.num_clusters_range = num_clusters_range
            self.num_boxes_per_cluster_range = num_boxes_per_cluster_range
            self.box_size = box_size
            self.box_clusters = []
            self.create_boxes()
    
        def create_boxes(self):
            for room in self.rooms:
                num_clusters = random.randint(*self.num_clusters_range)
                clusters_in_room = []
                for _ in range(num_clusters):
                    num_boxes = random.randint(*self.num_boxes_per_cluster_range)
                    cluster_boxes = []
                    base_x = random.randint(room.left + 20, room.right - self.box_size[0] - 20)
                    base_y = random.randint(room.top + 20, room.bottom - self.box_size[1] - 20)
                    for _ in range(num_boxes):
                        new_box_rect = pygame.Rect(base_x, base_y, *self.box_size)
                        if all(not new_box_rect.colliderect(existing_box) for existing_box in cluster_boxes) and \
                           all(not new_box_rect.colliderect(chest) for chest in self.chests):
                            cluster_boxes.append(new_box_rect)
                            offset_x = random.choice([self.box_size[0], 0]) 
                            offset_y = random.choice([self.box_size[1], 0]) 
                            base_x += offset_x
                            base_y += offset_y
                            if base_x > room.right - self.box_size[0] - 20:
                                base_x = room.left + 20 
                                base_y += self.box_size[1] 
                            if base_y > room.bottom - self.box_size[1] - 20:
                                break 
    
                    clusters_in_room.append(cluster_boxes)
                self.box_clusters.append(clusters_in_room)
    
        def draw(self, screen, camera_x, camera_y):
            for cluster in self.box_clusters:
                for boxes in cluster:
                    for box_rect in boxes:
                        if box_rect:
                            adjusted_x = box_rect.x - camera_x
                            adjusted_y = box_rect.y - camera_y
                            screen.blit(self.box_image, (adjusted_x, adjusted_y))
    
        def check_bullet_collisions(self, bullet_rect):
            for cluster in self.box_clusters:
                for boxes in cluster:
                    for box_rect in boxes:
                        if box_rect.colliderect(bullet_rect): 
                            if random.random() < 0.3:
                                boxes.remove(box_rect)
                                self.drop_items()
                                return True 
                            else:
                                return True
            return False 
    
    
        def drop_items(self):

            if random.random() < 0.3:
                self.spawn_ammo(5) 
        
            if random.random() < 0.2:
                self.spawn_coins(5)
        
            if random.random() < 0.1:
                self.spawn_health(1)
        
        def spawn_ammo(self, amount):
            charges.current_charges += amount
            if charges.current_charges< 175:
                charges.current_charges += 5            
        
        def spawn_coins(self, amount):
            money.coins += amount
        
        def spawn_health(self, amount):
            if health.current_health< 6:
                health.current_health += 1 
            
        def get_boxes(self):
            all_boxes = []
            for cluster in self.box_clusters:
                for boxes in cluster:
                    all_boxes.extend(boxes)
            return all_boxes
        
        def get_box_rects(self):
            box_rects = []
            for cluster in self.box_clusters:
                for boxes in cluster:
                    for box_rect in boxes:
                        box_rects.append(box_rect)
            return box_rects

    
    class Chest:
        def __init__(self, rooms, closed_chest_image, opened_chest_image):
            self.closed_chest_image = closed_chest_image 
            self.opened_chest_image = opened_chest_image 
            self.chests = []  
            self.chest_states = [] 
            num_chests = random.randint(2, 5)

            while len(self.chests) < num_chests:
                room = random.choice(rooms)
                chest_x = random.randint(room.x + 20, room.x + room.width - 20)
                chest_y = random.randint(room.y + 20, room.y + room.height - 20)
                if all(math.dist((chest_x, chest_y), (cx, cy)) > 500 for cx, cy, _ in self.chests):
                    chest_rect = pygame.Rect(chest_x, chest_y, self.closed_chest_image.get_width(), self.closed_chest_image.get_height())
                    self.chests.append((chest_x, chest_y, chest_rect))
                    self.chest_states.append(False) 
    
        def draw(self, screen, camera_x, camera_y):
            for i, (chest_pos, chest_state) in enumerate(zip(self.chests, self.chest_states)):
                chest_image = self.opened_chest_image if chest_state else self.closed_chest_image
                screen.blit(chest_image, (chest_pos[0] - camera_x, chest_pos[1] - camera_y))
    
        def open_chest(self, chest_rect, keys):
            for i, (_, _, rect) in enumerate(self.chests):
                if rect == chest_rect and not self.chest_states[i]:
                    if keys[pygame.K_e]: 
                        self.chest_states[i] = True 
                        self.drop_item()
    
        def drop_item(self):
                random_chance = random.random()
                if random_chance < 0.1:
                    if health.current_health< 6:
                        health.current_health += 1
                    else:
                        money.coins += 50                
                elif random_chance < 0.2:
                    money.coins += 20
                elif random_chance < 0.3:
                    if charges.current_charges< 160:
                        charges.current_charges+= 20
                    else:
                        charges.current_charges = 180
                else:
                    money.coins += 10
                    
        def get_chest_rects(self):
            return [chest_rect for _, _, chest_rect in self.chests]
    
    class Bull:
        def __init__(self, x, y, enemies):
            self.x = x
            self.y = y
            self.speed = 10
            self.target = self.find_nearest_target(enemies)
    
            if self.target is not None:
                self.target_x, self.target_y = self.target.centerx, self.target.centery
            else:
                self.target_x = random.randint(0, 1000)
                self.target_y = random.randint(0, 600)
    
            self.angle = math.atan2(self.target_y - y, self.target_x - x)
            self.dx = math.cos(self.angle) * self.speed
            self.dy = math.sin(self.angle) * self.speed
            self.color = (255, 255, 0)
            
            self.length = 10
            self.thickness = 8
    
        def find_nearest_target(self, enemies):
            if not enemies:
                return None 

            detection_radius = 200 
            targets = [enemy for enemy in enemies if self.distance_to(enemy) <= detection_radius]
            
            if not targets:
                return None
            return min(targets, key=lambda rect: self.distance_to(rect))
    
        def distance_to(self, target):
            return math.sqrt((target.centerx - self.x) ** 2 + (target.centery - self.y) ** 2)
        
        def update(self, enemies, rooms, b, chest_rects):
            self.x += self.dx
            self.y += self.dy
            bullet_rect = pygame.Rect(self.x, self.y, self.thickness, self.thickness)
            for enemy in enemies:
                if bullet_rect.colliderect(enemy):
                    enemies.remove(enemy)
                    return True

            if boxes.check_bullet_collisions(bullet_rect):
                return True 
            if any(bullet_rect.colliderect(chest_rect) for chest_rect in chest_rects):
                return True 
            if not any(room.collidepoint(self.x, self.y) for room in rooms):
                return True 
            return False
    
        def draw(self, screen, camera_x, camera_y):
            end_x = self.x + math.cos(self.angle) * self.length
            end_y = self.y + math.sin(self.angle) * self.length
            pygame.draw.line(screen, self.color, (self.x - camera_x, self.y - camera_y), 
                             (end_x - camera_x, end_y - camera_y), self.thickness)

    
    def find_nearest_wall(hero_x, hero_y, rooms, corridors):
        nearest_x = None
        nearest_y = None
        min_distance = float('inf')

        for room in rooms:
            walls = [
                (room.x, hero_y), 
                (room.x + room.width, hero_y),
                (hero_x, room.y), 
                (hero_x, room.y + room.height)
            ]
            for wall_x, wall_y in walls:
                distance = math.hypot(wall_x - hero_x, wall_y - hero_y)
                if distance < min_distance:
                    min_distance = distance
                    nearest_x, nearest_y = wall_x, wall_y
        for corridor in corridors:
            walls = [
                (corridor.x, hero_y), 
                (corridor.x + corridor.width, hero_y),
                (hero_x, corridor.y),  
                (hero_x, corridor.y + corridor.height) 
            ]
            for wall_x, wall_y in walls:
                distance = math.hypot(wall_x - hero_x, wall_y - hero_y)
                if distance < min_distance:
                    min_distance = distance
                    nearest_x, nearest_y = wall_x, wall_y
        return nearest_x, nearest_y
    
    
    def generate_rooms():
        rooms = []
        for _ in range(num_rooms):
            room_width = random.randint(room_min_size, room_max_size) * tile_size
            room_height = random.randint(room_min_size, room_max_size) * tile_size
            x = random.randint(0, (MAP_WIDTH - room_width) // tile_size) * tile_size
            y = random.randint(0, (MAP_HEIGHT - room_height) // tile_size) * tile_size
            rooms.append(pygame.Rect(x, y, room_width, room_height))
        return rooms
    
    
    def connect_rooms(rooms):
        corridors = []

        connected_rooms = [rooms[0]] 
    
        for i in range(1, len(rooms)):
            room1 = connected_rooms[random.randint(0, len(connected_rooms) - 1)] 
            room2 = rooms[i] 
    
            room1_center = room1.center
            room2_center = room2.center

            if random.choice([True, False]):
                corridors.append(pygame.Rect(min(room1_center[0], room2_center[0]), room1_center[1] - corridor_width // 2,
                                             abs(room1_center[0] - room2_center[0]), corridor_width))
                corridors.append(pygame.Rect(room2_center[0] - corridor_width // 2, min(room1_center[1], room2_center[1]),
                                             corridor_width, abs(room1_center[1] - room2_center[1])))
            else:
                corridors.append(pygame.Rect(room1_center[0] - corridor_width // 2, min(room1_center[1], room2_center[1]),
                                             corridor_width, abs(room1_center[1] - room2_center[1])))
                corridors.append(pygame.Rect(min(room1_center[0], room2_center[0]), room2_center[1] - corridor_width // 2,
                                             abs(room1_center[0] - room2_center[0]), corridor_width))
    
            connected_rooms.append(room2)
    
        return corridors
    
    
    portal_images = [
        pygame.image.load('portal1.png'),
        pygame.image.load('portal2.png'),
        pygame.image.load('portal3.png'),
        pygame.image.load('portal4.png')
    ]
    
    portal_images = [pygame.transform.scale(img, (img.get_width() * 2, img.get_height() * 2)) for img in portal_images]
    def draw_markers(screen, rooms, camera_x, camera_y):
        frame_duration = 0.5 
        animation_time = 1 
        first_room_center = rooms[0].center
        max_distance = 0
        farthest_room_center = None
        for room in rooms[1:]:
            distance = math.sqrt((room.centerx - first_room_center[0]) ** 2 + (room.centery - first_room_center[1]) ** 2)
            if distance > max_distance:
                max_distance = distance
                farthest_room_center = room.center
        start_time = time.time()
        elapsed_time = 0
        while elapsed_time < animation_time:
            elapsed_time = time.time() - start_time

            frame_index = int((elapsed_time // frame_duration) % len(portal_images))
            current_portal_image = portal_images[frame_index].copy() 

            alpha = max(0, 100 * (1 - (elapsed_time / 3)))  
            current_portal_image.set_alpha(alpha) 

            current_image = hero_images[animation_index]
            screen.blit(current_image, (player_x - camera_x, player_y - camera_y))           
    
            portal_width, portal_height = 60, 50
    
            screen.blit(current_portal_image, (first_room_center[0] - portal_width // 2 - camera_x,
                                               first_room_center[1] - portal_height // 2 - camera_y))
            
            if farthest_room_center:
                pygame.draw.rect(screen, (0, 0, 255), (farthest_room_center[0] - 5 - camera_x, farthest_room_center[1] - 5 - camera_y, 10, 10))
            
            pygame.display.flip()
    
        return
    
           
    rooms = generate_rooms()
    f = True
    corridors = connect_rooms(rooms)
    money = Money()
    player_x, player_y = rooms[0].center
    player_x -= player_width // 2 
    player_y -= player_height // 2 

    def update_player_animation(is_moving):
        global animation_index, animation_counter
    
        if is_moving: 
            animation_counter += animation_speed
            if animation_counter >= 1:
                animation_counter = 0
                animation_index = (animation_index + 1) % len(hero_images) 
        else:
            animation_index = 0  
    
    def is_in_bounds(rect, rooms, corridors, chestss, box_rects, keys, hero):
        if hero:
            for chest_rect in chestss:
                smaller_chest_rect = chest_rect.inflate(-40, -10)
                if rect.colliderect(smaller_chest_rect):
                    chests.open_chest(chest_rect, keys)
                    return False   
        for box in box_rects:
            smaller_box_rect = box.inflate(-40, -40)
            if rect.colliderect(smaller_box_rect):
                return False           
        for room in rooms:
            if rect.colliderect(room):
                return True
        for corridor in corridors:
            if rect.colliderect(corridor):
                return True
        return False
    
    running = True
    clock = pygame.time.Clock()
    
    def draw_walls(rooms, corridors, camera_x, camera_y, wall_texture):
        wall_thickness = 30  # Толщина стен
        texture_width = wall_texture.get_width()
        texture_height = wall_texture.get_height()
        for room in rooms:
            for x in range(room.x - wall_thickness - camera_x, room.x + room.width + wall_thickness - camera_x, texture_width):
                screen.blit(wall_texture, (x, room.y - wall_thickness - camera_y), (0, 0, min(texture_width, room.width + 2 * wall_thickness - (x - (room.x - wall_thickness - camera_x))), wall_thickness))

            for x in range(room.x - wall_thickness - camera_x, room.x + room.width + wall_thickness - camera_x, texture_width):
                screen.blit(wall_texture, (x, room.y + room.height - camera_y), (0, 0, min(texture_width, room.width + 2 * wall_thickness - (x - (room.x - wall_thickness - camera_x))), wall_thickness))

            for y in range(room.y - wall_thickness - camera_y, room.y + room.height + wall_thickness - camera_y, texture_height):
                screen.blit(wall_texture, (room.x - wall_thickness - camera_x, y), (0, 0, wall_thickness, min(texture_height, room.height + 2 * wall_thickness - (y - (room.y - wall_thickness - camera_y)))))

            for y in range(room.y - wall_thickness - camera_y, room.y + room.height + wall_thickness - camera_y, texture_height):
                screen.blit(wall_texture, (room.x + room.width - camera_x, y), (0, 0, wall_thickness, min(texture_height, room.height + 2 * wall_thickness - (y - (room.y - wall_thickness - camera_y)))))

        for corridor in corridors:
            # Верхняя стена
            for x in range(corridor.x - wall_thickness - camera_x, corridor.x + corridor.width + wall_thickness - camera_x, texture_width):
                screen.blit(wall_texture, (x, corridor.y - wall_thickness - camera_y), (0, 0, min(texture_width, corridor.width + 2 * wall_thickness - (x - (corridor.x - wall_thickness - camera_x))), wall_thickness))

            for x in range(corridor.x - wall_thickness - camera_x, corridor.x + corridor.width + wall_thickness - camera_x, texture_width):
                screen.blit(wall_texture, (x, corridor.y + corridor.height - camera_y), (0, 0, min(texture_width, corridor.width + 2 * wall_thickness - (x - (corridor.x - wall_thickness - camera_x))), wall_thickness))

            for y in range(corridor.y - wall_thickness - camera_y, corridor.y + corridor.height + wall_thickness - camera_y, texture_height):
                screen.blit(wall_texture, (corridor.x - wall_thickness - camera_x, y), (0, 0, wall_thickness, min(texture_height, corridor.height + 2 * wall_thickness - (y - (corridor.y - wall_thickness - camera_y)))))

            for y in range(corridor.y - wall_thickness - camera_y, corridor.y + corridor.height + wall_thickness - camera_y, texture_height):
                screen.blit(wall_texture, (corridor.x + corridor.width - camera_x, y), (0, 0, wall_thickness, min(texture_height, corridor.height + 2 * wall_thickness - (y - (corridor.y - wall_thickness - camera_y)))))
    bullets = []
    chest_image = pygame.image.load('chest.png')
    opened_chest_image = pygame.image.load('chest_open.png')
    chest_image = pygame.transform.scale(chest_image, (chest_image.get_width() * 1.5, chest_image.get_height() * 1.5))
    opened_chest_image = pygame.transform.scale(opened_chest_image, (opened_chest_image.get_width() * 1.5, opened_chest_image.get_height() * 1.5))
    enemy = Enemy(rooms)
    chests = Chest(rooms, chest_image, opened_chest_image)    
    boxes = Boxes(rooms, chests.get_chest_rects())   
    
    health = Health()
    shield = Shield()
    charges = Charges()
    bullet = None
    current_time = 0
    can_shoot = True
    shoot_delay = 0.5 
    last_shot_time = 0
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Выбор режима")

    font = pygame.font.Font(None, 36)
    game_mode = None
    
    def draw_start_screen():
        screen.fill(BLACK) 
        
        title_text = font.render("Выберите режим:", True, WHITE)
        screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 150))
        lagoon_text = font.render("1 - Голубая Лагуна", True, BLUE)
        dungeon_text = font.render("2 - Подземелья", True, (100, 100, 100))
        meadows_text = font.render("3 - Заливные Луга", True, DARK_GREEN)
        screen.blit(lagoon_text, (screen_width // 2 - lagoon_text.get_width() // 2, 250))
        screen.blit(dungeon_text, (screen_width // 2 - dungeon_text.get_width() // 2, 300))
        screen.blit(meadows_text, (screen_width // 2 - meadows_text.get_width() // 2, 350))
        pygame.display.flip()
    
    def handle_menu_events():

        global game_mode
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_mode = "lagoon"
                    filterr(image1, "floor", 0, 0, 255, 30)
                    filterr(image2,"wall",  0, 0, 255, 30)
                    return True
                elif event.key == pygame.K_2:
                    game_mode = "dungeon"
                    return True
                elif event.key == pygame.K_3:
                    game_mode = "meadows"
                    filterr(image1, "floor", 0, 255, 0, 30)
                    filterr(image2,"wall",  0, 255, 0, 30)                  
                    return True
        return False
    running = True
    menu_active = True
    
            
            
    while running:
        if menu_active:
            draw_start_screen()
    
            if handle_menu_events(): 
                menu_active = False 
    
        else:        
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
            old_x, old_y = player_x, player_y 
        
            is_moving = False 
            new_x, new_y = player_x, player_y
        
            if keys[pygame.K_LEFT]:
                barrier_rect = pygame.Rect(new_x - player_speed - 20, new_y + 40, player_width - 20, player_height - 20)
                chest_rects = chests.get_chest_rects()
                box_rects = boxes.get_box_rects()
            
                if is_in_bounds(barrier_rect, rooms, corridors, chest_rects, box_rects, keys, True):
                    new_x -= player_speed
                is_moving = True
            
            if keys[pygame.K_RIGHT]:
                barrier_rect = pygame.Rect(new_x + player_speed + 20, new_y + 40, player_width - 20, player_height - 20)
                chest_rects = chests.get_chest_rects()
                box_rects = boxes.get_box_rects()
                
                if is_in_bounds(barrier_rect, rooms, corridors, chest_rects, box_rects, keys, True):
                    new_x += player_speed
                is_moving = True
            
            if keys[pygame.K_UP]:
                barrier_rect = pygame.Rect(new_x + 10, new_y - player_speed + 10, player_width - 20, player_height - 20)
                chest_rects = chests.get_chest_rects()
                box_rects = boxes.get_box_rects()
                
                if is_in_bounds(barrier_rect, rooms, corridors, chest_rects, box_rects, keys, True):
                    new_y -= player_speed
                is_moving = True
            
            if keys[pygame.K_DOWN]:
                barrier_rect = pygame.Rect(new_x + 10, new_y + player_speed + 10 + 35, player_width - 20, player_height - 20)
                chest_rects = chests.get_chest_rects()
                box_rects = boxes.get_box_rects()
                
                if is_in_bounds(barrier_rect, rooms, corridors, chest_rects, box_rects, keys, True):
                    new_y += player_speed
                is_moving = True

            if keys[pygame.K_SPACE] and can_shoot:
                if charges.shoot():
                    current_time = pygame.time.get_ticks() / 1000
                    bullet = Bull(player_x, player_y, enemy.get_enemy_rects())
                    bullets.append(bullet)
                    can_shoot = False 
                    last_shot_time = current_time 

            if pygame.time.get_ticks() / 1000 - last_shot_time >= shoot_delay:
                can_shoot = True
        
            new_bullets = []
            for bullet in bullets:
                if not bullet.update(enemy.get_enemy_rects(), rooms, box_rects, chest_rects): 
                    new_bullets.append(bullet) 
            bullets = new_bullets 

            for bullet in bullets:
                bullet.draw(screen, camera_x, camera_y)
                
            pygame.display.flip()
        
            player_x = max(0, min(MAP_WIDTH - player_width, new_x))
            player_y = max(0, min(MAP_HEIGHT - player_height, new_y))
        
            camera_x = player_x - SCREEN_WIDTH // 2 + player_width // 2
            camera_y = player_y - SCREEN_HEIGHT // 2 + player_height // 2
        
            camera_x = max(0, min(MAP_WIDTH - SCREEN_WIDTH, camera_x))
            camera_y = max(0, min(MAP_HEIGHT - SCREEN_HEIGHT, camera_y))

            update_player_animation(is_moving)

            screen.fill(BLACK)
           
            floor_image = pygame.image.load('floor.png')
            wall_texture = pygame.image.load('wall.png')
            floor_image = pygame.transform.scale(floor_image, (MAP_WIDTH, MAP_HEIGHT))
            draw_walls(rooms, corridors, camera_x, camera_y, wall_texture)
            for room in rooms:
                room_surface = pygame.Surface((room.width, room.height))
                room_surface.blit(floor_image, (0, 0), (room.x, room.y, room.width, room.height)) 
                screen.blit(room_surface, (room.x - camera_x, room.y - camera_y))
        
            for corridor in corridors:
                corridor_surface = pygame.Surface((corridor.width, corridor.height))
                corridor_surface.blit(floor_image, (0, 0), (corridor.x, corridor.y, corridor.width, corridor.height)) 
                screen.blit(corridor_surface, (corridor.x - camera_x, corridor.y - camera_y))
        
            if f:
                draw_markers(screen, rooms, camera_x, camera_y)
                f = False
                
            chests.draw(screen, camera_x, camera_y)
            boxes.draw(screen, camera_x, camera_y)
            player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
            dt = clock.tick(60) / 1000 
            
            enemy.move_enemies(rooms, chests, boxes, is_in_bounds, player_x, player_y)
            enemy.shoot_bullets(player_x, player_y)
            enemy.update_bullets(player_rect, shield, health)
            enemy.draw(screen, camera_x, camera_y)  # Отрисовка врагов и их пул
                
            money.draw(screen)
            chest_rects = chests.get_chest_rects()
            box_rects = boxes.get_box_rects()    
        
            pygame.draw.rect(screen, LIGHT_BROWN, (0, 0, 260, 90))
            health.draw(screen)
            shield.draw(screen)
            charges.draw(screen)    
            shield.recharge_shield()
        
            current_image = hero_images[animation_index]
            screen.blit(current_image, (player_x - camera_x, player_y - camera_y))
            bullet = None

            if len(enemy.get_enemy_rects()) == 0 and not portal.portal_active:
                portal.spawn_portal(player_x, player_y)

            portal.update()
            portal.draw(screen, camera_x, camera_y)  
            if health.current_health <= 0: 
                screen.fill((0, 0, 0)) 
                font = pygame.font.Font(None, 74)
                text = font.render("Смерть", True, (255, 0, 0)) 
                text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                screen.blit(text, text_rect) 
                time.sleep(5)
            pygame.display.flip()
            clock.tick(60)
    
if __name__ == "__main__":
    import pygame
    
    
    pygame.init()    
    main()
