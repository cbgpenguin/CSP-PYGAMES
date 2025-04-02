import pygame
import animatedSprite
from pointOfInterest import PointOfInterest

def game():
    counter = 0
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
    text = font.render("Objective: Find evidence", True, (20, 60, 60))
    textPos = text.get_rect()
    textPos.centerx = background.get_rect().centerx
    background.blit(text, textPos)

    # make Player: object of playerSprite + animations
    playerSpriteSheet = loadAndScaleImage("resources/playerFiles/playerStandSpriteSheet.png", imageScale)
    playerSpriteFrames = loadSpriteSheet(playerSpriteSheet, 121 * imageScale, 200 * imageScale, 1, 9, True)

    playerSprite = animatedSprite.AnimatedSprite(screen, 0, 300, playerSpriteFrames, 6)

    playerWalkSpriteSheet = loadAndScaleImage("resources/playerFiles/detective-walk-animation-place-holder.png", imageScale)
    playerWalkSpriteFrames = loadSpriteSheet(playerWalkSpriteSheet, 121 * imageScale, 200 * imageScale, 1, 1, False) #todo: change numbers when there are real frames

    pointOfInterestImage = loadAndScaleImage("resources/pointOfInterest.png", imageScale)

    bookLines = ["Hmm, a books detailing water", "quality. Doesn't seem", "important... The man was", "stabbed could this be", "evidence? I'm going to keep", "walking around to look", "for evidence"]
    book = PointOfInterest(screen, 150, 300, pointOfInterestImage, "book", bookLines)

    boardLines = ["it seems they were", "doing their own kind", "of detective work", "what could this be about?", "bla bla bla bla", "bla bla bla bla"]
    board = PointOfInterest(screen, 620, 170, pointOfInterestImage, "board", boardLines)

    calenderLines = ["They had a day marked off on", "on their calender", "three days ago just a", "day before he was killed"]
    calender = PointOfInterest(screen, 1200, 130, pointOfInterestImage, "calender", calenderLines)

    pointsOfInterest = [book, board, calender]

    menu = None
    # Event loop
    while True:
        screen.blit(background, (0, 0))
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

        # Update the play animation and draw
        playerSprite.update()
        # print("called update")

        # if point is in range of the player then draw it. If not then close it. Super important the point is in the list
        for point in pointsOfInterest:
            if abs(playerSprite.rect[0] - point.rect[0]) < point.visibleRange:
                print("player is close to", point.name)
                point.isPlayerInRange = True
                point.update()
            else:
                point.isPlayerInRange = False
                point.close()
            

        
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
