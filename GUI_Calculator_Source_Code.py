import pygame as pg

pg.init()
window = pg.display.set_mode((400,500))  # width and height
pg.display.set_caption("Arithmetic calculator")
clock = pg.time.Clock()

#giving color tuple their name for better readibility:
white = (255,255,255)
gray = (200,200,200)
black = (0,0,0)
red = (240,0,0)
green = (0,250,0)
color = (67,67,39)

# function definition for button formation
def make_button(text,rect,color):
    pg.draw.rect(window,color,rect)
    font = pg.font.SysFont(None,40)
    text_surface = font.render(text,True,black)
    text_rect = text_surface.get_rect(center = (rect[0] + rect[2] // 2, rect[1] + rect[3] // 2 ))
    window.blit(text_surface,text_rect)


def display_text(text, position):
    font = pg.font.SysFont(None, 60)
    text_surface = font.render(text, True, black)
    window.blit(text_surface, position)

w = 100 # width of each button
h = 50  # height of each button

buttons = {
    1 : pg.Rect(25, 250, w, h),
    2 : pg.Rect(150, 250, w, h),
    3 : pg.Rect(275, 250, w, h),
    4 : pg.Rect(25, 310, w, h),
    5 : pg.Rect(150, 310, w, h),
    6 : pg.Rect(275, 310, w, h),
    7 : pg.Rect(25, 370, w, h),
    8 : pg.Rect(150, 370, w, h),
    9 : pg.Rect(275, 370, w, h),
    0 : pg.Rect(150, 430, w, h),
}

operators = {
    "CLR": pg.Rect(25, 430, 100, 50),
    "=": pg.Rect(275, 430, 100, 50),
    "*": pg.Rect(25, 190, 50, 50),
    "/": pg.Rect(100, 190, 50, 50),
    "%": pg.Rect(175, 190, 50, 50),
    "+": pg.Rect(250, 190, 50, 50),
    "-": pg.Rect(325, 190, 50, 50),
}

current_expression = ""
result = ""

working = True
while working:
    window.fill(white)
    
    # making numerical buttons
    for button,rect in buttons.items():
        make_button(str(button),rect,gray)
    
    # mking operational buttons
    for operator,rect in operators.items():
        if(operator == "CLR"):
            make_button(operator,rect,red)
        elif(operator == "="):
            make_button(operator,rect,green)
        else:
            make_button(operator,rect,color)

     # Display the current expression and result
    display_text(current_expression, (20, 50))
    if result != "":
        display_text("= " + result, (20, 100))

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

    pg.display.update()
    clock.tick(60) #frame rate
pg.quit()
