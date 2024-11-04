# Stone Paper Scissors Game

This is a simple graphical user interface (GUI) game for Stone Paper Scissors (also known as Rock Paper Scissors) developed in Python using the Pygame library. The player can compete against the computer, and scores are tracked throughout multiple rounds.

## Table of Contents
1. [Requirements](#requirements)
2. [Setup and Execution](#setup-and-execution)
3. [Game Rules](#game-rules)
4. [Code Walkthrough](#code-walkthrough)
    - [Initialization](#initialization)
    - [Main Game Loop](#main-game-loop)
    - [Game Variables](#Game-Variables)
5. [Exiting The Game](#Exiting-the-Game)
6. [Source Code](#Source-Code)

## Requirements

- **Python 3.x**
- **Pygame** library (installable via pip)

To install Pygame, run:
```bash
pip install pygame
```

## Setup and Execution

1. Ensure Pygame is installed.
2. Save the code as stone_paper_scissors.py.
3. Run the game using:
```bash
python stone_paper_scissors.py
```
## Game Rules

- The game presents three options for the player:
    - **STONE**
    - **PAPER**
    - **SCISSORS**
- The computer randomly selects one of the options each round.
- The results are determined as follows:
    - **Stone beats Scissors**
    - **Scissors beat Paper**
    - **Paper beats Stone**
- A message is displayed after each round indicating the winner.
- Scores are tracked for both the player and the computer.
- A **Next** button starts a new round.

## Code Walkthrough

This document provides a detailed walkthrough of the Rock Paper Scissors game created using Python and the `pygame` library.

## Initialization

- The game is initialized with `pygame.init()` to set up Pygame's functionalities.
- A display window with dimensions **500x430 pixels** is created using `pg.display.set_mode((main_width, height))`.
- The window's title is set to "Rock Paper Scissors game" using `pg.display.set_caption()`.
- Colors are defined for the game's buttons and text:
    - `white = (255, 255, 255)` for the background.
    - `gray = (200, 200, 200)` for the **STONE** button.
    - `green = (0, 250, 0)` for the **PAPER** button.
    - `red = (240, 0, 0)` for the **SCISSORS** and **NEXT** buttons.
- Main **game variables** include:
    - `user_choice` and `computer_choice` for storing player and computer selections.
    - `user_score` and `computer_score` for tracking scores.
    - `round_ended`, a boolean variable to check if the round is over.

## Main Game Loop

The main game loop runs continuously to control the game. It performs the following tasks:

1. **Handling Events**:
    - Listens for the **QUIT** event, allowing the player to close the game.
    - Detects **mouse clicks** to register the player’s choice or the **NEXT** button click.

2. **Updating the Display**:
    - Clears the display and fills it with a white background at the start of each loop iteration.
    - Key elements are drawn:
        - The `display_text()` function is used to show the player’s and computer’s scores and the result of each round.
        - The `make_button()` function draws the STONE, PAPER, SCISSORS, and NEXT buttons.
    - If a round has ended, the player's and computer's choices, scores, and result are displayed.

3. **Game Logic**:
    - **User Choice**: When the player clicks one of the options (STONE, PAPER, or SCISSORS), the selection is saved in `user_choice`.
    - **Computer Choice**: The computer randomly selects an option.
    - **Result Determination**:
        - If `user_choice` and `computer_choice` match, it is a tie.
        - Winning conditions are checked, and the `user_score` or `computer_score` is updated.

4. **Restarting Rounds**:
    - Clicking the **NEXT** button resets the choices and prepares for a new round.

## Game Variables

- **Button Sizes**: Option buttons are 100x50 pixels, and the **Next** button appears after each round.
- **Choices and Results**:
    - After the player selects an option, the computer randomly chooses one.
    - The winner is determined based on the game's rules, and scores are updated.

## Exiting the Game

The player can exit the game at any time by closing the Pygame window.

## Source Code

Below is the full source code of the game:

```python
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
    pg.draw.rect(main_window, color, rect)
    font = pg.font.SysFont(None, 40)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect(center=(rect[0] + rect[2] // 2, rect[1] + rect[3] // 2))
    window.blit(text_surface, text_rect)

def display_text(text, position, window, size):
    font = pg.font.SysFont(None, size)
    text_surface = font.render(text, True, black)
    window.blit(text_surface, position)

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
    display_text("______________________________", (25, 310), main_window, size)
    display_text("Computer Score: " + str(computer_score), (25, 340), main_window, size)
    display_text("Your Score: " + str(user_score), (25, 370), main_window, size)

    if round_ended:
        display_text("Your Choice:  " + user_choice, (25, 25), main_window, size)
        display_text("Computer's Choice:  " + computer_choice, (25, 60), main_window, size)
        display_text(result, (40, 150), main_window, 70)

    for option, rect in game_options.items():
        if option == "STONE":
            make_button(option, rect, gray, main_window)
        elif option == "PAPER":
            make_button(option, rect, green, main_window)
        else:
            make_button(option, rect, red, main_window)

    make_button("NEXT", pg.Rect(180, 270, w, h), red, main_window)

    for action in pg.event.get():
        if action.type == pg.QUIT:
            playing = False
        if action.type == pg.MOUSEBUTTONDOWN:
            mouse_position = pg.mouse.get_pos()
            for option, rect in game_options.items():
                if rect.collidepoint(mouse_position):
                    user_choice = option
            if pg.Rect(180, 270, w, h).collidepoint(mouse_position):
                round_ended = False
                user_choice = ""
                computer_choice = ""
            computer_choice = random.choice(("STONE", "PAPER", "SCISSORS"))
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
    clock.tick(60)

pg.quit()
```

