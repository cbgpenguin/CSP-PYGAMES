import pygame
import animatedSprite



def main():
    clock = pygame.time.Clock()
    scale = 2
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1500, 1000))
    pygame.display.set_caption('Detective Game')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((30, 30, 250))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Objective: Find evidince", 1, (10, 255, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)


    # make Player: opject of playersprite
    playerSpriteSheet = loadAndScaleImage("resorces/playerFiles/pixilart-sprite.png")
    playerSpriteFrames = load_sprite_sheet(playerSpriteSheet, 121 * scale, 200 * scale, 1, 9, True)
    playerSprite = animatedSprite.AnimatedSprite(screen, 0, 500, playerSpriteFrames, 6)

    # Event loop
    while True:
        delta = clock.tick() / 1000.0
        print("event update:", delta)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerSprite.moveLeft()
                    # playerSprite.changeAnimation(load_sprite_sheet("walkingAnimation", 121, 200, 2, 10, False))
                elif event.key == pygame.K_RIGHT:
                    playerSprite.moveRight()
                    # playerSprite.changeAnimation(load_sprite_sheet("walkingAnimation", 121, 200, 2, 10, False))
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerSprite.movepos = [0,0]
                    playerSprite.state = "still"
                    playerSprite.defaltAnimation()
            
        screen.blit(background, (0, 0))

        # Update the animation
        playerSprite.update()
        
        # Draw the animation
        playerSprite.draw()

        pygame.display.flip()


def load_sprite_sheet(spriteSheet, frameWidth, frameHeight, rows, columns, bounce):

    frames = []
    for row in range(rows):
        for column in range(columns):
            print("column", column)
            rect = pygame.Rect(column * frameWidth, row * frameHeight, frameWidth, frameHeight)
            print("top left rectangle", rect.topleft)
            frame = spriteSheet.subsurface(rect)
            frames.append(frame)
            print("length of frames", len(frames))

    if bounce:
        for bounceRow in range(rows):
            realRow = (rows-1 - bounceRow)
            print("bounce row:", bounceRow)
            print("real row:", realRow)
            for bounceColumn in range(columns):
                realColumn = ((columns-1) - bounceColumn)
                print("bounce column is:", bounceColumn)
                print("real column:", realColumn)
                if bounceColumn != 0:
                    rect = pygame.Rect(realColumn * frameWidth, realRow * frameHeight, frameWidth, frameHeight)
                    print("top left rectangle:", rect.topleft)
                    frame = spriteSheet.subsurface(rect)
                    frames.append(frame)
                    print("length of frames:", len(frames))
                else:
                    print("skiping the doing last frame twice")
            
    return frames

def loadAndScaleImage(originalImagePath):
    scaled_image = -1
    try:
        originalImage = pygame.image.load(originalImagePath)
    except:
        print("faild to load resorce about to crash")
        return -1 # ERROR
    
    newWidth = originalImage.get_width() * 2
    newHeight = originalImage.get_height() * 2
    scaled_image = pygame.transform.scale(originalImage, (newWidth, newHeight))

    return scaled_image
main()


