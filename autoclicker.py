#!/usr/bin/python3
# autoclicker.py: a simple autoclicker, intended for incremental games

import pyautogui, sys

# check command-line arguments
if len(sys.argv) != 4:
    print("usage: %s iterations x y" %(sys.argv[0]))
    sys.exit()

# pyautogui settings
pyautogui.PAUSE = 0.0
pyautogui.FAILSAFE = True

# set up coordinates to click and the number of iterations
iterations = int(sys.argv[1])
coords = (int(sys.argv[2]), int(sys.argv[3]))
print("Starting the clicker (" + str(iterations) + " iteration(s))...")

try:
    # slowly move the mouse to the desired point so the user can see
    pyautogui.moveTo(coords[0], coords[1], duration=0.50)
    for i in range(1, iterations + 1):
        # click!
        pyautogui.click(coords[0], coords[1])
        # print progress
        if i%1000 == 0 and i != iterations:
            print(i, end=", ", flush=True)
        elif i == iterations:
            print(i)
except pyautogui.FailSafeException:
    print("\nExiting early after completing " + str(i) + " iteration(s)...")

print("Done.")
