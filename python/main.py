import pygame
import animatedSprite as animatedSprite
from pointOfInterest import pointOfInterest

playerSprite = None
def game():
    counter = 0
    global playerSprite
    # clock = pygame.time.Clock()
    imageScale = 2 # Scale the images up to this
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1500, 700))
    pygame.display.set_caption('Detective Game')

    # Fill background
    # background = pygame.Surface(screen.get_size())
    # background = background.convert()
    background = loadAndScaleImage("resources/backdrop1.png", imageScale)

    # Display text
    font = pygame.font.Font(None, 36)
    text = font.render("Objective: Find evidence", 1, (10, 255, 10))
    textPos = text.get_rect()
    textPos.centerx = background.get_rect().centerx
    background.blit(text, textPos)

    # make Player: object of playerSprite + animations
    playerSpriteSheet = loadAndScaleImage("resources/playerFiles/playerStandSpriteSheet.png", imageScale)
    playerSpriteFrames = loadSpriteSheet(playerSpriteSheet, 121 * imageScale, 200 * imageScale, 1, 9, True)

    playerSprite = animatedSprite.AnimatedSprite(screen, 0, 300, playerSpriteFrames, 6)

    playerWalkSpriteSheet = loadAndScaleImage("resources/playerFiles/detective-walk-animation-place-holder.png", imageScale)
    playerWalkSpriteFrames = loadSpriteSheet(playerWalkSpriteSheet, 121 * imageScale, 200 * imageScale, 1, 1, False) #todo: change numbers when there are real frames

    pointOfInterestImage = loadAndScaleImage("resources/backdrop1.png", imageScale)

    book = pointOfInterest(screen, 50, 50, pointOfInterestImage, "book")

    pointsOfInterest = [book]
    menu = None
    # Event loop
    while True:
        counter += 1
        print("~~~~~~ Event Loop Start ~~~~~~", counter)
        # delta = clock.tick() / 1000.0
        # print("event update:", delta)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    # print("left pressed")
                    playerSprite.changeAnimation(playerWalkSpriteFrames)
                    playerSprite.newFrame()
                    playerSprite.image = pygame.transform.flip(playerSprite.image, True, False)
                    playerSprite.state = "moveLeft"
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    # print("right pressed")
                    playerSprite.changeAnimation(playerWalkSpriteFrames)
                    playerSprite.update()
                    playerSprite.state = "moveRight"
                elif event.key == pygame.K_e:
                    for point in pointsOfInterest:
                        if point.isPlayerInRange:
                            point.open()
                                 

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d or pygame.K_LEFT or pygame.K_RIGHT:
                    playerSprite.defaultAnimation()
                    playerSprite.moveDistance = [0, 0]
                    playerSprite.state = "still"

        for point in pointsOfInterest:
            if abs(playerSprite.rect[0] - point.rect[0]) < point.visibleRange:
                print("player is close to", point.name)
                point.isPlayerInRange = True

            else:
                point.isPlayerInRange = False
            point.update()
        screen.blit(background, (0, 0))

        # Update the animation
        playerSprite.update()
        # print("called update")
        
        pygame.display.flip()

def loadSpriteSheet(spriteSheet, frameWidth, frameHeight, rows, columns, bounce):
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


def loadAndScaleImage(originalImagePath, scale):
    try:
        originalImage = pygame.image.load(originalImagePath)
    except:
        print("failed to load resource about to crash")
        return -1  # ERROR
    
    newWidth = originalImage.get_width() * scale
    newHeight = originalImage.get_height() * scale
    scaledImage = pygame.transform.scale(originalImage, (newWidth, newHeight))

    return scaledImage


game()
