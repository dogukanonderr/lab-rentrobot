import pygame  # Gerekli kütüphanelerimizi import ediyoruz
import sys

# Pygame'i başlatıp kütüphaneye dahil olangi fonksiyonlarımızı çalıştırıyoruz
pygame.init()

# Ekran boyutları
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 40

#Blok renkleri
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Labirent şeması: 0 = duvar, 1 = yol, 'E' = çıkış
labi = [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 'E']
]

# Oyuncunun başlangıç konumu
player_pos = [0, 0]

# Pygame ekranı oluştur
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labirent Robot")

# Oyuncu resmi
player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (CELL_SIZE, CELL_SIZE))

def draw_labi():
    # Labirenti ekrana çizer.
    for row in range(len(labi)):
        for col in range(len(labi[row])):
            color = WHITE if labi[row][col] == 1 else BLACK
            if labi[row][col] == 'E':
                color = GREEN
            pygame.draw.rect(screen, color,
                             (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, (200, 200, 200),
                             (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def move_player(dx, dy):
    # Oyuncuyu belirtilen yöne hareket ettirir.
    global player_pos
    x, y = player_pos
    new_x, new_y = x + dx, y + dy

    # Yeni pozisyonun geçerliliğini kontrol et
    if 0 <= new_x < len(labi) and 0 <= new_y < len(labi[0]):
        if labi[new_x][new_y] != 0:  # Duvar değilse hareket et
            player_pos = [new_x, new_y]

            # Çıkış noktasına ulaşıldı mı?
            if labi[new_x][new_y] == 'E':
                print("Tebrikler! Çıkışa ulaştınız!")
                pygame.quit()
                sys.exit()

# Ana oyun döngüsü
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)

    # Pygame kontrol etme ve tuş atamaları
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Klavye tuşlarına basıldığında
            if event.key == pygame.K_UP:
                move_player(-1, 0)
            elif event.key == pygame.K_DOWN:
                move_player(1, 0)
            elif event.key == pygame.K_LEFT:
                move_player(0, -1)
            elif event.key == pygame.K_RIGHT:
                move_player(0, 1)

    # Labirenti ve oyuncuyu çiz
    draw_labi()
    player_x, player_y = player_pos[1] * CELL_SIZE, player_pos[0] * CELL_SIZE
    screen.blit(player_img, (player_x, player_y))

    # Ekranı güncelle
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
