# Arithmetic Calculator using Pygame

This project is a simple **Arithmetic Calculator** built using **Pygame**, a Python library for building games and graphical interfaces. The calculator provides basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Features

- Numeric buttons (0-9) for input.
- Arithmetic operation buttons: addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), and modulo (`%`).
- **Clear (CLR)** button to reset the input.
- **Equals (`=`)** button to evaluate the expression and display the result.
- Displays both the input expression and the result.

## Requirements

- **Python 3.x**
- **Pygame Library**

## Installing Pygame

To install Pygame, use the following command:

```bash
pip install pygame
```
## Code Overview 

1. **Setting Up the Display**

```python
pg.init()
window = pg.display.set_mode((400,500))
pg.display.set_caption("Arithmetic calculator")
clock = pg.time.Clock()
```
This initializes Pygame, sets up a window of size 400x500 pixels, and sets a title for the window.

2. **Defining Colors**

A set of colors is defined using RGB values for ease of reference throughout the code.
```python
white = (255,255,255)
gray = (200,200,200)
black = (0,0,0)
red = (240,0,0)
green = (0,250,0)
color = (67,67,39)
```

3. **Helper Functions**

`make_button`
Draws buttons on the screen, including both numerical and operational buttons.
```python
def make_button(text, rect, color):
    pg.draw.rect(window, color, rect)
    font = pg.font.SysFont(None, 40)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect(center = (rect[0] + rect[2] // 2, rect[1] + rect[3] // 2 ))
    window.blit(text_surface, text_rect)
```

`display_text`
Displays the current expression and result at a specified position.
```python
def display_text(text, position):
    font = pg.font.SysFont(None, 60)
    text_surface = font.render(text, True, black)
    window.blit(text_surface, position)
```

4. **Creating Buttons**
Numerical and operational buttons are defined using `pg.Rect` to specify position and dimensions.
```python
buttons = {
    1 : pg.Rect(25, 250, 100, 50),
    2 : pg.Rect(150, 250, 100, 50),
    ...
}

operators = {
    "CLR": pg.Rect(25, 430, 100, 50),
    "=": pg.Rect(275, 430, 100, 50),
    "*": pg.Rect(25, 190, 50, 50),
    ...
}
```

5. **Main Game Loop**

The loop listens for user interactions, updates the display, and processes calculations.
- **Event Handling**: Listens for quit events and mouse clicks.
- **Updating Expression**: Adds digits or operators to the current expression based on button clicks.
- **Calculation**: Evaluates the expression using Python’s `eval()` function when `=`is pressed.
- **Clearing**: Clears the expression and result when `CLR` is clicked.

```pyhton
for action in pg.event.get():
    if action.type == pg.QUIT:
        working = False

    if action.type == pg.MOUSEBUTTONDOWN:
        mouse_position = pg.mouse.get_pos()
        # Checking if digits are clicked
        for key, value in buttons.items():
            if value.collidepoint(mouse_position):
                current_expression += str(key)

        # Checking if operators are clicked
        for op ,rect in operators.items():
            if rect.collidepoint(mouse_position):
                if op == "CLR":
                    current_expression = ""
                    result = ""
                elif op == "=":
                    try:
                         result = str(eval(current_expression))
                    except:
                        result = "Error"
                else:
                    current_expression += op
```

6. **Display and Frame Rate**

Each frame, the display is updated, and the frame rate is set to 60 FPS:
```python
pg.display.update()
clock.tick(60)
```

7. **Screenshot**
   ![Alt text](image_path)




