import pygame
import animatedSprite


def main():
    # clock = pygame.time.Clock()
    scale = 2
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1500, 1000))
    pygame.display.set_caption('Detective Game')

    # Fill background
    # background = pygame.Surface(screen.get_size())
    # background = background.convert()
    background = loadAndScaleImage("resources/backdrop1.png")

    # Display text
    font = pygame.font.Font(None, 36)
    text = font.render("Objective: Find evidence", 1, (10, 255, 10))
    textPos = text.get_rect()
    textPos.centerx = background.get_rect().centerx
    background.blit(text, textPos)

    # make Player: object of playerSprite
    playerSpriteSheet = loadAndScaleImage("resources/playerFiles/playerStandSpriteSheet.png")
    playerSpriteFrames = load_sprite_sheet(playerSpriteSheet, 121 * scale, 200 * scale, 1, 9, True)
    playerSprite = animatedSprite.AnimatedSprite(screen, 0, 500, playerSpriteFrames, 6)
    playerWalkSpriteSheet = loadAndScaleImage("resources/playerFiles/detective-walk-animation-place-holder.png")
    playerWalkSpriteFrames = load_sprite_sheet(playerWalkSpriteSheet, 121 * scale, 200 * scale, 1, 1, False)

    # Event loop
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # delta = clock.tick() / 1000.0
        # print("event update:", delta)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("left pressed")
                    playerSprite.moveLeft()
                    playerSprite.changeAnimation(playerWalkSpriteFrames)
                elif event.key == pygame.K_RIGHT:
                    print("right pressed")
                    playerSprite.moveRight()
                    playerSprite.changeAnimation(playerWalkSpriteFrames)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerSprite.movePos = [0, 0]
                    playerSprite.state = "still"
                    playerSprite.defaultAnimation()
            
        screen.blit(background, (0, 0))

        # Update the animation
        playerSprite.update()
        # print("called update")
        
        # Draw the animation
        playerSprite.draw()

        pygame.display.flip()


def load_sprite_sheet(spriteSheet, frameWidth, frameHeight, rows, columns, bounce):
    frames = []
    for row in range(rows):
        for column in range(columns):
            # print("column", column)
            rect = pygame.Rect(column * frameWidth, row * frameHeight, frameWidth, frameHeight)
            # print("top left rectangle", rect.topleft)
            frame = spriteSheet.subsurface(rect)
            frames.append(frame)
            # print("length of frames", len(frames))

    if bounce:
        for bounceRow in range(rows):
            realRow = (rows - 1 - bounceRow)
            # print("bounce row:", bounceRow)
            # print("real row:", realRow)
            for bounceColumn in range(columns):
                realColumn = ((columns - 1) - bounceColumn)
                # print("bounce column is:", bounceColumn)
                # print("real column:", realColumn)
                if bounceColumn != 0:
                    rect = pygame.Rect(realColumn * frameWidth, realRow * frameHeight, frameWidth, frameHeight)
                    # print("top left rectangle:", rect.topleft)
                    frame = spriteSheet.subsurface(rect)
                    frames.append(frame)
                    # print("length of frames:", len(frames))
                # else:
                    # print("skipping the doing last frame twice")
            
    return frames


def loadAndScaleImage(originalImagePath):
    scaledImage = -1
    try:
        originalImage = pygame.image.load(originalImagePath)
    except:
        # print("failed to load resource about to crash")
        return -1  # ERROR
    
    newWidth = originalImage.get_width() * 2
    newHeight = originalImage.get_height() * 2
    scaledImage = pygame.transform.scale(originalImage, (newWidth, newHeight))

    return scaledImage


main()

