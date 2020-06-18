import time

from PIL import ImageGrab
import pyautogui

#coordinates where the bot will search for obstacles
x_start, x_end, y_start, y_end = 475.0, 500.0, 547, 659
enemy_color_white = (83, 83, 83) #enemies' colors when the background is white
enemy_color_black = (172, 172, 172) #enemies' colors when the background is black

def capture_screen():
    screen_capture = ImageGrab.grab()
    return screen_capture


def detect_enemy(screen):
    for x in range(int(x_start), int(x_end)):
        for y in range(y_start, y_end):
            color = screen.getpixel((x, y))
            if color == enemy_color_white or color == enemy_color_black:
                return True


def jump():
    pyautogui.press("up")
    global x_end
    x_end += 1.8

print("Starting in 3 seconds...")
time.sleep(3)
while True:
    screen = capture_screen()
    if detect_enemy(screen):
        jump()
