# Study Drills

# 1. Make new parts of the game and change what decisions people can make
# Expand the game out as much as you can before it gets ridiculous.

# 2. Write a completely new game. Maybe you don't like this one, so make your own.
# This is your computer; do what you want.

import webbrowser
# The webbrowser module provides a high-level interface to allow displaying Web-based documents to users.
# Under most circumstances, simply calling the open() function from this module will open url using the
# default browser . You have to import the module and use open() function.

print("Can't be bothered to re-invent a new mud.")
input("Press enter to search for MUDs on-line or press ^C (CTRL+C) to exit. ")

webbrowser.open('https://www.google.com/search?q=list+of+mud+games', new=2)

# If new is 0, the url is opened in the same browser window if possible.
# If new is 1, a new browser window is opened if possible.
# If new is 2, a new browser page ("tab") is opened if possible.
