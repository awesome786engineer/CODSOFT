import random
import pygame as pg

pg.init()

main_width = 500
height = 430

main_window = pg.display.set_mode((main_width, height))
pg.display.set_caption("Rock Paper Scissors game")

clock = pg.time.Clock()

white = (255, 255, 255)
gray = (200, 200, 200)
black = (0, 0, 0)
red = (240, 0, 0)
green = (0, 250, 0)
size = 40

def make_button(text, rect, color, window):
    # border rectangle
    border_width = 5
    border_rect = pg.Rect(rect[0] - border_width, rect[1] - border_width, rect[2] + 2 * border_width, rect[3] + 2 * border_width)
    pg.draw.rect(main_window, black, border_rect)
    # button rectangle
    pg.draw.rect(main_window, color, rect)
    font = pg.font.SysFont(None, 40)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
    window.blit(text_surface, text_rect)

def display_text(text, position, window,size):
    font = pg.font.SysFont(None, size)
    text_surface = font.render(text, True, black)
    window.blit(text_surface, position)

# Size of option buttons
w = 100
h = 50
game_options = {
    "STONE": pg.Rect(30, 200, w, h),
    "PAPER": pg.Rect(180, 200, w, h),
    "SCISSORS": pg.Rect(330, 200, 150, h),
}

user_choice = ""
computer_choice = ""
user_score = 0
computer_score = 0
playing = True
round_ended = False
result = ""
while playing:
    main_window.fill(white)
    display_text("______________________________",(25,310),main_window,size)
    display_text("Computer Score: "+ str(computer_score),(25,340),main_window,size)
    display_text("Your Score: "+ str(user_score),(25,370),main_window,size)
    if round_ended:
        display_text("Your Choice:  "+user_choice,(25,25),main_window,size)
        display_text("Computer's Choice:  "+computer_choice,(25,60),main_window,size)
        display_text(result,(40,150),main_window,70)
    for option, rect in game_options.items():
        if option == "STONE":
            make_button(option, rect, gray, main_window)
        elif option == "PAPER":
            make_button(option, rect, green, main_window)
        else:
            make_button(option, rect, red, main_window)
    
    # Make button for next round:
    make_button("NEXT", pg.Rect(180, 270, w, h), red, main_window)
    
    for action in pg.event.get():
        # Logic for quitting the game
        if action.type == pg.QUIT:
            playing = False

        # Getting position of cursor
        if action.type == pg.MOUSEBUTTONDOWN:
            mouse_position = pg.mouse.get_pos()

            # Checking the choice of user
            for option, rect in game_options.items():
                if rect.collidepoint(mouse_position):
                    user_choice = option
            # checking if next Button was Clicked
            if pg.Rect(180, 270, w, h).collidepoint(mouse_position):
                round_ended = False
                user_choice = ""
                computer_choice = ""
            # Getting choice of computer
            computer_choice = random.choice(("STONE", "PAPER", "SCISSORS"))
            # Winning logic
            if user_choice == computer_choice:
                result = "TIE!!!"
            
            elif (user_choice == "STONE" and computer_choice == "SCISSORS") or \
                (user_choice == "SCISSORS" and computer_choice == "PAPER") or \
                (user_choice == "PAPER" and computer_choice == "STONE"):
                user_score += 1
                result = "YOU WIN!!!"
            elif user_choice == "":
                result = "Make a Choice"
            else:
                computer_score += 1
                result = "COMPUTER WINS!!!"
    round_ended = True
    pg.display.update()
    clock.tick(60)  # Frame rate

pg.quit()
