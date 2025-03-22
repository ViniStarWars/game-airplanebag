import pygame
import random

pygame.init()

# Configuração da tela
largura, altura = 440, 450
janela = pygame.display.set_mode([largura, altura])
pygame.display.set_caption('First Game')

# Carregando imagens
imagem_display = pygame.image.load(r'C:\Users\User\python\programa1\python\jogo1\14401936-fundo-de-céu-nublado-5.jpg')
image_player = pygame.image.load(r'C:\Users\User\python\programa1\python\jogo1\icons8-avião-48.png')
imagem_against = pygame.image.load(r'C:\Users\User\python\programa1\python\jogo1\icons8-bagagem-de-mão-48.png')

# Configuração do jogador
pos_x_player = largura // 2
pos_y_player = 380
vel_nave_player = 1

# Configuração das malas
malas = []
velocidade_malas = 0.2
tempo_nova_mala = 30  # Intervalo para gerar malas
contador_frames = 0

# Pontuação
pontuacao = 0
fonte = pygame.font.Font(None, 36)

loop = True

while loop:
    pygame.time.delay(10)
    
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
    
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        pos_x_player -= vel_nave_player
    if teclas[pygame.K_RIGHT]:
        pos_x_player += vel_nave_player
    if teclas[pygame.K_UP]:
        pos_y_player -= vel_nave_player
    if teclas[pygame.K_DOWN]:
        pos_y_player += vel_nave_player
    
    # Impedir que o jogador saia da tela
    pos_x_player = max(0, min(pos_x_player, largura - 48))
    pos_y_player = max(0, min(pos_y_player, altura - 48))
    
    # Criar novas malas
    contador_frames += 1
    if contador_frames >= tempo_nova_mala:
        x_mala = random.randint(0, largura - 48)
        malas.append([x_mala, 0])
        contador_frames = 0
    
    # Movendo as malas
    for mala in malas:
        mala[1] += velocidade_malas
    
    # Verificando colisão entre o player e as malas
    novas_malas = []
    for mala in malas:
        if (pos_x_player < mala[0] + 48 and pos_x_player + 48 > mala[0] and
            pos_y_player < mala[1] + 48 and pos_y_player + 48 > mala[1]):
            pontuacao += 1
            print(f"Mala coletada! Pontuação: {pontuacao}")
        else:
            novas_malas.append(mala)
    malas = novas_malas
    
    # Atualizando a tela
    janela.blit(imagem_display, (0, 0))
    janela.blit(image_player, (pos_x_player, pos_y_player))
    for mala in malas:
        janela.blit(imagem_against, (mala[0], mala[1]))
    
    # Exibir pontuação
    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, (255, 255, 255))
    janela.blit(texto_pontuacao, (10, 10))
    
    pygame.display.update()
    
pygame.quit()