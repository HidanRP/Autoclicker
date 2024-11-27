from pynput.mouse import Controller, Button
import keyboard as kb
import time as t

mouse = Controller()
autoclick_enabled = False  # Drapeau pour savoir si l'autoclick est activé

while True:
    # Activation de l'autoclick lorsque la touche 'y' est pressée
    if kb.is_pressed('y') and not autoclick_enabled:
        autoclick_enabled = True
        print("Autoclick activé")

    # Désactivation de l'autoclick lorsque la touche 'u' est pressée
    if kb.is_pressed('u') and autoclick_enabled:
        autoclick_enabled = False
        print("Autoclick désactivé")
        t.sleep(0.2)  # Petites pause pour éviter les pressions multiples rapides

    # Si l'autoclick est activé, on effectue les clics
    if autoclick_enabled:
        mouse.press(Button.left)
        mouse.release(Button.left)
        t.sleep(0.001)  # Pause entre les clics

